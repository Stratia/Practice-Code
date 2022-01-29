
Number = 5

def main():
  converted = str(Number)
  try:
    val = str(converted)
    print("Converted is String")
  except:
    print("Converted is a Interger")
    return False

main()