# 중첩 반복문(2중 for문)
for i in range(5):
    for j in range(5):
        print(j, end = ' ')
    print() # 줄바꿈

for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print() 

# 별찍기
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print() 

# 별 거꾸로
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()