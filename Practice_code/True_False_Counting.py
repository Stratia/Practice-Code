
list = [True,True,True,False,True,False,True
,False,True,False,True,True,False,True,True,True,True]

def main():
  Positive = 0
  Fal = 0

  for index in list:
    if index is True:
      Positive+=1
    if index is False:
      Fal+=1

  print(f"Positive: {Positive}\n")
  print(f"False: {Fal}")

main()