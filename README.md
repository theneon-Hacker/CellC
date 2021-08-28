# CellC

CellC is my programming language which combines 'C' syntax and cell-based memory. 

**add** command adding some value to the current cell's value.
For example, `add;` will add 1, but `add -2;` will add -2.

**next** command moves pointer at another cell, depends from number after this command.
For example, `next;` moves pointer on next one cell, but `next -1;` move pointer on previous cells.

**new** command creates new cell in the end of cells list.

**del** command delete last cell.

Variable **NOW** returning value in current cell.
Variable **DATA** returning cells list.

**echo** command prints text or result of expression after command
For example, `echo 'Hello World!'` prints 'Hello World!', but `echo (9 > 0)` prints True

**$** command is input.

**if** command is condition statement.
For example, `if (1 < NOW) {
               echo 'Hello World!'
              }` will not prints something 'cause default value of all cells is equals 0.
              
**while** command is 'while' loop.
For example, `while (NOW ~ 10) {
                add;
                }` will adding cell's value while it not equals 10.
                
And operator **>** means 'more than', **<** - 'less than', **=** - 'equals', **~** - 'not equals'\n
Operator **;** is not terminator of statement, it is needed for readability

__Code Samples:__

_Truth Machine:_
  
  `while ($) {
	  echo 1;
  }
  echo 0;`
  
_Create as many cells as the user enters:_

  `add $;
  while (NOW) {
	   new;
	   add -1;
  }`
  
_Hello World:_

  `echo 'Hello World!'`

