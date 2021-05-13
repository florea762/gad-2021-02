# # import my_module  // if you need to import * from the module use this one.
# from my_module import my_age, str_
# # import my_package.my_package_module as m
# from my_package import my_age as aux_age
# # from my_module import * // not recommended
# # from my_package.my_package_module import * // not recommended
#
# # print("Hello world!")
# print('main name = ', __name__)
#
# print('my_module.my_age', my_age)
# print('my_module.str_', str_)
# print('my_package.my_package_module.my_age', aux_age) # inline comment


# my_int = 7
# print('my_int', my_int, type(my_int))
# my_float_from_int = float(my_int)
# print('my_float_from_int', my_float_from_int, type(my_float_from_int))
# my_complex_from_int = complex(my_int)
# print('my_complex_from_int', my_complex_from_int, type(my_complex_from_int))
# print('\n')
#
# my_float = 6.540
# print('my_float', my_float, type(my_float))
# my_int_from_float = int(my_float)
# print('my_int_from_float', my_int_from_float, type(my_int_from_float))
# my_complext_from_float = complex(my_float)
# print('my_complext_from_float', my_complext_from_float, type(my_complext_from_float))
# print('\n')
#
# my_complex = 3+5j
# print('my_complex', my_complex, type(my_complex))

# Python's None is actually null from other languages.
# print(7 is 7, 7 == 7)
# print([1, 2] is [1, 2])

# a = 7
# b = '7'
# print(a == b)  # False: a is an int and b is a string (although they have the same value)

# a = 7
# print(type(a), id(a))
# a = '7'
# print(type(a), id(a))

# a = 7
# b = 7
# print(a is b, id(a), id(b))
#
# a = [1, 2]
# b = [1, 2]
# print(a is b, id(a), id(b), id([1, 2]), id([1, 2, 3]))

# a = 5
# print(a)
# a += 3  # is the same as a = a + 3
# print(a)

# a = 'bfsdfsfs \' _\tsdfdgsd'
# print(a, type(a))
# a = "bfsdfsfs \" _\tsdfdgsd"
# print(a, type(a))


# print('linia 1\nlinia 2\nlinia 3')
# print('\n')
# print('''linia 1
# linia 2
# linia 3''')

# print(r'linia 1\nlinia 2\nlinia 3')
# print(R'linia 1\nlinia 2\nlinia 3')
# print('''linia 1\nlinia 2\nlinia 3
# linia 1\nlinia 2\nlinia 3
# linia 1\nlinia 2\nlinia 3
# linia 1\nlinia 2\nlinia 3\tlinia 1\nlinia 2\nlinia 3''')
# a = r'linie 1 \n linie 2'
# print(a)

# price = 10.00
# name = 'Hamburger'
# # msg = 'Top product: {} costs only ${:.2f}.'.format(name, price)
# # msg = 'Top product: {1} costs only ${0:.2f}.'.format(price, name)
# msg = 'Top product: {name} costs only ${price:.2f}.'
# print('msg', msg)
# msg = msg.format(price=price, name=name,)
# print('msg', msg)

# a = 1
# b = 2
# c = 3
# d = 4
# msg = 'a = {}, b = {b_placeholder}, c = {}, d = {d_placeholder}'.format(a, c, b_placeholder=b, d_placeholder=d)
# print('msg', msg)

# price = 10.00
# name = 'Hamburger'
# msg = f'Top product: {name} costs only {price:.2f}.'
# print('msg', msg)

# price = 10.00
# name = 'Hamburger'
# msg = 'Top product: %s costs only %.2f.' % (name, price)
# print('msg', msg)

