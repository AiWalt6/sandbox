from employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, department, salary)

    def __str__(self):
        return f'{self.get_name()} (Salaried Employee)'
