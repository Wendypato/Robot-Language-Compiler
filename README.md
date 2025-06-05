# Robot-Language-Compiler

El objetivo de este proyecto es simular el CPU de un robot, el cual debe soportar dos instrucciones (move and turn), dentro de una matriz cuadrada de 10 bloques. El sistema debe validar cada instrucción, asegurándose de que el movimiento permanezca dentro de los límites de la matriz, de lo contrario, debe devolver un error. Además, el lenguaje utilizado para comunicarse con el robot debe ser cordial, es decir, las instrucciones deben ser de manera educada, ya que si la instrucción no es educada, el robot no debe atender la indicación.Se desarrolló el analizador léxico y sintáctico del lenguaje para interactuar con el robot. Esto parte se concentra en que el compilador pueda interpretar oraciones estructuradas y educadas que representen instrucciones válidas para el robot. Esto con el objetivo de detectar correctamente los diferentes componentes de las instrucciones mediante Lex (como sustantivos, verbos, números y palabras amables), y validar su estructura gramatical con YACC.

El archivo yacc espera un archivo de texto con múltiples instrucciones, las instrucciones deben de tener la palabra “Robot” con R mayúscula, y las demás letras en minúscula. Esto se puede gracias a la ayuda de los archivos Lex (lex_robot.l) y YACC (lex_robot.y).

La instrucciones se encunetran en el archivo llamado comandos.txt

Un ejemplo de comandos validos son:
- Robot please move 2 blocks ahead
- Robot please turn 90 degrees
- Robot please move 3 blocks ahead and then turn 90 degrees
- Robot please move 3 blocks ahead and then turn 90 degrees and then move 2 block
- Robot pretty please move 4 block
- Robot move 1 block pretty please

Sus salidas serían:
- mov,2
- turn,90
- mov,3
- turn,90
- mov,3
- turn,90
- mov,2
- mov,4
- mov,1

Instrucciones a seguir en linuxzoo para que sirva una vez ya creados el Lex y el YACC:
- lex_robot.l
- yacc -d lex_robot.y
- gcc lex.yy.c y.tab.c -o lex_robot
- ./lex_robot comandos.txt
