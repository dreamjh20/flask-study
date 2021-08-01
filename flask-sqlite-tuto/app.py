import sqlite3
import sys

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text, nickname text)")

global A
A = 1

print("\'sudo shutdown\' to exit")
def put(AA):
    a, b =input("INPUT NAME AND NICKNAME: ").split()
    if a == 'sudo' and b == 'shutdown':
        print("SHUTDOWN")
        sys.exit()
    else:
        c.execute("INSERT INTO users VALUES(?, ?, ?)",(AA, a, b))

while True:
    put(A)
    A += 1