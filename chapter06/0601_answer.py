def test(idx):
    try:
        abc = ['a','b','c']
        print(abc[idx])
    except IndexError as ie:
        print('インデックスが範囲外となっています。')

test(10)
