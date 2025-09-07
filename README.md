Objective
Create a system to manage student grades using Object-Oriented Programming (OOP) principles. This exercise will help you understand how to define classes, create objects, and implement methods that handle multiple grades and calculate averages.

Requirements
Define a Student Class:

The Student class should have the following attributes:
name: A string representing the student's name.
grades: A list of integers representing the student's grades.
Add Methods to the Student Class:

__init__ method: Initialize the name and grades attributes.
add_grade method: Add a new grade to the grades list.
get_average_grade method: Return the average of the student's grades.
__str__ method: Return a string representation of the student in the format "Name: <name>, Grades: <grades>, Average: <average>".
Create a Classroom Class:

The Classroom class should manage multiple Student objects.
Attributes:
students: A list that holds Student objects.
Methods:
add_student method: Add a Student object to the students list.
get_top_students method: Return the top three students based on their average grades.
get_failed_students method: Return a list of students whose average grade is below 51.
Implement the Solution:

Create instances of the Student class for several students.
Add multiple grades to each student.
Add these students to an instance of the Classroom class.
Use the Classroom methods to retrieve and display the top students and those who failed.
Example Code Structure
class Student:
    def __init__(self, name):
        # Initialize name and an empty list for grades

    def add_grade(self, grade):
        # Add a new grade to the grades list

    def get_average_grade(self):
        # Return the average of the grades

    def __str__(self):
        # Return a string representation of the student

class Classroom:
    def __init__(self):
        # Initialize an empty list for students

    def add_student(self, student):
        # Add a student to the classroom

    def get_top_students(self):
        # Return the top 3 students based on average grades

    def get_failed_students(self):
        # Return students with an average grade below 51