import sqlite3, datetime
db = sqlite3.connect('../cartoon.db')
db.execute("CREATE TABLE cartoon (id INTEGER PRIMARY KEY, episode INTEGER, title CHAR(100), slug CHAR(100), season INTEGER, path CHAR(1000), panels INTEGER)")
db.commit()
db.close()