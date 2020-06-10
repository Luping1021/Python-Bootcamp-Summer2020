#Programming Challenge 1-Temperature convertor
#1. Converts user input from degree Fahrenheit to Celsius
#2. Converts user input from degrees Fahrenheit to Kelvin

user_input = int(input("Enter a temperature in degree F: "))
user_selection = int(input("Pick a option: "))

if user_selection == 1:
    temperature = (5/9)*(user_input - 32)
    print(f"{user_input} degree Fahrenheit is {temperature} degree Celsius")
elif user_selection == 2:
    temperature = ((5/9)*(user_input - 32))+273.15
    print(f"{user_input} degree Fahrenheit is {temperature} Kelvin")
else:
    print("Wrong Choice, please restart")
print("Conversion finished")


#Programming Challenge 2-Voltage division

input_voltage = int(input("Enter an V_in: "))
resistor_1 = int(input("Enter an R_1: "))
resistor_2 = int(input("Enter an R_2: "))
output_voltage = (resistor_2 / (resistor_1 + resistor_2)) * input_voltage
print(f"V_out is {output_voltage} when V_in is {input_voltage}, R_1 is {resistor_1}, and R_2 is {resistor_2}")


#Programming Challenge 3-3&7 Fizz-Buzz
#write a loop from 1 to N
#"Fizz"-a number is divisible by 3 but NOT divisible by 7
#"Buzz"-a number is divisible by 7 NOT 3
#"FizzBuzz"-a number is both divisible by 3 and 7

N = int(input("Enter a number: "))
for i in range (1, N+1):
    if i % 3 == 0 and i % 7 != 0:
        print("Fizz")
    elif i % 7 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBuzz")
    else:
        print(i)


#Programming Challenge 4-Kiosk machine at McBurger Queen
#Menu option-
    #1.McWhopper-$ 6.89
    #2.Crispy McFish-$4.99
    #3.Fries
        #a. small-$0.99
        #b. Medium-$1.99
        #c. Large-$2.99
    #4.Sode
        #a. small-$0.50
        #b. Medium-$1.50
        #c. Large-$2.00
    #5. Happy Meal-$6.99
    #6. Family Deal-$19.99
    #7. Finish ordering
    #sales tax is 8.875%

print("Welcome to McBurger Queen!")
subtotal = 0
while True:
    user_selection = int(input("Please start to order your meal: "))
    if user_selection == 1:
        print("You choose a McWhopper")
        subtotal += 6.89
    elif user_selection == 2:
        print("You choose a Crispy McFish")
        subtotal += 4.99
    elif user_selection == 3:
        print("You choose a Fries")
        size = int(input("What size you want? "))
        if size == 1:
            print("You choose a small fries")
            subtotal += 0.99
        elif  size == 2:
            print("You choose a medium fries")
            subtotal += 1.99
        elif size == 3:
            print("You choose a large fries")
            subtotal += 2.99
        else:
            print("Wrong choise. Please choose again.")
    elif user_selection == 4:
        print("You choose a Soda")
        size = int(input("What size you want? "))
        if size == 1:
            print("You choose a small fries")
            subtotal += 0.50
        elif  size == 2:
            print("You choose a medium fries")
            subtotal += 1.50
        elif size == 3:
            print("You choose a large fries")
            subtotal += 2.00
        else:
            print("Wrong choise. Please choose again.")
    elif user_selection == 5:
        print("You choose a Happy Meal")
        subtotal += 6.99
    elif user_selection == 6:
        print("You choose a Family Deal")
        subtotal += 19.99
    elif user_selection == 7:
        print("Finish ordering. Thank you for ordering with McBurger Queen")
        break
    else:
        print("It's an invalid option. Please choose again")
print(f"Your subtotal is: ${subtotal}")
sales_tax = 0.08875*subtotal
print(f"Your taxes is:${sales_tax}")
total = subtotal + sales_tax
print(f"Your total is:${total}")


#Programming Challenge 5-Day of the Programmer
#range from 1700 -2700 inclusive, 256th day -day of the programmer
#1918-09.26
#leap year-09.12
#other years-09.13

user_input = int(input("Enter a year: "))
if user_input > 1700 and user_input < 2700:
    if user_input == 1918:
        print(f"In {user_input}, the day of the programmer is 09.26")
    elif user_input % 400 == 0:
        print(f"In the leap year of {user_input}, the day of programmer is 09.12 ")
    elif user_input % 4 == 0 and user_input % 100 != 0:
        print(f"In the leap year of {user_input}, the day of programmer is 09.12 ")
    else:
        print(f"In {user_input}, the day of the programmer is 09.13")
else:
    print("Invalid year. Pick anther year that is between 1700 to 2700.")



