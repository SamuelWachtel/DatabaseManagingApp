import App_functions

evidence = App_functions
evidence.greet()
while True:
    choice = " "
    try:
        choice = input("1 = Create user\n"
                       "2 = Edit user\n"
                       "3 = Show all users\n"
                       "4 = Find user\n"
                       "5 = Delete single user\n"
                       "6 = Delete all users\n"
                       "7 = Quit\n")
    except ValueError:
        print("Error, you didn't chose any operations. Try again:\n")
        continue

    if choice == "1":
        print("Create new user:")
        evidence.create()

    elif choice == "2":
        print("Edit user:")
        evidence.change()

    elif choice == "3":
        evidence.print_users()

    elif choice == "4":
        evidence.search()

    elif choice == "5":
        evidence.delete_single_user()

    elif choice == "6":
        safety_check = input("Are you sure? [Y/N]").upper()
        if safety_check == "Y":
            evidence.delete_everyone()
        else:
            pass
    elif choice == "7":
        break
    print("\nChoose next operation:")
print("\nGoodbye.")