# my_list = [1, 2, True, 'abc']
# .......  0  1   2      3 ....
# ....... -4 -3  -2     -1 ....
# print(my_list, type(my_list))
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# # print(len(my_list))
# # print(my_list[-1])
# # print(my_list[-2])
# # print(my_list[-3])
# # print(my_list[-4])
# new_list = my_list[::]  # the same as: new_list = my_list[0:len(my_list):1]
# print('new_list', new_list)
# print(my_list)
# my_list[2] = ['a', [1, 2], 4, 5, 6, 7]
# print(my_list)
# print(my_list[2][1][1])
# new_list = my_list[::-1]
# new_list = my_list[len(my_list)::-1]
# print('new_list', new_list)
# print(my_list)
# print(new_list)
# my_list = [1, 2] + [3, 4, 5]
# print(my_list)

# my_list = [1, 2, 3]
# print(my_list, type(my_list))
# my_list = tuple(my_list)
# print(my_list, type(my_list))
#
# print('\n')
#
# my_tuple = (1, 2, 3)
# print(my_tuple, type(my_tuple), id(my_tuple))
# my_tuple = list(my_tuple)
# print(my_tuple, type(my_tuple), id(my_tuple))
# my_tuple.append(4)
# print(my_tuple, type(my_tuple), id(my_tuple))
# my_tuple = tuple(my_tuple)
# print(my_tuple, type(my_tuple), id(my_tuple))

# my_dict = {'a': 12, 'b': 'abc', 3: 22, (1, 2, 3): [1, 2, 3], 'dict_in_dict': {'a': 1, 'b': 2}}
# print('my_dict', my_dict)
# print(my_dict['a'])
# print(my_dict['b'])
# print(my_dict[3])
# print(my_dict.get('abc', 'my default value'))
# print('abc' in my_dict and my_dict['abc'] == 22)
# print(my_dict.get('abc') == 22)

# students = [{
#     'name': 'Name 1',
#     'age': 29,
#     'address': {
#         'street': 'Str.',
#         'city': 'Craiova'
#     }
# }, {
#     'name': 'Name 2',
#     'age': 25,
#     'address': {
#         'street': 'Str.',
#         'city': 'Cluj'
#     }
# }]
# print('students', students)
# print('1st student', students[0], type(students[0]))
# print(list(students[0].keys()))
# print(list(students[0].values()))
# print(list(students[0].items()))

# my_dict = {}
# print(my_dict, type(my_dict))
# my_dict['a'] = 2
# print(my_dict, type(my_dict))
# my_dict['b'] = 10
# print(my_dict, type(my_dict))
# my_dict['a'] = 100
# print(my_dict, type(my_dict))

# my_dict = dict([('a', dict([('d', 400)])), ('b', 200), ('c', 300)])
# print('my_dict', my_dict)

# empty_list = []
# empty_list_with_constructor = list()
# list_with_one_element = ['abc']
# list_with_one_element_with_constructor = list((1,))
# # print('list_with_one_element_with_constructor', list_with_one_element_with_constructor)
#
# empty_tuple = ()
# tuple_with_one_element = (1,)
# tuple_with_constructor = tuple('abc')
# # print(tuple_with_constructor, type(tuple_with_constructor))
#
# empty_dict = {}
# print('empty_dict', empty_dict, type(empty_dict))

# my_set = {'abc', 'my string', 'my other string', 'abc2', 'a3'}
# print('my_set', my_set, type(my_set))
# # my_set.pop()
# my_set.remove('abc2')
# print('my_set', my_set, type(my_set))

# my_set = set()
# my_set.add(27)
# my_set.add('abc')
# my_set.add(True)
# my_set.add('abc')
# print(my_set, type(my_set))

# grocery_list = {'mere', 'pere', 'banane', 'kiwi'}
# items = {'mere', 'kiwi', 'abc'}
# print(items.issubset(grocery_list))  # print(grocery_list.issuperset(items))
# print(grocery_list.intersection(items))
# print(grocery_list.difference(items))
# print(grocery_list.union(items))

# print('this is a string', 15, True)
# message_from_keyboard = input('add your data here: ')
# print(message_from_keyboard, type(message_from_keyboard))

my_age = input('How old are you?: ')
print(my_age, type(my_age))
my_age = int(my_age)
print(my_age, type(my_age))
