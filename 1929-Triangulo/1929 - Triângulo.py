# Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.

# Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

# Entrada
# A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

# Saída
# Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser ‘S’ caso seja possível formar o triângulo, ou ‘N’ caso não seja possível formar o triângulo.
A, B, C, D = map(int, input().split())
if (A<B+C) and (B<A+C) and (C<A+B):
  print("S")
elif (A<C+D) and (C<A+D) and (D<A+C):
  print("S")
elif (A<B+D) and (B<A+D) and (D<A+B):
  print("S")
elif (B<C+D) and (C<B+D) and (D<B+C):
  print("S")
else:
  print("N")