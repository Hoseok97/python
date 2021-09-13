# 딕셔너리, 집합 자료형
# 딕셔너리(Dictionary) : 슨서 x ,중복 x ,수정 o ,삭제 o
# Key, Value (json) - > MongoDB
# 선언 {}
a = {'name' : 'Byun', 'Phone': '010-7777-7777', 'Birth': 970710}
b = {0: 'Hello Pyhton', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys())) # 리스트로 형변환
temp = list(a.keys())
print(temp[1:3])

print(a.items())
print(1 in b)

# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c) # 중복 허용 x

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) # 중복 찾기
print(s1 & s2)
print(s1 | s2) # 합집합
print(s1.union(s2))
print(s1 - s2) # 차집합
print(s1.difference)


# 추가 & 제거
s3 = set([7, 8, 10 ,14])

s3.add(18)
# s3.add(7) 중복 추가 x
print(s3)
s3.remove(14)
print(s3)



