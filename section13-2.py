# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본완성
# 사운드 적용 및 DB 연동

import random
import time

# 사운드 출력 필요 모듈
import winsound
import sqlite3
import datetime

# Db 생성 & Autocommit
conn = sqlite3.connect('C:/python_basic/resource/record.db',isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

# 테이블 생성
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)"
)

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
        winsound.PlaySound('./sound/good.wav',winsound.SND_FILENAME)
        cor_cnt += 1
    else:
         winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)
         print("Wrong..")

    n += 1

    
end = time.time()
et = end - start
et = format(et, ".3f")                        # 소수 셋째 자리 출력(시간)

if cor_cnt > 2:
    print("합격")
else:
    print("불합격!")

# 기록 DB 삽입
cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
    (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),)
)


print("총 걸린 시간: ", et,"초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass



   

