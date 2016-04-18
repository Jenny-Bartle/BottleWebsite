import sys, sqlite3, os, fnmatch, re

db = sqlite3.connect('../cartoon.db')
db.execute("CREATE TABLE cartoon (id INTEGER PRIMARY KEY, episode INTEGER, title CHAR(100), slug CHAR(100), season INTEGER, path CHAR(1000), panels INTEGER)")

initFile = open("MandTNumberNameMap.txt")
for line in initFile.readlines() :
	args = line.split(",")
	season = args[0]
	episode = args[1]
	title = args[2]
	toonDir = os.getcwd() + "\\..\\cartoons\\cartoon" + episode
	allPanels = os.listdir(toonDir)
	panels = len(allPanels)
	slug = re.sub('[^\w]+', '-', title.lower())	
	db.execute('INSERT INTO cartoon (episode, title, slug, season, path, panels) VALUES (?, ?, ?, ?, ?, ?)', (episode, title, slug, season, "./cartoons/cartoon" + episode, panels))
db.commit()
db.close()
