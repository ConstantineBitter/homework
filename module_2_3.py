my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
print('Positive numbers')
while start < len(my_list):
    number = my_list[start]
    start = start + 1
    if number == 0:
        continue
    elif number <0:
        print('Negative number')
        break
    elif start == len(my_list):
        print(number, '\n End of the list')
    else:
        print(number)