<!DOCTYPE html>
<html lang="es">
<head>
  <title>Index</title>
  <meta charset="utf-8" />
</head>

<body>

  <header>
    <h2>Welcome {{name}}! What do you want to do?</h2>
  </header>

  <p> <a href="inventory?id={{id}}&name={{name}}">Show inventory</a> </p>
  <p><a href="search?id={{id}}&name={{name}}">Search for an item in inventory</a></p>
  <p><a href="add?id={{id}}&name={{name}}">Add an item to inventory</a></p>
  <p><a href="delete?id={{id}}&name={{name}}">Delete an item to inventory</a></p>
  <p><a href="modify?id={{id}}&name={{name}}">Modify an item to inventory</a></p>

  <form action="login">
    <input value="Log Out" type="submit">
  </form>

</body>
</html>
