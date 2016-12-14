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
<PRE> Elements found: {{data.count()}}</PRE>
% if data.count() > 0:
  <table>
    <tr>
      <th class="block">UserName</th>
      <th class="block">E-Mail</th>
      <th class="block">Web Page</th>
      <th class="block">Credit Card</th>
      <th class="block">Password Hash</th>
      <th class="block">Name</th>
	  <th class="block">SurName</th>
	  <th class="block">Adress</th>
	  <th class="block">Likes</th>
	  <th class="block">Birthdate</th>
    </tr>
	%for user in data:
      <tr>
          <td class="block">{{user['_id']}}</td>
           <td class="block">{{user['email']}}</td>
           <td class="block">{{user['webpage']}}</td>
          <td class="block">
            <p>Number: {{user['credit_card']['number']}}</p>
            <p>Expires: {{user['credit_card']['expire']['month']}}/{{user['credit_card']['expire']['year']}}</p>
          </td>
          <td class="block">{{user['password']}}</td>
          <td class="block">{{user['name']}}</td>
          <td class="block">{{user['surname']}}</td>
          <td class="block">
            <p>Street: {{user['address']['street']}}</p>
            <p>Number: {{user['address']['num']}}</p>
            <p>Country: {{user['address']['country']}}</p>
            <p>Zip: {{user['address']['zip']}}</p>
          </td>
          <td class="block">
	          <ul>
              %for like in user['likes']:
                <li>
                  {{like}}
                </li>
              %end
            </ul>
          </td>
          <td class="block">{{user['birthdate']}}</td>
      </tr>
	  %end
  </table>

</body>
</html>
