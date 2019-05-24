import datetime
import re


def readTime(times: tuple):
    result = [None, None]
    for idx, item in enumerate(times):
        if idx > 2:
            break
        now = datetime.datetime.now()
        searched = re.search(r'(\d{1,2})/(\d{1,2})', item)
        monthStr = searched.groups()[0]
        month = int(monthStr)
        dateStr = searched.groups()[1]
        date = int(dateStr)
        year = now.year
        if (now.month > month or (now.month == month and now.day > date)):
            year += 1
        result[idx] = (datetime.datetime.strptime(
            str(year) + '/' + item + '+09:00', '%Y/%m/%d %H:%M%z'))

    if (result[1] == None):
        start = result[0]
        result[1] = start + datetime.timedelta(hours=1)
    return tuple(result)


def parseMessage(message: str):
    splittedMessage = message.splitlines()
    splittedMessage.pop(0)
    title: str = splittedMessage.pop(0)
    timesList: [str] = splittedMessage.pop(0).split(' ~ ')
    times = readTime(timesList)
    description = ''
    for _idx, item in enumerate(splittedMessage):
        description += item + '\n'

    return (title, times, description)
