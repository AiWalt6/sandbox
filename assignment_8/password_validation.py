MIN_PASSWORD_LENGTH = 8


def validate_password(password):
    if len(password) < MIN_PASSWORD_LENGTH:
        print(
            f'Password must be at least {MIN_PASSWORD_LENGTH} characters long.'
        )
        return False

    if not password.isalnum():
        print('Password may only contain letters and digits.')
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        if character.islower():
            has_lowercase = True
        if character.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        print(
            'Password must contain at least one uppercase letter, '
            'one lowercase letter, and one digit.'
        )
        return False

    return True


def main():
    try:
        password = input('Enter a password: ')
    except EOFError:
        print('Error: No password was entered.')
        return

    if validate_password(password):
        print('Password is valid.')
    else:
        print('Password is invalid.')


if __name__ == '__main__':
    main()
