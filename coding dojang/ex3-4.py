with open('ex3_5.txt', 'r') as f:
    line = f.readlines() 

word = [i.split() for i in line]
word = sum(word,[])
set_word = set(word)

for i in set_word:
    count_dict.setdefault(i,0)
    
for i in count_dict.keys():
    for j in word:
        if i == j:
            count_dict[i] +=1
result = sorted(count_dict.items(), key=lambda x:x[1], reverse = True)
print(result[0:10])
