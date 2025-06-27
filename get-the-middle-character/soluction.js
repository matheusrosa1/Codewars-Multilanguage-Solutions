/**
 * Retorna o(s) caractere(s) do meio de uma string.
 *
 * @param {string} s A string de entrada.
 * @return {string} O(s) caractere(s) do meio.
 */
function getMiddle(s) {
  // Calcula o comprimento da string.
  const length = s.length;
  // Encontra o índice do meio. Math.floor arredonda para baixo.
  const middle = Math.floor(length / 2);

  // Verifica se o comprimento da string é par.
  if (length % 2 === 0) {
    // Se for par, retorna os dois caracteres do meio.
    // O método slice extrai uma seção de uma string.
    return s.slice(middle - 1, middle + 1);
  } else {
    // Se for ímpar, retorna o caractere do meio.
    return s.charAt(middle);
  }
}

// Exemplos de uso:
console.log(getMiddle("test"));    // Saída: es
console.log(getMiddle("testing")); // Saída: t
console.log(getMiddle("middle"));  // Saída: dd
console.log(getMiddle("A"));       // Saída: A