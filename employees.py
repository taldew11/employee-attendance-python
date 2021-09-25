"""The main functions for Employees' Data and Attendance."""

from datetime import datetime
import csv
from utils_employees import quit_this, employee_num, employee_name, employee_birth_date, read_csv_file
from utils_employees import write_to_csv, update_file, approve_file, print_csv_attend_file, check_id_num
from utils_employees import find_last_month, unique_list_id, append_to_csv


def add_employee_manually():
    """display messages to the user to input all employee's data
    and add it to the employees' data file.

    :rtype: None

    .. note:: main employees data csv path = testmycsv3.csv

    """
    input_msg_id = 'ID number. Nine digits required.'
    id_num2 = employee_num(input_msg_id, len_num=9)
    base_path6 = 'testmycsv3.csv'
    if id_num2 is not None:
        if check_id_num(id_num2, base_path6):
            print('\n This employee already exists in file')
        else:
            name = employee_name()
            input_msg_phone = 'ten digit  phone number without a hyphen: '
            phone_num = employee_num(input_msg_phone, len_num=10)
            birth_date = employee_birth_date()
            employee_data = [id_num2, name, birth_date, phone_num]
            # Initialize the variable with None value before if conditions.
            updated1_csv = None
            if None not in employee_data:
                main_employees_file = 'testmycsv3.csv'
                updated1_csv = append_to_csv(main_employees_file, employee_data)
                print(f'\n Employee\'s  data added successfully to {updated1_csv}.')


def add_employees_from_file():
    """Add employees' data from a file to main employees' file.

    :rtype:None

    .. note:: main employees data csv path = testmycsv3.csv.
    ...warning:: No missing data permitted.

    ..exemples::

     testmycsv1.csv

    The file is empty of data
     testmycsv2.csv

    Input file: testmycsv2.csv, has missing data. Process will not continue.
     testmycsv.csv

    Data has been added successfully.

    """
    updated2_csv = None
    app = approve_file()
    if app is None:
        print('\n The file is empty of data')
    elif app[0] is False:
        print(f'\n Input file: {app[1]}, has missing data. Process will not continue.')
    elif app[0] is True:
        the_input_file = app[1]
        base_path1 = 'testmycsv3.csv'
        updated2 = unique_list_id(base_path1, the_input_file)
        if len(updated2) != 0:
            for ii in updated2:
                updated2_csv = append_to_csv(base_path1, ii)
            print(f'\n Data has been added successfully to {updated2_csv}.')
        else:
            print(f'\n Data from input file is already in main file.')


def del_employee_manually():
    """Delete employee from employees' data file using the ID number input from the user.

    :rtype: None

    .. note:: main employees data csv path = testmycsv3.csv.

    """
    base_path2 = 'testmycsv3.csv'
    input_msg_id1 = 'ID number. Nine digits required.'
    id_num3 = employee_num(input_msg_id1, len_num=9)
    if id_num3 is not None:
        # Check if ID is in csv file of employees
        if check_id_num(id_num3, base_path2):
            updated_list = [i for i in read_csv_file(base_path2) if i[0] != id_num3]
            update_file(base_path2, updated_list)
        else:
            print(f'\n ID {id_num3} is not in employees csv file.')


def del_employees_by_file():
    """Delete employees written on input file from main employees' file.

    :rtype:None

    .. note:: Main employees data csv path = testmycsv3.csv.
    ...warning:: No missing data permitted in input file.
    ..example:: Deleting testmycsv.csv. from testmycsv3.csv if you added them before.
         Deleting testmycsv.csv. from testmycsv3.csv leaves only the header.
    >>> testmycsv1.csv

    The file is empty of data
    >>> testmycsv2.csv

    Input file: testmycsv2.csv, has missing data. Process will not continue.

    """
    app = approve_file()
    if app is None:
        print('\n The file is empty of data')
    elif app[0] is False:
        print(f'\n Input file: {app[1]}, has missing data. Process will not continue.')
    elif app[0] is True:
        the_file1 = app[1]
        base_path4 = 'testmycsv3.csv'
        updated3 = unique_list_id(the_file1, base_path4)
        columns = ['employeeid_num', 'name', 'birthdate', 'phonumber']
        write_to_csv(base_path4, columns)
        for row5 in updated3:
            append_to_csv(base_path4, row5)
        print('\n File updated.')


def mark_attendance():
    """Use employee's input ID number to mark attendance in the main attendance file.

    :rtype: None

    .. note:: main employees attendance csv path = myattendancecsv2.csv.

    """
    while True:
        input_msg_id2 = 'ID number. Nine digits required.'
        id_num1 = employee_num(input_msg_id2, len_num=9)
        base_path3 = 'testmycsv3.csv'
        if id_num1 is not None:
            # Check if ID is in csv file of employees
            if check_id_num(id_num1, base_path3):
                time_in = datetime.now().strftime('%H:%M:%S')
                date_in = datetime.today().strftime('%m/%d/%Y')
                employee_in_data = [id_num1, date_in, time_in]
                attendance_main = 'myattendancecsv2.csv'
                append_to_csv(attendance_main, employee_in_data)
                print('\n Attendance marked.')
                break
            else:
                want1 = input('\n There is no employee with this ID number. Would you like to try again? Enter y/n: ')
                if want1 == 'n':
                    quit_this()
                    break


