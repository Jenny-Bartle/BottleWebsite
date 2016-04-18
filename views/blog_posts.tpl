% rebase('base.tpl')
% import datetime
% from datetime import datetime
<h2>Recent Posts</h2>
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