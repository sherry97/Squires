<h1>Check the boxes of the fruits and veggies to remove:</h1>

<form method="GET" action="/rmfruit">
%for row in data:
<input type="checkbox" class="do" name="{{row[0]}}" value="{{row[0]}}">
{{row[0]}}</input><br />
%end
<button type="submit" name="rfruit" value="rfruit">Submit</button>
</form>

%rebase views/layout.tpl
