import sqlite3

class Database:
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def get_fullName(self, StudenteID):
        self.cursor.execute("""SELECT Cognome, Nome
                            FROM Studente
                            WHERE ID = ?""",
                            (StudenteID,))
        output_fullName = self.cursor.fetchone()
        fullName = f"{output_fullName[0]} {output_fullName[1]}"
        return fullName

    def get_firstName(self, StudenteID):
            self.cursor.execute("""SELECT Nome
                                FROM Studente
                                WHERE ID = ?""",
                                (StudenteID,))
            firstName = self.cursor.fetchone()
            return firstName

    def get_lastName(self, StudenteID):
            self.cursor.execute("""SELECT Cognome
                                FROM Studente
                                WHERE ID = ?""",
                                (StudenteID,))
            lastName = self.cursor.fetchone()
            return lastName

    def get_email(self, StudenteID):
            self.cursor.execute("""SELECT Email
                                FROM Studente
                                WHERE ID = ?""",
                                (StudenteID,))
            email = self.cursor.fetchone()
            return email
          