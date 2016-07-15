class A:
    def hello(self):
        print('Class A says Hello')

class B(A):
    def hello(self):
        print('Class B says Hello')

b = B()
b.hello()
