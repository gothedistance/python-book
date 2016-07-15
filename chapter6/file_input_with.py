try:
    with open('test.txt') as f:
        print(f.read())
except FileNotFoundError as fne:
    print(fne)
