grammar marzo;

program: expression+ | statement+;

expression:
	expression '+' expression	# suma
	| Numero					# primaria
	| Variable					# var
	| 'if' expression			# conditional;

statement:
	'int' Variable				# declaracion
	| Variable '=' expression	# asignacion
	| expression '<' expression	# comparacion
	| 'print(' expression ')'	# imprimir;

// A continuación los tokens (comienzan con mayúscula)
Numero: [0-9]+;
Variable: [a-z]+;
WS: [ \t\n\r]+ -> skip;

