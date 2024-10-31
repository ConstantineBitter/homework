n = int(input())
result = str()
dividers = list()
for div in range(2, n//2+1):
    if div in dividers:
        break
    if n % div == 0:
        dividers.append(div)
        dividers.append(n//div)
if 2 in dividers:
    del dividers[0]
dividers = sorted(dividers)
dividers.append(n)
print(dividers)
for j in range (1, n):
    for div in dividers:
        if j < div//2+1 and j != div - j:
            result += f'{j}{div-j}'
print(result)
