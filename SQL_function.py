import sqlite3
import App_functions


class Database:
    file_name = None
    connection = None
    cursor = None

    def __init__(self, file_name):
        self.file_name = file_name

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.file_name)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()

    def create_table(self):
        try:
            self.connect()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users (User_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                "Name TEXT, Surname TEXT, Date_of_birth TEXT, "
                                "Phone_number INTEGER, "
                                "Email_address TEXT, Address TEXT)")
            self.connection.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()

    def create_user(self, user):
        try:
            self.connect()
            self.cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)", (None, user.name,
                                                                             user.surname,
                                                                             user.date_of_birth,
                                                                             user.phone_number,
                                                                             user.email,
                                                                             user.address))
            self.connection.commit()

        except Exception as e:
            print(e)
        finally:
            self.close()

    def find_user(self, user_id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            rows = cursor.execute("SELECT * FROM users WHERE User_ID = ?", (str(user_id))).fetchall()
            return [App_functions.User(row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
        except Exception as e:
            print(e)
        finally:
            self.close()

    def all_users(self):
        try:
            self.connect()
            rows = self.cursor.execute("SELECT User_ID, Name, Surname, Date_of_birth, Phone_number, Email_address, Address FROM users").fetchall()
            return [App_functions.User(row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
        except Exception as e:
            print(e)
        finally:
            self.close()

    def update_user(self, user, user_id):
        try:
            self.connect()
            self.cursor.execute("UPDATE users SET Name = ?, "
                                "Surname = ?, Date_of_birth = ?, "
                                "Phone_number = ?, Email_address = ?, "
                                "Address = ?  WHERE User_ID = ?",
                                (user.name, user.surname, user.date_of_birth,
                                 user.phone_number, user.email, user.address, user_id))
            self.connection.commit()
            print("User changed successfully.")
        except Exception as e:
            print(e)
        finally:
            self.close()

    def delete_user(self, user_id):
        try:
            self.connect()
            self.cursor.execute(f"DELETE FROM users WHERE User_ID = ?", (user_id,))
            self.connection.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()

    def delete_all_users(self):
        try:
            self.connect()
            self.cursor.execute("DELETE FROM users")
            self.connection.commit()
        except Exception as e:
            print("Delete users error")
            print(e)
        finally:
            self.close()


myDatabase = Database("User_database.db")

myDatabase.create_table()
