#세 정수 a, b, c를 입력으로 받아 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

def print_median(a,b,c):
    list_ = [a,b,c]
    del list_[list_.index(min(list_))]
    del list_[list_.index(max(list_))]
    return list_

print_median(1,2,3)
