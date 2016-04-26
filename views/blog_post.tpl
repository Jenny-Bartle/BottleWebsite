% rebase('base.tpl')
% import datetime
<title>Jenny Bartle</title>
% from datetime import datetime
<div class="post" >
	<h3>{{post[0]}}</h3>
	% postTime = datetime.strptime(post[3], "%Y-%m-%d %H:%M:%S.%f")
	% timeString = postTime.strftime("%d %B, %Y")
	<div class="date">Posted on {{timeString}}</div>
	{{!post[2]}}
</div>