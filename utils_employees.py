""" Util file for Employees' Data and Attendance."""


from datetime import datetime, timedelta  # To find previous month
import csv


def quit_this():
    """Display a gentle quiting message to the user.

    :rtype: None
     """
    print('\n You chose to quit.')


def employee_num(input_msg, len_num):

    """Show an input prompt with input_msg to user for employee's number (ID, phone).

        :param len_num: number of digits
        :type len_num: int
        :param input_msg: massage assigned by the caller
        :return: ID or phone number or for "quit"--->None
        :rtype: str, optional

        >>> 12345
        Input error.
        Please enter employee's ID number. Nine digits required.
        If you want to quit enter: "quit":
        >>> Q
        Input was blank or not digits only.
        Please enter employee's ID number. Nine digits required.
        If you want to quit enter: "quit":
        >>> 012345678
        Assigned number: 012345678.
        Please enter employee's name or enter "quit":
        >>>
         Input was blank or not digits only.
        Please enter employee's ten digit  phone number without a hyphen:
         If you want to quit enter: "quit":
        >>>0546397320
        Assigned number: 0546397320.
        Please type in employee's birth date as in mm/dd/yyyy format or enter "quit":
    """
    str_num = None
    while str_num is None:
        str_num = input(f'Please enter employee\'s {input_msg} \n If you want to quit enter: "quit": ')
        if str_num != 'quit':
            try:
                if isinstance(int(str_num), int) and len(str_num) == len_num and int(str_num) > 0:
                    print(f' Assigned number: {str_num}.')
                    return str_num  # Let the input remain type str.
                else:
                    print('\n Input error.')
                    str_num = None  # To continue the while loop.
            except ValueError:
                print('\n Input was blank or not digits only.')
                str_num = None  # To continue the while loop.
        else:
            quit_this()
            break


def employee_name():
    """Show an input prompt for user to insert a name.

    :return: the name which the user input or None
    :rtype: str, optional

    >>> 78
    Input error.
   Please enter employee's name or enter "quit":
    >>> sheri
     Assigned name: sheri.
    Please enter employee's ten digit  phone number without a hyphen:
     If you want to quit enter: "quit":
    """
    while True:
        entry1 = input(' Please enter employee\'s name or enter "quit": ')
        if entry1 != 'quit':
            if any(x.isalpha() for x in entry1) and all(x.isalpha() or x.isspace() for x in entry1):
                print(f' Assigned name: {entry1}.')
                return entry1
            else:
                print('\n Input error.')
        else:
            quit_this()
            break


def employee_birth_date():
    """Display the message to the user to input date of birth.

    :return: a birth date in mm/dd/yyyy format or None
    :rtype: datetime.datetime, optional
    >>> 3/12/168
    Incorrect format. Try again.
    Please type in employee's birth date as in mm/dd/yyyy format or enter "quit":
    >>> 02/15/1973

    Assigned birth date: 02/15/1973.

    Employee's  data added successfully to testmycsv3.csv.
    """
    while True:
        birth_date = input(' Please type in employee\'s birth date as in mm/dd/yyyy format or enter "quit": ')
        if birth_date != 'quit':
            try:
                # `strptime` throws an exception if the input doesn't match the pattern
                datetime.strptime(birth_date, "%m/%d/%Y")
                print(f'\n Assigned birth date: {birth_date}.')
                return birth_date
            except ValueError:
                print(' Incorrect format. Try again.')
        else:
            quit_this()
            break


def read_csv_file(csv_file_path):
    """Open and read the file csv_file_path and return a list of it's rows.

    :param csv_file_path: a path to a csv file between quotation marks
    :type csv_file_path: str
    :return :list of file rows
    :rtype: list [list [str]]
    """
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        list_rows = [row for row in csv_reader]
        return list_rows


def write_to_csv(csv_path, row1):
    """Open the file csv_path and write a row to it.

    :param csv_path: a path to a csv file between quotation marks
    :type csv_path: str
    :param row1: a list of row strings
    :type row1: list [str]
    """
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row1)


