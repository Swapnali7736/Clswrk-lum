#weight = float(input("Enter weight:"))
#height = float(input("Enter height:"))
#bmi = weight / (height ** 2)
#print( bmi)

#if bmi <= 18.4:
 #   print("Underweight")
#elif bmi <= 24.9:
 #   print("Normal")
#elif bmi <= 39.9:
  #  print("Overweight")
#else:
 #   print("Obese")






#num = int(input("Enter a number: "))
#if (num % 3 == 0 and num % 5 == 0):
 #  print("FizzBuzz")
#elif num % 3 == 0:
 #   print("Fizz")
#elif num % 5 == 0:
 #   print("Buzz")
#else:
 #   print(num)




amount =int(input("Enter amount: "))

code = int(input("Enter product code (1/2/3): "))


if code == 1:
    if amount > 1000:
        amount = amount - (amount * 10 / 100)

elif code == 2:
    if amount > 100:
        amount = amount - (amount * 5 / 100)

elif code == 3:
    if amount > 500:
        amount = amount - (amount * 10 / 100)

print(amount)