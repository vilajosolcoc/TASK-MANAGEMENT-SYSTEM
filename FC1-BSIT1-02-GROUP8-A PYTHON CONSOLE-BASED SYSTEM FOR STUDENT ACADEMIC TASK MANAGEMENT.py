from datetime import date

accounts = {}
tasks = {}

while True:
    print("\n==== STUDENT TASK MANAGEMENT SYSTEM ====")
    print("1. Register Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # REGISTER ACCOUNT
    if choice == "1":
        print("\n==== REGISTER ACCOUNT ====")

        student_id = input("Enter Student ID (00-0000-000000): ")

        if (len(student_id) != 14 or student_id[2] != "-"
                or student_id[7] != "-"
                or not (student_id[:2] + student_id[3:7]
                        + student_id[8:]).isdigit()):

            print("Error: Invalid Student ID format.")

        elif student_id in accounts:
            print("Error: Account already exists.")
            print("Please log in using your existing credentials.")

        else:
            while True:
                password = input("Create password: ")

                has_uppercase = False
                has_lowercase = False
                has_number = False
                has_symbol = False

                symbols = "!@#$%^&*()-_+=[]{};:,.?/"

                for character in password:
                    if character.isupper():
                        has_uppercase = True
                    elif character.islower():
                        has_lowercase = True
                    elif character.isdigit():
                        has_number = True
                    elif character in symbols:
                        has_symbol = True

                if (len(password) >= 6
                        and has_uppercase
                        and has_lowercase
                        and has_number
                        and has_symbol):

                    accounts[student_id] = password
                    tasks[student_id] = []

                    print(
                        "\033[94mAccount registered successfully!\033[0m"
                    )
                    break

                else:
                    print(
                        "Error: Password must contain at least 6 characters, "
                        "one uppercase letter, one lowercase letter, "
                        "one number, and one symbol. Please try again."
                    )

    # LOGIN
    elif choice == "2":
        print("\n==== LOGIN ====")

        student_id = input("Enter Student ID: ")

        if student_id not in accounts:
            print("Error: Student ID not found. Please register first.")

        else:
            while True:
                password = input("Enter password: ")

                if accounts[student_id] == password:
                    print("\033[92mLog in successful!\033[0m")
                    break

                else:
                    print("Incorrect password. Please try again.")

            # TASK MANAGEMENT MENU
            while True:
                print("\n==== TASK MANAGEMENT SYSTEM ====")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Update Task")
                print("4. Mark as Completed")
                print("5. Delete Task")
                print("6. Logout")

                option = input("Enter your choice: ")

                # ADD TASK
                if option == "1":
                    print("\n==== ADD TASK ====")

                    subjects = [
                        "GEN 001 - PURPOSIVE COMMUNICATION",
                        "GEN 002 - UNDERSTANDING THE SELF",
                        "GEN 0006 - ETHICS",
                        "ITE 260 - COMPUTER PROGRAMMING 1",
                        "ITE 366 - INTRODUCTION TO COMPUTING",
                        "MAT 152 - MATHEMATICS IN THE MODERN WORLD",
                        "NST 021 - NATIONAL SERVICE TRAINING PROGRAM 1",
                        "PED 030 - PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS (PATHFIT1)"
                    ]

                    print("\n==== SELECT SUBJECT ====")

                    for i in range(len(subjects)):
                        print("{}. {}".format(i + 1, subjects[i]))

                    while True:
                        subject_choice = input(
                            "Choose subject number (1-8): "
                        )

                        if subject_choice in [
                            "1", "2", "3", "4", "5", "6", "7", "8"
                        ]:
                            subject = subjects[int(subject_choice) - 1]
                            break

                        else:
                            print(
                                "Error: Invalid subject choice. "
                                "Please select from 1 to 8."
                            )

                    while True:
                        task_name = input("Task name: ").strip()

                        if task_name == "":
                            print(
                                "Error: Task name cannot be empty. "
                                "Please try again."
                            )
                        else:
                            break

                    while True:
                        due_date = input("Due date (YYYY-MM-DD): ")

                        if (len(due_date) != 10
                                or due_date[4] != "-"
                                or due_date[7] != "-"
                                or not (
                                    due_date[:4] + due_date[5:7]
                                    + due_date[8:]
                                ).isdigit()):

                            print(
                                "Invalid date format. Please enter "
                                "the date as YYYY-MM-DD."
                            )

                        else:
                            year = int(due_date[:4])
                            month = int(due_date[5:7])
                            day = int(due_date[8:10])

                            if month < 1 or month > 12:
                                print(
                                    "Invalid month. Please enter "
                                    "a month from 01 to 12."
                                )

                            else:
                                try:
                                    task_date = date(year, month, day)
                                    break

                                except ValueError:
                                    print(
                                        "Invalid calendar date. "
                                        "Please enter a valid date again."
                                    )

                    task = [
                        task_name,
                        subject,
                        due_date,
                        "Pending",
                        "-"
                    ]

                    tasks[student_id].append(task)

                    # Sort tasks from earliest to latest due date
                    for i in range(len(tasks[student_id])):
                        for j in range(i + 1, len(tasks[student_id])):
                            if (tasks[student_id][i][2]
                                    > tasks[student_id][j][2]):

                                temporary = tasks[student_id][i]
                                tasks[student_id][i] = tasks[student_id][j]
                                tasks[student_id][j] = temporary

                    print("Task added successfully!")

                # VIEW TASKS
                elif option == "2":
                    print("\n==== STUDENT TASK LIST ====")

                    today = date.today()
                    print("Current Date:", today)

                    if tasks[student_id] == []:
                        print("No tasks available.")

                    else:
                        # Sort tasks by nearest deadline
                        for i in range(len(tasks[student_id])):
                            for j in range(i + 1, len(tasks[student_id])):
                                if (tasks[student_id][i][2]
                                        > tasks[student_id][j][2]):

                                    temporary = tasks[student_id][i]
                                    tasks[student_id][i] = tasks[student_id][j]
                                    tasks[student_id][j] = temporary

                        # Update overdue incomplete tasks to Missing
                        for task in tasks[student_id]:
                            due = date(
                                int(task[2][:4]),
                                int(task[2][5:7]),
                                int(task[2][8:10])
                            )

                            if task[3] != "Completed" and due < today:
                                task[3] = "Missing"

                        print("=" * 105)
                        print("{:<5} {:<21} {:<15} {:<13} {:<19} {}".format(
                            "No.", "Task Name", "Subject", "Due Date",
                            "Deadline Status", "Task Status"
                        ))
                        print("=" * 105)

                        number = 1

                        for task in tasks[student_id]:
                            due = date(
                                int(task[2][:4]),
                                int(task[2][5:7]),
                                int(task[2][8:10])
                            )

                            if task[3] == "Completed":
                                deadline_status = "COMPLETED"

                            elif due < today:
                                deadline_status = "OVERDUE"

                            elif due == today:
                                deadline_status = "DUE TODAY"

                            elif (due - today).days == 1:
                                deadline_status = "DUE TOMORROW"

                            else:
                                deadline_status = "DUE IN {} DAYS".format(
                                    (due - today).days
                                )

                            # Color the task status for display
                            if task[3] == "Missing":
                                status = "\033[91m" + "{:<15}".format("Missing") + "\033[0m"
                            elif task[3] == "Pending":
                                status = "\033[93m" + "{:<15}".format("Pending") + "\033[0m"
                            elif task[3] == "Completed":
                                status = "\033[92m" + "{:<15}".format("Completed") + "\033[0m"
                            else:
                                status = task[3]

                            print("{:<5} {:<21} {:<15} {:<13} {:<19} {}".format(
                                number,
                                task[0][:20],
                                task[1][:14],
                                task[2],
                                deadline_status,
                                status
                            ))

                            print("-" * 105)
                            number = number + 1

                # UPDATE TASK
                elif option == "3":
                    print("\n==== UPDATE TASK ====")

                    if tasks[student_id] == []:
                        print("No tasks available to update.")

                    else:
                        # Sort tasks by nearest deadline
                        for i in range(len(tasks[student_id])):
                            for j in range(i + 1, len(tasks[student_id])):
                                if (tasks[student_id][i][2]
                                        > tasks[student_id][j][2]):

                                    temporary = tasks[student_id][i]
                                    tasks[student_id][i] = tasks[student_id][j]
                                    tasks[student_id][j] = temporary

                        # Display tasks in table format
                        print("\n==== SELECT TASK TO UPDATE ====")

                        print("=" * 100)
                        print("{:<5} {:<25} {:<35} {:<15} {}".format(
                            "No.",
                            "Task Name",
                            "Subject",
                            "Due Date",
                            "Status"
                        ))
                        print("=" * 100)

                        number = 1

                        for task in tasks[student_id]:
                            if task[3] == "Missing":
                                status = "\033[91m" + "{:<15}".format("Missing") + "\033[0m"
                            elif task[3] == "Pending":
                                status = "\033[93m" + "{:<15}".format("Pending") + "\033[0m"
                            elif task[3] == "Completed":
                                status = "\033[92m" + "{:<15}".format("Completed") + "\033[0m"
                            else:
                                status = task[3]

                            print("{:<5} {:<25} {:<35} {:<15} {}".format(
                                number,
                                task[0][:24],
                                task[1][:34],
                                task[2],
                                status
                            ))
                            number = number + 1

                        print("=" * 100)

                        # Validate task selection
                        while True:
                            task_choice = input("Choose task to update: ")

                            if task_choice in [
                                str(i + 1)
                                for i in range(len(tasks[student_id]))
                            ]:
                                selected_task = tasks[student_id][
                                    int(task_choice) - 1
                                ]
                                break

                            else:
                                print(
                                    "Error: Invalid task number. "
                                    "Please try again."
                                )

                        # Choose what to update
                        while True:
                            print("\\nWhat would you like to update?")
                            print("1. Change Due Date Only")
                            print("2. Change Task Status Only")
                            print("3. Change Both Due Date and Status")

                            update_choice = input("Enter choice (1-3): ")

                            if update_choice in ["1", "2", "3"]:
                                break

                            else:
                                print(
                                    "Error: Invalid choice. "
                                    "Please select 1, 2, or 3."
                                )

                        # Keep the existing values unless the user changes them
                        new_due_date = selected_task[2]
                        new_status = selected_task[3]

                        # Update due date only or update both
                        if update_choice == "1" or update_choice == "3":
                            while True:
                                new_due_date = input(
                                    "New due date (YYYY-MM-DD): "
                                )

                                if (len(new_due_date) != 10
                                        or new_due_date[4] != "-"
                                        or new_due_date[7] != "-"
                                        or not (
                                            new_due_date[:4] + new_due_date[5:7]
                                            + new_due_date[8:]
                                        ).isdigit()):

                                    print(
                                        "Invalid date format. "
                                        "Please enter a new valid due date."
                                    )

                                else:
                                    year = int(new_due_date[:4])
                                    month = int(new_due_date[5:7])
                                    day = int(new_due_date[8:10])

                                    if month < 1 or month > 12:
                                        print(
                                            "Invalid calendar date. "
                                            "Please enter a new valid due date."
                                        )

                                    else:
                                        try:
                                            new_date = date(year, month, day)
                                            break

                                        except ValueError:
                                            print(
                                                "Invalid calendar date. "
                                                "Please enter a new valid due date."
                                            )

                        # Choose task status only or update both
                        if update_choice == "2" or update_choice == "3":
                            while True:
                                print("\\nChoose task status:")
                                print("1. Pending")
                                print("2. Completed")

                                status_choice = input("Enter choice (1-2): ")

                                if status_choice == "1":
                                    new_status = "Pending"
                                    break

                                elif status_choice == "2":
                                    new_status = "Completed"
                                    break

                                else:
                                    print(
                                        "Error: Invalid status choice. "
                                        "Please select 1 or 2."
                                    )

                        # Apply changes after valid inputs
                        selected_task[2] = new_due_date
                        selected_task[3] = new_status

                        # Update overdue incomplete tasks to Missing
                        today = date.today()
                        updated_date = date(
                            int(selected_task[2][:4]),
                            int(selected_task[2][5:7]),
                            int(selected_task[2][8:10])
                        )

                        if (selected_task[3] != "Completed"
                                and updated_date < today):
                            selected_task[3] = "Missing"

                        # Clear the old pending reason field if it exists
                        if len(selected_task) > 4:
                            selected_task[4] = "-"

                        # Sort tasks again after updating the due date
                        for i in range(len(tasks[student_id])):
                            for j in range(i + 1, len(tasks[student_id])):
                                if (tasks[student_id][i][2]
                                        > tasks[student_id][j][2]):

                                    temporary = tasks[student_id][i]
                                    tasks[student_id][i] = tasks[student_id][j]
                                    tasks[student_id][j] = temporary

                        print("\nTask updated successfully!")
                        print("=" * 100)
                        print("{:<25} {:<35} {:<15} {}".format(
                            "Task Name",
                            "Subject",
                            "Updated Due Date",
                            "Task Status"
                        ))
                        print("=" * 100)

                        if selected_task[3] == "Missing":
                            status = "\033[91m" + "{:<15}".format("Missing") + "\033[0m"
                        elif selected_task[3] == "Pending":
                            status = "\033[93m" + "{:<15}".format("Pending") + "\033[0m"
                        elif selected_task[3] == "Completed":
                            status = "\033[92m" + "{:<15}".format("Completed") + "\033[0m"
                        else:
                            status = selected_task[3]

                        print("{:<25} {:<35} {:<15} {}".format(
                            selected_task[0][:24],
                            selected_task[1][:34],
                            selected_task[2],
                            status
                        ))
                        print("=" * 100)

                # MARK AS COMPLETED
                elif option == "4":
                    print("\n==== MARK TASK AS COMPLETED ====")

                    if tasks[student_id] == []:
                        print("No tasks available to complete.")

                    else:
                        print("\n==== SELECT TASK TO COMPLETE ====")

                        print("=" * 100)
                        print("{:<5} {:<25} {:<35} {:<15} {}".format(
                            "No.",
                            "Task Name",
                            "Subject",
                            "Due Date",
                            "Status"
                        ))
                        print("=" * 100)

                        number = 1

                        for task in tasks[student_id]:
                            if task[3] == "Missing":
                                status = "\033[91m" + "{:<15}".format("Missing") + "\033[0m"
                            elif task[3] == "Pending":
                                status = "\033[93m" + "{:<15}".format("Pending") + "\033[0m"
                            elif task[3] == "Completed":
                                status = "\033[92m" + "{:<15}".format("Completed") + "\033[0m"
                            else:
                                status = task[3]

                            print("{:<5} {:<25} {:<35} {:<15} {}".format(
                                number,
                                task[0][:24],
                                task[1][:34],
                                task[2],
                                status
                            ))
                            number = number + 1

                        print("=" * 100)

                        # Validate task selection
                        while True:
                            task_choice = input(
                                "Choose a task to complete: "
                            )

                            if task_choice in [
                                str(i + 1)
                                for i in range(len(tasks[student_id]))
                            ]:
                                selected_task = tasks[student_id][
                                    int(task_choice) - 1
                                ]
                                break

                            else:
                                print(
                                    "Error: Invalid task number. "
                                    "Please try again."
                                )

                        # Check whether the task is already completed
                        if selected_task[3] == "Completed":
                            print("This task is already completed.")

                        else:
                            selected_task[3] = "Completed"

                            # Clear the old pending reason field if it exists
                            if len(selected_task) > 4:
                                selected_task[4] = "-"

                            # Show the completed task in table format
                            print("\n\033[92mTask marked as completed!\033[0m")
                            print("=" * 100)
                            print("{:<5} {:<25} {:<35} {:<15} {}".format(
                                "No.",
                                "Task Name",
                                "Subject",
                                "Due Date",
                                "Status"
                            ))
                            print("=" * 100)
                            print("{:<5} {:<25} {:<35} {:<15} {}".format(
                                1,
                                selected_task[0][:24],
                                selected_task[1][:34],
                                selected_task[2],
                                "\033[92m" + "{:<15}".format("Completed") + "\033[0m"
                            ))
                            print("=" * 100)

                # DELETE TASK
                elif option == "5":
                    print("\n==== DELETE TASK ====")

                    if tasks[student_id] == []:
                        print("No tasks available to delete.")

                    else:
                        print("\n==== SELECT TASK TO DELETE ====")

                        print("=" * 100)
                        print("{:<5} {:<25} {:<35} {:<15} {}".format(
                            "No.",
                            "Task Name",
                            "Subject",
                            "Due Date",
                            "Status"
                        ))
                        print("=" * 100)

                        number = 1

                        for task in tasks[student_id]:
                            if task[3] == "Missing":
                                status = "\033[91m" + "{:<15}".format("Missing") + "\033[0m"
                            elif task[3] == "Pending":
                                status = "\033[93m" + "{:<15}".format("Pending") + "\033[0m"
                            elif task[3] == "Completed":
                                status = "\033[92m" + "{:<15}".format("Completed") + "\033[0m"
                            else:
                                status = task[3]

                            print("{:<5} {:<25} {:<35} {:<15} {}".format(
                                number,
                                task[0][:24],
                                task[1][:34],
                                task[2],
                                status
                            ))
                            number = number + 1

                        print("=" * 100)

                        # Validate task selection
                        while True:
                            task_choice = input("Choose a task to delete: ")

                            if task_choice in [
                                str(i + 1)
                                for i in range(len(tasks[student_id]))
                            ]:
                                selected_task = tasks[student_id][
                                    int(task_choice) - 1
                                ]
                                break

                            else:
                                print(
                                    "Error: Invalid task number. "
                                    "Please try again."
                                )

                        # Confirm before deleting
                        print("\nSelected Task:", selected_task[0])
                        print("Subject:", selected_task[1])

                        while True:
                            confirmation = input(
                                "Are you sure you want to delete this task? (Y/N): "
                            ).strip().upper()

                            if confirmation == "Y":
                                tasks[student_id].remove(selected_task)
                                print("Task deleted successfully!")
                                break

                            elif confirmation == "N":
                                print("Task deletion cancelled.")
                                break

                            else:
                                print("Invalid choice. Please enter Y or N.")

                # LOGOUT
                elif option == "6":
                    print("\033[91mLogged out successfully!\033[0m")
                    break

                else:
                    print("Invalid choice. Enter 1 to 6.")

    # EXIT
    elif choice == "3":
        print(
            "\033[1;3;97m"
            "Thank you for using the Student Task Management System!"
            "\033[0m"
        )
        print(
            "\033[1;3;95m"
            "Have a great day and good luck with your studies!"
            "\033[0m"
        )
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")