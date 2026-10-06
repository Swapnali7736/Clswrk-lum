# 1.Create a table named students to store student information.
# Table: students
# Column Name
# Data Type
# Description
#
# student_id
# INT (Primary Key)
# Unique student ID
#
# name
# VARCHAR(100)
# Name of the student
#
# age
# INT
# Age of the student
#
# gender
# VARCHAR(10)
# Gender
#
# course
# VARCHAR(100)
# Enrolled course
#
# marks
# INT
# Marks obtained
#
# city
# VARCHAR(100)
# City of the student
#
#
# Questions
# Display all records from the students table.

# Display name, course, and marks for all students.

# Display names and marks of students who scored more than 80.

# Display all details of students enrolled in Computer Science.

# Display names, ages, and cities of students whose age is between 18 and 22.

# # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.

# Insert a new record into the students table.

# # Update marks of all students who scored below 50 by adding 5 bonus marks.

# # Delete all student records where marks are less than 35.



import sqlite3
con=sqlite3.connect("student.db")
command="""create table if not exists student(studentid int primary key,name varchar(30),age int,gender varchar(10),course varchar(100),mark int,city varchar(100))"""
con.execute(command)
# print("Table created")


# command="""insert into student(studentid,name,age,gender,course,mark,city)
#         values(101,"anu",23,"female","python",92,"tvm"),
#         (102,"beena",26,"female","devops",70,"ekm"),
#         (103,"vanika",22,"female","ai engineering",69,"mirj"),
#         (104,"naswin",25,"male","testing",78,"aluva")"""
# con.execute(command)
# con.commit()
# print("Data Inserted Successfully")

## Display all records from the students table.
# e=con.execute("select * from student")
# print(e.fetchall())

# # Display name, course, and marks for all students.
# e=con.execute("select name,course,mark from student")
# print(e.fetchall())

# # Display names and marks of students who scored more than 80.
# e=con.execute("select name,mark from student where mark>80")
# print(e.fetchall())

# # Display all details of students enrolled in Computer Science.
# e=con.execute("select * from student where course='computer science'")
# print(e.fetchall())


# # Display names, ages, and cities of students whose age is between 18 and 22.
# e=con.execute("select name,age,city from student where age between 18 and 22")
# print(e.fetchall())

# # # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.
# e=con.execute("select name,mark,course from student where city='Kochi' order by mark desc ")
# print(e.fetchall())

# Insert a new record into the students table.
# command="""insert into student(studentid,name,age,gender,course,mark,city)
#            values(105,"fasna",30,"female","java",78,"thrissur")"""
# con.execute(command)
# con.commit()
# print("Data Inserted Successfully")

# # # Update marks of all students who scored below 50 by adding 5 bonus marks.
# con.execute("""update student set mark=mark+5 where mark<50""")
# con.commit()
# print("marks updated")

# # Delete all student records where marks are less than 35.
con.execute("""Delete from student where mark < 35""")
con.commit()
print("records deleted")