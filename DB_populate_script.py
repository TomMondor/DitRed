import pymysql.cursors
import os
from dotenv import load_dotenv
from random_username.generate import generate_username
from lorem import get_sentence, get_word, get_paragraph
from random import randint, choice, sample
import hashlib
import datetime


def create_DB():
    connection = pymysql.connect(
        host="localhost", user=SQL_USER, password=SQL_PASSWORD, autocommit=True
    )
    cursor = connection.cursor()
    cursor.execute("DROP DATABASE IF EXISTS DitRed;")
    cursor.execute("CREATE DATABASE DitRed;")


def create_tables(cursor):
    commands = parse_SQL_script("DB_creation.sql")
    for command in commands:
        cursor.execute(command)


def parse_SQL_script(filename):
    """Taken from : http://adamlamers.com/post/GRBJUKCDMPOA
        Parses .sql file to extract every command.
    """
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip().replace('//', ''))
            stmt = ''
        else:
            stmts.append(line.strip().replace('//', ''))
    return stmts


def get_users_count(cursor):
    select_request = "SELECT COUNT(*) FROM Users;"
    cursor.execute(select_request)
    users_count = cursor.fetchone()[0]
    return users_count


def get_sub_timestamp(cursor, sub_id):
    select_request = f"""SELECT timestamp FROM Subs WHERE id = {sub_id};"""
    cursor.execute(select_request)
    timestamp = cursor.fetchone()[0]
    return timestamp


def generate_timestamp_after(other_timestamp):
    year = randint(other_timestamp.year, 2022)
    month = randint(other_timestamp.month, 12)
    day = randint(other_timestamp.day, 28)
    hour = randint(other_timestamp.hour, 23)
    minute = randint(other_timestamp.minute, 59)
    sec = randint(other_timestamp.second, 59)

    hour = 11 if month == 3 else hour  # winter/summer time bug in mySQL
    timestamp = datetime.datetime(year, month, day, hour, minute, sec)

    return str(timestamp)[:19]


def generate_random_timestamp():
    return generate_timestamp_after(datetime.datetime(2004, 1, 1))


def generate_users(cursor, users_number):
    user_names = set()
    while len(user_names) < users_number:
        user_names.add(generate_username(1)[0])
    user_names = list(user_names)

    for username in user_names:
        bio = get_sentence(count=(2, 5))
        age = randint(13, 100)
        request = f"""INSERT INTO Users (email, username, bio, age) VALUES ('{username}@mail.com', '{username[:30]}', '{bio}', {age});"""
        cursor.execute(request)

        generate_last_user_password(cursor)


def generate_last_user_password(cursor):
    user_id = get_users_count(cursor)

    raw_password = get_word(count=3, sep='')
    crypted_password = hashlib.sha384(raw_password.encode()).hexdigest()
    request = f"""INSERT INTO Passwords (user_id, hashed_password) VALUES ({user_id}, '{crypted_password}');"""
    cursor.execute(request)


def generate_wall_posts(cursor):
    users_count = get_users_count(cursor)
    for user_id in range(1, users_count + 1):
        posts_count = randint(0, 5)
        for _ in range(posts_count):
            message = get_paragraph(count=(1, 4), sentence_range=(2, 8))
            request = f"""INSERT INTO WallPosts (user_id, message, timestamp) VALUES """
            request += f"""({user_id}, '{message}', '{generate_random_timestamp()}');"""
            cursor.execute(request)


def generate_private_chat_messages(cursor):
    users_count = get_users_count(cursor)
    # starts at 6 because 0-5 discussions are created with people having lower ids than the current id 
    for user_id in range(6, users_count + 1):
        discussions_count = randint(0, 5)
        for _ in range(discussions_count):
            friend_id = randint(1, user_id - 1)
            messages_number = randint(5, 30)
            friends_ids = [user_id, friend_id]
            for _ in range(messages_number):
                sender = randint(0, 1)
                message = get_sentence(count=(1, 10), word_range=(1, 20))
                request = f"""INSERT INTO Messages (sender_id, receiver_id, timestamp, message) VALUES """
                request += f"""({friends_ids[sender]}, {friends_ids[1 - sender]}, '{generate_random_timestamp()}', '{message}');"""
                cursor.execute(request)


