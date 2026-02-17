# visualizer.py

import matplotlib.pyplot as plt

class Visualizer:

    def __init__(self, students):
        self.students = students

    # Bar chart of student averages
    def plot_averages(self):
        names = [s.name for s in self.students]
        averages = [s.get_average() for s in self.students]

        plt.figure()
        plt.bar(names, averages)
        plt.xticks(rotation=90)
        plt.title("Student Average Marks")
        plt.xlabel("Students")
        plt.ylabel("Average Marks")
        plt.tight_layout()
        plt.show()

    # Pie chart of Pass vs Fail
    def plot_pass_fail(self):
        pass_count = 0
        fail_count = 0

        for s in self.students:
            if s.get_average() >= 40:
                pass_count += 1
            else:
                fail_count += 1

        labels = ["Pass", "Fail"]
        values = [pass_count, fail_count]

        plt.figure()
        plt.pie(values, labels=labels, autopct='%1.0f%%')
        plt.title("Pass vs Fail Distribution")
        plt.show()
