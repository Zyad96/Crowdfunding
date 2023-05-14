import datetime
import time


def generate_id() -> int:
    return round(time.time())


def ask_for_string(message: str) -> str:
    while True:
        instr = input(message)
        if instr.isalpha():
            return instr
        print("Please enter a valid string.")


def ask_for_int(message: str) -> int:
    while True:
        innum = input(message)
        if innum.isdigit():
            return int(innum)
        print("Please enter a valid integer.")


def find_project_by_id(project_id: int) -> str:
    projects = get_all_projects()
    for project in projects:
        project_details = project.strip('\n').split(" ")
        if project_details[0] == str(project_id):
            return project
    return ""


def save_projects_to_file(list_of_projects: list) -> bool:
    try:
        with open("projectsDB.txt", 'w') as file_obj:
            file_obj.writelines(list_of_projects)
    except Exception as e:
        print(e)
        return False
    else:
        return True


def delete_project_from_file(project: str) -> bool:
    projects = get_all_projects()
    projects.remove(project)
    removed = save_projects_to_file(projects)
    return removed


def is_valid_date(date_text: str) -> bool:
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False


def get_all_projects() -> list:
    try:
        with open("projectsDB.txt", 'r') as file_obj:
            projects = file_obj.readlines()
    except Exception as e:
        print(e)
        return []
    else:
        return projects


def create_project() -> None:
    title = ask_for_string("Enter the title of your project: ")
    details = input("Enter the details of your project: ")
    target = ask_for_int("Enter the total target for your project (in EGP): ")
    email = input("Enter your email: ")
    while not target > 0:
        target = ask_for_int("Invalid target amount. Please enter a valid amount (in EGP): ")
    start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not is_valid_date(start_time):
        start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("Enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not is_valid_date(end_time):
        end_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    project_id = generate_id()
    with open("projectsDB.txt", "a") as file_obj:
        file_obj.write("{} {} {} {} {} {} {}\n".format(project_id, title, details, target, start_time, end_time, email))
    print("Project created successfully.")


def display_all_projects() -> None:
    projects = get_all_projects()
    if not projects:
        print('No projects found.')
    else:
        for project in projects:
            print(project)


def edit_project():
    project_id = ask_for_int("Please enter the id of the project you want to edit: ")  # int
    email = input("enter your email ")
    found = find_project_by_id(project_id)
    test = str(found).split()
    if found:
        print("found")
        print(test)
        if test[8] == str(email):
            title = input("Enter the title of your project: ")
            details = input("Enter the details of your project: ")
            target = input("Enter the total target for your project (in EGP): ")
            email = input("Enter your email ")
            while not target.isdigit():
                target = input("Invalid target amount. Please enter a valid amount (in EGP): ")
            start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
            while not is_valid_date(start_time):
                start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
            end_time = input("Enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
            while not is_valid_date(end_time):
                end_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
            id = generate_id()
            with open("projectsDB.txt", "a") as file:
                file.write("{} {} {} {} {} {} {}\n".format(id, title, details, target, start_time, end_time, email))
            print("Project edited successfully.")
        else:
            print("this project is not yours you can't edit it ")


def delete_project():
    project_id = ask_for_int("Please enter the id of the project you want to delete: ")  # int
    email = input("enter your email ")
    found = find_project_by_id(project_id)
    test = str(found).split()
    if found:
        print("found")
        if test[8] == str(email):
            removed = delete_project_from_file(found)
            if removed:
                print('project deleted successfully')
            else:
                print(" problem happened while deleting the project ")
        else:
            print("this project is not yours to delete ")
            return
    else:
        print("project not found, please try again with valid id ")
