<h1>Add Fruit</h1>

<p>Fill in the information below to add a fruit:</p>
<form method="post" action="/added">
  <label>Food: <input name="food" type="text"></label>
  <label>Serving: <input name="serving" type="number"></label>
  <label>Saturated Fat: <input name="satfat" type="number"></label>
  <label>Unsaturated Fat: <input name="unsatfat" type="number"></label>
  <label>Fiber: <input name="fiber" type="number"></label>
  <label>Sugar: <input name="sugar" type="number"></label>
  <label>Starch: <input name="starch" type="number"></label>
  <label>Protein: <input name="protein" type="number"></label>

  <button type="submit">Submit</button>
</form>

%rebase views/layout.tpl
