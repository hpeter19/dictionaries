#DAY OF THE WEEK

#USING OR '|' TO GROUP TOGETHER TRUE AND FALSE VALUES

def is_weekend(day):
    match day :
        case "SUNDAY" | "SATURDAY":
            return True
        case "MONDAY" | "TUESDAY"| "WEDNESDAY" | "THURSDAY" | "FRIDAY":
            return False
        case _:
            return False
print(is_weekend("TUESDAY"))





