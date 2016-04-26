%import os, re, sqlite3
% rebase('base.tpl')
<img class="mandtpanel" src="../images/tillymog.gif">

%db = sqlite3.connect('cartoon.db')
%c = db.cursor()
%c.execute("SELECT title,slug,episode FROM cartoon WHERE slug = '%s'" % name)
%cartoon = c.fetchone()
%episode = cartoon[2]
%c.execute("SELECT panelId,panelName FROM cartoon_panel WHERE episode = '%i' ORDER BY panelId" % episode)
%panels = c.fetchall()

<title>{{cartoon[0]}}</title>
%for panel in panels:
	<img class="mandtpanel" src={{cartoon[1]}}/{{panel[1]}}>
% end

<div class=mandtpanel>
	%cartoonId = int(cartoon[2])
	%if cartoonId > 1:
		%c.execute("SELECT slug FROM cartoon WHERE episode = '%s'" % (cartoonId-1))
		%prev = c.fetchone()
			<div class=prevButton>
				<a href={{prev[0]}}><< Previous</a>
			</div>
	%end
	%if cartoonId < 38:
		%c.execute("SELECT slug FROM cartoon WHERE episode = '%s'" % (cartoonId+1))
		%next = c.fetchone()
			<div class=nextButton>
				<a href={{next[0]}}>Next >></a>
			</div>
	%end
</div>
%c.close()