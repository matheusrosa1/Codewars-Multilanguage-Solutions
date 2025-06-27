def nb_year(p0, percent, aug, p):
  current_population = p0
  years = 0
  percent_decimal = percent / 100.0

  while current_population < p:
    current_population = int(current_population + (current_population * percent_decimal) + aug)
    years += 1
    
  return years