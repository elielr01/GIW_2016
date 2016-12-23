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
%if ejercicio == 1:
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
%elif ejercicio == 2:
<head>
  <title>Order Items</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Show Order Items</h2>
  </header>
  <table>
    <tr>
      <th class="block">Product Name</th>
      <th class="block">Quantity</th>
	  <th class="block">Unit Price</th>
    </tr>
	%for product in data:
      <tr>
          <td class="block">{{product['_id']}}</td>
           <td class="block">{{product['cantidadTotal']}}</td>
			<td class="block">{{product['precio']}}</td>
      </tr>
	  %end
  </table>

</body>	
</html>
