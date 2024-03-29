from repositories.repository import Repository
from exceptions.invalid_exception.invalid_sub_exception import *


class SubsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_subs(self):
        self.cursor.execute("SELECT S.*, U.username FROM Subs S, Users U WHERE U.id = S.creator_id")
        return self.cursor.fetchall()

    def get_sub(self, id):
        self.cursor.execute(f"SELECT S.*, U.username FROM Subs S, Users U WHERE S.id = %s AND U.id = S.creator_id",
                            (id,))
        return self.cursor.fetchone()

    def get_sub_name(self, id):
        self.cursor.execute(f"SELECT name FROM Subs WHERE id = %s", (id,))
        return self.cursor.fetchone()[0]

    def create_sub(self, name, creator_id, description):
        self.__check_new_sub_validity(name, creator_id)
        sub_id = self.__add_sub_to_database(name, creator_id, description)
        return sub_id

    def create_subscription(self, user_id, sub_id):
        self.cursor.execute(f"INSERT INTO Subscribers (user_id, sub_id)" +
                            f" VALUES (%s, %s)", (user_id, sub_id))

    def __add_sub_to_database(self, name, creator_id, description):
        self.cursor.execute(f"INSERT INTO Subs (name, creator_id, timestamp, description, subscribers_count) " +
                            f"VALUES (%s, %s, NOW(), %s, 0)", (name, creator_id, description))
        return self.cursor.lastrowid

    def __check_new_sub_validity(self, new_name, creator_id):
        self.__raise_error_if_creator_id_exists(creator_id)
        self.__raise_error_if_new_sub_name_exists(new_name)

    def __raise_error_if_creator_id_exists(self, creator_id):
        if not self.__check_creator_id_exists(creator_id):
            raise InvalidSubCreatorIdException()

    def __check_creator_id_exists(self, creator_id):
        self.cursor.execute(f"SELECT * FROM Users WHERE id = %s", (creator_id,))
        return self.cursor.fetchone() is not None

    def __raise_error_if_new_sub_name_exists(self, new_name):
        if self.__check_sub_name_exists(new_name):
            raise InvalidSubNameException()

    def __check_sub_name_exists(self, name):
        self.cursor.execute(f"SELECT * FROM Subs WHERE name = %s", (name,))
        return self.cursor.fetchone() is not None

    def __check_if_new_sub_name_different_than_old(self, sub_id, new_name):
        self.cursor.execute(f"SELECT name FROM Subs WHERE id = %s", (sub_id,))
        old_name = self.cursor.fetchone()[0]
        return old_name != new_name

    def update_sub(self, sub_id, name, creator_id, description):
        self.__check_if_sub_not_owned_by_creator(sub_id, creator_id)
        self.__check_updated_sub_validity(sub_id, name)
        self.__update_sub_content(sub_id, name, description)
        return self.__get_updated_sub_data(sub_id)

    def __check_if_sub_not_owned_by_creator(self, sub_id, creator_id):
        self.cursor.execute(f"SELECT * FROM Subs WHERE id = %s AND creator_id = %s", (sub_id, creator_id))
        if self.cursor.fetchone() is None:
            raise InvalidSubCreatorIdException()

    def __check_updated_sub_validity(self, sub_id, name):
        self.__raise_error_if_sub_id_does_not_exist(sub_id)
        if self.__check_if_new_sub_name_different_than_old(sub_id, name):
            self.__raise_error_if_new_sub_name_exists(name)

    def __raise_error_if_sub_id_does_not_exist(self, sub_id):
        if not self.__check_sub_id_exists(sub_id):
            raise InvalidSubIdException()

    def __check_sub_id_exists(self, sub_id):
        self.cursor.execute(f"SELECT * FROM Subs WHERE id = %s", (sub_id,))
        return self.cursor.fetchone() is not None

    def __update_sub_content(self, sub_id, name, description):
        self.cursor.execute(f"UPDATE Subs SET name = %s, description = %s WHERE id = %s", (name, description, sub_id))

    def __get_updated_sub_data(self, id):
        self.cursor.execute(f"SELECT * FROM Subs WHERE id = %s", (id,))
        return self.cursor.fetchone()
    
