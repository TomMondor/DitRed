from repositories.repository import Repository
from exceptions.invalid_exception.invalid_sub_exception import *


class SubsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_subs(self):
        self.cursor.execute("SELECT * FROM Subs")
        return self.cursor.fetchall()

    def get_sub(self, id):
        self.cursor.execute(f"SELECT * FROM Subs WHERE id = {id}")
        return self.cursor.fetchone()

    def create_sub(self, name, creator_id, description):
        self.__check_new_sub_validity(name, creator_id)
        sub_id = self.__add_sub_to_database(name, creator_id, description)
        return sub_id

    def __add_sub_to_database(self, name, creator_id, description):
        self.cursor.execute(f"INSERT INTO Subs (name, creator_id, timestamp, description, subscribers_count) " +
                            f"VALUES ('{name}', {creator_id}, NOW(), '{description}', 0)")
        return self.cursor.lastrowid

    def __check_new_sub_validity(self, name, creator_id):
        self.__raise_error_if_creator_id_exists(creator_id)
        self.__raise_error_if_sub_name_exists(name)

    def __raise_error_if_creator_id_exists(self, creator_id):
        if not self.__check_creator_id_exists(creator_id):
            raise InvalidSubCreatorIdException()

    def __check_creator_id_exists(self, creator_id):
        self.cursor.execute(f"SELECT * FROM Users WHERE id = {creator_id}")
        return self.cursor.fetchone() is not None

    def __raise_error_if_sub_name_exists(self, name):
        if self.__check_sub_name_exists(name):
            raise InvalidSubNameException()

    def __check_sub_name_exists(self, name):
        self.cursor.execute(f"SELECT * FROM Subs WHERE name = '{name}'")
        return self.cursor.fetchone() is not None
