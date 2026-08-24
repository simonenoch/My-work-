# city_name = input("Enter your city: ")
# pet = input("whats your pet's name? ")
# print(f"your band name is {city_name} {pet}.")


#welcome to bill calculator
# print("Welcome to bill calculator")
# people = int(input("How many people will split the bill? "))
# total = float(input("what was the total bill? "))
# tip = int(input("what percentage of tip would you like to give? "))

# tip_amount = (tip / 100) * total
# final_bill = total + tip_amount
# each_person = final_bill / people

# print("Each person should pay:", each_person)


# name = input("what's your name? ")
# colour = input("what's your favourite colour? ")
# print(f"{name} likes {colour} colour ")


# weight_pounds = int(input("what's your weight in pounds? "))
# weight_kg = weight_pounds * 0.45
# print(f"{weight_kg}kg")

# fruits = ["apple", "banana", "orange"]
# print(fruits[1])

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)

# fruits = ["apple", "banana", "orange"]
# print(len(fruits))

# foods = ["rice", "yam", "beans"]

# for food in foods:
#     print(f"I like {food}")

# foods = ["rice", "yam", "beans"]
# foods.append("pizza")
# print(foods)


# scores = [71, 80, 90, 100]

# for score in scores:
#     print(score)

# scores = [71, 80, 90, 100]

# for score in scores:
#     print(len(scores))


# name = "Christopher"
# print(name[1:-1])

# custumer_name = "christopher lawson"
# print(custumer_name[3] + custumer_name[17])

# msg = "today is good"
# print(msg[0:])
# print(msg[1:])
# print(msg[:])
# print(msg[:1])
# print(msg[:3])
# print(msg[3:5])

# first_name = "Simon"
# last_name = "Enoch"
# print(f"{first_name} [{last_name}] is a coder")

# name = input("what's your name? ")
# colour = input("what's your favourite colour? ")
# print(f'"{name} favorite colour is {colour}"')


# name = input("enter your name: ")
# print(f"Your name has {len(name)} character")

# print("social media platform")
# sentence = input("write a sentence with the word stupid: ")
# output = sentence.lower()
# clean_output = output.replace('stupid', '*****')
# print(f"clean message: {clean_output}")

# print("\n UNIVERSITY ADMISSION PORTAL")
# name = input("Enter your full name: ")
# age = input("enter your age: ")
# jamb_score = int(input("enter your jamb score: "))
# course = input("course of study: ")
# waec_neco = int(input("how many credits do you have? "))

# eligible = jamb_score >= 180 and waec_neco >= 5
# percentage = (jamb_score / 400) * 100
 
# print("\n======  ADMISSION SUMMARY =========")-
# print(f"NAME : {name}")
# print(f"COURSE : {course.upper()}")
# print(f"AGE :  {age}")
# print(f"JAMB SCORE : {jamb_score}")
# print(f"WAEC/NECO CREDITS : {waec_neco}")

# print("\n=======STATISTICS==========")
# print(f"JAMB SCORE PERCENTAGE : {percentage}%")
# if eligible:
#     print(f"ADMISSION STATUS: ADMITTED TO {course.upper()}" )


# COMBINING IF AND IN
# names = ["Aman", "Simon", "Mary"]
# name = input("Enter a name: ")

# if name in names:
#     print("Name found!")
# else:
#     print("Name not found!")

# students = ["Enoch", "Simon", "Chindo"]
# student = input("Enter student name: ")

# if student in students:  
#     print(f"{student} is registered.")
# else:
#     print(f"{student} is not registered.")

# ROLL DICE GAME
# import random 
# while True:
#       choice = input("Roll a dice? (Yes/No): ").lower()

#       if choice == "yes":
#          die1 = random.randint(1, 6)
#          die2 = random.randint(1, 6)
#          print(f"({die1}, {die2})")
#       elif choice == "no":
#          print("Thanks for playing!")   
#          break
#       else:
#        print("invalid choice!") 

# price_house = 1000000
# credit = input("is your credit good? (yes/no) ").lower()

# if credit == "yes":
#     down_payment = price_house * 0.10
# else:
#     down_payment = price_house * 0.20
# print(f"DOWN PAYMENT IS $ {down_payment}" )       


# print("\n ***** BMI CALCULATOR  ******")

# weight = float(input("Enter your weight: "))
# weight_unit = input("kg or lbs: ")
# height = float(input("Enter your height: "))
# height_unit = input("cm or m: ")

# if weight_unit == "lbs":
#     weight_kg = weight * 0.45
# else:
#     weight_kg = weight    
# if height_unit == "cm":
#     height_m = height / 100
# else:
#     height_m = height    
# bmi =round(weight / (height ** 2))        
# print(f"BMI = {bmi} ")


# print("\n **** YOUR LIFE CALCULATOR ****** ")
# name = input("Enter your name: ").upper()
# targeted_age =int (input("Enter your targeted age: "))
# age = int(input("What is your age? "))

# years_left = targeted_age - age
# days_left = years_left * 365
# weeks_left = years_left * 52
# months_left = years_left * 12

# print(f"{name} HAVE {days_left} DAYS, {weeks_left} WEEKS AND {months_left} MONTHS LEFT. ")

# LESSONS FOR LOOP WITH range()

