<!DOCTYPE html>
<html lang="es">
<head>
  <title>Delete Item Successful</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Item deleted from inventory</h1>
  <form action="index" method="post">
    <input type="hidden" name="id" value="{{id}}"/>
    <input type="hidden" name="name" value="{{name}}"/>
    <input value="Back to index" type="submit">
  </form>
</body>
</html>