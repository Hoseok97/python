# 문자열, 문자열 연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'

print(len(str1), len(str2)) # 문자열 길이

escape_str1 = "Do you have a \"big collection\"" # \로 "" 출력
print(escape_str1)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

# 멀티라인
# \ 가 나오면 뒤에 문자열이 연결됨을 표시
multi = \
""" 
문자열 
멀티라인 
테스트 
"""

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "NiceMan"

print(str_o1 * 10)
print('a' in str_o3) # a라는 문자가 포함되어 있냐 in
print('z' not in str_o3) # 반대

#문자열 형 변환
print(str(77) + 'a')

#문자열 함수
a = 'niceman'
b = 'Orange'

print(a.islower()) #소문자인가
print(b.endswith('e')) # 끝이 e로 꿑나는가
print(a.capitalize()) # 첫글자 대문자 출력
print(a.replace('nice', 'good')) # 교체

print(a[0:3]) # 마지막 숫자 전까지 출력
print(b[0:len(b)])
print(a[:5])
print(b[0:4:2]) # 마지막 만큼 건너뛴다
print(b[1:-2])
print(b[::-1])