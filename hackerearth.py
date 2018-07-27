from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver=webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://www.hackerearth.com/challenges/')
res=driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup=BeautifulSoup(res,'lxml')
box=soup.find('div',{'class':'upcoming challenge-list'})
all_hackthons=box.find_all('div',{'class':'challenge-card-modern'})

i=0
for hackthon in all_hackthons:
    i=i+1
    print(i)
    type=hackthon.find('div',{'class':'challenge-type'}).text.replace('\n',' ').strip()
    '''strip() is used to remove extra spaces'''
    name=hackthon.find('div',{'class':'challenge-name'}).text.replace('\n',' ').strip()
    date=hackthon.find('div',{'class':'date'}).text.replace('\n',' ').strip()
    print(type,name,date)
 