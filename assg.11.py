# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()



# class Movie:
#     def __init__(self):
#         self.moviename=input("enter the movie name:")
#         self.year=int(input("enter the year:"))
#         self.lang=input("enter the language:")
#         self.director=input("enter the director:")
#         self.rating=""
#     def display_details(self):
#         print(self.moviename,self.year,self.lang,self.director,self.rating)  

#     def update_rating(self):
#         self.rating=input("enter the updated rating:") 
#         if self.rating=="" :
#             print("not updated")
#         else:
#             print("updated rating:",self.rating) 
# m=Movie()
# m.display_details() 
# m.update_rating() 
# m.display_details()              




# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.



# class Vehicle:
#     def __init__(self):
#         self.brand=input("enter the brand:")
#         self.model=input("enter the model:")
#         self.color=input("enter the color:")
#         self.year=int(input("enter the year:"))
#     def display(self):
#         print(self.brand,self.model,self.color,self.year) 

# class Car(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.mileage=input("enter the mileage:") 
#     def display(self):
#         Vehicle.display(self)
#         print("mileage:",self.mileage)    


# class Bike(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.cc=input("enter the cc:")
#     def display(self):
#         Vehicle.display(self)
#         print("cc:",self.cc)    



# c=Car()
# c.display()
# b=Bike()
# b.display()






## Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.



# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
    


# class FullTimeEmployee(Employee):
#     def __init__(self):
#         self.monthlysalary = int(input("Enter the salary: "))

#     def calculate_salary(self):
#         print("FullTime salary=", self.monthlysalary)

# f=FullTimeEmployee()
# f.calculate_salary()    

# class PartTimeEmployee(Employee):
#     def __init__(self):
#         self.hour =int(input("Enter hour: "))
#         self.rate=int(input("enter the rate:"))

#     def calculate_salary(self):
#         print("PartTime salary=", self.hour*self.rate)

# p=PartTimeEmployee()
# p.calculate_salary()

    



#
# create an abstract class Shape with abstract methods get_area() and get_perimeter()
# create two subclasses
#  -Rectangle
#  -Square
#
#  -Each class should calculate area() and perimeter() differently.

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self):
#         self.length = int(input("Enter length: "))
#         self.breadth = int(input("Enter breadth: "))

#     def get_area(self):
#         print("Area of rectangle=", self.length * self.breadth)

#     def get_perimeter(self):
#         print("Perimeter of rectangle =", 2 * (self.length + self.breadth))


# class Square(Shape):
#     def __init__(self):
#         self.side = int(input("Enter side: "))

#     def get_area(self):
#         print("Area of square =", self.side * self.side)

#     def get_perimeter(self):
#         print("Perimeter of square =", 4 * self.side)


# r = Rectangle()
# r.get_area()
# r.get_perimeter()

# s = Square()
# s.get_area()
# s.get_perimeter()




# Create a Python program using Object-Oriented Programming (OOP) that includes the following:
# Class: Course
# Attributes:
# course_name
# instructor
# duration
# Methods:
# show_course() → to display course details
# • Subclass: Student (inherits from Course)
# Additional attributes:
# name
# roll_no
# marks
# Methods:
# show_student() → to display student details along with course details
# get_result() → return "Pass" if marks ≥ 50, otherwise "Fail"
# Create at least one object of the Student class
# Display all details and result


# class Course:
#     def __init__(self):
#         self.course_name=input("enter the course name:")
#         self.instructor=input("enter the instructor:")
#         self.duration=input("enter the duration:")
#     def show_course(self):
#         print("course:",self.course_name,"instructor:",self.instructor,"duration:",self.duration)
# class Student(Course):
#     def __init__(self):
#         Course.__init__(self)
#         self.sname=input("enter the sname:")
#         self.rollno=int(input("enter the rollno:")) 
#         self.marks=int(input("enter the marks:"))
#     def show_student(self):
#         Course.show_course(self)
#         print("sname:",self.sname,"rollno:",self.rollno,"marks:",self.marks)
#     def get_result(self):
#         if (self.marks>=50):
#             return ("Pass")
#         else:
#             return ("Fail")
# s=Student()
# s.show_student()
# print(s.get_result())                       





# Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with attributes such as id, name, age, designation, experience (in years), and salary. The class should include methods to display employee details and update the designation.

# It should also include a method to check promotion eligibility where an employee is eligible for promotion if experience is 5 years or more and age is above 30; otherwise, the employee is not eligible.

# Create at least one object of the Employee class, assign values directly, and display all the details along with the promotion eligibility result.


class Employee:
    def __init__(self,id,name,age,designation,experience,salary):
        self.id=id
        self.name=name
        self.age=age
        self.designation=designation
        self.experience=experience
        self.salary=salary

    def display_details(self):
        print("Employee ID :",self.id,"Name:",self.name,"Age:",self.age,"Designation:",self.designation,
              "Experience :",self.experience,"Salary:",self.salary)

    def update_designation(self,new_designation):
        self.designation=new_designation

    def check_promotion(self):
        if self.experience>=5 and self.age>30:
            return "Eligible for Promotion"
        else:
            return "Not Eligible for Promotion"


e1 = Employee(122,"Rohit",35,"Software Developer",4,70000)
e1.update_designation("Senior Software Developer")
e1.display_details()
print("Promotion Status:",e1.check_promotion())