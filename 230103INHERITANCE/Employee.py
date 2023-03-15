from Person import Person
import datetime


class Employee(Person):
    numOfEmployee = 0

    def __init__(self, id_number=0, firstN="", lastN="", start_date=0, nekudat_z=0.0):
        Employee.numOfEmployee += 1

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

    def calculate_seniority(self):
        current_year = datetime.date.today().year
        return current_year - self.begin_year
