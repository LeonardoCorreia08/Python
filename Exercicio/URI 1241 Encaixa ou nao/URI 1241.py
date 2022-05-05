#TODO: Complete os espaços em branco com uma solução possível para o problema.
qte = int(input())

for i in range(qte):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")






