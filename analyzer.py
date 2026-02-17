# analyzer.py

class Analyzer:

    def __init__(self, students):
        # students = list of Student objects
        self.students = students

    # find topper based on average marks
    def find_topper(self):
        topper = max(self.students, key=lambda s: s.get_average())
        return topper

    # calculate class average
    def class_average(self):
        return sum(s.get_average() for s in self.students) / len(self.students)

    # pass/fail check (pass if avg >= 40)
    def pass_fail_report(self):
        result = []
        for s in self.students:
            status = "PASS" if s.get_average() >= 40 else "FAIL"
            result.append((s.name, status))
        return result
    # search student by name
    def search_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None
    
    def top_five(self):
        sorted_students = sorted(self.students, key=lambda s: s.get_average(), reverse=True)
        return sorted_students[:5]
