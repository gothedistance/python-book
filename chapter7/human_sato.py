class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0
    weight = 0.0

sato = Human()
sato.age = 35
sato.lastname = '佐藤'
sato.firstname = '次郎'
sato.height = 174.1
sato.weight = 68.2

if( sato.age >= 35 and sato.lastname == '佐藤'):
    print('選ばれた人->' + sato.lastname + ' ' + sato.firstname)
