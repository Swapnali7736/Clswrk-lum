##1.prints all numbers between 1 and 100 that are divisible by 3 or 5

# for i in range(1, 101):
#     if(i%3==0 or i%5==0):
#         print(i)

##2.sum of a list

# l=[1,2,3,4]
# new=[]
# s=0
# for i in l:
#     s=s+i
#     new.append(s)
# print(new)

##3.sum of all numbers between them

# a = 2
# b = 5
# sum=0
# for i in range(a, b + 1):
#     sum = sum + i
# print(sum)


##4.sum only the elements at even indices

# l=[10, 20, 30, 40, 50]
# sum = 0
# for i in range(len(l)):
#     if(i%2==0):
#         sum = sum + l[i]
# print(sum)


##5.sum the elements until a 0 is encountered (stop at 0).

# l=[4,9,1,0,6,7]
# sum = 0
# for i in l:
#     if(i == 0):
#         break
#     sum = sum + i
# print(sum)

##6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11

# for i in range(1, 1001):
#     if(i%7==0 and i%11==0):
#         print(i)
#         break

##7.print only those with length ≥ 5. Use continue to skip shorter ones.

# l=["sapota", "apple", "cat", "coconut", "bat"]
# for i in l:
#     if(len(i)<5):
#         continue
#     print(i)

##8.create a new list containing the squares of each element.

# l=[1, 2, 3]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

##9.construct a new string with all vowels removed using a loop.

# s = "hello world"
# new = ""
# for i in s:
#     if(i not in "aeiouAEIOU"):
#         new = new + i
# print(new)

##10.create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).

# l=[5, 2, 8, 6, 2]
# new = []
# for i in l:
#     j = i**2
#     if j > 50:
#         break
#     new.append(j)
# print(new)

##11.From a string containing mixed characters, create a new string containing only digits

# s="abc123x7z"
# new = ""
# for i in s:
#     if(i>='0' and i<='9'):
#         new = new + i
# print(new)

##12.Given a list of strings, create a new list containing the length of each string.

# l=["cat", "banana", ""]
# new = []
# for i in l:
#     new.append(len(i))
# print(new)

##13.create a string made of the first letter of each word.

# l=["Python", "Is", "Great"]
# new=""
# for i in l:
#     new=new+i[0]
# print(new)

##14. create a new list where all negative numbers are replaced with 0.

# l=[4, -3, 2, -1]
# new=[]
# for i in l:
#     if(i<0):
#         new.append(0)
#     else:
#         new.append(i)
# print(new)

##15.print all names of students

# d={101: ['Arun', 23, 'ekm'],102: ['Amal', 25, 'tvm'],103: ['Anu', 26, 'tcr'],  104: ['Kiran', 27, 'ekm']}
# for i in d:
#     print(d[i][0])

##16. program to print the numbers from 1 to 100.But for multiples of:3, print “Fizz” instead of the number
##    5, print “Buzz” instead of the number Both 3 and 5, print “FizzBuzz” Otherwise, print the number itself.

# for i in range(1, 101):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


##17.Python program that prints numbers from 1 to 50:Skip multiples of 5 using continue Stop the loop if the number becomes
#    greater than 40 using break
    
# for i in range(1, 51):
#     if(i>40):
#         break
#     if(i%5==0):
#         continue
#     print(i)


##18.1.program to find reverse of a number(without[::-1])
 #   2.count the number of digits in a given number 
 #   3.sum of digits in  a number

#1.
# n=12345
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(int(rev)) 


#2.
# count=0
# n=1234567
# s=str(n)
# for i in s:
#     count=count+1
# print(count)    


#3.
sum=0 
n=12345
s=str(n)
for i in s:
    sum=sum+int(i)
print(sum)
