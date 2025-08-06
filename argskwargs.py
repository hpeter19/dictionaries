# args -allows you to pass multiple non -key arguments
# kwargs - allows you to pass multiple keyword -arguments
# *unpacking character
# the function is designed to accept both arguments
# args comes first followed n=by kwargs
#using both args and kwargs
# using formatted string instead of loops


def shipping_label(*args,  **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # iterating in the keyword arguments
    for value in kwargs.values():
    print(value, end=" ")

        

shipping_label("Mr","Paul","Jan",
street = "23 Molo",
city = "Nairobi",
state = "Nakuru",
zilp = "20100",
)