def generate_employee_attendance():
    """Generate employee attendance file for ID number inserted by user.

    :return: csv file path for employee's attendance.
    :rtype: str

    .. note:: main employees attendance csv path = myattendancecsv2.csv.

    """
    while True:
        input_msg_id3 = 'ID number. Nine digits required.'
        id_num4 = employee_num(input_msg_id3, len_num=9)
        base_path5 = 'testmycsv3.csv'
        attend_file = 'myattendancecsv2.csv'
        if id_num4 is not None:
            # Check if id_num4 in employees file
            if check_id_num(id_num4, base_path5):
                csv_for_employee1 = csv_employee_attendance(id_num4, attend_file)
                for i in read_csv_file(csv_for_employee1):
                    print(f'\n {id_num4}\'s attendance report csv path is: {csv_for_employee1}.')
                    return csv_for_employee1
            else:
                want2 = input('\n There is no employee with this ID number. Would you like to try again? Enter y/n: ')
                if want2 == 'n':
                    quit_this()
                    break


def csv_employee_attendance(id_num7, csv_attendance_file):
    """Generate an attendance log file of an employee.

    :param id_num7: employee's ID number
    :type id_num7: str
    :param csv_attendance_file: employees' attendance log file path
    :return: an employee's attendance log file path.
    :rtype: str
    """
    # Creating the file path and preparing a file for a particular employee.
    csv_for_employee = 'attend' + id_num7 + '.csv'
    columns = ['Employee ID', 'Date', 'Time In']
    write_to_csv(csv_for_employee, columns)
    # Initialize the variable with None value before if conditions.
    updated_csv = None
    if check_id_num(id_num7, csv_attendance_file):
        for i in read_csv_file(csv_attendance_file):
            if id_num7 == i[0]:
                updated_csv = append_to_csv(csv_for_employee, i)
        return updated_csv
    else:
        return csv_for_employee


def print_employees_attendance():
    """Print employees attendance on previous month.

    :rtype: None

    """
    emplos_attend, last_month1 = employees_attend_month()  # Assign returned tuple
    print(f'\n Employees {last_month1} attendance report csv path is {emplos_attend} .')
    print_csv_attend_file(emplos_attend)


def print_late(list_of_csvs=None):  # A csv file with employees attendance of previous month
    """Print employees' attendance log if were late than 9:30 AM on previous month.

    :param list_of_csvs: a list of csv path strings, defaults to None
    :type list_of_csvs: list [str], optional
    :rtype: None
    """
    # To instantiate a new list for every new call.
    if list_of_csvs is None:
        list_of_csvs = []
    # Assign from returned tuple
    the_attend_file = employees_attend_month()[0]
    late_emplo = find_late(the_attend_file)
    if len(late_emplo) == 0:
        print('\n No employee was late.')
    elif len(late_emplo) > 1:
        for id_num5 in late_emplo:
            csv_file_path1 = csv_employee_attendance(id_num5, the_attend_file)
            print(f'\n {id_num5}\'s attendance report csv path is {csv_file_path1}.')
            print_csv_attend_file(csv_file_path1)
    elif len(late_emplo) == 1:
        csv_file_path1 = csv_employee_attendance(late_emplo, the_attend_file)
        print(f'\n {late_emplo}\'s attendance report csv path is {csv_file_path1}.')
        print_csv_attend_file(csv_file_path1)


def find_late(csv1_file, ids_list=None):
    """
    :param csv1_file: a path to a csv file between quotation marks
    :type csv1_file: str
    :param ids_list: a list of ID number strings, defaults to None
    :type ids_list: list [str]
    :return:  a list of ID number strings
    :rtype: list [str]
    """
    if ids_list is None:  # To instantiate a new list for every new call.
        ids_list = []
    time_late = '09:30:00'
    time_a = datetime.strptime(time_late, '%H:%M:%S')
    #  strptime() is a class method in datetime class.converts string to datetime object.
    with open(csv1_file, "r") as csv_file1:
        csv_reader = csv.reader(csv_file1)
        next(csv_reader)
        for row4 in csv_reader:
            time_in = row4[2]
            time_b = datetime.strptime(time_in, '%H:%M:%S')
            id_num6 = row4[0]
            if time_b > time_a:
                ids_list.append(id_num6)
    ids_sort_list = sorted(ids_list)
    return ids_sort_list


def employees_attend_month():
    """Create a file for employees' attendance in previous month.

    :return: tuple (a path to csv file, last month %m/%Y format)
    :rtype: (str, datetime.datetime)

    ..note:: Uses employees' attendance file path as string 'myattendancecsv2.csv'
    :example:

    """
    # Assign returned tuple
    last_monthyear, last_bmonthyear = find_last_month()
    attend_file = 'myattendancecsv2.csv'
    employees_attend_file = 'attend' + last_bmonthyear + '.csv'
    columns = ['ID num', 'Date', 'Time in']
    write_to_csv(employees_attend_file, columns)
    for i in read_csv_file(attend_file)[1:]:
        date_month = i[1][:3] + i[1][6:]  # i[1] = mm/dd/yyyy format
        if date_month == last_monthyear:  # mm/yyyy format
            append_to_csv(employees_attend_file, i)
    return employees_attend_file, last_monthyear







