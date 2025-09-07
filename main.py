class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        avg = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {avg:.2f}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):

        sorted_students = sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)
        return sorted_students[:3]

    def get_failed_students(self):
        return [s for s in self.students if s.get_average_grade() < 51]

# სტუდენტები
alice = Student("Alice")
alice.add_grade(85)
alice.grades.append(90)

bob = Student("Bob")
bob.add_grade(40)
bob.grades.append(50)

charlie = Student("Charlie")
charlie.add_grade(95)
charlie.grades.append(80)

david = Student("David")
david.add_grade(70)
david.grades.append(80)

# Classroom
classroom = Classroom()
classroom.add_student(alice)
classroom.add_student(bob)
classroom.add_student(charlie)
classroom.add_student(david)

# ტოპ სტუდენტები
print("Top Students:")
for s in classroom.get_top_students():
    print(s)

# ჩაჭრილი სტუდენტები
print("\nFailed Students:")
for s in classroom.get_failed_students():
    print(s)
