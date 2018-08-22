import datetime
import time
def function2(year,month,day):
    date = datetime.date(year,month,day)
    return date.strftime("%j")
