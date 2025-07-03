<?php

function isSquare($n)
{
  return $n >= 0 && sqrt($n) == floor(sqrt($n));
}

// floor(sqrt($n)) == floor(sqrt($n)) // isso sempre será true!
/* Exemplo: se n = 26:
sqrt(26) dá algo como 5.099...
floor(sqrt(26)) dá 5.0
E aí:
5.099 != 5.0 // false
*/