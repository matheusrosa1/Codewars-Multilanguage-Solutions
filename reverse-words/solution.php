<?php

/**
 * Inverte cada palavra em uma string, mantendo os espaços.
 *
 * @param string $str A string de entrada.
 * @return string A string com cada palavra invertida.
 */
function reverseWords(string $str): string
{
  // 1. Divide a string em um array de palavras usando o espaço como delimitador.
  // Isso preserva múltiplos espaços, criando entradas vazias no array.
  $words = explode(' ', $str);

  echo "Palavras: " . print_r($words, true) . "\n";

  // 2. Usa array_map para aplicar a função strrev a cada palavra no array.
  // strrev() inverte uma string.
  $reversedWords = array_map('strrev', $words);

  echo "Palavras invertidas: " . print_r($reversedWords, true) . "\n";

  // 3. Junta o array de palavras invertidas de volta em uma string, usando o espaço como cola.
  return implode(' ', $reversedWords);
}

// Exemplos de uso:
echo reverseWords("This is an example!") . "\n"; // Saída: sihT si na !elpmaxe
echo reverseWords("double  spaces") . "\n";     // Saída: elbuod  secaps
