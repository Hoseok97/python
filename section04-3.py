# 리스트, 튜플

# 리스트(순서,  중복, 수정, 삭제 가능)
# 선언

a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'Pen', 'Orange']
e = [10, 100, ['Pen', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = [a, b, c]

del c[1] # 그 자리에 있는 값을 삭제
print(c)
del c[-1]
print()


# 리스트 함수
y= [5, 2, 3, 1, 4]
y.append(6) # 마지막에 새로운 원소 추가
print(y)

y.sort() # 오름차순으로 정렬
y.reverse() # 반대
y.insert(2, 7) # 2번 인덱스에 7 삽입
print(y)
y.remove(2) #  2라는 값을 삭제 
y.pop() # 마지막을 꺼내고 삭제
ex = [88, 77]
y.extend(ex) # 연장 괄호 없이
y.append(ex) # 괄호 있이 연장
print(y)


# 튜플 (순서 0, 중복 0, 수정 삭제 x )

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])


# 튜플 함수
z = (5,2,1,3,4)

print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))



