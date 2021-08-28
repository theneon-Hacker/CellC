# CellC

CellC is my programming language which combines 'C' syntax and cell-based memory. 

**add** command adding some value to the current cell's value.
For example, __add;__ will add 1, but __add -2;__ will add -2.

**next** command moves pointer at another cell, depends from number after this command.
For example, __next;__ moves pointer on next one cell, but __next -1;__ move pointer on previous cells.

**new** command creates new cell in the end of cells list.

**del** command delete last cell.

Variable **NOW** returning value in current cell.
Variable **DATA** returning cells list.

**echo** command prints text or result of expression after command
For example, __echo 'Hello World!'__ prints 'Hello World!', but __echo (9 > 0)__ prints True

**$** command is input.

**if** command is condition statement.
For example, __if (1 < NOW) {
               echo 'Hello World!'
              }__ will not prints something 'cause default value of all cells is equals 0.
              
**while** command is 'while' loop.
For example, __while (NOW ~ 10) {
                add;
                }__ will adding cell's value while it not equals 10.
                
And operator **>** means 'more than', **<** - 'less than', **=** - 'equals', **~** - 'not equals'
Operator **;** is not terminator of statement, it is needed for readability

__Code Samples:__

_Truth Machine:_
  
  while ($) {
	  echo 1;
  }
  echo 0;
  
_Create as many cells as the user enters:_

  add $;
  while (NOW) {
	   new;
	   add -1;
  }
  
_Hello World:_

  echo 'Hello World!'

