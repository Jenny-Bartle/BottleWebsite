%import os, re, sqlite3
% rebase('base.tpl')
<img class="mandtpanel" src="../images/tillymog.gif">

%db = sqlite3.connect('cartoon.db')
%c = db.cursor()
%c.execute("SELECT panels,slug,episode FROM cartoon WHERE slug = '%s'" % name)
%cartoon = c.fetchone()

%for panel in range(0,cartoon[0]):
	<img class="mandtpanel" src={{cartoon[1]}}/panel{{panel}}.gif>
% end

%c.execute("SELECT slug FROM cartoon WHERE episode = '%s'" % (cartoon[2]-1))
%prev = c.fetchone()
<div class=mandtpanel>
	<div class=prevButton>
		<a href=cartoons/{{prev[0]}}><< Previous</a>
	</div>
%c.execute("SELECT slug FROM cartoon WHERE episode = '%s'" % (cartoon[2]+1))
%next = c.fetchone()
	<div class=nextButton>
		<a href=cartoons/{{next[0]}}>Next >></a>
	</div>
</div>
%c.close()