<!DOCTYPE html>
<html lang="es">
<head>
  <title>Log in with TOTP</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Log In with TOTP</h1>

  <form action="login_totp" method="post">
    Username: <input name="nickname" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
  </form>

  <p>No account?</p>
  <form action="signup_totp">
    <input value="Sign up" type="submit">
  </form>
</body>
</html>