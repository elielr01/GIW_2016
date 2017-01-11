<!DOCTYPE html>
<html lang="es">
<head>
  <title>Log in</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Log In</h1>

  <form action="login" method="post">
    Nickname: <input name="nickname" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
  </form>

  <p>No account?</p>
  <form action="signup">
    <input value="Sign up" type="submit">
  </form>
</body>
</html>