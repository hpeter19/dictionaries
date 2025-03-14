#DAY OF THE WEEK
from tkinter.messagebox import RETRY


def is_weekend(day):
    match day :
        case "SUNDAY":
            return True
        case "MONDAY":
            return False
        case "TUESDAY":
            return False
        case "WEDNESDAY":
            return False
        case "THURSDAY":
            return False
        case "FRIDAY":
            return False
        case "SATURDAY":
            return True
        case _:
            return False
print(is_weekend("MONDAY"))

