x = float(input())

for i in range(0,100):
  print("N[{}] = ".format(i), end="")
  print('{0:.4f}'.format(x))
  x /= 2