# for i in range(5):
#     print(i)
# for i in range(1, 6):
# #     print("Hello World")
# for i in range(4):
#     print("Welcome to python first program")
# for i in range(1, 4):
#     print(f"Day {i}")
# for i in range(5, 0, -1):
#     print(i)
# print("✈ blast off")    

# print("\n")
# Gender = input("what is your gender(male / female): ")
# age= int( input("enter your age: "))
# if Gender == "male":
#      print("use door_A")
#      if age > 12 :
#        print("Sit at the  back") 
#      else :
#         print("Not qualified")
# elif Gender == "female" :
#    print("Use door_B")
#    if age < 12 :
#       print("Sit in the front row")
#    else:
#        print("Not qualified")

# print("======LEAP YEAR VERIFIER=====")

# year = int(input("Enter a year: "))   
# if year % 400 == 0:
#     is_leap = True
# elif year % 100 == 0:
#     is_leap = False
# elif year % 4 == 0:
#     is_leap = True
# else:
#     is_leap = False
# print(f"\nYear: {year}")        
# print(f"Leap Year:{is_leap}")

# if is_leap:
#      print(f"{year} is a Leap Year✅✅.")
# else:
#      print(f"{year} is Not a Leap year❌❌.")

# print(f"\n====== GUESSING GAME ========")

# import random

# secrete_number = random.randint(1, 20)
# guess_count = 0
# guess_limit = 5

# while guess_count < guess_limit:
#     guess = int(input("guess a number between 1 and 20: "))
#     guess_count += 1
#     if guess == secrete_number:
        
#        print("\n 🎉👏👏Correct you guessed the right number .")
#        print("🎉🎉WINNER🎁🎁🎁")
    
#        break
#     elif guess < secrete_number:
#             print("Too low! try again.👇👇")
#     else:
#        print("Too high! Try again.👆👆")
# else:       
#  print(f"\n ❌❌Game over 😭😭😢! the number was {secrete_number}.")

# print(f"🍕🍕🍕🍕PIZZA DELIVERY APP")
# print(f"\n Welcome to SMAN pizza 🍕🍕🍕🍕delivery app ")
# pizza_price = 0
# pepperoni_price = 0
# cheese_price = 0

# name = input("Enter your name: ")
# size = input("choose pizza size (S,M,L): ").upper()

# if size == "S":
#     pizza_price = 10
# elif size == "M":
#     pizza_price = 15
# elif size == "L":
#     pizza_price = 20
# pepperoni = input("Pepperoni? (Y(S,M,L), N): ").upper()
# if pepperoni == "YN":
#     pepperoni_price = 2
# elif pepperoni == "YM" or "YL":
#     pepperoni_price = 3
# cheese = input("Extra cheese? (Y/N): ").upper()
# if cheese == "Y" :
#     cheese_price = 1
# total = pizza_price + pepperoni_price + cheese_price
# print(f"{name} your total bill is ${total} ")              

# print("🌴🌴Welcome to treasure Island! ")
# print("Your mission is to find hidden treasure.💰👑👑")   
# direction = input("You are at a cross road.Go Left or Right? ").lower()        
# if direction == "left"  :
#     print("You have arrived safely at the lake.🌊🌊")        
#     action = input("Do you want to wait or swim? ").lower()
#     if action == "wait" :
#      print("A boat takes you to an island.🏝🏝")
#      door = input("Choose a door: Red, Yellow, or Blue :").lower()
#     if door == "yellow":
#         print("🎉🎉congratulatins! you found the treasure!💰👑👑")
#     elif door == "red":
#         print("🔥you entered the room of fire. GAME OVER!!🔥🔥🔥")
#     elif door == "blue":
#         print("🐊🐊Full of crocodiles!GAME OVER!!!")
#     else :   
#         print("❌❌invalid door.GAME OVER!!")
# else:     
#     print("you fell into a dip hole.GAME OVER!!😭)
           

# sentence = input("write a setence: ").lower()
# checked = ""
# highest = 0
# most_letter = ""
# for letter in sentence:
#     if letter !=" "    and letter not in checked:
#         count = sentence.count(letter)
#         print(f"{letter} appears {count} times")
#         if count > highest:
#             highest = count
#             most_letter = letter
# print(f"\nThe most repeated letter is {most_letter}.")
# print(f"it appears {highest} times.")
# checked += letter
# reverse = ""        
# for letter in sentence :
#     reverse = letter + reverse
# print(reverse) 
       
class BankAccount:
    
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance
    def   greet(self):
        print("Good Morning sir/Ma ")  
    def deposit(self, amount):
        self.balance += amount
        print(f"Account: {self.owner_name}")
        print(f"Deposited: {amount}")
        print(f"New balance: {self.balance}")
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance ") 
        else:
            self.balance -= amount 
            print(f"New balance: {self.balance}")
    def current_balance(self):
        print(f"Current Balance : {self.balance}") 
name = input("Enter your name : ")   
balance = float(input("Enter starting balance : "))
deposit_amount = float(input("Enter deposit amount : "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

account = BankAccount(name,balance)       
account.greet()
account.deposit(deposit_amount)
account.withdrawal(withdrawal_amount)
account.current_balance()
    
 
           
           
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
           