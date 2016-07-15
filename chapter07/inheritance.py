class A:
    name = 'Class A'

class B(A):
    pass

b = B()
print(b.name) # Class A と表示されます。
