#finding out  a future date
import datetime

tday = datetime.date.today()

tdelta =datetime.timedelta(days=7)

print(tday + tdelta)

bday = datetime.date(2025,11,10)

till_bday =bday -tday

print(till_bday)