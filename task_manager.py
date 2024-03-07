# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password

#=====importing libraries===========
import os
from datetime import datetime, date

# Datetime String Format
DSF = "%Y-%m-%d"

def task_list_to_file():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for task in task_list:
            str_attrs = [
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DSF),
                task['assigned_date'].strftime(DSF),
                "Yes" if task['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def reg_user():
    '''
    Allows user to add a new username to the program
    '''
    user_valid = False
    while not user_valid:        

        # - Request inputs of new username
        new_username = input("New Username: ")

        # - Check if username already exists 
        if new_username in username_password.keys():
            print("Username already exists, please try another name.")
        else:
            user_valid = True

    # Better functioning password match check 
    password_valid = False
    while not password_valid:
        # - Request input of password and confirmation
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file and break loop.
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
            
            password_valid = True
            os.system('cls')
            print("New user successfully added.")

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do not match")


def add_task():
    '''
    Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and 
    - the due date of the task.
    '''
    
    # Username input and validation  
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break
        
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    # Due date input and validation
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DSF)
            break

        except ValueError:
            print("Invalid datetime format. "
                  "Please use the format specified")

    # Get the current date.
    curr_date = date.today()

    # Task info to dictionary and add to list
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)

    # Write new task to file
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for task in task_list:
            str_attrs = [
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DSF),
                task['assigned_date'].strftime(DSF),
                "Yes" if task['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    
    os.system('cls')
    print("Task successfully added.")


def view_all():
    ''' 
    Reads the tasks from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''
    for t in task_list:
        disp_str  = f"{d_line}\n"
        disp_str += f"Task:{tab*2}\t{t['title']}\n"
        disp_str += f"Assigned to:{tab*2}{t['username']}\n"
        disp_str += f"Date Assigned:{tab*2}"
        disp_str += f"{t['assigned_date'].strftime(DSF)}\n"
        disp_str += f"Due Date:{tab*2}{t['due_date'].strftime(DSF)}\n\n"
        disp_str += f"Task Description:\n"
        disp_str += f"{d_line2}\n{t['description']}\n"
        print(disp_str)


def view_mine():
    ''' 
    Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''
    vm_menu = True
    while vm_menu:
        '''
        Display user's tasks and request input for 
        which task to edit/mark as complete
        '''
        while True:
            count_list = []
            for counter, t in enumerate(task_list):
                if t['username'] == curr_user:
                    disp_str  = f"{d_line}\n"
                    disp_str += f"Task:{tab*2}\t{t['title']}\n"
                    disp_str += f"Assigned to:{tab*2}{t['username']}\n"
                    disp_str += f"Date Assigned:{tab*2}"
                    disp_str += f"{t['assigned_date'].strftime(DSF)}\n"
                    disp_str += f"Due Date:{tab*2}"
                    disp_str += f"{t['due_date'].strftime(DSF)}\n\n"
                    disp_str += f"Task Description:\n"
                    disp_str += f"{d_line2}\n{t['description']}\n"
                    print(f"{d_line}\nTask no.:{tab*2}{counter}\n{disp_str}")
                    count_list.append(counter)
            
            try:
                edit_mark_task = input("If you wish to edit a task\n"
                                       f"Please enter corresponding number {count_list}:\n"
                                       "Or to go back, enter [-1]: ")
                os.system('cls')
                
                # Cast to integer to use as list index for task
                edit_mark_task = int(edit_mark_task)

                # Return to main menu with -1
                if edit_mark_task == -1:
                    edit_mark_menu = False
                    vm_menu = False
                    os.system('cls')
                    break

                if edit_mark_task not in count_list:
                    raise TypeError
                
                # Test if valid index within try/except block
                task_list[edit_mark_task]
                edit_mark_menu = True
                break

            except TypeError:
                os.system('cls')
                print(f"You have selected another user's task.")
                print(f"Please select from the following: {count_list}")
            
            except Exception:
                print("Invalid entry, please try again")

        # Request input for whether to edit task or mark as complete
        while edit_mark_menu:
            edit_mark = input("1. Edit task\n"
                              "2. Mark task as complete\n"
                              "3. Return to main menu: ")

            #=============== Edit Task ===================================#
            if edit_mark == '1':
                task_list[edit_mark_task]["username"] = input(
                    "Please enter new username for task: ")
                
                # Take new inputs and write task_list to file
                while True:
                    try:
                        task_due_date = input("Due date of task "
                                              "(YYYY-MM-DD): ")
                        task_list[edit_mark_task]["due_date"] = (
                            datetime.strptime(
                                task_due_date, DSF))
                        
                        task_list_to_file()
                        os.system('cls')

                        break

                    except ValueError:
                        print("Invalid datetime format. "
                              "Please use the format specified")

            #=============== Mark as complete ===========================#            
            elif edit_mark == '2':
                task_list[edit_mark_task]["completed"] = "Yes"

                task_list_to_file()
                os.system('cls')
            
            #=============== Main Menu ===================================#
            elif edit_mark == '3':
                edit_mark_menu = False
                vm_menu = False
                os.system('cls')

            #=============== Rewrite task_list to tasks.txt ===============#
            elif edit_mark == '4':
                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(
                                DSF),
                            t['assigned_date'].strftime(
                                DSF),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))

            else:
                print("Invalid entry, please try again")


