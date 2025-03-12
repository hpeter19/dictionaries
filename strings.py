word = "APPLE"
letter =input("Guess a letter in the secret word:")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found")    