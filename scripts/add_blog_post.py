import sqlite3, datetime, os, fnmatch, re, shutil
from markdown import markdown

blogDir = os.getcwd() + "\\..\\blog_archive\\"
archiveDir = blogDir + "\\archive"
	
db = sqlite3.connect('..\\blog.db')
for fileName in os.listdir(blogDir):
	filePath = os.path.join(blogDir, fileName)
	if fnmatch.fnmatch(filePath, '*.txt'):
		with open(filePath) as file:
			content = markdown(file.read())
			file.close()
			title = os.path.splitext(fileName)[0]
			slug = re.sub('[^\w]+', '-', title.lower())
			time = datetime.datetime.now()
			db.execute('INSERT INTO blog (title, slug, content, published, time) VALUES (?, ?, ?, 1, ?)', (title, slug, content, time))
			shutil.move(filePath, archiveDir)
db.commit()
db.close()