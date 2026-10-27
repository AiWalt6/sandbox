ABSOLUTE_ZERO_C = -273.15

while True:
    try:
        if (celsius_limit := int(input("Enter a Celsius degree: "))) < ABSOLUTE_ZERO_C:
            print("Error: temperature cannot be below absolute zero (-273.15 C).")
        else:
            break
    except ValueError:
        print("Error: enter an integer Celsius temperature.")

print(f"{'Celsius':<15}Fahrenheit")
print("-" * 30)

# Count downward when the requested endpoint is below zero.
if celsius_limit >= 0:
    step = 1
else:
    step = -1
for celsius in range(0, celsius_limit + step, step):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:<15}{fahrenheit:.1f}")