def display_statistics():
    '''
    If the user is an admin they can display statistics about number of users
    and tasks.
    '''
    # Check if user.txt and tasks.txt exist
    # Create if not
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as f:
            pass
    
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as f:
            pass

    # Read from user.txt and task.txt
    with open("user.txt", "r") as f:
        read_users = f.read().split("\n")

    with open("tasks.txt", "r") as f:
        read_tasks = f.read().split("\n")
        read_tasks = [t for t in read_tasks if t != ""]

    # Display statistics
    print(f"{d_line}\n"
          f"Number of users: \t\t {len(read_users)}\n"
          f"Number of tasks: \t\t {len(read_tasks)}")
    

def generate_reports():
    '''
    Generate 2 files: [task_overview.txt] and [user_overview.txt]  
    task_overview shows:
        total no. of tasks, completed tasks, incomplete tasks
        % of incomplete tasks,  % of overdue and incomplete tasks
    user_overview shows (for each user):
        total no. of tasks, % of tasks assigned, % of complete tasks,
        % of incomplete tasks, % of incomplete and overdue tasks
    '''
    # Read tasks.txt to task_list
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Convert all tasks to dictionaries and add them to task_list list
    task_list = []
    for task_str in task_data:
        current_task = {}

        # Split by semicolon and manually add each component
        task_components = task_str.split(";")
        current_task['username'] = task_components[0]
        current_task['title'] = task_components[1]
        current_task['description'] = task_components[2]
        current_task['due_date'] = datetime.strptime(
            task_components[3], DSF)
        current_task['assigned_date'] = datetime.strptime(
            task_components[4], DSF)
        current_task['completed'] = (
            True if task_components[5] == "Yes" else False)

        task_list.append(current_task)

    # Task overview ======================================================#

    # Number of tasks
    total_tasks = len(task_list)
        
    # Number of finished and unfinished tasks
    finished_tasks = 0
    unfinished_tasks = 0

    for x in task_list:
        if x['completed'] == True:
            finished_tasks += 1
        else:
            unfinished_tasks += 1

    # Number of unfinished and overdue
    # Sort date data and compare to current date
    curr_date = date.today()
    curr_date = int(date.isoformat(
        curr_date).replace("-", "").strip(" 00:00:00"))

    overdue_tasks = 0
    for x in task_list:
        y = str(x['due_date']).replace("-", "").strip(" 00:00:00")
        if int(y) < curr_date and x['completed'] == False:
            overdue_tasks += 1

    # % of tasks incomplete
    incomplete_percent = (unfinished_tasks / total_tasks) * 100

    # % of tasks overdue
    overdue_percent = int((overdue_tasks / total_tasks) * 100)

    # Write to file formatted
    with open("task_overview.txt", "w") as file:
        file.write(f"{d_line}\n\n{tab*3}\t"
                   f"Task Overview\n\n"
                   f"{d_line}\n"
                   f"Total number of tasks:{tab*4}{total_tasks}\n"
                   f"{d_line2}\n"
                   f"Completed tasks:\t{tab*4}{finished_tasks}\n"
                   f"Incomplete tasks:\t{tab*4}{unfinished_tasks}\n"
                   f"Incomplete & overdue tasks:\t{tab*3}{overdue_tasks}\n"
                   f"{d_line2}\n"
                   f"% of tasks incomplete:"
                   f"{tab*4}{int(incomplete_percent)}%\n"
                   f"% of tasks incomplete & overdue:\t"
                   f"{tab*2}{overdue_percent}%\n"
                   f"{d_line}")
    
    # User overview ======================================================#

    # Read and store user.txt data
    with open("user.txt", "r") as file:
        user_data = file.read().split("\n")

    user_list = []
    for x in user_data:
        y = x.split(";")
        user_list.append(y[0])

    # Total no. of users
    total_users = len(user_list)

    # Number of tasks per user
    user_task_list = []
    for user in user_list:
        user_tasks = 0
        for task in task_list:
            if task['username'] == user:
                user_tasks += 1
        user_task_list.append(user_tasks)

    # Lists to store values for each user
    total_percent               = []
    total_complete_percent      = []
    total_incomplete_percent    = []
    total_overdue_percent       = []

    # Find user's percentage of total tasks
    for x in user_task_list:
        y = int((x / total_tasks) * 100)
        total_percent.append(y)

    # Find current date and cast to int for comparison
    curr_date = date.today()
    curr_date = int(date.isoformat(
        curr_date).replace("-", "").strip(" 00:00:00"))

    # Find for each user:
    ''' Percentage of completed tasks
        Percentage of incomplete tasks
        Percentage of overdue and incomplete tasks '''
    user_count = 0
    for user in user_list:
        complete_count = 0
        incomplete_count = 0
        overdue_tasks = 0
        for task in task_list:
            if task['completed'] == True and task['username'] == user:
                complete_count += 1

            elif task['completed'] == False and task['username'] == user:
                incomplete_count += 1

            y = str(task['due_date']).replace("-", "").strip(" 00:00:00")
            if int(y) < curr_date and task['completed'] == False:
                if task['username'] == user:
                    overdue_tasks += 1

        # Convert to % and account for zero division errors
        if user_task_list[user_count] > 0:
            x = int((complete_count / user_task_list[user_count])* 100)
            total_complete_percent.append(x)

            x = int((incomplete_count / user_task_list[user_count])* 100)
            total_incomplete_percent.append(x)

            x = int((overdue_tasks / user_task_list[user_count])* 100)
            total_overdue_percent.append(x)

        else:
            total_complete_percent.append(0)
            total_incomplete_percent.append(0)
            total_overdue_percent.append(0)

        user_count += 1

    # Build string for user_overview output
    user_print = (f"{d_line}\n\n{tab*3}\t"
                  f"User Overview\n\n"
                  f"{d_line}\nTotal registered users:"
                  f"{tab*4}{total_users}\n"
                  f"{d_line}\nTotal number of tasks:"
                  f"{tab*4}{total_tasks}\n{d_line}\n\n")
    
    # Iterate through lists
    for counter, x in enumerate(user_list):
        user_print += f"\nUsername:\t{tab*5}{x}\n{d_line}\n"
        user_print += f"Total tasks assigned to user:{tab*3}"
        user_print += f"{user_task_list[counter]}\n{d_line2}\n"
        user_print += f"% of total tasks assigned to user:\t{tab*2}"
        user_print += f"{total_percent[counter]}%\n{d_line2}\n"
        user_print += f"% of user's tasks completed:{tab*3}"
        user_print += f"{total_complete_percent[counter]}%\n{d_line2}\n"
        user_print += f"% of user's tasks incomplete:{tab*3}"
        user_print += f"{total_incomplete_percent[counter]}%\n{d_line2}\n"
        user_print += f"% of user's tasks incomplete and overdue:{tab}\t"
        user_print += f"{total_overdue_percent[counter]}%\n{d_line}\n\n"

    # Write to file
    with open("user_overview.txt", "w") as file:
        file.write(user_print)
    print("Successfully generated reports.")

