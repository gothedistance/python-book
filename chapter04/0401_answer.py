def compare_string(a,b):
    if len(a) > len(b):
        return a
    return b

# 動作確認
result = compare_string('AAA','BBBBB')
print(result)
