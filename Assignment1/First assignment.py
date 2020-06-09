'''
N = int(input("Enter your number: "))
y = 0
for i in range (0, N+1):
  if i % 2 != 0:
    y += i
    print(i)
print(y)    
'''
'''
#exercise FizzBuzz game
# 3-5 Fizz Buzz game
# for every number between 1 and N:
# print Fizz if the number is divisible by 3 but NOT 5
# print Buzz if the number is divisible by 5 but NOT 3
# print FizzBuzz if the number is divisble by BOTH (3 and 5)
# otherwise print the number

N = int(input("Enter a number: "))
for i in range (0, N+1):
  if i % 3 == 0 and i % 5 != 0:
    print("Fizz")
  elif i % 5 == 0 and i % 3 != 0:
    print("Buzz")
  elif i % 3 == 0 and i % 5 == 0:
      print("fizzbuss")
  else:
      print(i)
'''
'''
#while loop

y = 0
i = 0
while i <= 5:
    y += i
    i = i + 1
print(y)
'''
subtotal = 0
while True:
    user_selection = int(input("What is your selection? "))
    if user_selection == 1:
        print("You chose waffle cone")
        subtotal += 3.99
        flavor = int(input("What flavor do you want?"))
        if flavor == 1:
            print("you chose chocolate")
            subtotal += 0.50
        elif flavor == 2:
            print("you choose vanilla")
            subtotal += 0.50
        elif flavor == 3:
            print("you choose strawberry")
            subtotal += 0.50
        elif flavor == 4:
            print("you choose Rocky road")
            subtotal += 0.75
        elif flavor == 5:
            print("you choose Cookie Dough")
            subtotal += 0.75
        elif flavor == 6:
            print("you choose no ice cream")
        else:
            print("please choose again1")
    elif user_selection == 2:
        print("You chose cup")
        subtotal += 2.99
        flavor = int(input("What flavor do you want?"))
        if flavor == 1:
            print("you chose chocolate")
            subtotal += 0.50
        elif flavor == 2:
            print("you choose vanilla")
            subtotal += 0.50
        elif flavor == 3:
            print("you choose strawberry")
            subtotal += 0.50
        elif flavor == 4:
            print("you choose Rocky road")
            subtotal += 0.75
        elif flavor == 5:
            print("you choose Cookie Dough")
            subtotal += 0.75
        elif flavor == 6:
            print("you choose no ice cream")
        else:
            print("please choose again1")
    elif user_selection == 3:
        print("You chose regular cone")
        subtotal += 1.99
        flavor = int(input("What flavor do you want?"))
        if flavor == 1:
            print("you chose chocolate")
            subtotal += 0.50
        elif flavor == 2:
            print("you choose vanilla")
            subtotal += 0.50
        elif flavor == 3:
            print("you choose strawberry")
            subtotal += 0.50
        elif flavor == 4:
            print("you choose Rocky road")
            subtotal += 0.75
        elif flavor == 5:
            print("you choose Cookie Dough")
            subtotal += 0.75
        elif flavor == 6:
            print("you choose no ice cream")
        else:
            print("please choose again1")
    elif user_selection == 4:
        print("Thank you for shopping with us today")
        break
    else:
        print("Invalid option -- please pick again!")
print(f"Your subtotal is: ${subtotal}")
sales_tax = 0.08875*subtotal
print(f"Your taxes is:${sales_tax}")
total = subtotal + sales_tax
print(f"Your total is:${total}")




