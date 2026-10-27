import math

ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


def get_temperature_type():
    while (temperature_type := input(
        "Enter the type of temperature (F for Fahrenheit, C for Celsius): "
    ).strip().upper()) not in ("F", "C"):
        print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
    return temperature_type


def get_temperature(temperature_type):
    if temperature_type == "F":
        absolute_zero = ABSOLUTE_ZERO_F
    else:
        absolute_zero = ABSOLUTE_ZERO_C

    while True:
        try:
            temperature = float(input("Enter the temperature you want to convert: "))
        except ValueError:
            print("Invalid temperature. Please enter a number.")
        else:
            if not math.isfinite(temperature):
                print("Invalid temperature. Please enter a finite number.")
            elif temperature < absolute_zero:
                print(
                    "Invalid temperature. Please enter a temperature "
                    f"above absolute zero ({absolute_zero})."
                )
            else:
                return temperature


def display_conversion(temperature_type, temperature):
    if temperature_type == "F":
        converted_temperature = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {converted_temperature:.2f}")
    else:
        converted_temperature = temperature * 9 / 5 + 32
        print(f"The temperature in Fahrenheit is: {converted_temperature:.2f}")


if __name__ == "__main__":
    main()
