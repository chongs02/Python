#디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 
#일까요?
#- 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됨.
#00:00 (60초간 표시)
#00:01 
#…
#23:59


def clock_of_three():
    sec = 0
    for h in range(24):
        for m in range(60):
            clock = str(h) + str(m)
            if '3' in clock:
                sec += 60

    print('총 ', sec ,'초')


clock_of_three()
