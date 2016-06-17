<h1>Matched Candidates</h1>

<form method="post" action="/output">
%for row in data:
<input type="checkbox" class="do" name="{{row[0]}}" value="{{row[0]}}">
{{row[0]}}</input><br />
%end
<button type="submit" name="rfruit" value="rfruit">Submit</button>
</form>

  <button type="submit">Submit</button>
</form>

%rebase views/layout.tpl