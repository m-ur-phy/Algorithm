# 문자열과 내장함수
msg = "It is Time"
print(msg.upper()) # upper() 모든 문자를 대문자로 바꿔줌
print(msg.lower()) # lower() 모든 문자를 소문자로 바꿔줌
print(msg) # 원본은 그대로 있음!

tmp = msg.upper() # tmp는 대문자화된 변수
print(tmp)
print(tmp.find('T')) # 해당하는 문자를 찾아 순서를 반환해준다. 참고로 먼저 나오는 것을 찾아준다.
print(tmp.count('T')) # 해당하는 문자가 몇개 있는지 알려줌

# 문자열 슬라이싱
print(msg)
print(msg[:2]) # 문자열의 제일 처음부터 2번까지(0,1) 출력
print(msg[3:5]) # 공백도 문자에 포함!

print(len(msg)) # 문자 길이 총 10
for i in range(len(msg)): 
    print(msg[i], end=' ')
print()

for x in msg: # 위 코드와 출력 결과는 똑같다
    print(x, end=' ')
print()

for x in msg:
    if x.isupper(): # 대문자일때 참 = 대문자일때 출력
        print(x, end=' ')
print()

for x in msg:
    if x.islower(): # 소문자일때 참 = 소문자일때 출력
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # 알파벳일때만 참 = 알파벳만 출력
        print(x, end=' ')
print()

tmp='AZ' # 대문자 아스키 넘버 A(65) ~ Z(90)
for x in tmp:
    print(ord(x)) # ord()는 아스키 넘버를 출력해준다.

tmp='az' # 소문자 아스키 넘버 a(97) ~ z(122)
for x in tmp:
    print(ord(x))

tmp=65
print(chr(tmp)) # 아스키 넘버에 대응되는 문자를 출력해준다.