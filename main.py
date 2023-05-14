import registration as reg
import crud_functions as crud
from Telecom import welcome

welcome()

while True:
    print("Select an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter the option number: ")

    if choice == "1":
        reg.register()
    elif choice == "2":
        reg.login()
        while True:
            print("Select an option:")
            print("1. Create a new project")
            print("2. Display all projects")
            print("3. Edit a project")
            print("4. Delete a project")
            print("5. Logout")

            operation = input("Enter the option number: ")

            if operation == "1":
                crud.create_project()
            elif operation == "2":
                crud.display_all_projects()
            elif operation == "3":
                crud.edit_project()
            elif operation == "4":
                crud.delete_project()
            elif operation == "5":
                print("Logged out.")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 5.")
    elif choice == "3":
        print("Bye!")
        exit()
    else:
        print("Invalid option. Please enter a number between 1 and 3.")
