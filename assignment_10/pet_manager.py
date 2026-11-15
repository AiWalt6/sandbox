from pet import Pet


def main():
    name = input('Enter the name of the pet: ').strip()
    animal_type = input('Enter the type of animal: ').strip()

    while True:
        try:
            age = int(input('Enter the age of the pet: '))
        except ValueError:
            print('Please enter a nonnegative whole number for age.')
            continue
        if age >= 0:
            break
        print('Please enter a nonnegative whole number for age.')

    pet = Pet(name, animal_type, age)
    print('Here is the data that you entered:')
    print(pet)


if __name__ == '__main__':
    main()
