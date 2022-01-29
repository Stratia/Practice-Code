import math

def main():
  width = int(input("Width: "))
  height = int(input("Height: \n"))

  """"for index in range(height):
    print("|")
  for index in range(height):
    print("-", end="")
  print("\n")"""
  #For Real Size Triangle

  print(f"\n{height} (Height)\n|\n|\n|\n|")
  print(f"---------\n{width} (Width)",end="")
  print("\n")

  sqaured_width = (width * width)
  squared_height = (height * height)

  squared_sum = squared_height + sqaured_width
  root_sum = math.sqrt(squared_sum)
  
  print(f"The Hyp is {root_sum}")
  choice = input("Retry (Y/N)\n")
  if choice.capitalize == "Y":
    main()
  elif choice.capitalize == "N":
    quit()
    return
main()
