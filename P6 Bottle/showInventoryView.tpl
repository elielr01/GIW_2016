<!DOCTYPE html>
<html lang="es">
<style>
  td{
    align-items: flex-start;
    border:1px solid #000;
  }

  tr td:last-child{
    width:1%;
    white-space:nowrap;
  }
</style>
<head>
  <title>Inventory</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Show Inventory</h2>
  </header>

  <table>
    <tr>
      <th class="block">Id</th>
      <th class="block">Item Name</th>
      <th class="block">Category</th>
      <th class="block">Date Added</th>
      <th class="block">Quantity</th>
      <th class="block">Description</th>
    </tr>
    %for row in data:
      <tr>
        %for col in row:
          <td class="block">{{col}}</td>
        %end
      </tr>
    %end
  </table>

  <form action="index" method="post">
    <input type="hidden" name="id" value="{{id}}" />
    <input type="hidden" name="name" value="{{name}}" />
    <input value="Back to menu" type="submit">
  </form>
</body>
</html>
