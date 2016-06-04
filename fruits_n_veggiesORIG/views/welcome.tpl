<h1>Welcome to Nutritional Info of Common Fruits and Veggies!</h1>

<table>
<tr>
  <th>Food</th>
  <th>Serving</th>
  <th>Saturated Fat</th>
  <th>Unsaturated Fat</th>
  <th>Fiber</th>
  <th>Sugar</th>
  <th>Starch</th>
  <th>Protein</th>
</tr>
%for row in data:
<tr>
  %for col in row:
  <td>{{col}}</td>
  %end
</tr>
%end
</table>

<form class="buttons">
<button formaction="/addfruit">Add Fruit</button>
<button formaction="/removefruit">Remove Fruit</button>
</form>

%rebase views/layout.tpl
