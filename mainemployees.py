"""This program/module is for updating employees' data and attendance files.
Have methods for getting data from attendance file

NAVIGATION: The commands to the user.
call functions from other files.

"""
import employees


def main():
    """Call for user's choice and than for the appropriate function.

    :return: None
    """
    choice_dict = {1: employees.add_employee_manually,
                   2: employees.add_employees_from_file,
                   3: employees.del_employee_manually,
                   4: employees.del_employees_by_file,
                   5: employees.generate_employee_attendance,
                   6: employees.print_employees_attendance,
                   7: employees.print_late,
                   8: employees.mark_attendance,
                   9: employees.quit_this}
    while True:
        n = your_choice()
        print(f'\nGot your choice: {n}.')
        choice_dict[n]()
        want = input('\n Would you like to choose another option from main menu? Please Enter y/n: ')
        if want == 'n':
            employees.quit_this()
            break


def your_choice():
    """Display to user the index for choice, evaluate the input index and return it.

    :return: the index
    :rtype: int
    """
    choice = None
    while choice is None:
        print('\n To add directly employee to employees file--> 1\n\
            \n To add employees from file to employees file--> 2\n\
            \n To delete directly from employees file--> 3\n\
            \n To delete by file from employees file--> 4\n\
            \n To generate attendance report of an employee--> 5\n\
            \n To print a report for current month for all employees--> 6\n\
            \n To print an attendance report for all employees who were late--> 7\n\
            \n To mark attendance by employee--> 8\n\
            \n To quit--> 9')
        entry = input('\n Enter your choice: ')
        try:
            choice = int(entry)
            if choice not in range(1, 10):
                choice = None
                raise ValueError
        except ValueError:
            print('\n\tINPUT ERROR, try again.')
        else:
            return choice


if __name__ == '__main__':
    main()

