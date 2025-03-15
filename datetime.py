import datetime
import pytz
from datetime import timedelta

dt=datetime.datetime(2025,3,15,12,1,26, tzinfo=pytz.UTC)
print(dt)
dt_now=datetime.datetime.now(pytz.UTC)
print(dt_now)
dt_utcnow =datetime.datetime.utcnow().replace( tzinfo=pytz.UTC)
print(dt_utcnow)


#using pytz to print UTC time