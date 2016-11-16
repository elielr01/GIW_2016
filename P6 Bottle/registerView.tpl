<!DOCTYPE html>
<html lang="es">
<head>
  <title>Sign Up</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Sign Up</h1>

  <form action="signUp" method="post">
    <table>
      <tr>
        <td>
          First Name: <input name="firstName" type="text">

        </td>
        <td>
          Last Name: <input name="lastName" type="text">
        </td>
      </tr>
      <tr>
        <td>
            Username: <input name="username" type="text">
        </td>
      </tr>
      <tr>
        <td>
            Password: <input name="password" type="password">
        </td>
      </tr>
      <tr>
        <td>
            Confirm password: <input name="confirm_password" type="password">
        </td>
      </tr>
      <tr>
        <td>
            Email: <input name="email" type="text">
        </td>
      </tr>
      <tr>
        <td>
            Confirm email: <input name="confirm_email" type="text">
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
