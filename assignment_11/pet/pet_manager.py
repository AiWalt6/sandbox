from bird import Bird
from cat import Cat
from dog import Dog


def print_menu():
    print('Pet Menu')
    print('1. Add Dog')
    print('2. Add Cat')
    print('3. Add Bird')
    print('4. Show All Pets')
    print('5. Exit')


def main():
    pets = []

    while True:
        print_menu()
        choice = input('Enter choice: ').strip()

        if choice in ('1', '2', '3'):
            if choice == '1':
                name = input("Enter dog's name: ").strip()
            elif choice == '2':
                name = input("Enter cat's name: ").strip()
            else:
                name = input("Enter bird's name: ").strip()

            if not name:
                print('A pet name cannot be empty.')
            elif choice == '1':
                pets.append(Dog(name))
            elif choice == '2':
                pets.append(Cat(name))
            else:
                pets.append(Bird(name))
        elif choice == '4':
            print('\nYour Pets:')
            if not pets:
                print('No pets have been added.')
            for pet in pets:
                print(f'{pet} says {pet.speak()}')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Enter a number from 1 to 5.')

        print()


if __name__ == '__main__':
    main()
