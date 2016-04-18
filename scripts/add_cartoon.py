import sys, sqlite3, os, fnmatch, re
from markdown import markdown

def main():
	title = sys.argv[1]
	episode = sys.argv[2]
	season = sys.argv[3]
	toonDir = os.getcwd() + "\\..\\cartoons\\" + title
	allPanels = os.listdir(toonDir)
	panels = len(allPanels)
	slug = re.sub('[^\w]+', '-', title.lower())	
	db = sqlite3.connect('../cartoon.db')
	db.execute('INSERT INTO cartoon (episode, title, slug, season, path, panels) VALUES (?, ?, ?, ?, ?, ?)', (episode, title, slug, season, "./cartoons/" + title, panels))
	db.commit()
	db.close()

if __name__ == "__main__":
   main()