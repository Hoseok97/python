# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본완성

import random
import time

words = []
cor_cnt = 0
n = 1

with open('./resource/word.txt','r') as f:         # 문제 txt 파일 로드
    for c in f:
        words.append(c.strip())

input("Press Enter Key!!")
start = time.time()

while n <= 5:
    random.shuffle(words)                        # List shuffle!
    q = random.choice(words)                     # List -> words random extract!

    print()

    print("*Qustion # {}".format(n))
    print(q)
    x = input()

    print()

    if q.strip() == x.strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong..")

    n += 1

    
end = time.time()
et = end - start
et = format(et, ".3f")                        # 소수 셋째 자리 출력(시간)

if cor_cnt > 2:
    print("합격")
else:
    print("불합격!")

print("총 걸린 시간: ", et,"초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass



   

