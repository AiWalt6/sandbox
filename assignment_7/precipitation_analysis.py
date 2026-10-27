import os


OUTPUT_FILE = 'precipitation.txt'
MIN_PRECIPITATION = 0.0
MAX_PRECIPITATION = 366.0


def main():
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    precipitation = get_precipitation(months)
    display_results(months, precipitation)
    write_precipitation_file(OUTPUT_FILE, months, precipitation)


def get_precipitation(months):
    precipitation = []

    for month in months:
        while True:
            try:
                amount = float(input(f'Enter the rainfall for {month}: '))
                if MIN_PRECIPITATION <= amount <= MAX_PRECIPITATION:
                    precipitation.append(amount)
                    break
                print(
                    'Invalid input. Please enter a value between '
                    f'{MIN_PRECIPITATION} and {MAX_PRECIPITATION}.'
                )
            except ValueError:
                print('Invalid input. Please enter a number.')

    return precipitation


def display_results(months, precipitation):
    total = sum(precipitation)
    average = total / len(precipitation)
    highest = max(precipitation)
    lowest = min(precipitation)
    highest_month = months[precipitation.index(highest)]
    lowest_month = months[precipitation.index(lowest)]

    print(f'Total rainfall: {total:.2f}')
    print(f'Average rainfall: {average:.2f}')
    print(f'Highest rainfall: {highest_month:<15}{highest:.1f}')
    print(f'Lowest rainfall: {lowest_month:<15}{lowest:.1f}')


def write_precipitation_file(filename, months, precipitation):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    with open(path, 'w') as output_file:
        for index in range(len(months)):
            output_file.write(f'{months[index]},{precipitation[index]}\n')


if __name__ == '__main__':
    main()
