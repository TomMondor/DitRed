USE DitRed;

-- ---------------------
-- USERS
-- ---------------------

CREATE TABLE Users (
    id      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    email   VARCHAR(256) UNIQUE NOT NULL,
    username VARCHAR(30) UNIQUE NOT NULL,
    bio     VARCHAR(1000),
    age     INT NOT NULL
);

CREATE TABLE Passwords (
    user_id INT UNSIGNED UNIQUE REFERENCES Users(id),
    hashed_password CHAR(96) NOT NULL
);

-- ---------------------
-- PRIVATE CHATS
-- ---------------------

CREATE TABLE Messages (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sender_id   INT UNSIGNED NOT NULL REFERENCES Users(id),
    receiver_id INT UNSIGNED NOT NULL REFERENCES Users(id),
    timestamp   TIMESTAMP NOT NULL,
    message     VARCHAR (3000) NOT NULL
);

-- ---------------------
-- WALL POSTS
-- ---------------------

CREATE TABLE WallPosts (
    id        BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id   INT UNSIGNED NOT NULL REFERENCES Users(id),
    message   TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

-- ---------------------
-- SUBS
-- ---------------------

CREATE TABLE Subs (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    creator_id INT UNSIGNED NOT NULL REFERENCES Users(id),
    timestamp TIMESTAMP NOT NULL,
    description VARCHAR(1000) NOT NULL,
    subscribers_count INT UNSIGNED NOT NULL
);

CREATE TABLE Subscribers (
    user_id INT UNSIGNED NOT NULL REFERENCES Users(id),
    sub_id BIGINT UNSIGNED NOT NULL REFERENCES Subs(id),
    PRIMARY KEY (user_id, sub_id)
);

CREATE TABLE SubPosts (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sub_id      BIGINT UNSIGNED NOT NULL REFERENCES Subs(id),
    creator_id  INT UNSIGNED NOT NULL REFERENCES Users(id),
    timestamp   TIMESTAMP NOT NULL,
    title       VARCHAR(256) NOT NULL,
    content     TEXT NOT NULL,
    score       INT NOT NULL,
    comments_count INT UNSIGNED NOT NULL
);

CREATE TABLE SubPostsVotes (
    sub_post_id BIGINT UNSIGNED REFERENCES SubPosts(id),
    user_id     INT UNSIGNED NOT NULL REFERENCES Users(id),
    vote        ENUM('upvote', 'downvote'),
    PRIMARY KEY (sub_post_id, user_id)
);

CREATE TABLE SubPostComments (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sub_post_id BIGINT UNSIGNED NOT NULL REFERENCES SubPosts(id),
    user_id     INT UNSIGNED NOT NULL REFERENCES Users(id),
    timestamp   TIMESTAMP NOT NULL,
    comment     VARCHAR(3000) NOT NULL,
    score       INT NOT NULL,
    answered_comment_id BIGINT UNSIGNED REFERENCES SubPostComments(id)
-- null means this comment replies to the post itself
);

CREATE TABLE SubPostCommentsVotes (
    sub_post_comment_id BIGINT UNSIGNED REFERENCES SubPostComments(id),
    user_id             INT UNSIGNED NOT NULL REFERENCES Users(id),
    vote                ENUM('upvote', 'downvote'),
    PRIMARY KEY (sub_post_comment_id, user_id)
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
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER IncrementCommentsCount
AFTER INSERT ON SubPostComments
FOR EACH ROW
BEGIN
    UPDATE SubPosts S
    SET S.comments_count = S.comments_count + 1
    WHERE S.id = NEW.sub_post_id;
END;//
DELIMITER ;


DELIMITER //
CREATE TRIGGER AssertAnsweredCommentIsOnSamePost
BEFORE INSERT ON SubPostComments
FOR EACH ROW
BEGIN
    IF NEW.sub_post_id NOT IN (SELECT S.sub_post_id
                                FROM SubPostComments S
                                WHERE S.id = NEW.answered_comment_id)
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The comment answers a comment on a different post';
    END IF;
END;//
DELIMITER ;

-- ---------------------
-- INDEXES
-- ---------------------

-- ---------------------
-- SEE THE DB
-- ---------------------
SHOW databases;
SHOW tables;
SELECT * FROM Users;
SELECT * FROM Passwords;
SELECT * FROM WallPosts;
SELECT * FROM Messages;
SELECT * FROM Subs;
