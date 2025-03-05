
import random


lowest_num =1
highest_num =100
answer = random.randint(lowest_num,highest_num)
#count the number of guesses
guesses =0
is_running =True

print("Python number guessing game")
print(f"select a number between {lowest_num } and {highest_num}")
#while loop to continue each round
while is_running:

    guess= input("Enter your guess ")
    #telling the user input is invalid after putting characters
    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess <lowest_num or guess> highest_num:
            print("Number out of range!!!!")
            print(f"please select a number between {lowest_num} and {highest_num}")
        elif guess< answer:
            print("Too low try again")
        elif guess > answer:
            print("Too high!,try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"number of guesses: {guesses}")
            is_running =False


    else:
        print("Invalid Guess")
        print(f"please select a number between {lowest_num} and {highest_num}")
