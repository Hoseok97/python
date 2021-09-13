# 파이썬 흐름 제어
# 조건문 실습

print(type(True))
print(type(False))

# 예제
# if True:
    #  print("Yes")

# 관계연산자
# > < == != >= <= 
a = 10
b = 0
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

# 참: "내용", [내용], (내용), {내용}, 1
# 거짓: "", [], (), {}, 0

city = ""
if city:
    print("True")
else:
    print("False")  

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and :', a > b and b > c)
print('or :', a > b or c > b)
print('not :', not a > b)

# 산술, 관게 논리 연산자
# 우선순위 산 > 관 > 논 순서로 적용
print('es1 ', 5 + 10 > 0 and not 7 + 3 ==10)


