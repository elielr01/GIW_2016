<!DOCTYPE html>
<html lang="es">
<head>
  <title>Find User Successful</title>
  <meta charset="utf-8" />
</head>

<body>
  <h1>Information User: {{doc['_id']}} </h1>
  <ul>
    %for row in doc:
		<li>
		{{row}} : {{doc[row]}} 
		</li>
    %end 
  </ul>
</body>
</html>