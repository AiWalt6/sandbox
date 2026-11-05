MONTH_NAMES = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def parse_date(date_text):
    parts = date_text.strip().split('/')
    if len(parts) != 3:
        raise ValueError('Date must be in mm/dd/yyyy format with slashes.')

    for part in parts:
        if not part.isdigit():
            raise ValueError('Month, day, and year must contain only digits.')

    if not (1 <= len(parts[0]) <= 2 and 1 <= len(parts[1]) <= 2
            and len(parts[2]) == 4):
        raise ValueError('Date must be in mm/dd/yyyy format with slashes.')

    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])

    if not 1 <= month <= 12:
        raise ValueError('Month must be between 1 and 12.')
    if not 1 <= day <= 31:
        raise ValueError('Day must be between 1 and 31.')
    if year == 0:
        raise ValueError('Year must be between 0001 and 9999.')

    days_in_month = MONTH_DAYS[month - 1]
    if month == 2 and (year % 400 == 0
                       or (year % 4 == 0 and year % 100 != 0)):
        days_in_month = 29

    if day > days_in_month:
        raise ValueError(
            f'{MONTH_NAMES[month - 1]} {year} has only {days_in_month} days.'
        )

    return f'{MONTH_NAMES[month - 1]} {day}, {year}'


def main():
    try:
        date_text = input('Enter a date in the format mm/dd/yyyy: ')
        print(parse_date(date_text))
    except ValueError as error:
        print(f'Error: {error}')
    except EOFError:
        print('Error: No date was entered.')


if __name__ == '__main__':
    main()
