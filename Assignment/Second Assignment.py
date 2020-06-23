#Part 1--Programming Challenges for Everyone
#Programming Challenge # 1. The odd list
#The input should be a list. The function should return a new list containing only the add numbers from the input list
'''
N = 20
some_list = []
for i in range(0,N):
    some_list.append(i)

def odd_list(input_list):
    output_list = []
    for index in range(0, len(input_list)):
        num_in_question = input_list[index]
        if num_in_question % 2 != 0:
            output_list.append(num_in_question)
    return output_list
print(f"The input list will be {some_list}")
list_of_odds = odd_list(some_list)
print(f"The odd list is {list_of_odds}")
'''

#Programming Challenge # 2. Multiple
#The input to the function should be an integer. The function should return a list of all integers between a and 100 (non-inclusive)
#that are multiples of the input
'''
N = int(input("Enter a number: "))
def multiple_func(input_value):
    output_list = []
    for i in range(1, 100):
        element_multiple = input_value * i
        output_list.append(element_multiple)
    return output_list
multiple_list = multiple_func(N)
print(multiple_list)
'''

#Programming Challenge # 3. Sorted or not
#The input of the function should be a list of number. The function should return a list of numbers (either integers or floating-point number)
#The function should determine if the list is sorted in ascedind order or not
'''
N = 20
some_list = []
for i in range(0,N):
    some_list.append(i)

def is_sorted(input_list):
    output_list = []
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[i-1]:
            return "It's not sorted"
    return "It's sorted"
print(some_list)
output_list = is_sorted(some_list)
print(output_list)
'''

#Programming Challenge # 4. Slot Machine
#The slot machine has three columns much like the one shown on the right. Each column has the possibilities of:
#['Cherry', '7', 'J', '10', 'Apple', 'A', 'Q', 'M']
#Write a function that picks three random items from the list. Put these three items into a new list and return it
'''
import random
slotlist_each_column = ['Cherry', '7', 'J', '10', 'Apple', 'A', 'Q', 'M']
def random_list(input_list):
    random_list = []
    item1 = random.choice(input_list)
    item2 = random.choice(input_list)
    item3 = random.choice(input_list)
    random_list.append(item1)
    random_list.append(item2)
    random_list.append(item3)
    return random_list
    
slot_machine = random_list(slotlist_each_column)
print(slot_machine)
'''
#Part III Programming Challenges for ChemE 
# 1 - Charles' Law
# Charles's law is a special case of the ideal gas law where the pressure of a gas remins constant
# Vi/Ti = Vf/Tf, T in Kelvin
#  Write a function that takes in 3 inputs: Vi, Ti, and Tf. Assume that the units for temperature is given in Celsius, the output should be the final volume
'''
V_i = float(input("What's your initial volume?"))
T_i = float(input("What's your initial temperature?"))
T_f = float(input("What's ypur final temperature?"))
def final_Volume(Vin, Tin, Tfi):
    Vfi = (Vin * (Tfi + 273.15)) / (Tin + 273.15) 
    return Vfi
V_f = round(final_Volume(V_i, T_i, T_f), 3)
print(f"When Vi = {V_i}, Ti ={T_i} degree C, Tf = {T_f} degree C, the final volume is {V_f}")
'''

#2--Average Atomic Mass
#Average Atom Mass = sum(Fractional Abundance)(Isotope atomic mass)
#Write a function that takes in 2 inputs: a list of isotope atomic masses, and a list of fractional abundances.
#the output should be a floating-point number that represent the average atomic mass
'''
isotope_Atomic_mass = [12.0, 13.49]
fractional_abundance = [0.7577, 0.2423]

def average_massFunc(isotopemass, fraction):
    average_value = 0
    average_mass_list = []
    for A, B in zip(isotopemass, fraction):
        averagemass = A * B
        average_mass_list.append(averagemass)
    for value in average_mass_list:
        average_value += value
    return average_value

average_value = average_massFunc(isotope_Atomic_mass, fractional_abundance)
print(f"the average atomic mass of this element is {average_value} amu")
'''
#Part V. Extra Credit Problem
#1 - Playing slots
#from challenge #4 1000 times, count how many times a iackpot occurs
#A jackport--when all three elements are the same
'''
import random

slotlist_each_column = ['Cherry', '7', 'J', '10', 'Apple', 'A', 'Q', 'M']
def random_list(input_list):
    random_list = []
    item1 = random.choice(input_list)
    item2 = random.choice(input_list)
    item3 = random.choice(input_list)
    random_list.append(item1)
    random_list.append(item2)
    random_list.append(item3)
    return random_list

attempt = 0
jackpot = 0
while True:
    attempt += 1
    slot_machine = random_list(slotlist_each_column)
    item1 = slot_machine[0]
    item2 = slot_machine[1]
    item3 = slot_machine[2]
    if attempt < 1000:
        if item1 == item2  == item3:
            jackpot += 1
            # print(f"{item1}, {item2}, {item3} it's jackpot")
        # else:
        #     print(f"{item1}, {item2}, {item3} it's not jackpot")
    else:
        break
print(f"there are {jackpot} times jackpot")
'''

#Extra Credit 2---Uno deck
#there are 108 cards in an Uno deck. There are four suits, Red, Green, Yellow, and Blue
#each consisting of one 0 card, two 1 cards, two 2s, 3s, 4s, 5s, 6s, 7s, 8s, and 9s; two Draw Two cards
#two skip cards and two Reverse cards
#four Wild cards and four Wild Draw Four cards

deck_of_Uno =[]
suits = ['Red', 'Green', 'Yellow', 'Blue']
card_values = []
for i in range(1, 10):
    card_values.append(str(i))
card_values.append("Draw Two")
card_values.append("Skip")
card_values.append("Reverse")
# print(card_values)
card_value1 =  [ele for ele in card_values for i in range(2)] 
card_value1.append('0')
# print(card_value1)

for value in card_value1:
    for suit in suits:
        deck_of_Uno.append(value + ' of ' + suit)
# OR:
# for value in card_values:
#     #print(value)
#     deck_of_cards.append(value + ' of Diamonds')
#     deck_of_cards.append(value + ' of Clubs')
#     deck_of_cards.append(value + ' of Hearts')
#     deck_of_cards.append(value + ' of Spadess')
# print(len(deck_of_cards))
card_value2 =[]
card_value2.append("Wild")
card_value2.append("Wild Draw")
card_value2 = [ele for ele in card_value2 for i in range(4)] 
deck_of_Uno = deck_of_Uno + card_value2

print(len(deck_of_Uno))
import random
print("unshuffled")
print(deck_of_Uno)
random.shuffle(deck_of_Uno)
print("shuffle")
print(deck_of_Uno)