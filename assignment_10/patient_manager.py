import math

from patient import Patient
from procedure import Procedure


def create_patient():
    """Collect every patient field shown in the assignment sample."""
    print('Enter patient information:')
    first_name = input('First Name: ').strip()
    middle_name = input('Middle Name: ').strip()
    last_name = input('Last Name: ').strip()
    address = input('Address: ').strip()
    city = input('City: ').strip()
    state = input('State: ').strip()
    zip_code = input('ZIP: ').strip()
    phone = input('Phone: ').strip()
    emergency_contact = input('Emergency Contact: ').strip()
    emergency_phone = input('Emergency Phone: ').strip()
    return Patient(first_name, middle_name, last_name, address, city,
                   state, zip_code, phone, emergency_contact, emergency_phone)


def create_procedure():
    """Collect procedure details and require a finite positive charge."""
    print('\nEnter procedure information:')
    description = input('Description: ').strip()
    date = input('Date (e.g., 8-24-2019): ').strip()
    practitioner = input('Practitioner: ').strip()

    while True:
        try:
            charge = float(input('Enter the charge: '))
        except ValueError:
            print('Please enter a valid number for charge.')
            continue
        if math.isfinite(charge) and charge > 0:
            break
        print('Please enter a finite positive number for charge.')

    return Procedure(description, date, practitioner, charge)


def main():
    patient = create_patient()
    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")

    while True:
        answer = input('Add a procedure? (y/n): ').strip().lower()
        if answer == 'n':
            break
        if answer != 'y':
            print("Please enter 'y' or 'n'.")
            continue
        procedures.append(create_procedure())

    print('\nPatient and Procedure Information:')
    print(patient)
    total = 0.0
    for procedure in procedures:
        print()
        print(procedure)
        total += procedure.get_charge()
    print(f'\nTotal Charges: {total:.2f}')


if __name__ == '__main__':
    main()
