# Robot-Language-Compiler

El objetivo de este proyecto es simular el CPU de un robot, el cual debe soportar dos instrucciones (move and turn), dentro de una matriz cuadrada de 10 bloques. El sistema debe validar cada instrucción, asegurándose de que el movimiento permanezca dentro de los límites de la matriz, de lo contrario, debe devolver un error. Además, el lenguaje utilizado para comunicarse con el robot debe ser cordial, es decir, las instrucciones deben ser de manera educada, ya que si la instrucción no es educada, el robot no debe atender la indicación.Se desarrolló el analizador léxico y sintáctico del lenguaje para interactuar con el robot. Esto parte se concentra en que el compilador pueda interpretar oraciones estructuradas y educadas que representen instrucciones válidas para el robot. Esto con el objetivo de detectar correctamente los diferentes componentes de las instrucciones mediante Lex (como sustantivos, verbos, números y palabras amables), y validar su estructura gramatical con YACC.

El archivo yacc espera un archivo de texto con múltiples instrucciones, las instrucciones deben de tener la palabra “Robot” con R mayúscula, y las demás letras en minúscula. Esto se puede gracias a la ayuda de los archivos Lex (lex_robot.l) y YACC (lex_robot.y).

La instrucciones se encunetran en el archivo llamado comandos.txt

Un ejemplo de comandos validos son:
-Robot please move 2 blocks ahead
-Robot please turn 90 degrees
-Robot please move 3 blocks ahead and then turn 90 degrees
-Robot please move 3 blocks ahead and then turn 90 degrees and then move 2 block
-Robot pretty please move 4 block
-Robot move 1 block pretty please

Sus salidas serían:
-mov,2
-turn,90
-mov,3
-turn,90
-mov,3
-turn,90
-mov,2
-mov,4
-mov,1

Archivo Lex:
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"
%}

%option noyywrap

%%

90|180|270|360                        { yylval.dval = atoi(yytext); return DEGREES; }
[0-9]+                                { yylval.dval = atoi(yytext); return BLOCKS; }
blocks\ ahead|block|blocks    { yylval.sval = strdup(yytext); return MNOUN; }
degrees                              { yylval.sval = strdup(yytext); return TNOUN; }
(,)?[ ]*then|and[ ]+then    { yylval.sval = strdup(yytext); return CONNECTOR; }
Robot                                { yylval.sval = strdup(yytext); return ROBOT; }
please|pretty\ please|porfis        { yylval.sval = strdup(yytext); return KIND; }
move                                 { yylval.sval = strdup(yytext); return MVERB; }
turn                                 { yylval.sval = strdup(yytext); return TVERB; }

[ \t]+                               ; // ignora espacios
[\n\r]+ { /* ignora saltos de línea */ }
.                                    { yylval.sval = strdup(yytext); return ERROR; }

%%                                                                                                                                                                                                                                      
Archivo YACC:
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
extern FILE *yyin;       
int yyparse();           
%}

%union {
    char *sval;
    int dval;
}

%token ROBOT KIND MVERB BLOCKS MNOUN TVERB DEGREES TNOUN CONNECTOR ERROR

%%

commands   : commands A | A ;  
A          : ROBOT KIND B  | ROBOT B KIND{  
}
B          : B CONNECTOR MVERB BLOCKS MNOUN { printf("mov,%d\n", $4); }
           | B CONNECTOR TVERB DEGREES TNOUN { printf("turn,%d\n", $4); }
           | MVERB BLOCKS MNOUN { printf("mov,%d\n", $2); }
           | TVERB DEGREES TNOUN { printf("turn,%d\n", $2); }

%%


int main(int argc, char **argv) {
    if (argc == 2) {
        FILE *fd = fopen(argv[1], "r");
        if (!fd) {
            perror("Error al abrir el archivo");
            return EXIT_FAILURE;
        }

        yyin = fd;     
        yyparse();      
        fclose(fd);
    } else {
        fprintf(stderr, "Uso: %s archivo.txt\n", argv[0]);
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
