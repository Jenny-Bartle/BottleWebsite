import sys, sqlite3, os, fnmatch, re

initFile = open("MandTNumberNameMap.txt")
db = sqlite3.connect('../cartoon.db')
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
