#6번

vegetables = {'가지':800, '오이':600, '수박':15000, '호박':1000, '깻잎':500}

a = sorted(vegetables.items(), key = lambda x: x[1], reverse = True)
for i in a:
    print('{0}:{1:>8,}'.format(i[0],i[1]), sep="")
