# 파이썬 에외처리의 이해

# 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 에외 처리도 중요
# linter : 코드 스타일, 문법 체크

# syntaxError : 잘못된 문법
# print('Test)

# if True
#  pass

# x => y

# NameError : 참조변수 없음
#  a = 10
#  b = 15
#  print(c)

# ZerodivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
# x = [10, 20 ,30]
# print(x[3])

# KeyError
# dic = {'name': 'Kim', 'Age' : 33}
# print(dic['hobby'])
# gey 메소드 활용 하면 None 이라 뜸

# AttributeError : 모듈 클래스에 있는 잘못된 속성 사용시에 에외
# import time
# print(time.month)

# ValuError : 창조값 없을 때 발생
# x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open('test.tst','r') # 예외 발생

# TypeError
# x = [1,2]
# y = (1,2)
# z = 'Test'

# print(x + y)

# 예외 처리 기본
# Try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 에제1
# name = ['Kim', 'Lee', 'Park']

# try:
#     z = 'cho'
#     x = name.index(z)
#     print('{}Found it ! in name'.format(z, x+1))
# except ValueError:
#     print('Not Found it! - Occurred ValueError')
# else: # try가 정상 처리 되면 작동
#     print('OK!')

# 에제2
name = ['Kim', 'Lee', 'Park']

try:
    z = 'cho'
    x = name.index(z)
    print('{}Found it ! in name'.format(z, x+1))
except: # 에러가 뭐가 나올지 모를 때 그냥 처리 가능
    print('Not Found it! - Occurred ValueError')
else: # try가 정상 처리 되면 작동
    print('OK!')


# 에제 3
name = ['Kim', 'Lee', 'Park']

try:
    z = 'cho'
    x = name.index(z)
    print('{}Found it ! in name'.format(z, x+1))
except ValueError:
    print('Not Found it! - Occurred ValueError')
else: # try가 정상 처리 되면 작동
    print('OK!')
finally: # 무조건 실행
    print('finally ok!')

# 에제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print("OK!")

# 예제5
# 에외 발생 : raise
try:
    a = 'Kim'
    if a == 'Kim':
        print('OK')
    else:
        raise ValueError
except ValueError:
    print('문제발생!')
else:
    print('OK!')


