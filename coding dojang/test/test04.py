#4번
money, rate = input('원금과 이율을 입력하세요.: ex) 1000원 4%   -->').split()

money = int(money[:-1])
rate = int(rate[:-1])/100

target = 2*money
year = 0

while money < target :
    year += 1
    money = money +money*rate

print('{}년차 예상금액 : {}'.format(year, money))
