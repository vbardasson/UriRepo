while True:
  try:
    entrada = input()
    while entrada!="":
      A, B, C = entrada.split()
      if A == B == C:
        print("*")
      elif A !=B and A!=C:
        print("A")
      elif B !=A and B!=C:
        print("B")
      elif C !=(A) and C!=B:
        print("C")
      else:
        print("*") 
      entrada = input()
  except EOFError:
    break