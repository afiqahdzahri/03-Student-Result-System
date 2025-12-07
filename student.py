import csv
from statistics import mean

class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.courses = []  # list of (course_code, credit, grade_point)

    def add_course(self, code, credit, grade_point):
        self.courses.append((code, float(credit), float(grade_point)))

    def gpa(self):
        if not self.courses:
            return 0.0
        total_points = sum(credit * gp for _, credit, gp in self.courses)
        total_credits = sum(credit for _, credit, _ in self.courses)
        return round(total_points / total_credits, 2)

def save_students(students, filename='students.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name','courses'])
        for s in students:
            writer.writerow([s.id, s.name, json.dumps(s.courses)])