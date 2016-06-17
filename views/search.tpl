<h1>Find potential employees</h1>

<p>Choose skills and location:</p>
<form method="post" action="/searched">
  <label>Required skills: <input name="required_skills" type="text"></label>
  <label>Preferred skills: <input name="preferred_skills" type="text"></label>
  <label>Location (zipcode): <input name="zip" type="text"></label>
  <label>Preferred skills match threshold: <input name="threshold" type="text"></label>

  <button type="submit">Submit</button>
</form>

%rebase views/layout.tpl
