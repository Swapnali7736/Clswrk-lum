#1Given a string
s="I am learning Python"

# find the length of the string
print(len(s))

# find the reverse of the string
print(s[::-1])

# find the last character of the strings
print(s[-1])

#find the 13th character
print(s[12])   
#print the characters from 2nd index to 15 th index
print(s[2:16])

#combines the string s with word "programming"
print(s + " programming")

# #2.Given a list
l=['Guitar','Piano','Violin','Drums','Flute']
#Add a new item 'Veena' to the list
l.append('Veena')

#
# #3Declare a list of 5 food items
foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Sandwich']



#     #Add new fooditem to the list
foods.append("rice")
#     #change the second food item
foods[1] = 'Idli'

#     #print the updated list
print(foods)

#     #print the last food item
print(foods[-1])

#     #print the number of food items

print(len(foods))

#
#4.Given a string
s="python is a programming language"
# #Remove the first 10 characters and print the remaining
print(s[10:])
# #print the last 5 characters
print(s[-5:])
#5.
l=[10,56,23,67,19,70]

#interchange 2nd index and 5th index numbers
l[2],l[5]=l[5],l[2]
print(l)
#6 Given a set
s={10,20,30,40}
# Add a new number 50 to the set
s.add(50)
print(s)
