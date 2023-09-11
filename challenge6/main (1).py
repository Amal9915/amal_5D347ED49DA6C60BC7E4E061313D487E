class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", "001", 3.9),
    Student("Bob", "002", 3.6),
    Student("Charlie", "003", 3.8),
    Student("David", "004", 3.5),
    Student("Eve", "005", 4.0),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
