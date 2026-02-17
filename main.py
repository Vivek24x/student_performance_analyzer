import pandas as pd
from student import Student
from analyzer import Analyzer
from visualizer import Visualizer

# ---------------- LOAD DATA ----------------
data = pd.read_csv("data.csv")

# create student objects
students = []

for index, row in data.iterrows():
    s = Student(row["name"], row["maths"], row["science"], row["english"])
    students.append(s)

# create analyzer and visualizer objects
analyzer = Analyzer(students)
viz = Visualizer(students)

# ---------------- MENU LOOP ----------------
while True:
    print("\n===== STUDENT PERFORMANCE ANALYZER =====")
    print("1. Show Topper")
    print("2. Show Class Average")
    print("3. Show Pass/Fail Report")
    print("4. Show Graphs")
    print("5. Search Student")
    print("6. Show Top 5 Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        topper = analyzer.find_topper()
        print("\n🏆 Topper Details:\n")
        topper.display()

    elif choice == "2":
        avg = analyzer.class_average()
        print("\n📊 Class Average:", round(avg, 2))

    elif choice == "3":
        print("\n✅ Pass/Fail Report:\n")
        report = analyzer.pass_fail_report()
        for name, status in report:
            print(name, "-", status)

    elif choice == "4":
        viz.plot_averages()
        viz.plot_pass_fail()

    elif choice == "5":   # Search Student
        name = input("Enter student name: ")
        student = analyzer.search_student(name)
        if student:
            student.display()
        else:
            print("Student not found.")

    elif choice == "6":   # Top 5 Students
        print("\n🏆 Top 5 Students:\n")
        for s in analyzer.top_five():
            s.display()
            print("----------------")

    elif choice == "7":   # Exit
        print("\nExiting program... 👋")
        break

    else:
        print("\n❌ Invalid choice. Try again.")
