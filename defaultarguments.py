#arbitrary Argument
#Kwargs
#values in an kwargs for key items
def address_info(**kwargs):
    for key in kwargs.keys():
        print(key)

address_info(street="Mungoni",
             city="Chuka",
             state="Ndagani",
             zip=2389)
