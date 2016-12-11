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
		%if row == 'likes':
			<li>
			{{row}} : 
			%for col in doc[row]:
				{{col}}
			%end
			</li>
			
		%elif row == 'address':
			<li>
			{{row}} : 
			%for col in doc[row]:
			  {{col}}	: {{doc[row][col]}} |
			%end
			</li>
		%elif row == 'credit_card':
			<li>
			{{row}} : mes: {{doc[row]['expire']['month']}} | año: {{doc[row]['expire']['year']}} | numero: {{doc[row]['number']}}
			</li>
		%else:
			<li>
			{{row}} : {{doc[row]}}
			</li>
    %end 
  </ul>
</body>
</html>
