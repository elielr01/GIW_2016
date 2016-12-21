<!DOCTYPE html>
<html lang="es">
<style>
  td{
    align-items: flex-start;
    border:1px solid #000;
  }

  tr td:last-child{
    width:1%;
    white-space:nowrap;
  }
</style>
<head>
  <title>Users</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Show Users</h2>
  </header>
  <table>
    <tr>
      <th class="block">Country</th>
      <th class="block">Number of Users</th>
    </tr>
	%for user in data:
      <tr>
          <td class="block">{{user['_id']}}</td>
           <td class="block">{{user['sum_users']}}</td>
      </tr>
	  %end
  </table>

</body>
</html>
