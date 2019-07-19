with open('test.txt', 'r') as f:
    line = None    # 변수 line을 None으로 초기화
    i = 1
    while line != '':
        line = f.readline()
        if 'public' in line:
            print(i,':  ',line.strip('\n')) 
        i+=1
