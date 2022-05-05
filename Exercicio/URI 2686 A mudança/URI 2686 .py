while True:
    try:
        # Implemente seu código aqui
              graus = int(input())
              if graus == 360 or graus >= 0 and graus < 90:
                  print('Bom Dia!!')
              elif graus >= 90 and graus < 180:
                  print('Boa Tarde!!')
              elif graus >= 180 and graus < 270:
                  print('Boa Noite!!')
              else:
                  print('De Madrugada!!')

    except EOFError:
        break