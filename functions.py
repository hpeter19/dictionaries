def display_invoice(username,amount,due_date):
    print(f"Hello {username}!")
    print(f"you bill of Ksh{amount:.2f} is due: {due_date}")

display_invoice("Mark",2300, "01/12")
