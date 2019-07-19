a, b = map(int, input().split())
list_ = [2 ** i for i in range(a,b+1)]
list_.pop(1)
list_.pop(-2)
print(list_)
