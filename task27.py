#Define a class called student. Display the marks details of top five students using inheritance.
# Base Class
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def display_student(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name}", end=" | ")


# Derived Class inheriting from Student
class Marks(Student):
    def __init__(self, roll_no, name, marks):
        # Call the base class constructor to inherit properties
        super().__init__(roll_no, name)
        self.marks = marks
        self.total = sum(marks)

    def display_details(self):
        self.display_student()
        print(f"Marks: {self.marks} | Total: {self.total}")


# Main Execution Block
if __name__ == "__main__":
    # Sample list of 8 student objects with marks for 3 subjects
    student_records = [
        Marks(101, "Alice", [85, 90, 88]),
        Marks(102, "Bob", [70, 65, 80]),
        Marks(103, "Charlie", [95, 92, 98]),
        Marks(104, "David", [60, 55, 70]),
        Marks(105, "Eva", [90, 88, 92]),
        Marks(106, "Frank", [82, 85, 79]),
        Marks(107, "Grace", [94, 91, 89]),
        Marks(108, "Henry", [87, 84, 91])
    ]

    # Sort students in descending order based on total marks
    # x.total is used to filter out the highest achieving students
    sorted_students = sorted(student_records, key=lambda x: x.total, reverse=True)

    # Slice the sorted list to select and display the top 5 records
    print("--- TOP 5 STUDENTS MARKS DETAILS ---")
    for rank, student in enumerate(sorted_students[:5], start=1):
        print(f"Rank {rank} -> ", end="")
        student.display_details()
