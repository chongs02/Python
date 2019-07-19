
price = str(input())
list_ = list(map(int, price.split(';')))
list_.sort()

for p in list_[::-1]:
    print('{:>9,}'.format(p))
