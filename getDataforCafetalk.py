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
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(chrome_options=options)

# 清除雲端原有資料
package ={}
package['clear'] = 'C'
package['sheet'] = ''
r = requests.post("https://script.google.com/macros/s/AKfycbzCtHtve9_BA58bR5x0Kb1Jv9zqelrAV2zwu9l7DSrxbtYjU7Ot-eb4RlAzOQW9hCaVgA/exec",data=package)

# 以下區域爬取"Cafetalk"網站
# =========================================================================================================================================================================
# 啟動瀏覽器
page = 1
while True:   
    browser.get("https://cafetalk.com/tutors/?timezone=Asia%2FTaipei&lang=zh-tw&term=lesson-language&term_sub=lesson-language-chinese&page=" + str(page) + "&new_acceptance=1&search_type=tutor")
    time.sleep(10)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    techer = soup.find_all('div',{'class':'tutor-brick-detail-wrap small-9 columns'})
    
    # 判斷換頁後是否還有資料
    if len(techer) == 0:
        print("爬取結束")
        break
    
    for i in range(len(techer)):
        name = techer[i].find_all('h3')[0].find_all('a')[0].getText().strip()
        classNum = techer[i].find_all('div',{'class':'tutor-stats'})[0].getText().strip().replace('\t','').replace('\n',',').split(',,')[0]
        StudentNum = techer[i].find_all('div',{'class':'tutor-stats'})[0].getText().strip().replace('\t','').replace('\n',',').split(',,')[1]
        # 本段較為複雜: 先將bs4物件強制轉為str，藉由str物件先以空格做切個並取元素2出來，在將元素2中字元位置7開始作保留，最後以'"><'做切割後取第0元素
        fromWhere = techer[i].find_all('span',{'class':'tip'})[1].get('title')
        techerURL = "https://cafetalk.com" + techer[i].find_all('h3')[0].find_all('a')[0].get('href')
        print(name)
        print(classNum)
        print(StudentNum)
        print(fromWhere)
        print(techerURL)
        print('------------------------------------')
        UpdateToGoogleSheet(sheetName='Cafetalk',techerName=name,FinalClass=classNum,StudentNum=StudentNum,Country=fromWhere,techerURL=techerURL)
    page = page + 1
    time.sleep(3)
browser.quit()
print("共爬取" + str(page) + "頁") 
print("爬取結束")