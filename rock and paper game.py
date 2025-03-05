import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)

    # Ensure player input is in lowercase and within options
    while player not in options:
        player = input("[Enter a choice (Rock, Paper, Scissors): ").lower()

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the player wants to play again
    play_again = input("Play again (Y/N): ").upper()
    if play_again != "Y":
        running = False

print("Thanks for playing!")
