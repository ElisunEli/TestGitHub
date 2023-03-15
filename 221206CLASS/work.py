class Student:
    numOfStudent = 0

    def __init__(self, firstName="", lastName="", id_num=0):
        Student.numOfStudent += 1
        self.firstName = firstName
        self.lastName = lastName
        self.id_num = id_num
        self.listOfCourse = []
        self.marks = {}

    def addCourseMark(self, course, mark):
        if course in self.listOfCourse:
            self.marks[course] = mark
        else:
            print("This student don't has this course")

    def numOfCourses(self):
        return len(self.listOfCourse)

    def avgOfMarks(self):
        count = 0.0
        for i in self.marks:
            count += self.marks[i]
        return count / self.numOfCourses()

    @staticmethod
    def getNumOfS():
        print(Student.numOfStudent)

    def __str__(self):
        return self.firstName + " " + self.lastName + " " +self.id_num + " " + str(self.listOfCourse) + " " + str(self.marks)

student = Student("Saher", "Taher", "1233")
student.listOfCourse = ["Math", "Chemistry"]
student.marks = {"Math": 78, "Chemistry": 79}
print(student)
print(student.avgOfMarks())