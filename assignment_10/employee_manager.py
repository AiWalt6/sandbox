import os
import pickle

from employee import Employee

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'employees.dat')


def main():
    employees = load_employees()
    choice = get_user_choice()

    while choice != QUIT:
        changed = False
        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            changed = add(employees)
        elif choice == CHANGE:
            changed = change(employees)
        elif choice == DELETE:
            changed = delete(employees)
        if changed:
            save_employees(employees)
        choice = get_user_choice()

    save_employees(employees)
    print('Employee information saved. Goodbye!')


def load_employees():
    # Only unpickle trusted files created by this program.
    try:
        with open(FILENAME, 'rb') as input_file:
            employees = pickle.load(input_file)
    except FileNotFoundError:
        return {}
    except EOFError:
        if os.path.getsize(FILENAME) == 0:
            return {}
        raise ValueError('The employee data file is incomplete.')

    if not isinstance(employees, dict):
        raise ValueError('The employee data file must contain a dictionary.')
    for id_number in employees:
        employee = employees[id_number]
        if (not isinstance(id_number, str)
                or not isinstance(employee, Employee)):
            raise ValueError('The file contains invalid employee records.')
        if id_number != employee.get_id_number():
            raise ValueError('An employee ID differs from its directory key.')
    return employees


def get_user_choice():
    print('\nMenu')
    print('-' * 55)
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit the program')

    while True:
        try:
            choice = int(input('\nEnter your choice: '))
        except ValueError:
            print('Invalid choice. Enter a number from 1 to 5.')
            continue
        if LOOK_UP <= choice <= QUIT:
            return choice
        print('Invalid choice. Enter a number from 1 to 5.')


def read_required(prompt):
    value = input(prompt).strip()
    while not value:
        print('This field cannot be empty.')
        value = input(prompt).strip()
    return value


def look_up(employees):
    id_number = read_required('Enter an employee ID number: ')
    if id_number in employees:
        print(employees[id_number])
    else:
        print('The specified ID number was not found')


def add(employees):
    name = read_required('Enter employee name: ')
    id_number = read_required('Enter employee ID number: ')
    if id_number in employees:
        print('That employee ID number already exists.')
        return False
    department = read_required('Enter employee department: ')
    title = read_required('Enter employee title: ')
    employees[id_number] = Employee(name, id_number, department, title)
    print('The new employee has been added.')
    return True


def change(employees):
    id_number = read_required('Enter employee ID number: ')
    if id_number not in employees:
        print('The specified ID number was not found')
        return False
    name = read_required('Enter the new name: ')
    department = read_required('Enter the new department: ')
    title = read_required('Enter the new title: ')
    employee = employees[id_number]
    employee.set_name(name)
    employee.set_department(department)
    employee.set_title(title)
    print('Employee information updated.')
    return True


def delete(employees):
    id_number = read_required('Enter employee ID number: ')
    if id_number in employees:
        del employees[id_number]
        print('Employee information deleted.')
        return True
    print('The specified ID number was not found')
    return False


def save_employees(employees):
    with open(FILENAME, 'wb') as output_file:
        pickle.dump(employees, output_file)


if __name__ == '__main__':
    main()
