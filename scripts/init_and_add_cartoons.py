import sys, sqlite3, os, fnmatch, re

db = sqlite3.connect('../cartoon.db')
db.execute("CREATE TABLE cartoon (id INTEGER PRIMARY KEY, episode INTEGER, title CHAR(100), slug CHAR(100), season INTEGER, path CHAR(1000))")
db.execute("CREATE TABLE cartoon_panel (id INTEGER PRIMARY KEY, episode INTEGER, panelId INTEGER, panelName CHAR(100))")

def putPanels(episode):
	toonDir = os.getcwd() + "\\..\\cartoons\\cartoon" + episode
	allPanels = os.listdir(toonDir)
	for panel in allPanels:	
		panelId = re.search("[\d]+", panel)
		db.execute('INSERT INTO cartoon_panel (episode, panelId, panelName) VALUES (?, ?, ?)', (episode, int(panelId.group()), panel))
		#print('episode {}, panelId {}, panelName {}'.format(episode, int(panelId.group()), panel))
	db.commit()

initFile = open("MandTNumberNameMap.txt")
for line in initFile.readlines() :
	args = line.split(",")
	season = args[0]
	episode = args[1]
	title = re.sub('[\r\n]+', '', args[2])
	putPanels(episode)
	slug = re.sub('[^\w]+', '-', title.lower())	
	db.execute('INSERT INTO cartoon (episode, title, slug, season, path) VALUES (?, ?, ?, ?, ?)', (episode, title, slug, season, "./cartoons/cartoon" + episode))
	#print('episode {}, title {}, slug {}, season {}, path {}'.format(episode, title, slug, season, "./cartoons/cartoon" + episode))
db.commit()
db.close()
