a = [str(i*j) for i in range(100,1000) for j in range(999,100,-1)]

b = []
for v in a:
    for i in range(len(v)//2-1):
        if v[i] == v[-1-i] and v[i+1] == v[-2-i]:
            b.append(v)
            
