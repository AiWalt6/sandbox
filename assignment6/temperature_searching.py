from pathlib import Path


MIN_CELSIUS = 0
MAX_CELSIUS = 50
TEMPERATURE_FILE = (
    Path(__file__).resolve().parent / "temperature_forloop.txt"
)


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def search_with_for(target_celsius):
    with TEMPERATURE_FILE.open("r") as infile:
        infile.readline()
        infile.readline()
        for line in infile:
            celsius, fahrenheit = line.split()
            if int(celsius) == target_celsius:
                return float(fahrenheit)
    return None


def search_with_while(target_celsius):
    with TEMPERATURE_FILE.open("r") as infile:
        infile.readline()
        infile.readline()
        line = infile.readline()
        while line:
            celsius, fahrenheit = line.split()
            if int(celsius) == target_celsius:
                return float(fahrenheit)
            line = infile.readline()
    return None


def append_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    with TEMPERATURE_FILE.open("a") as outfile:
        outfile.write(f"{celsius:10d}{fahrenheit:18.2f}\n")
    return fahrenheit


def get_target_celsius():
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
    target_celsius = get_target_celsius()
    for_result = search_with_for(target_celsius)
    while_result = search_with_while(target_celsius)
    print(f"For-loop search result:   {for_result}")
    print(f"While-loop search result: {while_result}")

    if for_result is None:
        fahrenheit = append_temperature(target_celsius)
        print(
            "No match found. New record added: "
            f"{target_celsius} Celsius = {fahrenheit:.2f} Fahrenheit."
        )
    else:
        print(
            f"Match found: {target_celsius} Celsius is "
            f"{for_result:.2f} Fahrenheit."
        )


if __name__ == "__main__":
    main()
