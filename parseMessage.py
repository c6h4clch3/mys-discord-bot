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
        result.append(datetime.datetime.strptime(str(year) + '/' + item, '%Y/%m/%d %H:%M'))

    return tuple(result)


def parseMessage(message: str):
    splittedMessage = message.splitlines()
    splittedMessage.pop(0)
    title: str = splittedMessage.pop(0)
    timesList: [str] = splittedMessage.pop(0).split(' ~ ')
    times = (timesList[0], timesList[1])
    times = readTime(times)
    description = ''
    for _idx, item in enumerate(splittedMessage):
        description += item + '\n'

    return (title, times, description)

