#6. Binary 파일을 16진수 값으로 출력하는 HexaDump 프로그램을 작성하시오.
#입력 형태
#찾을 파일명: C:/Temp/james.p
#출력 형태
#00000000:  00 01 44 E4 00 01 64 E4  41 42 43 11 00 61 F4 E4  ..D...d. ABC..a..
#00000010:  41 42 63 13 00 62 F4 E5  00 01 46 E9 FF 01 65 E2  ABc..b.. ..F...e. 
#00000020:



import pickle
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathmatics': 85, 'science': 82}

with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

def group(a, *ns):
    for n in ns:
        a = [a[i:i+n] for i in range(0, len(a), n)]
    return a

def join(a, *cs):
    return [cs[0].join(join(t, *cs[1:])) for t in a] if cs else a

def hexdump(data):
    to_hex = lambda c: '{:02X}'.format(c)
    to_chr = lambda c: chr(c) if 32 <= c < 127 else '.'
    make = lambda f, *cs: join(group(list(map(f, data)), 8, 2), *cs)
    hs = make(to_hex, '  ', ' ')
    cs = make(to_chr, ' ', '')
    for i, (h, c) in enumerate(zip(hs, cs)):
        print ('{:010X}: {:48}  {:16}'.format(i * 16, h, c))
        
with open ('james.p','rb') as file:
    data=file.read()
    hexdump(data)
