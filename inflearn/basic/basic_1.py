# 1. 값 교환
a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)

# 2. 변수 타입
a = 12345
print(type(a))

a = 12.123123311432165165156    # 실수형은 8바이트 까지만 출력된다
print(type(a))

a = 'student'
print(type(a))


# 3. 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)

print(a, b, c, sep = ', ')  # 원하는 키워드로 나눠주는 sep
print(a, b, c, sep = '')
print(a, b, c, sep = '\n')


print(a, end = ' ') # 줄바꿈 없애주는 end
print(b, end = ' ')
print(c)
