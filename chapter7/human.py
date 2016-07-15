class Human:
    age = 0 #年齢
    lastname = '' #苗字
    firstname = ''  #名前
    height = 0.0
    weight = 0.0

a = Human()
a.age = 30
a.lastname = '田中'
a.firstname = '一郎'
a.height = 180.5
a.weight = 70.2

print(a.age)
print(a.lastname + " " + a.firstname)
