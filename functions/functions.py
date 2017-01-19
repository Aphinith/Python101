def my_func(param1):
  print(param1)

# my_func('Aralya')
names = ['Aralya', 'Rosa', 'Tubesock']

# print(list(map(my_func, names)))

# list(map(my_func, names))

list(map(lambda name: print(name), names))