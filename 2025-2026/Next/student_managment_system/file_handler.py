FILE_NAME = "D:/Private/GitHub/pythonCourse/2025-2026/Next/student_managment_system/students.csv"
import csv
def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("File not found.")
    return students

def save_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)
        print("Students saved successfully.")
        

