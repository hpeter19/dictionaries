from tkinter.messagebox import RETRY


def day_of_week(day):
    match day :
        case 1 :
            return "it is Sunday"
        case 2:
            return "It is MONDAY"
        case 3 :
            return "It is TUESDAY"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is Thursday"
        case 6:
            return "it is on Friday"
        case 7:
            return "it is on Saturday"
        case _:
            return "not valid"

print(day_of_week(1))
