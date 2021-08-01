import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text, nickname text)")

c.execute("INSERT INTO users VALUES(1, '문준혁', '문통')")