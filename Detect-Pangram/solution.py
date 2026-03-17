import string

def is_pangram(s: str) -> bool:
    # Converte a string inteira para letras minúsculas
    s = s.lower()
    
    # Cria um conjunto (Set) a partir da string. Sets removem duplicatas automaticamente.
    chars_in_string = set(s)
    
    # Cria um conjunto com todas as 26 letras minúsculas do alfabeto inglês ('a' até 'z')
    alphabet = set(string.ascii_lowercase)
    
    # Retorna True se o alfabeto inteiro for um subconjunto dos caracteres da string
    return alphabet.issubset(chars_in_string)