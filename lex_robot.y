%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
extern FILE *yyin;       // Necesario para que Flex lea desde archivo
int yyparse();           // Declaración del parser
%}

%union {
    char *sval;
    int dval;
}

%token ROBOT KIND MVERB BLOCKS MNOUN TVERB DEGREES TNOUN CONNECTOR ERROR

%%

commands   : commands A | A ;  /* Permite múltiples entradas */
A          : ROBOT KIND B  | ROBOT B KIND{ //Robot recibe comando// 
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

        yyin = fd;      // Redirige la entrada del lexer al archivo
        yyparse();      // Ejecuta el parser completo
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
