<?php

/**
 * Conta o número de bits '1' na representação binária de um inteiro.
 *
 * @param int $n O número inteiro não negativo.
 * @return int O número de bits '1'.
 */
function countBits(int $n): int
{
  // Converte o inteiro para sua representação binária como uma string.
  $binaryString = decbin($n);

  // Conta o número de ocorrências do caractere '1' na string binária.
  // A função substr_count é eficiente para essa tarefa.
  return substr_count($binaryString, '1');
}

// Exemplo de uso:
$number = 1234;
echo "O número de bits '1' em " . $number . " é: " . countBits($number); // Saída: 5
