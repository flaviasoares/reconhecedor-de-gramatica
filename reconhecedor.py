# programa reconhecedor de gramáticas

def gramatica1(palavra):
  '''
  G1::
  S → bB 
  B → Baa
  B → a

  Exemplos: ba, baaa, baaaaa, baaaaaaa, ...
  '''
  quantA = 0
  quantOutro = 0
  if palavra[0] == 'b':
    for i in range(len(palavra) - 1):
      if palavra[i + 1] == 'a':
        quantA += 1
      else:
        quantOutro +=1
    if (quantA % 2) == 1 and quantOutro == 0:
      print('A palavra pertende à gramática 1.')
    else:
      print('A palavra não pertende à gramática 1.')
  else:
    print('A palavra não pertende à gramática 1.')


def gramatica2(palavra):
  '''
  G2::
  S → AB
  A → aAb
  A → ^
  B → Bb
  B → b

  Exemplos: ^b, a^bb, aa^bbb, ^bb, ^bbb, ...
  '''
  quantA = 0
  quantB = 0
  countE = palavra.count('^')
  if countE == 1:
    indexE = palavra.index('^')
    for i in range(indexE + 1):
      if palavra[i] == 'a':
        quantA += 1
      for i in range(len(palavra) - indexE):
        if palavra[i + indexE] == 'b':
          quantB += 1
      if quantA == 0:
        if quantB >= 1:
          print('A palavra pertende à gramática 2.')
      elif quantB >= (quantA * 2):
          print('A palavra pertende à gramática 2.')
      else:
          print('A palavra não pertende à gramática 2.')
  else:
    print('A palavra não pertende à gramática 2.')

def gramatica3(palavra):
  '''
  G3::
  S’ → Sc
  S  → SA
  S  → A    
  A  → aSb
  A  → ab

  Exemplos: abc, abaabbc, aabbc, ababaabbc, aabaabbb...
  '''
  if palavra[len(palavra) - 1] == 'c':
    if palavra[0] == 'a' and palavra[len(palavra) - 2] == 'b':
      countA = palavra.count('a')
      countB = palavra.count('b')
      if countA == countB:
        print('A palavra pertende à gramática 3.')
      else:
        print('A palavra não pertende à gramática 3.')
  else:
    print('A palavra não pertende à gramática 3.')

def gramatica4(palavra):
  '''
  G4::
  S → E + S
  S → E * S 
  S → E
  E → a

  Exemplos: a, a+a, a*a, a+a*a, a+a+a, a*a*a, ...
  '''
  verificaA = 0
  verificaOutros = 0

  if palavra[0] == 'a':
    for i in range(len(palavra)):
      if (i % 2) == 0 and palavra[i] == 'a':
        verificaA += 1
      elif (i % 2) != 0 and (palavra[i] == '+' or palavra[i] == '*'):
        verificaOutros += 1
    if (verificaA - 1) == verificaOutros:
      print('A palavra pertende à gramática 4.')
    else:
      print('A palavra não pertende à gramática 4.')
  else:
    print('A palavra não pertende à gramática 4.')

def gramatica5(palavra):
  '''
  G5:: 
  S → 0A1
  A → 0A1
  A → 0

  Exemplos: 001, 00011, 0000111, ...
  '''
  metadeLista = int(len(palavra) / 2)
  quant0 = 0
  quant1 = 0
  if (len(palavra)) % 2 != 0:
    for i in range(metadeLista + 1):
      if palavra[i] == '0':
        quant0 += 1
    for i in range(metadeLista):
      if palavra[i + metadeLista + 1] == '1':
            quant1 += 1

    if (quant0 + quant1) == len(palavra):
      print('A palavra pertende à gramática 5.')
    else:
      print('A palavra não pertende à gramática 5.')
  else:
    print('A palavra não pertende à gramática 5.')

linguagem = input('Digite a palavra a ser testada:\n')
lingSemEsp = linguagem.replace(' ', '')
lingSemBN = lingSemEsp.replace('\n', '')
palavra = list(lingSemBN)

# verificando se pertence à primeira gramática
gramatica1(palavra)

# verificando se pertence à segunda gramática
gramatica2(palavra)

# verificando se pertence à terceira gramática
gramatica3(palavra)

# verificando se pertence à quarta gramática
gramatica4(palavra)

# verificando se pertence à quinta gramática
gramatica5(palavra)
