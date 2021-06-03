% rebase('layout.tpl', year=year)
<h3> Leave us a review </h3>
<form action="/otzivi" method="post">

<p><textarea rows="2" cols="50" name="NICK" placeholder="Your name"></textarea></p>
<p><textarea rows="5" cols="50" name="REV" placeholder="Your review"></textarea></p>
<p><textarea rows="2" cols="3" name="MRK" placeholder="Mark (1-5)"></textarea></p>

<p><input type="submit" value="Send" class="btn btn-default";></p>

<h3> Reviews of other users</h3>
<br>
%f = open('revstxt.txt', 'r')
%a=''
%for line in f: 
%a = (line) 
<p>{{a}}</p>
%end
%f.close()