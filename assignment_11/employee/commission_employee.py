from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, department, base_pay, sales, commission_rate):
        super().__init__(name, department, base_pay)
        self.__sales = sales
        self.__commission_rate = commission_rate

    def get_commission(self):
        return self.__sales * self.__commission_rate

    def get_pay(self):
        return super().get_pay() + self.get_commission()

    def get_commission_breakdown(self):
        base_pay = super().get_pay()
        commission = self.get_commission()
        total_pay = self.get_pay()
        if total_pay == 0:
            percentage = 0
        else:
            percentage = commission / total_pay * 100
        return (f'Base ${base_pay:.2f} + Commission ${commission:.2f} '
                f'({percentage:.1f}% of earnings)')

    def __str__(self):
        return f'{self.get_name()} (Commission Employee)'
