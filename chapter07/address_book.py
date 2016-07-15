class AddressBook:

    person_list = []

    def add(self, person):
        self.person_list.append(person)

    def show_all(self):
        for person in self.person_list:
            print(person.lastname + " " + person.firstname)

    def search(self,keyword):
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.firstname + " " + person.lastname)

class Person:
    import datetime

    firstname = ''  # 名前
    lastname = ''  # 苗字
    tel = ''  # 電話番号
    maiL_address = ''  # メアド
    birthday = datetime.datetime(2000, 1, 1)  # 生年月日


ab = AddressBook()

p = Person()
p.firstname = 'みちたか'
p.lastname = 'ゆもと'
p.tel = '090-1234-5678'

ab.add(p)

p2 = Person()
p2.firstname = 'John'
p2.lastname = 'Lennon'
p2.tel = '090-1234-0098'

print('---動作確認---')
ab.add(p2)

print('アドレス帳の人数->' + str(len(ab.person_list)) + ' 人')

print('---一覧表示---')
ab.show_all()

print('--検索--')
ab.search('John')
