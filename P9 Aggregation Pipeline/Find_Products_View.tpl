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
	%for item in data:
      <tr>
          <td class="block">{{item['_id']}}</td>
           <td class="block">{{item['cantidadTotal']}}</td>
      </tr>
	  %end
  </table>

</body>
</html>
