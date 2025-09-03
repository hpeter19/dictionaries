class ConcessionStand:
    def __init__(sself):
    self.menu =  {
            'Popcorn': 50.00,
            'Soda': 2.50,
            'Hot Dog': 3.00,
            'Candy': 1.50,
            'Nachos': 4.00Nachos': 4.00
        }
        }
        self.sales = 0.00  # Total sales
    
    def display_menu(self):
        print("Welcome to the Concession Stand!")
        print("Here is the menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")
    
    def take_order(self):
    order = {}
        while True:
            item = input("\nEnter an item to add to your order (or type 'done' to finish): ").title()
            if item == 'Done':
                break
            elif item in self.menu:
                quantity = int(input(f"How many {item}s would you like? "))
                order[item] = quantity
            else:
                print(f"Sorry, we don't have {item}. Please choose from the menu.")
        return order
    
    def calculate_total(self, order):
        total = 0.00
        for item, quantity in order.items():
            total += self.menu[item] * quantity
        return total
    
    def print_receipt(self, order, total):
        print("\n--- Receipt ---")
        for item, quantity in order.items():
            print(f"{item} x{quantity}: ${self.menu[item] * quantity:.2f}")
        print(f"Total: ${total:.2f}")
    
    def update_sales(self, total):
        self.sales += total
        def main():
    stand = ConcessionStand()
    
    while True:
        stand.display_menu()
        order = stand.take_order()
        
        if order:
            total = stand.calculate_total(order)
            stand.print_receipt(order, total)
            stand.update_sales(total)
        
        another_order = input("\nWould you like to take another order? (yes/no): ").lower()
        if another_order != 'yes':
            break
    
    stand.show_sales()
    print("Thank you for visiting the 

    def show_sales(self):
        print(f"\nTotal uSales: ${self.sales:.2f}")

def main():
    stand = ConcessionStand()
    
    while True:
        stand.display_menu()
        order = stand.take_order()
        
        if order:
            total = stand.calculate_total(order)
            stand.print_receipt(order, total)
            stand.update_sales(total)
        
        another_order = input("\nWould you like to take another order? (yes/no): ").lower()
        if another_order != 'yes':
            break
    
    stand.show_sales()
    print("Thank you for visiting the Concession Stand!")

if __name__ == "__main__":
    main()
if __namte__ == "__main__":
    main()
if __name__ == "__main__":
    main()
