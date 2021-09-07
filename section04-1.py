# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "byun",
    "age" : 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7,8,9} 

print(type(v_tuple))
print(type(v_float))

i1 = 39
i2 = 798
big_int1 = 12345
big_int2 = 67890
f1 = 1.765
f2 = 3.987
f3 = .5
print(i1 * i2)
print(big_int1 * big_int2)
print(f3 + i2)

result = f1 + f2
print(result, type(result))

a = 5.
b = 4

print(type(a), type(b))
result2 = a + b 
print(result2)

# 형변환
# int float complex(복소수)
print(int(result2))
print(int('3'))

# 단항 연산자
y = 100
y = y + 100
y += 100

# 수치 연산
print(abs(-7)) #절댓값
n , m = divmod(100, 8) # 몫과 나머지
print(n, m)

import math

print(math.ceil(5.1)) # 크면서 가장 작은 정수
print(math.floor(3.874)) # 가까운 정수

