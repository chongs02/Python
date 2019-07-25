import random

s = [[random.randint(1,4) for i  in range(5)] for k in range(5)]

print('초기 타일판')
for i in s:
    print(i)

# 가로
for i in s:
    score =0
    for k in range(4):
        if i[k] == i[k+1]:
            score += 1
            if score == 2:
                i[k-1] = '*'
                i[k] = '*'
                i[k+1] ='*'

#세로

for k in range(5):
    score = 0
    for i in range(len(s)-1):
        if s[i][k] == s[i+1][k]:
            score += 1
            if score == 2:
                s[i-1][k] = '*'
                s[i][k] = '*'
                s[i+1][k] ='*'

print()
print('변경후 타일판')
            
for i in s:
    print(i)
