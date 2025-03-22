#arbitrary Argument
#Kwargs
#values in an kwargs
def address_info(**kwargs):
    for value in kwargs.values():
        print(value)

address_info(street="Mungoni",
             city="Chuka",
             state="Ndagani",
             zip=2389)
