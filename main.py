from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import pandas as pd

# 키워드 검색하기

a=input("검색할 키워드를 입력 : ")
image_name = input("저장할 이미지 이름 : ")
#b=int(input("몇 개 저장할래? : "))
driver = webdriver.Chrome('C:\chromedriver_win32 (1)\chromedriver.exe')
driver.get('http://www.google.co.kr/imghp?hl=ko')
browser = driver.find_element(By.NAME, "q")
browser.send_keys(a)
browser.send_keys(Keys.RETURN)



# 클래스를 찾고 해당 클래스의 src 리스트를 만들자
for c in range(100) :
     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN) # 스크롤하여 이미지를 많이 확보
     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)



'''이미지 src요소를 리스트업해서 이미지 url 저장'''

images = driver.find_elements(By.CLASS_NAME, "rg_i.Q4LuWd") #  클래스 네임에서 공백은 .을 찍어줌
images_url = []
for i in images: 
   
   if i.get_attribute('src')!= None :
        images_url.append(i.get_attribute('src'))
   else :
       images_url.append(i.get_attribute('data-src'))
driver.close()



# 겹치는 이미지 url 제거

print("전체 다운로드한 이미지 개수: {}\n동일한 이미지를 제거한 이미지 개수: {}".format(len(images_url), len(pd.DataFrame(images_url)[0].unique())))
images_url=pd.DataFrame(images_url)[0].unique()

for t, url in enumerate(images_url, 0):        
     urllib.request.urlretrieve(url, image_name + '_' + str(t) + '.jpg')