def generate_subs(cursor, subs_number):
    users_number = get_users_count(cursor)

    sub_names = set()
    while len(sub_names) < subs_number:
        sub_names.add(get_sentence(count=1, word_range=(1, 10))[:100].strip('. '))
    sub_names = list(sub_names)

    for i in range(subs_number):
        sub_name = sub_names[i]
        user_id = randint(1, users_number)
        descr = get_paragraph(count=1, sentence_range=(1, 4))
        request = f"""INSERT INTO Subs (name, creator_id, timestamp, description, subscribers_count) VALUES """
        request += f"""('{sub_name}', {user_id}, '{generate_random_timestamp()}', '{descr}', 0);"""
        cursor.execute(request)


def generate_subscribers(cursor, subscribers_number, subs_number):
    for subscriber_id in range(1, subscribers_number+1):
        request = f"""INSERT INTO Subscribers (user_id, sub_id) VALUES ({subscriber_id}, {((subscribers_number - subscriber_id) % subs_number) + 1});"""
        cursor.execute(request)


def generate_sub_posts(cursor, subs_number, users_number):
    for sub_id in range(1, subs_number+1):
        creator_id = randint(1, users_number)
        sub_timestamp = get_sub_timestamp(cursor, sub_id)
        timestamp = generate_timestamp_after(sub_timestamp)
        title = get_sentence(count=1, word_range=(1, 10))[:100].strip('. ')
        content = get_sentence(count=randint(1, 5), word_range=(1, 10))

        request = f"""INSERT INTO SubPosts (sub_id, creator_id, timestamp, title, content, score, comments_count) """
        request += f"""VALUES ({sub_id}, {creator_id}, '{timestamp}', '{title}', '{content}', 0, 0);"""
        cursor.execute(request)


def generate_posts_votes(cursor, subs_number, users_number):
    for sub_post_id in range(1, subs_number+1):
        user_ids = sample(range(1, users_number), randint(1, 10))
        for user_id in user_ids:
            vote = get_random_vote()
            request = f"""INSERT INTO SubPostsVotes (sub_post_id, user_id, vote) """
            request += f"""VALUES ({sub_post_id}, {user_id}, '{vote}');"""
            cursor.execute(request)


def get_random_vote():
    possible_votes = ["upvote", "downvote"]

    return choice(possible_votes)


def generate_sub_post_comments(cursor, subs_number, users_number):
    for sub_post_id in range(1, subs_number+1):
        user_id = randint(1, users_number)
        sub_timestamp = get_sub_timestamp(cursor, sub_post_id)
        timestamp = generate_timestamp_after(sub_timestamp)
        comment = get_sentence(count=randint(1, 5), word_range=(1, 10))

        request = f"""INSERT INTO SubPostComments (sub_post_id, user_id, timestamp, comment, score, answered_comment_id) """
        request += f"""VALUES ({sub_post_id}, {user_id}, '{timestamp}', '{comment}', 0, NULL);"""
        cursor.execute(request)


def generate_sub_post_comments_votes(cursor):
    pass


if __name__ == '__main__':
    load_dotenv()
    SQL_USER = os.getenv('SQL_USER')
    SQL_PASSWORD = os.getenv('SQL_PASSWORD')

    create_DB()

    connection = pymysql.connect(
        host="localhost", user=SQL_USER, password=SQL_PASSWORD, db="DitRed", autocommit=True
    )
    cursor = connection.cursor()

    create_tables(cursor)

    users_number = 50
    generate_users(cursor, users_number)
    generate_wall_posts(cursor)
    generate_private_chat_messages(cursor)

    subs_number = 25
    subscribers_number = 30
    generate_subs(cursor, subs_number)
    generate_subscribers(cursor, subscribers_number, subs_number)
    generate_sub_posts(cursor, subs_number, users_number)
    generate_posts_votes(cursor, subs_number, users_number)
    generate_sub_post_comments(cursor, subs_number, users_number)
    generate_sub_post_comments_votes(cursor)
