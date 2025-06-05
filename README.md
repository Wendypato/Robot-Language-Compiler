# Robot-Language-Compiler

El objetivo de este proyecto es simular el CPU de un robot, el cual debe soportar dos instrucciones (move and turn), dentro de una matriz cuadrada de 10 bloques. El sistema debe validar cada instrucción, asegurándose de que el movimiento permanezca dentro de los límites de la matriz, de lo contrario, debe devolver un error. Además, el lenguaje utilizado para comunicarse con el robot debe ser cordial, es decir, las instrucciones deben ser de manera educada, ya que si la instrucción no es educada, el robot no debe atender la indicación.Se desarrolló el analizador léxico y sintáctico del lenguaje para interactuar con el robot. Esto parte se concentra en que el compilador pueda interpretar oraciones estructuradas y educadas que representen instrucciones válidas para el robot. Esto con el objetivo de detectar correctamente los diferentes componentes de las instrucciones mediante Lex (como sustantivos, verbos, números y palabras amables), y validar su estructura gramatical con YACC.

El archivo yacc espera un archivo de texto con múltiples instrucciones, las instrucciones deben de tener la palabra “Robot” con R mayúscula, y las demás letras en minúscula.

La instrucciones se encunetran en el archivo llamado comandos.txt
