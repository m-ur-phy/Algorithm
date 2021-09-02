# 1. 변수 직접 입력 받기
a = input("숫자를 입력해주세요 : ")
print(a)

a, b = input("숫자를 입력해주세요 : ").split() # 두 개의 수를 받을 때 split을 이용해서 분리
print(a + b) # 이대로 +를 이용하게 되면 입력을 str으로 받았기에 문자열 그대로 붙은 채 반환된다.

# 2. 사칙연산자
a, b = map(int, input("숫자를 입력해주세요 : ").split()) # map 함수 이용 -> int형으로 바꿔주기
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 몫만 구하기
print(a % b) # 나머지 구하기
print(a ** b) # 거듭제곱 구하기

# 3. 형
a = 4.3
b = 5
c = a+b #  과연 c는 무슨 형일까?
print(type(c)) # 실수 > 정수 , 즉 실수 범위가 크기에 실수형으로 나온다.
