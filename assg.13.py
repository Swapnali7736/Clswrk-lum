# Create a database file school.db
#
# create a table Student with fields roll_no(pk),name,age,gender,course,mark
#
# write a menu driven code
#
#                     1.Insert Student details
#                     2.Read all student details
#                     3.search a student by rollno
#                     4.update the mark of a student
#                     5.Delete a student record
#                     6.Exit



import mysql.connector
# con=mysql.connector.connect(user="root",password="root",host="localhost")
# c=con.cursor()   
# c.execute("create database school")
# print("database created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="school")
c=con.cursor()
c.execute('''create table if not exists student(rollno int primary key,name varchar(20),age int,gender varchar(20),course varchar(20),mark int)''')
print("Table created")


def insert_record():
    r=int(input("enter the rollno:"))
    n=input("enter the name:")
    a=int(input("enter the age:"))
    g=input("enter the gender:")
    co=input("enter the course:")
    m=int(input("enter the mark:"))
    c.execute('insert into student (rollno,name,age,gender,course,mark)values(%s,%s,%s,%s,%s,%s)',(r,n,a,g,co,m))
    con.commit()
    print("Student inserted succesfully")

def read_record():
    c.execute('select * from student')
    k=c.fetchall()
    print(k)

def search_record():
    r=int(input("enter the rollno:"))
    c.execute('select * from student where rollno=%s',(r,))
    k=c.fetchone()
    if k:
        print(k)
    else:
        print("student not found")

def update_record():
    r=int(input("enter the rollno:"))
    m=int(input("enter the mark:"))
    c.execute('select * from student where rollno=%s',(r,))
    k=c.fetchone()
    if k:
        c.execute('update student set mark=%s where rollno=%s',(m,r))
        c.commit()
        print("mark updated")
    else:
        print("student not found")
        
def delete_record():
    r=int(input("enter the rollno:"))
    c.execute('select * from student where rollno=%s',(r,))
    k=c.fetchone()
    if k:
        c.execute('delete from student where rollno=%s',(r,))
        c.commit()
        print("Record deleted")
    else:
        print("student not found")    

while(1):
    print("1.Insert Student Details")
    print("2.Read all Student Details")
    print("3.Search a Student by rollno")
    print("4.Update the mark of a student")
    print("5.Delete a student record")
    print("6.Exit")


    ch =int(input("enter the choice:"))
    if ch==1:
        insert_record()
    elif ch==2:
        read_record()
    elif ch==3:
        search_record()
    elif ch==4:
        update_record()
    elif ch==5:
        delete_record()
    elif ch==6:
        exit()
    else:
        print("Invalid Choice")    


