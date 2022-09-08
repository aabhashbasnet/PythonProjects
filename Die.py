# Dice Roller 
import random
min = 1
max = 6
roll_again = input("Roll the die ?")
if roll_again == "yes" or roll_again =="y":
    print("Rollin the dies")
    print("The values are ")
    print(random.randint(min,max))

