n = int(input('숫자를 넣으세요'))
alpha = input('알파벳을 넣으세요')

''.join(list(map(chr,[ord(i)+n for i in alpha])))
