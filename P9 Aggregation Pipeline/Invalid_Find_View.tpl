<!DOCTYPE html>
<html lang="es">
<head>
  <title>Find {{tipo}} Fail</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Cannot search for the {{tipo}}. Invalid arguments:</h1>
  %for parameter in invalid_arguments:
  <ul>
      <li>
        {{parameter}}
      </li>
  </ul>
</body>
</html>
