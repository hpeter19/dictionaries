
#printing the date of the next week
import datetime

tday = datetime.date.today()

tdelta =datetime.timedelta(days=7)
#knowing what day was 7 days ago
print(tday - tdelta)