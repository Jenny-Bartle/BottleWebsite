% rebase('base.tpl')
<title>Jenny Bartle</title>
% import datetime
% from datetime import datetime
<div>
	<h2>Recent Posts</h2>
	<a href=feed>RSS feed</a>
</div>
 % for post in rows:
	 <div class="post">
		<h3>
			<a href=posts/{{post[1]}}>
				{{post[0]}}
			</a>
		</h3>
		% postTime = datetime.strptime(post[3], "%Y-%m-%d %H:%M:%S.%f")
		% timeString = postTime.strftime("%d %B, %Y")
		<div class="date">{{timeString}}</div>
		{{!post[2]}}
	 </div>
 % end