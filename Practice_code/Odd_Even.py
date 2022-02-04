
#Param: Output unique outputs for even of odd inputs

class OddEven():
  def __init__(self):
    try:
      self.number = int((input('Enter Number: ')))
      self.parsed = self.number/2 # Divides input by 2
      number_dec = self.parsed % 1 # Get's Decimal points

      if number_dec == 0: # Evens always print whole numbers
        print('Even') 
        OddEven()

      else:
        print("Odd") # Odd Numbers always print non-zero decimals
        OddEven()
    except:
      print('Invalid input, likely str instead of expected int.')
      OddEven()
      

OddEven() # Declares Function