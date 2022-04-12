from repositories.repository import Repository
from exceptions.invalid_exception.invalid_user_exception import *
import hashlib


class UsersRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_users(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute(f"SELECT * FROM Users WHERE id = %s", (id,))
        return self.cursor.fetchone()

    def get_username(self, user_id):
        self.cursor.execute(f"""SELECT username FROM Users WHERE id = %s""", (user_id,))
        return self.cursor.fetchone()[0]

    def create_user(self, user):
        self.__verify_username_and_email_are_unique(user['username'], user['email'])
        self.cursor.execute(f"""INSERT INTO Users (email, username, bio, age, createdAt)
                            VALUES (%s, %s, 
                            %s, %s, CURDATE());""", (user['email'], user['username'], user['bio'], user['age']))
        self.cursor.execute(f"""SELECT id FROM Users WHERE username = %s""", (user['username'],))
        user_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"""INSERT INTO Passwords (user_id, hashed_password) 
                            VALUES (%s, %s);""", (user_id, hashlib.sha384(user['password'].encode()).hexdigest()))
        return user_id

    def __verify_username_and_email_are_unique(self, username, email):
        if self.does_username_exist(username):
            raise InvalidUsernameException()
        if self.does_email_exist(email):
            raise InvalidEmailException()

    def does_username_exist(self, username):
        self.cursor.execute(f"""SELECT * FROM Users WHERE username = %s""", (username,))
        return self.cursor.fetchone() is not None

    def does_email_exist(self, email):
        self.cursor.execute(f"""SELECT * FROM Users WHERE email = %s""", (email,))
        return self.cursor.fetchone() is not None

    def create_wallpost(self, user_id, wall_post):
        self.cursor.execute(f"""INSERT INTO WallPosts (user_id, message, timestamp)
                            VALUES (%s, %s, NOW());""", (user_id, wall_post))
        self.cursor.execute(f"""SELECT id FROM WallPosts WHERE user_id = %s AND message = %s""", (user_id, wall_post))
        wall_post_id = self.cursor.fetchone()[0]
        return wall_post_id

    def get_wallposts(self, user_id):
        self.cursor.execute(f"""SELECT message FROM WallPosts WHERE user_id = %s""", (user_id,))
        return self.cursor.fetchall()

    def verify_login(self, user_info):
        self.cursor.execute(f"""SELECT * FROM Users WHERE username = %s""", (user_info['username'],))
        user = self.cursor.fetchone()
        if user is None:
            raise InvalidUsernameException()

        self.cursor.execute(f"""SELECT * FROM Passwords WHERE user_id = %s""", (user[0],))
        hashed_password = self.cursor.fetchone()[1]
        if hashed_password != hashlib.sha384(user_info['password'].encode()).hexdigest():
            raise InvalidPasswordException()

        return user[0]

    def get_matching_usernames(self, username_substring):
        self.cursor.execute(f"""SELECT username FROM Users WHERE username
         LIKE CONCAT('%%', %s, '%%') """, (username_substring,))
        return self.cursor.fetchall()

    def get_user_by_username(self, username):
        self.cursor.execute(f"""SELECT * FROM Users WHERE username = %s""", (username,))
        return self.cursor.fetchone()
