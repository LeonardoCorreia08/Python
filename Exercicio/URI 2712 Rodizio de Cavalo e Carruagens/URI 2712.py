n = int(input())

while n:
  n -= 1
  placa = input().split('-')
  
  if (placa[0].isupper() and placa[0].isalpha() and placa[1].isnumeric() and len(placa[0]) == 3 and len(placa[1]) == 4):
    try:
      check = int(placa[1])
      r = int(placa[1][3])
      
      if (r > 8 or r == 0):
        print('SEXTA')
      elif r > 6:
        print('QUINTA')
      elif r > 4:
        print('QUARTA')
      elif r > 2:
        print('TERCA')
      else:
        print('SEGUNDA')
    except:
      print('FALHA')
  else:
    print('FALHA')