"""
print("\t\t\tFancy Credits")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")
print ("\nSpecial thanks goes out to:")

print ("\tWelcome to the 'Three-Year-Old Simulator'\n")
print ("This program simulates a conversation with a three-year-old child.")
print ("Try to stop the madness.\n")

health = 50
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health = health - damage

    print("Your hero swings and defeats an evil troll, " \
           "but takes", damage, "damage points.\n")
print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")


print("Welcome to the Chateau D' Food")
print ("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'? "))

if money:
    print("Ah, I am reminded of a table. Right this way.")
else:
    print("Please, sit. It may be a while.")

input("\n\nPress the enter key to exit.")


count = 0
while True:
    count += 1
    # end loop if count is greater than 10
    if count > 10:
       break
    # skip 5
    if count == 5:
        continue
    print(count)

input("\n\nPress the enter key to exit.")

"""
import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randrange(100) + 1
guess = int(input("Take a guess: "))
tries = 1
# guessing loop
while (guess != the_number):
    if (guess > the_number):
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")





