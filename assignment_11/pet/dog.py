from pet import Pet


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Woof!'

    def __str__(self):
        return f'{super().__str__()} the Dog'
