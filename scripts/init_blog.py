import sqlite3, datetime
db = sqlite3.connect('../blog.db')
db.execute("CREATE TABLE blog (id INTEGER PRIMARY KEY, title CHAR(100) NOT NULL, slug CHAR(100) NOT NULL, content CHAR(10000) NOT NULL, published BOOLEAN NOT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
db.commit()
db.close()