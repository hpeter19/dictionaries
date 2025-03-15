#finding out  a future date
import datetime

tday = datetime.date.today()

tdelta =datetime.timedelta(days=7)

print(tday + tdelta)

bday = datetime.date(2025,11,10)

till_bday =bday -tday
#prints the amount of seconds to an event
print(till_bday.total_seconds())