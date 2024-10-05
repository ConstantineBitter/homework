my_dict = {'Serhio': 1994, 'Dan': 2000, 'Helen': 1969, 'Max': 1990}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Tony'))
my_dict['Jack'] = 1950
my_dict['Mac'] = 1967
del my_dict['Dan']
print(my_dict.get('Dan'))
print(my_dict)

my_set = {4, 4, 44, 4444, 'Fourty four', 'Fourty four', 'Decimal', False, (12, 23, 34)}
print(my_set)
my_set.add(90)
my_set.add('Nine')
my_set.remove('Decimal')
print(my_set)