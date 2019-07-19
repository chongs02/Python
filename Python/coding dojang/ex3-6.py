binary_number = []
line_ = []
with open('ex3_7.txt', 'r') as f:
    line = None
    while line != '':
        line = f.readline()
        line_.append(line)
        line2 = '0b'+line
        
        line2 = line.strip('\n')
        binary_number.append(line2)
binary_number = binary_number[:-1]

list_ = []
for i in binary_number:
    hex_number = hex(int(i,2))
    hex_number = hex_number[2:]
    list_.append(hex_number)

for num in list_:
    a = ''
    for i in range(len(num) - 1):
        a += num[i]+num[i + 1] + ' '
    print(line_[i],':    ',a)
