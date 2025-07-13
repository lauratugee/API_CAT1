class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments={}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grade(self):
        if not self.assignments:
            return "No assignments completed yet"
        print(f"\n Grades for {self.name} (ID: {self.student_id})")
        for assignment_name, grade in self.assignments.items():
            print(f"{assignment_name}: {grade}")

class Instructor:
    def __init__(self,name,course_name):
        self.name = name
        self.course_name = course_name
        self.students=[]

    def add_student(self, student):
        self.students.append(student)
        return f"Added {student.name} to {self.course_name}"

    def assign_grade(self,student_id,assignment_name,grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name,grade)
                return f"Grade for {assignment_name}"
            return "Student not found"

    def display_all_grades(self):
        if not self.students:
            print("No students enrolled yet")
            return
        print(f"\nAll grades for {self.course_name}")
        for student in self.students:
            student.display_grades()

if __name__ == "__main__":
    instructor_name=input("Enter instructor name: ")
    course_name=input("Enter course name: ")
    instructor=Instructor(instructor_name,course_name)

    while True:
        print("\nCourse management system")
        print("1.Add student")
        print("2.Assign grade")
        print("3.Display all grades")
        print("4.Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            student_name=input("Enter student name: ")
            student_id=input("Enter student ID: ")
            new_student=Student(student_name,student_id)
            print(instructor.add_student(new_student))

        elif choice=="2":
            if not instructor.students:
                print("No students enrolled yet")
                continue

            print("\nCurrent students:")
            for i