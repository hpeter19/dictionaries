
fruit="apple"

letter = input("Guess a letter in a secret word:")
if letter in fruit:
    print(f"there is a letter {letter}")
else:
    print(f"{letter} was not found")