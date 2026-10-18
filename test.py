import random

secret = random.randint(1, 15)

# Convert input from string to integer
user_input = int(input("guess a number: "))

if user_input == secret:
    print("you guessed the correct number!!!")
    print("you win!")
elif user_input < secret:
    print("the number was too small")
else:
    print("the number was too big")