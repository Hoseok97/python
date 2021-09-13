# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k1 in q1.keys():
    if k1 == '가을':
        print(q1['가을'])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k2 in q2.values():
    if k2 == '사과':
        print('포함')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
num3 = int(input())
if num3 > 80:
    print('A학점')
elif num3 > 60:
    print('B학점')
elif num3 > 40:
    print('C학점')        
elif num3 > 20:
    print('D학점')
else:
    print('E학점')


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a4 = 12
b4 = 6
c4 = 18
if a4 > b4 and a4 > c4:
    print(a4)
elif b4 > a4 and b4 > c4:
    print(b4)
else:
    print(c4)        

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
num5 = input()
if list(num5[0]) == ['1'] or list(num5[0]) == ['3']:
    print("남자")
else:
    print("여자")   

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for a6 in q3:
    if a6 == "정":
        continue
    else:
        print(a6, end='')

print('')
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

for a7 in range(1,101):
    if (a7 % 2) != 0:
        print(a7, end = '')

print('')
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for a8 in q4:
    if len(a8) >= 5:
        print(a8)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for a9 in q5:
    if a9.islower():
        print(a9)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for a10 in q6:
    if a10.isupper():
        print(a10.lower())
    else:
        print(a10.upper())    

# 리스트 컴프리  헨션
# x = [x for x in range() if 조건문]

numbers = [x for x in range(1,101)]
print(numbers)      