class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def getName(self):
        return self._name

    def getAddress(self):
        return self._address

    def setAddress(self, add):
        self._address = add

    def toString(self):
        return f"{self._name}({self._address})"


class Teacher(Person):
    numCourses = 0
    courses = []

    def __init__(self, name, address):
        super().__init__(name, address)

    def addCourse(self, course):
        for items in range(0, len(course)):
            if course[items] not in Teacher.courses:
                Teacher.courses.append(course[items])
                Teacher.numCourses += 1
            else:
                return False

    def removeCourse(self, course):
        for items in range(0, len(course)):
            if course[items] in Teacher.courses:
                Teacher.courses.remove(course[items])
                Teacher.numCourses -= 1
            else:
                return False

    def toString(self):
        return f"Teacher : {super().toString()}"


class Student(Person):
    numCourses = 0
    courseGrade = {}
    grades = []

    def __init__(self, names, address):
        super().__init__(names, address)

    def addCourseGrade(self, course, grade):
        Student.courseGrade[course] = grade
        Student.numCourses += 1
        Student.grades.append(grade)

    def printGrades(self):
        for items, things in Student.courseGrade.items():
            print(f"{items} : {things}")

    def getAverageGrade(self):
        return sum(Student.grades) / Student.numCourses

    def toString(self):
        return f"Student : {super().toString()}"










