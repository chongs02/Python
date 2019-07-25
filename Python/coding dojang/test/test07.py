#7번
result = []

for i in range(100, 1001):
    a = 0
    for k in range(100, 1001):
        a = str(i*k)
        for l in range(len(a)//2):
            
            if a[l] == a[-1-l]:
                if a[l+1] == a[-1-l-1] and a[l+2] == a[-1-l-2]:
                
                    result.append(a)
                    result.append(i)
                    result.append(k)
            if a[l] != a[-1-l]:
                a = '123456'

                
print('x 는 {}, y는 {}'.format(result[-2],result[-1]))         
                    
        
    
