import random
import os
os.chdir('D:\\git_ec\\Python\\Python\\coding dojang')

wd = os.getcwd()
content = random.randint(1,3)
os.mkdir(wd+'/low/')
os.mkdir(wd+'/low/1/')
os.mkdir(wd+'/low/2/')
os.mkdir(wd+'/low/3/')
os.mkdir(wd+'/mid/')
os.mkdir(wd+'/mid/1')
os.mkdir(wd+'/mid/2')
os.mkdir(wd+'/mid/3')
os.mkdir(wd+'/high/')
os.mkdir(wd+'/high/1')
os.mkdir(wd+'/high/2')
os.mkdir(wd+'/high/3')

filename = random.randint(1000,9999)
print(filename)
print(content)
if filename <= 3333:
    os.chdir('D:\\git_ec\\Python\\Python\\coding dojang\\low')
    folderlist = os.listdir(os.getcwd())
    for i in folderlist:
        fn = os.path.splitext(i)[0]
        b = [str(content)]
        if str(content) == fn:
            os.chdir(os.getcwd()+"\\"+str(fn))
            a = open(str(filename)+'.txt', mode='at', encoding='utf-8')
            a.writelines(b)
            a.close()    
elif filename > 3333 and filename < 6667:
    print(filename,'2')
    os.chdir('D:\\git_ec\\Python\\Python\\coding dojang\\mid')
    folderlist = os.listdir(os.getcwd())
    for i in folderlist:
        fn = os.path.splitext(i)[0]
        b = [str(content)]
        if str(content) == fn:
            os.chdir(os.getcwd()+"\\"+str(fn))
            a = open(str(filename)+'.txt', mode='at', encoding='utf-8')
            a.writelines(b)
            a.close()  
else:
    os.chdir('D:\\git_ec\\Python\\Python\\coding dojang\\high')
    folderlist = os.listdir(os.getcwd())
    for i in folderlist:
        fn = os.path.splitext(i)[0]
        b = [str(content)]
        if str(content) == fn:
            os.chdir(os.getcwd()+"\\"+str(fn))
            a = open(str(filename)+'.txt', mode='at', encoding='utf-8')
            a.writelines(b)
            a.close()  
