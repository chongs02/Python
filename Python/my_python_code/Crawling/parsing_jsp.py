import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#url ="https://www.adic.or.kr/index.waple;jsessionid=0B5BC0E255269EC5130E4EC3F3096E7C/"

#web_r = requests.get(url)
#web_soup = BeautifulSoup(web_r.text, 'html.parser')

#print(web_soup.findAll('img'))





                         
driver = webdriver.Chrome('chromedriver')

driver.implicitly_wait(5)

#driver.get('https://www.adic.or.kr/index.waple;jsessionid=0B5BC0E255269EC5130E4EC3F3096E7C/')

driver.get('https://nid.naver.com/nidlogin.login')

#아이디/비번 

driver.find_element_by_name('id').send_keys('chongs02')
driver.find_element_by_name('pw').send_keys('tls9031515')


time.sleep(10)

#로그인 버튼 누르기

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
