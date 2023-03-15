class Person:

    def __init__(self, id_number, firstN, lastN):  # initilization
        self.id = id_number
        self.firstname = firstN
        self.lastname = lastN

    def __str__(self):
        return str(self.id) + " - " + self.firstname + " - " + self.lastname

person = Person(2424, "David", "Mazkin")

print(person)

print("end")
