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