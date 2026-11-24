from pet import Pet


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Tweet!'

    def __str__(self):
        return f'{super().__str__()} the Bird'
