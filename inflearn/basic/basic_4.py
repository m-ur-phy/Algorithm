# 반복문 (for, while)

a = range(1, 11)
print(list(a))


# 반복문 for
for i in range(10):
    print("hello")

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1): # 꼭 세번째 인자(간격)를 추가해야함
    print(i)


# 반복문 while
i = 1 # 항상 i를 정의 해주고 시작
while i <= 10:
    print(i)
    i = i + 1

i = 10
while i >= 1:
    print(i)
    i = i - 1


# break
i = 1
while True: # 무한반복 코드
    print(i)
    if i == 10:
        break
    i += 1 # i = i + 1의 축약형!!!


# continue
for i in range(1, 11):
    if i%2 == 0: # 이 조건의 참은 짝수
        continue # 이 조건이 참이 되었을 때 continue 해라 -> 밑 코드들을 지나가고 다시 실행해라
    print(i)


# for else 구문!!
for i in range(1, 11): 
    print(i)
    if i==5:
        break
else: # 브레이크에 걸리지 않고 정상 종료시에 else가 실행된다. break에 걸린 경우에는 else문 실행 안됨.
    print(11)