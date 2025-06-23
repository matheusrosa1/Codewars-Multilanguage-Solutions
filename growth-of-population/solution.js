function nbYear(p0, percent, aug, p) {
  const multiplicador = percent / 100;
  let populacaoAtual = p0;
  let anos = 0;
  while (populacaoAtual < p) {
    populacaoAtual = Math.floor(populacaoAtual + populacaoAtual * multiplicador + aug);
    anos++;
  }
  return anos;
}