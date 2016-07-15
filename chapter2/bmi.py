weight = 57
height = 1.7
bmi = weight / (height ** 2)

if bmi < 18.5:
    print ('やせてる')
elif bmi < 25:
    print ('ふつう')
elif bmi < 35:
    print ('ちょっと太ってる')
else:
    print('だいぶ太ってる')
