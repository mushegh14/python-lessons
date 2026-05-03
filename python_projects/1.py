import json

students = [
    {
        "name": "Alice",
        "grades": {
            "Math": 85,
            "Science": 92
        }
    },
    {
        "name": "Bob",
        "grades": {
            "Math": 78
        }
    }
]


def find_student(students, name):
    for i in students:
        if i["name"] == name:
            return i
    return None


def add_student(students):
    anun = input("Enter the name: ")

    student = find_student(students, anun)

    if student is not None:
        print("There is already this student")
        return

    new_student = {
        "name": anun,
        "grades": {}
    }

    students.append(new_student)
    print("Student added successfully")
    









def add_or_update_grade(students):
    pass

def calculate_student_average(student):
    pass

def view_student(students):
    pass

def calculate_class_average(students):
    pass

def save_to_file(students):
    pass

def load_from_file():
    pass

def menu():
    pass