
col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for r in range(row):
    for c in range(col):

        if matrix[r][c] != '*':
            matrix[r][c] = 0

        for i in range(r-1, r+2):
            for k in range(c-1, c+2):
                
                if i < 0 or k < 0 or i >= row or k >= row:
                    continue
                elif matrix[r][c] == '*':
                    continue
                elif matrix[i][k] == '*':
                    matrix[r][c] += 1

for r in matrix:
    for v in r:
        print(v, end='')
    print()
