import os
import matplotlib.pyplot as plt


INPUT_FILE = 'precipitation.txt'


def main():
    months, precipitation = read_precipitation_file(INPUT_FILE)

    if len(months) > 0:
        show_bar_chart(months, precipitation)


def read_precipitation_file(filename):
    months = []
    precipitation = []

    # Look for the file in the same folder as this program.
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'r') as input_file:
            for line in input_file:
                month, amount = line.strip().split(',')
                amount = float(amount)
                if not month.strip() or not 0.0 <= amount <= 366.0:
                    raise ValueError('Invalid month or precipitation amount.')
                months.append(month)
                precipitation.append(amount)
    except FileNotFoundError:
        print(f"Could not find '{filename}'. Run precipitation_analysis.py first.")
    except ValueError:
        print(f"'{filename}' is not in the expected 'month,amount' format.")
        months = []
        precipitation = []

    return months, precipitation


def show_bar_chart(months, precipitation):
    # Use the first three letters of each month name so the labels fit.
    short_names = [month[:3] for month in months]

    plt.figure(figsize=(10, 7))
    plt.bar(short_names, precipitation, color='steelblue')
    plt.title('Monthly Precipitation')
    plt.xlabel('Month')
    plt.ylabel('Precipitation')
    plt.tight_layout()
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'precipitation_chart.png'
    )
    plt.savefig(path)
    plt.show()


if __name__ == '__main__':
    main()
