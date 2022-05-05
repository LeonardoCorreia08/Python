N=[0,0,0,0,0,0,0,0,0,0]
v= int(input())

#TODO: Complete os espaços em branco com uma solução possível para o problema.
for i in range(len(N)):
    N[i] = v
    v = v*2
    print('N[{}] = {}'.format(i,N[i]))
