# Reto de Lenguaje del Hacker (Leet) by Luis Zenteno

# diccionario 
leet = {
  'a': '4',
  'b': 'l3',
  'c': '[',
  'd': ')',
  'e': '3',
  'f': '|=',
  'g': '&',
  'h': '#',
  'i': '1',
  'j': ',_|',
  'k': '<|',
  'l': '1',
  'm': '/\/\.',
  'n': '^/',
  'o': '0',
  'p': '|*',
  'q': '(_,)',
  'r': 'l2',
  's': '5',
  't': '7',
  'u': '(_)',
  'v': '\/',
  'w': 'vv',
  'x': '><',
  'y': 'j',
  'z': '2'
}

#texto ingresado por teclado
texto = input('Escribir texto a transformar: ').lower()

#variable que guardará el texto transformado
txt_leet = ''

#recorre la variable texto original
for i in texto:
    if i in leet:
        txt_leet += leet[i]
    else:
        txt_leet += i

print(txt_leet)