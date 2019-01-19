'''
  Python Program to Merge Two Lists and Sort it
  '''

  n_1 = int(input("Enter the number of items you want in the list: "))

  lst_1 = []

  for i in range(n_1):
    num = int(input("Enter the number now: "))
    lst_1.append(num)

  n_2 = int(input("Enter the number of items you want in the list: "))

  lst_2 =[]

  for i in range(n_2):
    num = int(input("Enter the number now: "))
    lst_2.append(num)

  final = lst_1 + lst_2 # two list are merged by adding

  print(final)
