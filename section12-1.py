# 파이썬 데이터 베이스 연동
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y - %m - %d %H:%M:%S')
print(nowDatetime)

#sqllite3
print(sqlite3.version)

# DB 생성 및 Auto Commit(Rollback)
conn = sqlite3.connect('C:/python_basic/resource/datebase.db',isolation_level = None)

# Cursor
c = conn.cursor()

# 테이블 생성(Date Type: Text, INTEGER, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
 c.execute("INSERT INTO users VALUES(1, 'Byun', 'qusghtjr95@naver.com', '010-4903-1879', 'naver.com', ?)", (nowDatetime,))

# Many 삽입(튜플, 리스트)
userList = (
    (2, 'Lee', 'ajhbf.com', '010-1111-1111', 'Lee.com', nowDatetime),
    (3, 'cho', 'cho.com','010-3333-2222','cho.net',nowDatetime)
)

 c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", userList)

# 데이터 삭제
# conn.execute("DELETE FROM users")
# print("user db delete :", conn.execute("DELETE FROM users").rowcount)



















