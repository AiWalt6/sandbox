class Pet:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def speak(self):
        raise NotImplementedError('A specific pet must provide its sound.')

    def __str__(self):
        return self.__name
