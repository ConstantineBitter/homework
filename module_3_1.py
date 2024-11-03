calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    string_ = str(string)
    count_calls()
    return (len(string_), string_.upper(), string.lower())


def is_contains(string, list_to_search):
    global result
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        if string not in list_to_search:
            result = False
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
