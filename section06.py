# 파이썬 함수식 및 람다
# 함수 정의 방법
# def function name(parameter):
#  code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 선언 후 함수 사용 가능

#예제1
def hello(world):
    print('Hello ',world)

hello("Python!")    

# 예제 2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Pyhon!!!")
print(str)


# 다중 return
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4
# *args, *kwargs
# 튜플로 여러 값 받는거 가능

def args_func(*args):
    # print(args)
    for i,v in enumerate(args): # 앞에 숫자를 붙여 인덱스 처럼 보여줄 수 있다.
        print(i, v)
    

args_func('Kim')
args_func('Kim', 'Park')

# kwargs
# 딕셔너리로 받음
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1 = 'Kim', name2 = "Park", name3 = "Byun")

# 중첩 함수(클로저)
# 큰 함수 후 작은 함수 실행..?
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)        

# 예제 6 (힌트가 있는 함수)
def func_mul3(x : int) -> list:
    y12 = x * 100
    y21 = x * 200
    y31 = x * 300
    return [y12, y21, y31]

print(func_mul3(5))    

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

lambda_mul_10 = lambda x: x * 10

print(lambda_mul_10(10))

# 람다 응용

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10,10,lambda_mul_10)

print(func_final(10,10,lambda x : x * 1000))