#i5. 다음의 지시대로 폴더와 파일을 프로그램에서 만드시오.
#랜덤으로 1, 2, 3 중 하나를 내용으로 갖는 txt 파일100개를 
#하나의 디렉토리(c:/Temp/Ex04) 안에 생성하는 코드를 작성하시오.
#(파일 제목은 4자리 정수를 랜덤으로 할당. ex - 1382.txt , 0201.txt , 9012.txt , ......... )
#제목이 0000~3333 인 txt 파일은 low 폴더로, 3334~6666인 txt 파일은 mid 폴더로, 
#6667~9999 인 파일은 high 폴더로 이동시키는 코드를 작성하시오.
#low, mid, high 폴더 안에 제목이 1, 2, 3 인 폴더를 각각 만들고, 
#txt 파일 안의 내용에 따라 txt파일을 폴더안으로 이동시켜 분류하시오.
#결론적으로 c:/Temp/Ex04 폴더 밑에는 low, mid, high 폴더 3개가 생기고, 
#이 각각의 폴더에는 1, 2, 3 폴더가 각각 생기고 이 폴더밑에 파일이 들어 있어야 함.

import random

 for _ in range(100):
     filenames = '{:0>4}.txt'.format(random.randint(0,9999))
     file_number = int(filenames[:4])
   
     if file_number <= 3333:
         path = 'low/'    
     elif file_number <= 6666:
         path = 'mid/'
     else:
         path = 'high/'
       
     rn = str(random.randint(1,3))
   
     with open(path+rn+'/'+filenames, 'w') as file:
         file.write(rn)
