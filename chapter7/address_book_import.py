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
                print(person.lastname + " " + person.firstname)

    def import_data(self,file):
        import csv
        import datetime

        with open(file, 'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # ヘッダーがあればスルー

            for row in reader:
                #rowに1行1行のデータが配列になって入ってくる
                p = Person()
                p.lastname = row[0]
                p.firstname = row[1]
                p.mail_address = row[2]
                #日付の文字列から日付型のデータを作る
                p.birthday = datetime.datetime.strptime(row[3], "%Y/%m/%d")
                p.tel = row[4]

                self.person_list.append(p)

class Person:
    import datetime

    firstname = ''  # 名前
    lastname = ''  # 苗字
    tel = ''  # 電話番号
    maiL_address = ''  # メアド
    birthday = datetime.datetime(2000, 1, 1)  # 生年月日

ab = AddressBook()
ab.import_data('sample100.csv')

print('アドレス帳の人数->' + str(len(ab.person_list)) + ' 人')

ab.search('片山')