# Variables to display outputs clearly to user
d_line = "=-"*35+'='
d_line2 = "-"*71
tab = "\t"*2

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# Convert all tasks to dictionaries and add them to task_list list
task_list = []
for task_str in task_data:
    current_task = {}

    # Split by semicolon and manually add each component
    task_components = task_str.split(";")
    current_task['username'] = task_components[0]
    current_task['title'] = task_components[1]
    current_task['description'] = task_components[2]
    current_task['due_date'] = datetime.strptime(
        task_components[3], DSF)
    current_task['assigned_date'] = datetime.strptime(
        task_components[4], DSF)
    current_task['completed'] = (
        True if task_components[5] == "Yes" else False)

    task_list.append(current_task)

# #==================== Login Section ========================#
'''
This code reads usernames and password from the user.txt file to 
allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Requests inputs for username/password and checks if correct
logged_in = False
while not logged_in:
    print("Please enter your username and password to login:")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
    else:
        print("\nLogin Successful!")
        logged_in = True

# Displays main menu
    '''
    Asks for input & converts to lower case
    Clears terminal after input for readability 
    '''
while logged_in:
    menu = input(f"{d_line}\n"
                 "Select one of the following options below:\n"
                 f"{d_line}\n"
                 "r  -\tRegister a new user\n"
                 "a  -\tAdd a new task\n"
                 "va -\tView all tasks\n"
                 "vm -\tView my tasks\n"
                 "gr -\tGenerate reports\n"
                 "ds -\tDisplay task statistics\n"
                 "e  -\tExit Task Manager\n"
                 f"{d_line}\n"
                 ": ").lower()
    
    os.system('cls')

    # r - Add a new user to the user.txt file
    if menu == 'r':
        reg_user()

    # a - Add a new task
    elif menu == 'a':
        add_task()

    # va - View all tasks
    elif menu == 'va':
        view_all()

    # vm - View current user's tasks only        
    elif menu == 'vm':
        view_mine()

    # gr - Generate reports
    elif menu == 'gr':
        generate_reports()

    # ds - Display statistics (only if user is admin)            
    elif menu == 'ds':
        if curr_user == 'admin':
            display_statistics()
        else:
            print(f"{d_line}\nData restricted to admin user only!")  

    # e - Exit program
    elif menu == 'e':
        print('Thank you for using the Task Manager!\n\nGoodbye!')
        exit()

    # Print error message if input is not a menu choice
    else:
        print("You have made a wrong choice, please try again")