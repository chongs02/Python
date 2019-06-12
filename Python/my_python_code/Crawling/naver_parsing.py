import urllib.request
import bs4

url = 'https://www.naver.com/'

html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html,'html.parser')

# print(html.read())
# print(bsObj)

#
# # div class로 뽑아오기
# top_right = bsObj.find('div',{'class':'area_links'})
# first_a = top_right.find('a')
# # print(top_right.text)


##네이버 메뉴뽑아내기
# ul = bsObj.find('ul',{'class':'an_l'})
# lis = ul.findAll('li')
#
# for li in lis:
#     a_tag = li.find('a')
#     span = a_tag.find('span',{'class':'an_txt'})
#     print(span.text)


#네이버 뉴스 뽑아내기

ul = bsObj.fine('ul', {'id':'text_today_main_news_801001'})
print(ul)
