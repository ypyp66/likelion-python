weight, height = map(float,input("몸무게와 키 입력: ").split())
bmi = weight / height*100**2

if bmi>20.0 and bmi<25.0:
    print('표준입니다')
else:
    print('체중관리가 필요합니다')


