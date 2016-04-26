import sys, sqlite3, os, fnmatch, re
from markdown import markdown

db = sqlite3.connect('../cartoon.db')

def putPanels(episode):
	toonDir = os.getcwd() + "\\..\\cartoons\\cartoon" + episode
	allPanels = os.listdir(toonDir)
	for panel in allPanels:	
		panelId = re.search("[\d]+", panel)
		db.execute('INSERT INTO cartoon_panel (episode, panelId, panelName) VALUES (?, ?, ?)', (episode, int(panelId.group()), panel))
	db.commit()

def main():
	title = re.sub('[\r\n]+', '', sys.argv[3])
	episode = sys.argv[2]
	season = sys.argv[1]
	slug = re.sub('[^\w]+', '-', title.lower())	
	putPanels(episode)
	db.execute('INSERT INTO cartoon (episode, title, slug, season, path) VALUES (?, ?, ?, ?, ?)', (episode, title, slug, season, "./cartoons/cartoon" + episode))
	db.commit()
	db.close()

if __name__ == "__main__":
   main()