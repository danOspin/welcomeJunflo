import re
from datetime import datetime

def getDates(data):
    regex = re.findall(r'[0-9]*-[0-9]*-[0-9]*', data)
    print (regex)
    print (regex[0])
    print (regex[1])
    dateFrom = datetime.strptime(regex[0], '%Y-%m-%d')
    dateTo = datetime.strptime(regex[1], '%Y-%m-%d')
    return dateFrom-datetime.now()


if __name__ == "__main__":
    data = "<checkin>2018-10-23T15:28:36.8159478-05:00</checkin><checkout>2018-10-24T15:28:36.8159478-05:00</checkout>"
    print(getDates(data))

