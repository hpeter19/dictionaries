# args -allows you to pass multiple non -key arguments
# kwargs - allows you to pass multiple keyword -arguments
# *unpacking character
# item method returns key value pairs


def address_name(**kwargs):
    for key,values in kwargs.items():
        print(f"{key},{values}")
address_name(street="23 Molo",
             city="Nairobi",
             state="Nakuru",
             zip="20100")





