import pymysql.cursors
import os
from dotenv import load_dotenv
from random_username.generate import generate_username
from lorem import get_sentence, get_word, get_paragraph
from random import randint
import hashlib
import datetime


def create_DB(cursor):
    commands = parse_SQL_script("DB_creation.sql")
    for command in commands:
        cursor.execute(command)

def parse_SQL_script(sql_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    stmt = ''
    stmts = []
    for line in data:
        if line:
            if line.startswith('--'):
                continue
            stmt += line.strip() + ' '
            if ';' in stmt:
                stmts.append(stmt.strip())
                stmt = ''
    return stmts

def get_users_count(cursor):
    selectRequest = "SELECT COUNT(*) FROM Users;"
    cursor.execute(selectRequest)
    usersCount = cursor.fetchone()[0]
    return usersCount

def generate_timestamp_after(other_timestamp):
    year = randint(int(other_timestamp[:4]), 2022)
    month = randint(int(other_timestamp[5:7]), 12)
    day = randint(int(other_timestamp[8:10]), 28)
    hour = randint(int(other_timestamp[11:13]), 23)
    minute = randint(int(other_timestamp[14:16]), 59)
    sec = randint(int(other_timestamp[17:19]), 59)

    hour = 11 if month == 3 else hour #winter/summer time bug in mySQL
    timestamp = datetime.datetime(year, month, day, hour, minute, sec)

    return str(timestamp)[:19]

def generate_random_timestamp():
    return generate_timestamp_after("2004-01-01 00:00:00")

def generate_users(cursor, usersNumber):
    for username in generate_username(usersNumber):
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
    usersCount = get_users_count(cursor)
    for user_id in range(1, usersCount + 1):
        postsCount = randint(0, 5)
        for _ in range(postsCount):
            message = get_paragraph(count=(1,4), sentence_range=(2, 8))
            request = f"""INSERT INTO WallPosts (user_id, message, timestamp) VALUES """
            request += f"""({user_id}, '{message}', '{generate_random_timestamp()}');"""
            cursor.execute(request)

def generate_private_chat_messages(cursor):
    usersCount = get_users_count(cursor)
    # starts at 6 because 0-5 discussions are created with people having lower ids than the current id 
    for user_id in range(6, usersCount + 1):
        discussionsCount = randint(0, 5)
        for _ in range(discussionsCount):
            friend_id = randint(1, user_id - 1)
            messagesNumber = randint(5, 30)
            friends_ids = [user_id, friend_id]
            for _ in range(messagesNumber):
                sender = randint(0, 1)
                message = get_sentence(count=(1, 10), word_range=(1, 20))
                request = f"""INSERT INTO Messages (sender_id, receiver_id, timestamp, message) VALUES """ 
                request += f"""({friends_ids[sender]}, {friends_ids[1 - sender]}, '{generate_random_timestamp()}', '{message}');"""
                cursor.execute(request)

def generate_subs(cursor, subsNumber):
    usersNumber = get_users_count(cursor)
    for _ in range(subsNumber):
        sub_name = get_sentence(count=1, word_range=(1, 10))[:100].strip('. ')
        user_id = randint(1, usersNumber)
        descr = get_paragraph(count=1, sentence_range=(1, 4))
        request = f"""INSERT INTO Subs (name, creator_id, timestamp, description, subscribers_count) VALUES """ 
        request += f"""('{sub_name}', {user_id}, '{generate_random_timestamp()}', '{descr}', 0);"""
        cursor.execute(request)

def generate_subscribers(cursor):
    #INSERT INTO Subscribers (user_id, sub_id) VALUES ();
    #TODO il faut faire la gâchette SQL pour incrémenter le nb de subscribers du Sub
    pass

def generate_sub_posts(cursor):
    pass

def generate_posts_votes(cursor):
    pass

def generate_sub_post_comments(cursor):
    pass

def generate_sub_post_comments_votes(cursor):
    pass


if __name__ == '__main__':
    load_dotenv()
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')

    connection = pymysql.connect(
        host="localhost", user=USER, password=PASSWORD, db="ditred", autocommit=True
    )
    cursor = connection.cursor()

    create_DB(cursor)

    generate_users(cursor, 400)
    generate_wall_posts(cursor)
    generate_private_chat_messages(cursor)
    
    generate_subs(cursor, 120)
    generate_subscribers(cursor)
    generate_sub_posts(cursor)
    generate_posts_votes(cursor)
    generate_sub_post_comments(cursor)
    generate_sub_post_comments_votes(cursor)
