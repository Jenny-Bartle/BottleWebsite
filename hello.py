import sqlite3
from bottle import route, run, template, static_file

@route('/styles/<filename>')
def server_static(filename):
    return static_file(filename, root='./styles')

@route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root='./images')
	
@route('/')
@route('/home')
def serve_homepage():
    return template('home')

@route('/posts')
def posts():
    db = sqlite3.connect('blog.db')
    c = db.cursor()
    c.execute("SELECT title,slug,content,time FROM blog ORDER BY time DESC")
    data = c.fetchall()
    c.close()
    return template('blog_posts', rows=data)
	
@route('/posts/<name>')
def posts(name):
	db = sqlite3.connect('blog.db')
	c = db.cursor()
	c.execute("SELECT title,slug,content,time FROM blog WHERE slug = '%s'" % name)
	post = c.fetchone()
	c.close()
	return template('blog_post', post=post)

@route('/cartoons')
def cartoons():
	return template('cartoons')

@route('/cartoons/<name>')
def cartoons(name):
	return template('cartoon', name=name)

@route('/cartoons/<name>/<panel>')
def server_static(name, panel):
	db = sqlite3.connect('cartoon.db')
	c = db.cursor()
	c.execute("SELECT path FROM cartoon WHERE slug = '%s'" % name)
	cartoon = c.fetchone()
	c.close()
	print(cartoon[0] + '/' + panel)
	return static_file(panel, root=cartoon[0])
	
@route('/mandtintro')
def mandtintro():
	return template('mandtintro')

run(host='localhost', port=8080, debug=True)