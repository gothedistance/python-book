class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0 # メートル
    weight = 0.0 # Kg

    def get_bmi(self):
        return (self.weight) / (self. height ** 2 )

nakata = Human()
nakata.lastname = '中田'
nakata.firstname = '敦彦'
nakata.weight = 68
nakata.height = 1.7

bmi = nakata.get_bmi()
print(bmi)
