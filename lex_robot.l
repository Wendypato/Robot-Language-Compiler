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
