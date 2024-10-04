immutable_var = tuple([4, 4.4, '44', False, [0, 1.0, 1.1, 4.4]])
print(immutable_var)

#immutable_var [1] = 5
#print(immutable_var)
#значение элементов кортежа нельзя изменить, т.к. кортеж - неизменяемая коллекция, не поддерживающая обращение по элементам.Но я могу изменить\заменить элементы списка внутри данного кортежа:
immutable_var [4][2] = 22
print(immutable_var)

mutable_list = [True, 4444, 'contest', 'competition', 'race', 'versus']
print(mutable_list)
mutable_list [0] = False
mutable_list.append('means evolution')
mutable_list [6] = 'for the best! ' *3
print(mutable_list)
