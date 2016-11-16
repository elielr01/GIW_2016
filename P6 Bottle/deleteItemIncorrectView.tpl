<!DOCTYPE html>
<html lang="es">
<head>
  <title>Add Item</title>
  <meta charset="utf-8" />
</head>

<body>
  <font color="#FF0000"> It doesn't exist. Try again </font>
  <header>
    <h2>Delete Item</h2>
  </header>

  <form action="delete" method="post">
    <p>Item Name: <input name="itemName" type="text"></p>
    <p>Item Category: <input name="itemCategory" type="text"></p>
    <p><input value="Delete from inventory" type="submit"></p>
    <input type="hidden" name="id" value="{{id}}" />
    <input type="hidden" name="name" value="{{name}}" />
  </form>

  <form action="index" method="post">
    <input type="hidden" name="id" value="{{id}}" />
    <input type="hidden" name="name" value="{{name}}" />
    <input value="Back to menu" type="submit">
  </form>

</body>
</html>
