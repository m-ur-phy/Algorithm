# 조건문
x = 7
if x == 7:  # 같냐?
    print("lucky") # 들여쓰기는 꼭 네칸!
    print("hello")

y = 5
if x != 7:  # 같지 않냐?
    print("lucky") # 들여쓰기는 꼭 네칸!
    print("hello")


# 1. 중첩 if문
x = 15
if x >= 10:
    if x % 2 == 1: # %는 나머지 구하기. 2로 나눴을 때 1이 나온다면 그것은 홀수니까!
        print("10이상의 홀수")

x = 9
if x > 0: # 자연수니까 0보다 커야
    if x < 10: 
        print("10보다 작은 자연수")

# 논리 연산자 이용해서 한줄로 더 쉽게 만들기
x = 7
if x > 0 and x < 10: # and 즉 교집합 이용해서 한줄로!!!
    print("10보다 작은 자연수")

# 파이썬은 and 연산 없이도 가능해
x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")


# 2. 분기 if문
x = -3
if x > 0:
    print("양수")
else:   # 그렇지 않으면
    print("음수")

# 다중 if
x = 93
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")


# 가장 중요한건 조건이 맞아야 print가 나타난다요
