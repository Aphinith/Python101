def my_func(param1):
  print(param1)

# my_func('Aralya')
names = ['Aralya', 'Rosa', 'Tubesock']

# print(list(map(my_func, names)))

# list(map(my_func, names))

list(map(lambda name: print(name), names))

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda num: num%2 == 0, numbers))
print(result)