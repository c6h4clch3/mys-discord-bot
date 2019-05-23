from parseMessage import parseMessage

with open('./example.txt') as f:
    print('---input--------------------------')

    message = f.read()
    print(message)

    print('---parsed--------------------------')
    parsed = parseMessage(message)
    print(parsed)
