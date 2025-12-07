from student import Student
import json, csv, os

DATA_FILE = 'students_data.csv'

def load_students():
    students = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                s = Student(r['id'], r['name'])
                s.courses = json.loads(r['courses'])
                students[s.id] = s
    return students

def save_students(students):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name','courses'])
        for s in students.values():
            writer.writerow([s.id, s.name, json.dumps(s.courses)])

def menu():
    students = load_students()
    while True:
        print('\n1. Add student\n2. Add course to student\n3. Show GPA\n4. Exit')
        c = input('Choose: ')
        if c=='1':
            sid = input('ID: '); name = input('Name: ')
            students[sid] = Student(sid, name)
            save_students(students)
        elif c=='2':
            sid = input('Student ID: ')
            if sid not in students: print('Not found'); continue
            code = input('Course code: '); credit = input('Credit: '); gp = input('Grade point: ')
            students[sid].add_course(code, credit, gp); save_students(students)
        elif c=='3':
            sid = input('Student ID: ')
            if sid in students:
                print('GPA:', students[sid].gpa())
            else:
                print('Not found')
        else:
            break

if __name__=='__main__':
    menu()