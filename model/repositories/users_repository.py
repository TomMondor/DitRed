from repositories.repository import Repository


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
        self.cursor.execute(f"""INSERT INTO Users (email, username, bio, age) 
                            VALUES ({user.email}, '{user.email}', '{user.bio}', {user.age});""")
        #TODO TOM : ajouter une méthode au user_assembler pour valider que le body de la requête contient tt les champs (et bon format)
        #TODO TOM : checker si on peut faire user.XX pour un dicto python
        #TODO TOM : fetch le user_id dans la BD (peut-on juste prendre le nb de lignes insérées ?)
        # et l'utiliser dans la requête ci-dessous (décider aussi si le pword est hashé déjà)
        self.cursor.execute(f"""INSERT INTO Passwords (user_id, password) VALUES ({}, '{}');""")
