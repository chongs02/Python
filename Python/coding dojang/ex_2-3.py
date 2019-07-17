#디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 
#일까요?
#- 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됨.
#00:00 (60초간 표시)
#00:01 
#…
#23:59


def count_3():
    for i in range(1,25):
        if i == 3 or i == 13 or i == 23:
            count = 3 * 60
        else :
            a = []
            count_2 = 0
            for i in range(1,61):
                a.append(str(i))
            for i in a:
                if len(i) >1 and (i[0]=='3' or i[1] =='3'):
                    count_2 += 1
                elif len(i) ==1 and(i[0]=='3'):
                    count_2 +=1
    print('총 ',count + count_2,'번')


count_3()
