%import os, re, sqlite3
% rebase('base.tpl')
<img class="mandtpanel" src="images/tillymog.gif">
<div>
	<p class="spacedPara"> Read <a href="/mandtintro">this</a> for an introduction</p>	
	%db = sqlite3.connect('cartoon.db')
	%c = db.cursor()
	%c.execute("SELECT title,slug FROM cartoon WHERE season = 0 ORDER BY episode ASC")
	%cartoons = c.fetchall()
	<div class="spacedPara">
		<h2>Pilot</h2>
		<ul>
			%for cartoon in cartoons:
				<li class="cartoonListItem">
					<a href=cartoons/{{cartoon[1]}}>{{cartoon[0]}}</a>
				</li>
			% end
		</ul>
	</div>
	%c.execute("SELECT title,slug FROM cartoon WHERE season = 1 ORDER BY episode ASC")
	%cartoons = c.fetchall()
	<div class="spacedPara">
		<h2>Season 1</h2>
		<ul>
			%for cartoon in cartoons:
				<li class="cartoonListItem">
					<a href=cartoons/{{cartoon[1]}}>{{cartoon[0]}}</a>
				</li>
			% end
		</ul>
	</div>
	%c.execute("SELECT title,slug FROM cartoon WHERE season = 2 ORDER BY episode ASC")
	%cartoons = c.fetchall()
	<div class="spacedPara">
		<h2>Season 2</h2>
		<ul>
			%for cartoon in cartoons:
				<li class="cartoonListItem">
					<a href=cartoons/{{cartoon[1]}}>{{cartoon[0]}}</a>
				</li>
			% end
		</ul>
	</div>
</div>
%c.close()