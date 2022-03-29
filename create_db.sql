USE DitRed;

-- ---------------------
-- USERS
-- ---------------------

CREATE TABLE Users (
    id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    email       VARCHAR(256) UNIQUE NOT NULL,
    username    VARCHAR(30) UNIQUE NOT NULL,
    bio         VARCHAR(1000),
    age         INT NOT NULL,
    createdAt   DATE NOT NULL
);

CREATE TABLE Passwords (
    user_id INT UNSIGNED UNIQUE,
    hashed_password CHAR(96) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- ---------------------
-- PRIVATE CHATS
-- ---------------------

CREATE TABLE Messages (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sender_id   INT UNSIGNED NOT NULL,
    receiver_id INT UNSIGNED NOT NULL,
    timestamp   TIMESTAMP NOT NULL,
    message     VARCHAR (3000) NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES Users(id),
    FOREIGN KEY (receiver_id) REFERENCES Users(id)
);

-- ---------------------
-- WALL POSTS
-- ---------------------

CREATE TABLE WallPosts (
    id        BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id   INT UNSIGNED NOT NULL,
    message   TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- ---------------------
-- SUBS
-- ---------------------

CREATE TABLE Subs (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    creator_id INT UNSIGNED NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    description VARCHAR(1000) NOT NULL,
    subscribers_count INT UNSIGNED NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES Users(id)
);

CREATE TABLE Subscribers (
    user_id INT UNSIGNED NOT NULL,
    sub_id BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (user_id, sub_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (sub_id) REFERENCES Subs(id)
);

CREATE TABLE SubPosts (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sub_id      BIGINT UNSIGNED NOT NULL,
    creator_id  INT UNSIGNED NOT NULL,
    timestamp   TIMESTAMP NOT NULL,
    title       VARCHAR(256) NOT NULL,
    content     TEXT NOT NULL,
    score       INT NOT NULL,
    comments_count INT UNSIGNED NOT NULL,
    FOREIGN KEY (sub_id) REFERENCES Subs(id),
    FOREIGN KEY (creator_id) REFERENCES Users(id)
);

CREATE TABLE SubPostsVotes (
    sub_post_id BIGINT UNSIGNED,
    user_id     INT UNSIGNED NOT NULL,
    vote        ENUM('upvote', 'downvote'),
    PRIMARY KEY (sub_post_id, user_id),
    FOREIGN KEY (sub_post_id) REFERENCES SubPosts(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE SubPostComments (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sub_post_id BIGINT UNSIGNED NOT NULL,
    user_id     INT UNSIGNED NOT NULL,
    timestamp   TIMESTAMP NOT NULL,
    comment     VARCHAR(3000) NOT NULL,
    score       INT NOT NULL,
    answered_comment_id BIGINT UNSIGNED,
-- null means this comment replies to the post itself
    FOREIGN KEY (sub_post_id) REFERENCES SubPosts(id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (answered_comment_id) REFERENCES SubPostComments(id)
);

CREATE TABLE SubPostCommentsVotes (
    sub_post_comment_id BIGINT UNSIGNED,
    user_id             INT UNSIGNED NOT NULL,
    vote                ENUM('upvote', 'downvote'),
    PRIMARY KEY (sub_post_comment_id, user_id),
    FOREIGN KEY (sub_post_comment_id) REFERENCES SubPostComments(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);


-- ---------------------
-- TRIGGERS
-- ---------------------

DELIMITER //
CREATE TRIGGER IncrementSubscribersCount
AFTER INSERT ON Subscribers
FOR EACH ROW
BEGIN
    UPDATE Subs S
    SET S.subscribers_count = S.subscribers_count + 1
    WHERE S.id = NEW.sub_id;
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER IncrementCommentsCount
AFTER INSERT ON SubPostComments
FOR EACH ROW
BEGIN
    UPDATE SubPosts S
    SET S.comments_count = S.comments_count + 1
    WHERE S.id = NEW.sub_post_id;
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER UpdateSubPostsScore
AFTER INSERT ON SubPostsVotes
FOR EACH ROW
BEGIN
    IF NEW.vote = 'upvote' THEN
        UPDATE SubPosts S
        SET S.score = S.score + 1
        WHERE S.id = NEW.sub_post_id;
    ELSE
        UPDATE SubPosts S
        SET S.score = S.score - 1
        WHERE S.id = NEW.sub_post_id;
    END IF;
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER UpdateSubPostCommentsScore
AFTER INSERT ON SubPostCommentsVotes
FOR EACH ROW
BEGIN
    IF NEW.vote = 'upvote' THEN
        UPDATE SubPostComments S
        SET S.score = S.score + 1
        WHERE S.id = NEW.sub_post_comment_id;
    ELSE
        UPDATE SubPostComments S
        SET S.score = S.score - 1
        WHERE S.id = NEW.sub_post_comment_id;
    END IF;
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER AssertAnsweredCommentIsOnSamePost
BEFORE INSERT ON SubPostComments
FOR EACH ROW
BEGIN
    IF NEW.answered_comment_id IS NOT NULL AND
         NEW.sub_post_id NOT IN (SELECT S.sub_post_id
                                FROM SubPostComments S
                                WHERE S.id = NEW.answered_comment_id)
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The comment answers a comment on a different post';
    END IF;
END; //
DELIMITER ;

-- ---------------------
-- INDEXES
-- ---------------------
