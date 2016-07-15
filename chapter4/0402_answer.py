def nabeatsu(v):
    if v % 3 == 0:
        return 'アホ'
    elif "3" in str(v):
        return 'アホ'
    return v

# 動作確認
result = nabeatsu(3)
print(result)
result = nabeatsu(32)
print(result)
result = nabeatsu(110)
print(result)
