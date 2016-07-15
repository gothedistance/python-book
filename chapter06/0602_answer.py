def add_number(a,b):
    try:
        return a + b
    except TypeError as te:
        print('数値以外のデータが与えられています。')

add_number(10,'abc')
