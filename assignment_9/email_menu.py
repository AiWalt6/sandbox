import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Keep the data file next to this script, regardless of the working folder.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    emails = load_emails()
    choice = get_user_choice()

    while choice != QUIT:
        changed = False
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            changed = add(emails)
        elif choice == CHANGE:
            changed = change(emails)
        elif choice == DELETE:
            changed = delete(emails)

        if changed:
            save_emails(emails)
        choice = get_user_choice()

    save_emails(emails)
    print('Email addresses saved. Goodbye!')


def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    # Only load trusted email.dat files created by this program.
    try:
        with open(FILENAME, 'rb') as input_file:
            emails = pickle.load(input_file)
    except FileNotFoundError:
        return {}
    except EOFError:
        if os.path.getsize(FILENAME) == 0:
            return {}
        raise ValueError('The email data file is incomplete.')

    if not isinstance(emails, dict):
        raise ValueError('The email data file must contain a dictionary.')
    for name in emails:
        if not isinstance(name, str) or not isinstance(emails[name], str):
            raise ValueError('Email names and addresses must be strings.')
    return emails


def get_user_choice():
    """Display the menu and return a validated choice."""
    print('\nMenu')
    print('-' * 55)
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
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


def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input('Enter a name: ').strip()
    if name in emails:
        print(f'Name: {name}')
        print(f'Email: {emails.get(name)}')
    else:
        print('The specified name was not found.')


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input('Enter name: ').strip()
    if not name:
        print('A name cannot be empty.')
        return False
    if name in emails:
        print('That name already exists.')
        return False

    address = input('Enter email address: ').strip()
    if not address:
        print('An email address cannot be empty.')
        return False
    emails[name] = address
    print('Name and address have been added.')
    return True


def change(emails):
    """Update the address for an existing name."""
    name = input('Enter name: ').strip()
    if name not in emails:
        print('The specified name was not found.')
        return False

    address = input('Enter the new address: ').strip()
    if not address:
        print('An email address cannot be empty.')
        return False
    emails[name] = address
    print('Information updated.')
    return True


def delete(emails):
    """Remove a name/address pair."""
    name = input('Enter name: ').strip()
    if name in emails:
        del emails[name]
        print('Information deleted.')
        return True
    print('The specified name was not found.')
    return False


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    with open(FILENAME, 'wb') as output_file:
        pickle.dump(emails, output_file)


if __name__ == '__main__':
    main()
