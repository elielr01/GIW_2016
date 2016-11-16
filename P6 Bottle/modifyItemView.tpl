<!DOCTYPE html>
<html lang="es">
<head>
  <title>Modify Item</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Modify Item</h2>
  </header>

  <form action="modify" method="post">
  <b>Only modify the fields which have been filled</b>
    <p>Item Name: <input name="itemName" type="text"></p>
    <p>Item Category: <input name="itemCategory" type="text"></p>
    <p>Quantity: <input name="quantity" type="text"></p>
    <p>Description:</p>
    <p>
      <textarea name="description" rows="12" cols="80">
        Description
      </textarea>
    </p>
    <p><input value="Modified from inventory" type="submit"></p>
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