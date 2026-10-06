# # # Q1.Define a function that takes 2 numbers and returns their product

def product(a, b):
    p = a * b
    return p

result = product(3, 4)
print(result)



# # Q2.Define a function that takes a string and returns number of vowels

def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count = count + 1
    return count

result=count_vowels("programming")
print(result)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

def area(l,b):
    a=l*b
    return a
result = area(10,5)
print(result)

#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]

def list(l):
    new=[]
    for i in l:
        if(i % 2 == 0):
            new.append(i)
    return new
l = [45, 78, 90, 12, 35]
result=list(l)
print(result)



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]



def sum(l):
    l = [123, 345, 111, 678, 134, 809]
    new = []
    for i in l:
        s = 0
        for j in str(i):
            s=s+int(j)
        new.append(s)
    return new

print(sum(l))
