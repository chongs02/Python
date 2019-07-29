#세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부른다. 
#(여기서 a < b < c 이고 a + b > c)
#예를 들면, 32 + 42 = 9 + 16 = 25 = 52 이므로 3, 4, 5는 피타고라스 수입니다.
#a + b + c = 1000 인 피타고라스 수를 구하시오. (답은 한가지 뿐이다.)

def pythagoras(n):
    for i in range(n//2):
        for j in range(i+1,n//2):
            for k in range(j+1,n//2):
                if (i+j+k == 1000) and (i**2+j**2==k**2) and(i+j >k):
                    print( '합이 ', n ,'인 피타고라스 수는',i,j,k, '입니다')



pythagoras(1000)
