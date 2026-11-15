class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError('The age must be a nonnegative whole number.')
        self.__age = age

    def __str__(self):
        return (f'Pet name: {self.__name}\n'
                f'Animal type: {self.__animal_type}\n'
                f'Age of pet: {self.__age}')
