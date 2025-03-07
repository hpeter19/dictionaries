    #2D list
    groceries = [["Oranges","Mangoes","Oranges"],
    ["Sukuma","Spinach","potatoes"],
    ["Chicken","Pork","Beef"]]

    #printing every item on  our loop using nested for loops
    for collection in groceries:
        for food in collection:
            print(food, end=" ")#these will print each item in a vertical manner
        print()  
