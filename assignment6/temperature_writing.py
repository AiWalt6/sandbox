from pathlib import Path


MIN_CELSIUS = 0
MAX_CELSIUS = 50
FOLDER = Path(__file__).resolve().parent
WHILE_FILE = FOLDER / "temperature_whileloop.txt"
FOR_FILE = FOLDER / "temperature_forloop.txt"


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def write_header(outfile):
    outfile.write(f"{'Celsius':>10}{'Fahrenheit':>18}\n")
    outfile.write("-" * 28 + "\n")


def write_with_while(max_celsius):
    with WHILE_FILE.open("w") as outfile:
        write_header(outfile)
        celsius = MIN_CELSIUS
        while celsius <= max_celsius:
            fahrenheit = celsius_to_fahrenheit(celsius)
            outfile.write(f"{celsius:10d}{fahrenheit:18.2f}\n")
            celsius += 1


def write_with_for(max_celsius):
    with FOR_FILE.open("w") as outfile:
        write_header(outfile)
        for celsius in range(MIN_CELSIUS, max_celsius + 1):
            fahrenheit = celsius_to_fahrenheit(celsius)
            outfile.write(f"{celsius:10d}{fahrenheit:18.2f}\n")


def get_max_celsius():
    while (
        celsius := int(
            input(
                f"Enter a Celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): "
            )
        )
    ) < MIN_CELSIUS or celsius > MAX_CELSIUS:
        print(
            "Invalid input. Please enter a temperature "
            f"between {MIN_CELSIUS} and {MAX_CELSIUS}."
        )
    return celsius


def main():
    max_celsius = get_max_celsius()
    write_with_while(max_celsius)
    write_with_for(max_celsius)


if __name__ == "__main__":
    main()
