class Employee:
    def __init__(self, name, department, pay):
        self.__name = name
        self.__department = department
        self.__pay = pay

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_pay(self):
        return self.__pay

    def __str__(self):
        return f'{self.__name} (Employee)'
