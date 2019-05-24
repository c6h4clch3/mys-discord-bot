from parseMessage import parseMessage
from registerGoogleCalendar import addCalendar

with open('./example.txt') as f:
    print('---input--------------------------')

    message = f.read()
    print(message)

    print('---parsed--------------------------')
    parsed = parseMessage(message)
    print(parsed)
    addCalendar(parsed[0],parsed[1], parsed[2])
