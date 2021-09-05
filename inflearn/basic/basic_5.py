# 반복문을 이용한 문제풀이

# 1) 1부터 N까지 홀수 출력하기
n = int(input())
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)


# 2) 1부터 N까지의 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum+i #  처음 sum은 0. 한번 돌면 0+1이니까 1. 두번 돌면 1+2가 되니까 3. 세번 돌면 3+4가 되니까 7.
    #print(sum) 여기서 출력하면 합이 안나오고 매번 도는것임
print(sum) # 여기서 해야함


# 3) N의 약수 출력하기
n = int(input())
for i in range(1, n+1):
    if n % i == 0: # n을 i라는 숫자로 나눴을 때 0이다? n의 약수인 것이다!!!
        print(i, end = ' ') # end란? 줄 바꿈 \n을 없애고 옆으로 바로 나타나게 해주는 녀석