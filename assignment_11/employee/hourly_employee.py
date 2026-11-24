from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        super().__init__(name, department, hourly_rate)
        self.__hours = hours

    def get_pay(self):
        return super().get_pay() * self.__hours

    def __str__(self):
        return f'{self.get_name()} (Hourly Employee)'
