#Shopping cart program using python

foods = []
prices= []
total = 0

while True:
    food = input("Enter food to buy( q to Quit ): ")
    if food.lower() == "q":
        break
    else:

        price = float(input(f"Enter the price of a{food}: Ksh"))
        foods.append(food)
        prices.append(price)
print("-----Your Order------")


for food in foods:
    print(food, end="  ")
for price in prices:
    total += price

print()
print(f"your total is:Ksh{total}")