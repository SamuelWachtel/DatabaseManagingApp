import SQL_function


def greet():
    print("User database.\nChoose from the options bellow:")


def create():
    SQL_function.myDatabase.create_user(temporary_stored_values())


def change():
    SQL_function.myDatabase.update_user(temporary_stored_values(), input("Choose ID of user you want to replace:\n"))


def temporary_stored_values():
    return User(input("write your first name:\n").title(),
                input("write your surname:\n").title(),
                input("write your birthday [DD/MM/YYYY]:\n"),
                int(input("write your phone number:\n")),
                input("write your email address:\n"),
                input("write your place of residence:\n"))


def print_users():
    print_all_users(SQL_function.myDatabase.all_users())


def search():
    search_user_id = input("Type user ID :\n")
    print_all_users(SQL_function.myDatabase.find_user(search_user_id))


def delete_single_user():
    SQL_function.myDatabase.delete_user(str(input("Type User ID you want to delete.\n")))


def delete_everyone():
    SQL_function.myDatabase.delete_all_users()


class User:
    def __init__(self, name, surname, date_of_birth, phone_number, email, address):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.name, self.surname, self.date_of_birth, self.phone_number, self.email, self.address)


def print_all_users(persons):
    print("Users:")
    for index, person in enumerate(persons):
        print(f"{index + 1}) {person}")
