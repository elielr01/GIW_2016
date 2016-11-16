<!DOCTYPE html>
<html lang="es">
<head>
  <title>Log in</title>
  <meta charset="utf-8" />
</head>

<body>
  <font color="#FF0000"> Can't do login. Try again </font>
  <h1>Welcome!</h1>

  <form action="login" method="post">
    Username: <input name="user" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
  </form>

  <p>No account?</p>
  <form action="signUp">
    <input value="Sign up" type="submit">
  </form>
</body>
</html>
