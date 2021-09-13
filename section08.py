# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현제 디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print(Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

print("ex2 : ", fb.fib2(400))
print(fb().title)

# 사용4(함수)
import pkg.calculations as c

print("ex4 : ",c.add(10, 100))
print("ex4 : ",c.div(10, 100))

# 사용5(함수)
from pkg.calculations import mul as m
print("ex5 : ", m(10, 100))

# 사용6
import pkg.prints as p
p.prt1()
p.prt2()
        

