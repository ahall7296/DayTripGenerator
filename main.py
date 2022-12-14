import random

Destination = ["Gettysburg", "Philadelphia", "York", "Ocean City", "Washington DC"]
print ("You are going to", random.choice(Destination))

Restuarant = ["Dough Roller", "Pizza Hut", "Jimmy's", "Chili's"]
print ("You are eating at", random.choice(Restuarant))

Mode_of_Transportation = ["Car", "Bus", "Plain"]
print ("You will be getting there by", random.choice(Mode_of_Transportation))

Entertainment = ["Museum", "Movie", "Hiking", "Guided Tour"]
print ("Your entertainment will be", random.choice(Entertainment))

Question_1 = input("Do you like all your choices? ")
if Question_1 == "Yes":
    print("Awesome, have a great Trip!")
elif Question_1 == "No":
    next
    def main():
        Question_2 = input("Which option do you not like? ")
        if Question_2 == ("The destination"):
            Destination = ["Gettysburg", "Philadelphia", "York", "Ocean City", "Washington DC"]
            print ("You are going to", random.choice(Destination))
        elif Question_2 == ("The restuarant"):
            Restuarant = ["Dough Roller", "Pizza Hut", "Jimmy's", "Chili's"]
            print ("You are eating at", random.choice(Restuarant))
        elif Question_2 == ("The mode of transportation"):
            Mode_of_Transportation = ["Car", "Bus", "Plain"]
            print ("You will be getting there by", random.choice(Mode_of_Transportation))
        elif Question_2 == ("The entertainment"):
            Entertainment = ["Museum", "Movie", "Hiking", "Guided Tour"]
            print ("Your entertainment will be", random.choice(Entertainment))
        Question_3 = input("Do you like all your options now? ")
        if Question_3 == ("Yes"):
            print("Awesome, have a great Trip!")
        elif Question_3 == ("No"):
            main()

main ()