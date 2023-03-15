class Person:
    numOfPerson = 0

    def __init__(self, id_number=0, firstN ="", lastN = "cohen"):
        Person.numOfPerson += 1

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

    def __str__(self):
        return str(self.id) + " - " + self.firstname + " - " + self.lastname

    def changeName(self, newName):
        self.firstname = newName

    @staticmethod
    def getNumOfPerson():
        print(Person.numOfPerson)