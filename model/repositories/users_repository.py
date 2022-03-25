from repositories.repository import Repository
from exceptions.invalid_exception.invalid_user_exception import *


class UsersRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_users(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute(f"SELECT * FROM Users WHERE id = {id}")
        return self.cursor.fetchone()

    def create_user(self, user):
        self.__verify_username_and_email_are_unique(user['username'], user['email'])
        self.cursor.execute(f"""INSERT INTO Users (email, username, bio, age)
                            VALUES ('{user['email']}', '{user['username']}', '{user['bio']}', {user['age']});""")
        self.cursor.execute(f"""SELECT id FROM Users WHERE username = '{user['username']}'""")
        user_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"""INSERT INTO Passwords (user_id, hashed_password) 
                            VALUES ({user_id}, '{user['password']}');""")
        return user_id

    def __verify_username_and_email_are_unique(self, username, email):
        if self.does_username_exist(username):
            raise InvalidUsernameException()
        if self.does_email_exist(email):
            raise InvalidEmailException()

    def does_username_exist(self, username):
        self.cursor.execute(f"""SELECT * FROM Users WHERE username = '{username}'""")
        return self.cursor.fetchone() is not None

    def does_email_exist(self, email):
        self.cursor.execute(f"""SELECT * FROM Users WHERE email = '{email}'""")
        return self.cursor.fetchone() is not None
