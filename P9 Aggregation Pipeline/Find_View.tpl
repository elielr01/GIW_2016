<!DOCTYPE html>
<html lang="es">
<style>
  td{
    align-items: flex-start;
    border:1px solid #000;
  }

  tr td:last-child{
    //width:1%;
    white-space:nowrap;
  }
</style>

%if ejercicio == 1:
<head>
  <title>Top Countries</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Top Countries</h2>
  </header>
  <table>
    <tr>
      <th class="block">Country</th>
      <th class="block">Number of Users</th>
    </tr>
	%count=0
	%for user in data:
      <tr>
          <td class="block">{{user['_id']}}</td>
           <td class="block">{{user['sum_users']}}</td>
      </tr>
	  %count+=1
	  %end
  </table>
<PRE> Elements found: {{count}}</PRE>
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
	%count=0
	%for product in data:
      <tr>
          <td class="block">{{product['_id']}}</td>
           <td class="block">{{product['cantidadTotal']}}</td>
			<td class="block">{{product['precio']}}</td>
      </tr>
	  %count+=1
	  %end
  </table>
<PRE> Elements found: {{count}}</PRE>
</body>
%elif ejercicio == 3:
<head>
  <title>Age Range Country Users</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Show Countries with their age range</h2>
  </header>
  <table>
    <tr>
      <th class="block">Country</th>
      <th class="block">Age Range</th>
    </tr>
	%count=0
	%for country in data:
      <tr>
          <td class="block">{{country['_id']}}</td>
           <td class="block">{{country['rangoEdades']}}</td>
      </tr>
	  %count+=1
	  %end
  </table>
<PRE> Elements found: {{count}}</PRE>
</body>

%elif ejercicio == 4:
<head>
  <title>AVG Lines</title>
  <meta charset="utf-8" />
</head>

<body>
  <header>
    <h2>Show Countries with their lines average</h2>
  </header>
  <table>
    <tr>
      <th class="block">Country</th>
      <th class="block">Line Average</th>
    </tr>
	%count=0
	%for country in data:
      <tr>
          <td class="block">{{country['_id']}}</td>
           <td class="block">{{country['promedioLineas']}}</td>
      </tr>
	  %count+=1
	  %end
  </table>
<PRE> Elements found: {{count}}</PRE>
</body>
</html>
