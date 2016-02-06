%{
#include "guppy.h"
%}

%%
=  return EQUALS;
[A-Za-z][_A-Za-z]* return PARAMETER;
[1-9][0-9]* return VALUE;
%%

int yywrap(void) {
    return 1;
}
