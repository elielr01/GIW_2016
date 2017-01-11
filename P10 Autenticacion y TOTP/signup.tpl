<!DOCTYPE html>
<html lang="es">
<head>
  <title>Sign Up</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Sign Up</h1>

  <form action="signup" method="post">
    <table>
      <tr>
        <td>
          NickName: <input name="nickname" type="text">

        </td>
        <td>
          Name: <input name="name" type="text">
        </td>
      </tr>
      <tr>
        <td>
            Country: <input name="country" type="text">
        </td>
      </tr>
      <tr>
        <td>
            Email: <input name="email" type="text">
        </td>
      </tr>
      <tr>
        <td>
            Password: <input name="password" type="password">
        </td>
      </tr>
      <tr>
        <td>
            Confirm password: <input name="password2" type="password">
        </td>
      </tr>
    </table>
    <input value="Sign up" type="submit">
  </form>
  <form action="login">
    <input value="Back to login" type="submit">
  </form>
</body>
</html>