def update_file(origin_path, new_list):
    """Open the file and write to it the rows from list.

    :param origin_path: a path to a csv file between quotation marks
    :type origin_path: str
    :param new_list: rows of strings
    :type new_list: list [list [str]]
    :return: None
    """
    with open(origin_path, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(new_list)
        print('\n Employees csv file has been updated.')


def check_id_num(num, base_path):  # `num` has to be type str
    """Check if a str number is in first column of  main employees data csv.

    :param num: a number to be looked for
    :type num: str
    :param base_path: a path to a csv file to be checked
    :type base_path: str
    :return: True if found, False otherwise.
    :rtype: bool

    >>> '143567892'
    False
    >>> '014138453'
    True

    """
    data = [i[0] for i in read_csv_file(base_path)]
    if num in data:
        return True
    else:
        return False




def find_last_month():
    """Find the previous month.

    :return: last_month_year %m/%Y, last_bmonth_year %b%Y (%b - Abbreviated month name)
    :rtype: (datetime.datetime)
    """
    st_of_this_month = datetime.now().replace(day=1)
    last_month = st_of_this_month - timedelta(days=1)
    last_month_year = last_month.strftime('%m/%Y')
    last_bmonth_year = last_month.strftime('%b%Y')
    return last_month_year, last_bmonth_year


def approve_file():
    """Show an input prompt for the user to insert a file path.

    :return: tuple (`True` if there is no missing data in the file,` False `otherwise , a file path) or defaults to None
    :rtype: (bool, str), optional

    Exemple:

        to test correct file use testmycsv.csv
        to test file missing data use testmycsv2.csv
        for file with only a header use testmycsv1.csv

    """
    csv_file = None
    while csv_file is None:
        entry = input('\n Please enter the path to your file If you want to quit enter: "quit": ')
        if entry != 'quit':
            csv_file_path = entry
            try:
                with open(csv_file_path, 'r') as csv_file:
                    try:
                        csv_reader = csv.reader(csv_file)
                    except csv.Error:
                        print('\n Error in reading csv file')
                        csv_file = None
                    else:
                        csv_file = entry
                        # First line is the header with names of columns.
                        next(csv_reader)
                        for i in enumerate(csv_reader):
                            # If file empty, len(i) will return 'None'
                            if len(i):
                                # Means file not empty of data. len(i) is two. i[1] is the whole row.
                                if '' in i[1] or 'None' in i[1]:
                                    # Missing data
                                    return False, csv_file
                                else:
                                    return True, csv_file
                            else:
                                break
            except IOError:
                print(f'\n I/O error(file not found/ file can not be opened). Try again.')
                csv_file = None
        else:
            quit_this()
            # for quiting while loop csv_file has not to be None
            csv_file = 2


def print_csv_attend_file(attend_csv_path):
    """Print the rows of the given file.

    :param attend_csv_path: a path to a csv file between quotation marks
    :type attend_csv_path: str
    :return: None

    """
    for row2 in (read_csv_file(attend_csv_path)):
        print(row2)


def append_to_csv(csv_path, row3):
    """Add row to the  file.

    :param csv_path: a path to a csv file between quotation marks
    :type csv_path: str
    :param row3: a row as list of data strings
    :type row3: list [str]
    :return: a path to a file csv_path that a row has been written to
    :rtype: str


    """
    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row3)
    return csv_path


def unique_list_id(file1, file4):
    """Return list of rows from file file1 that are not in file file4.

    :param file1: a path to a csv file from which rows will be returned in a list
    :type file1: str
    :param file4: a path to a csv file which rows won't be returned
    :type file4: str
    :return: A list of row strings without the header row therefor updated[1:],can be empty.
    :rtype: list [str]

    ..warning: file1, file2  are csv paths between quotation marks.

    """
    # seen[1:]=list of column[0] without the header line
    seen = [i[0] for i in read_csv_file(file1)]
    updated = [j for j in read_csv_file(file4) if j[0] not in seen[1:]]
    return updated[1:]  # Without the header row from file4




