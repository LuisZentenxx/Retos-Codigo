#1.- Reto Fizz Buzz

import os; os.system('cls')

'''for i in range(100):
    i+=1

    if i%3 ==0 and i%5 == 0:
        print('fizzbuzz')

    elif i%3 == 0:
        print('fizz')

    elif i%5 == 0:
        print('buzz')

    else:
        print(i)'''


#2.- Reto Lenguaje del Hacker


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

texto = input('Escribir texto a transformar: ').lower()

txt_leet = ''

for i in texto:
    if i in leet:
        txt_leet += leet[i]
    else:
        txt_leet += i

print(txt_leet)

