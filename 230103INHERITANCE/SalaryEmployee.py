from Employee import Employee


class SalaryEmployee(Employee):
    numOfSalaryEmployee = 0

    def __init__(self, id_number=0, firstN="", lastN="", start_date=0, nekudat_z=0.0,  monthly_salary=0):
        SalaryEmployee.numOfSalaryEmployee += 1

        if isinstance(id_number, int):
            self.id = id_number
        else:
            self.id = 0
        if isinstance(firstN, str):
            self.firstname = firstN
        else:
            self.firstname = ""

        if isinstance(lastN, str):
            self.lastname = lastN
        else:
            self.lastname = ""

        if isinstance(start_date, int):
            #2022
            self.start_date = start_date
        else:
            self.lastname = 0

        if isinstance(nekudat_z, float):
            nekudat_z = nekudat_z
        else:
            self.nekudat_z = 0.0

        if isinstance(monthly_salary, int):
            self.monthly_salary = monthly_salary
        else:
            self.monthly_salary = 0

    def calculateMonthlyPay(self):
        return self.monthly_salary