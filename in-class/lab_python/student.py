# Author: Josiah Campbell
# Version: Winter 2016
class Student:
    # two underscores cause the variable to
    # only be accessable within the class
    __num_students = 0
    # Constructor for student class
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.num_students += 1
    # "think Java's toString()"
    def __str__(self):
        return self.name + ": " + str(self.gpa)

if __name__ == "__main__":
    joey = Student('Joey Coder', 4.0)
    print joey
    print Student.num_students
