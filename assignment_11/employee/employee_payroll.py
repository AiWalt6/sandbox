from commission_employee import CommissionEmployee
from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalariedEmployee


def load_employees():
    employees = [
        HourlyEmployee('Nick DeFalco', 'Sales', 25, 2080),
        SalariedEmployee('Applejack Johnson', 'Sales', 44000),
        SalariedEmployee('Mario Dubois', 'Sales', 77200),
        SalariedEmployee('Anthony Jo', 'Engineering', 98000),
        Employee('Stephanie Johnson', 'Engineering', 31200),
        CommissionEmployee('Dominic Togo', 'Maintenance', 20000, 300000, 0.15),
        HourlyEmployee('Christina Gonzalez', 'Maintenance', 19.80, 2080),
        HourlyEmployee('Geoffrey Dav', 'HR', 65, 2080),
    ]
    return employees


def main():
    employees = load_employees()

    employee_dict = {}
    for emp in employees:
        department = emp.get_department()
        if department not in employee_dict:
            employee_dict[department] = []
        employee_dict[department].append(emp)

    for department, emp_list in employee_dict.items():
        print(f'Department: {department}')
        total_payroll = 0
        for emp in emp_list:
            pay = emp.get_pay()
            print(f'    {emp}: ${pay:.2f}')
            total_payroll += pay
            if isinstance(emp, CommissionEmployee):
                print(f'        {emp.get_commission_breakdown()}')
        print(f'Total Payroll: ${total_payroll:.2f}')
        print()


if __name__ == '__main__':
    main()
