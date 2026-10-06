# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


class Student:
    def __init__(self):
        self.name=input("enter the name:")
        self.rollno=int(input("enter the rollno:"))
        self.mark=int(input("enter the mark:"))
    def updatemarks(self):
        mark=int(input("enter the marks:"))
        self.mark=mark
        print("updated mark:",self.mark)
    def displaydetails(self):
        print(self.name,self.rollno,self.mark)

l=[]
while(1):
    print("Menu driven program")
    print("1.Add student")
    print("2.Update marks")
    print("3.Display all student details")
    print("4.Search student by roll number")
    print("5.Delete Student")
    print("6.Exit")
    
    ch=int(input("enter your choice:"))

    if ch==1:
        s=Student()
        l.append(s)
    elif ch==2:
        r=int(input("enter the rollno:"))
        for i in l:
            if r==i.rollno:
                i.updatemarks()
                break
        else:
            print("not found")    
    elif ch==3:


        for i in l:
            i.displaydetails()
    elif ch==4:
        r=int(input("enter the rollno:"))
        for i in l:
            if r==i.rollno:
                print(i.name)
                break
        else:
            print("not found")
    elif ch==5:
        r=int(input("enter the rollno:"))
        for i in l:
            if r==i.rollno:
             l.remove(i)
             break
        else:
            print("not found")

    else:
        exit()
