
#params: Reverse list using a variety of methods

org = [1,2,3,4,5,6,7,8,9,10]
print(f'Orginal List: {org}')

def method1():
  """
  Uses .reverse() method
  """

  list = [1,2,3,4,5,6,7,8,9,10]
  list.reverse()
  print(f"Method 1: {list}")

def method2():
  """
  Starts at the end and continues untill theres
  nothing left in the list. 
  Note: this can also work for strings/int aswell.
  """

  list2 = [1,2,3,4,5,6,7,8,9,10]
  print(f"Method 2: {list2[::-1]}")

def method3():
  """
  Same as reversed method but uses a for loop 
  to add numbers to new list
  """

  list3 = [1,2,3,4,5,6,7,8,9,10]
  new_list3 = []
  for index in reversed(list3):
    new_list3.append(index)

  print(f"Method 3: {new_list3}")

def method4():
  """
  iterates over the list using range
  """

  list4 = [1,2,3,4,5,6,7,8,9,10]
  new_list4 = []
  for i in range( len(list4) - 1, -1, -1):
    new_list4.append(list4[i])
  print(f"Method 4: {new_list4}")

method1()
method2()
method3()
method4()