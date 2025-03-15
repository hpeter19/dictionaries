import datetime
from datetime import timedelta

dt_today =datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow =datetime.datetime.utcnow()
#today returns current local time with today with no timezone
#now allows us to pass a timezone
#utcnow gives urrent uct time
print(dt_today)
print(dt_now)
print(dt_utcnow)

