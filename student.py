# student.py

class Student:
    
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english

    # method to calculate average marks
    def get_average(self):
        avg = (self.maths + self.science + self.english) / 3
        return avg

    # method to show student info
    def display(self):
        print(f"Name: {self.name}")
        print(f"Maths: {self.maths}, Science: {self.science}, English: {self.english}")
        print(f"Average Marks: {self.get_average():.2f}")
