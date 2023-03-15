class Person:
    numOfPerson = 0

    def __init__(self, id_number, firstN, lastN):  # initilization
        Person.numOfPerson += 1
        if isinstance(id_number, int):
            self.id = id_number
        else:
            self.id = 0

        if isinstance(firstN, str):
            self.firstname = firstN
        else:
            self.firstname = ""

        if isinstance(firstN, str):
            self.lastN = lastN
        else:
            self.lastN = ""

    def changeN(self, newN):  # functions
        self.firstname = newN

    @staticmethod
    def getNumOfP():
        print(Person.numOfPerson)