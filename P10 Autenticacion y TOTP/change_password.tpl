<!DOCTYPE html>
<html lang="es">
<head>
  <title>Log in</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Log In</h1>

  <form action="login" method="post">
    Username: <input name="nickName" type="text" />
    Old Password: <input name="old_password" type="password" />
    New Password: <input name="new_password" type="password" />
    <input value="Login" type="submit" />
  </form>

  <p>No account?</p>
  <form action="signup">
    <input value="Sign up" type="submit">
  </form>
</body>
</html>