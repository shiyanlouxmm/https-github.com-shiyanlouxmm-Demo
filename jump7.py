s = '7'
for n in range(1,101):
    if (s in str(n)) or (n % 7 == 0):
        continue
    else:
        print(n)
