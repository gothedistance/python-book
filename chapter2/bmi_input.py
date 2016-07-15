weight = input('体重をKg単位で入力して下さい　')
height = input('身長をm単位で入力して下さい　')
bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    print ('やせてる')
elif bmi < 25:
    print ('ふつう')
elif bmi < 35:
    print ('ちょっと太ってる')
else:
    print('だいぶ太ってる')
