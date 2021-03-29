# 引入套件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import json

# 定義上傳函數
def UpdateToGoogleSheet(sheetName,techerName='',techerStar='',Country='',FinalClass='',Price='',language='',techerURL='',StudentNum='',StudentName='',date='',tag1='',tag2='',tag3='',Content='',ClassName='',ClassURL=''):
    # 建立空封包
    package = {}

    # 建立封包內容
    package['sheet'] = sheetName
    package['techerName'] = techerName
    package['techerStar'] = techerStar
    package['country'] = Country
    package['finalClass'] = FinalClass
    package['language'] = language
    package['techerURL'] = techerURL
    package['studentNum'] = StudentNum
    package['studentName'] = StudentName
    package['price'] = Price
    package['date'] = date
    package['tag1'] = tag1
    package['tag2'] = tag2
    package['tag3'] = tag3
    package['feedBackContext'] = Content
    package['className'] = ClassName
    package['classLink'] = ClassURL

    # 傳送封包
    r = requests.post("https://script.google.com/macros/s/AKfycbzCtHtve9_BA58bR5x0Kb1Jv9zqelrAV2zwu9l7DSrxbtYjU7Ot-eb4RlAzOQW9hCaVgA/exec",data=package)
    
    # 取得回應
    print(r)
#===========================================================================================================================================================================================================================================

#設定瀏覽器驅動
options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome(chrome_options=options)

# 清除雲端原有資料
package ={}
package['clear'] = 'CFb'
package['sheet'] = ''
r = requests.post("https://script.google.com/macros/s/AKfycbzCtHtve9_BA58bR5x0Kb1Jv9zqelrAV2zwu9l7DSrxbtYjU7Ot-eb4RlAzOQW9hCaVgA/exec",data=package)

# 爬取"Cafetalk"網站評價
# =========================================================================================================================================================================
page = 1
while True:
    browser.get('https://cafetalk.com/feedback/?term=lesson-language&lang=zh-tw&sort=latest&term_sub=lesson-language-chinese&fblang=all&page=' + str(page))
    soup = BeautifulSoup(browser.page_source,"html.parser")
    feedback = soup.find_all('div',{'class':'comment-inner white-content-container'})
    
    # 判斷是否評論
    if len(feedback) == 0 :
        break
    
    for i in range(len(feedback)):
        name = feedback[i].find_all('p',{"class":"user-review"})[0].getText().strip().replace('\t','').replace('\n',',').split(',')[0]
        FBTime = feedback[i].find_all('p',{"class":"user-review"})[0].getText().strip().replace('\t','').replace('\n',',').split(',')[1]

        # 評價標籤異常處理
        try:
            FB = feedback[i].find_all('p',{"itemprop":"description"})[0].getText().strip()
        except:
            FB = feedback[i].find_all('div',{'class':'feedback-comment-wrap'})[0].find_all('p')[0].getText().strip()
        # 課程不一定還存在
        try:
            techer = feedback[i].find_all('a',{"target":"_blank"})[1].getText().strip()
            techerURL = "https://cafetalk.com" + feedback[i].find_all('a',{"target":"_blank"})[1].get('href')
            techerClass = feedback[i].find_all('a',{"target":"_blank"})[0].getText().strip()
            classURL = "https://cafetalk.com/" + feedback[i].find_all('a',{"target":"_blank"})[0].get('href')
        except:
            techerClass = feedback[i].find_all('span',{'style':'opacity: 0.7;'})[0].getText().strip()
            techer = feedback[i].find_all('a',{"target":"_blank"})[0].getText().strip()
            techerURL = "https://cafetalk.com" + feedback[i].find_all('a',{"target":"_blank"})[0].get('href')
            classURL='-'
        
        print(name)
        print(FBTime)
        # 爬取評價，不一定會有評價
        TagList =[]
        try:
            taglist = feedback[i].find_all('a',{"class":"feedback_tag btn btn-xs btn-primary tabOn"})
            for tag in taglist:
                TagList.append(tag.getText().replace('\t','').replace('○','').replace('\n','').replace('\xa0',''))
        except:
            pass
        print(TagList)
        print(FB)
        print(techerClass)
        print(techer)
        print(techerURL)
        print(classURL)
        print('------------------------------------')
        if len(TagList) == 3:
            UpdateToGoogleSheet(sheetName='Cafetalk 評價',techerName=techer,techerURL=techerURL,date=FBTime,Content=FB,ClassName=techerClass,ClassURL=classURL,StudentName=name,tag1=TagList[0],tag2=TagList[1],tag3=TagList[2])
        if len(TagList) == 2:
            UpdateToGoogleSheet(sheetName='Cafetalk 評價',techerName=techer,techerURL=techerURL,date=FBTime,Content=FB,ClassName=techerClass,ClassURL=classURL,StudentName=name,tag1=TagList[0],tag2=TagList[1])
        if len(TagList) == 1:
            UpdateToGoogleSheet(sheetName='Cafetalk 評價',techerName=techer,techerURL=techerURL,date=FBTime,Content=FB,ClassName=techerClass,ClassURL=classURL,StudentName=name,tag1=TagList[0])
        if len(TagList) == 0:
            UpdateToGoogleSheet(sheetName='Cafetalk 評價',techerName=techer,techerURL=techerURL,date=FBTime,Content=FB,ClassName=techerClass,ClassURL=classURL,StudentName=name)
    page = page + 1
browser.quit()
print("爬取結束")