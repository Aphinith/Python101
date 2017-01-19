alpha = 'abcdefghi'
# print('This is alpha[3:]: ', alpha[3:])
# print('this is alpha[:4]: ', alpha[:4])
# print('only get def: ', alpha[3:6])

my_list = ['a', 'b', 'c', 'd']
# print('Before append: ', my_list)

my_list.append('e')
# print('After append: ', my_list)

d = {'key1': 'value1', 'key2': 'abcde'}
# print('this is entire dictionary for d: ', d)
# print('this is the value at key1: ', d['key1'])
# print('this is the value at key2: ', d['key2'])

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3, 4)
# print('tuple1: ', tuple1)
# print('tuple2: ', tuple2)

#tuples are immutable. That is the main difference between lists and tuples

#below are examples of sets. They will not keep duplicate values
# print({1,1,1,1,1,2,2,2,2,2,3,3,3,3,3})
# print(set(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']))

set1 = {1, 2, 3, 4}
set1.add(5)
print('This is set1: ', set1)

print(list(9, 8, 7, 6, 5))