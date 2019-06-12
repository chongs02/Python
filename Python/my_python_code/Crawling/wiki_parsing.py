import urllib.request
import bs4

url = 'https://ko.wikipedia.org/wiki/%ED%8F%AC%ED%84%B8:%EC%9A%94%EC%A6%98_%ED%99%94%EC%A0%9C'

html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html,'html.parser')

# print(html.read())
# print(bsObj)
#

top_right = bsObj.find('div',{'class':'mw-parser-output'})
# print(top_right)

span = top_right.findAll('span')
# print(span.text)
