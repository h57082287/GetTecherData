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

# 以下區域爬取"verbling"網站
# =========================================================================================================================================================================
# 啟動瀏覽器
browser.get("https://www.verbling.com/zh-tw/find-teachers/mandarin?sort=magic")

# 完全加載所有資料
temp_height = 0
while True:
    browser.execute_script("window.scrollBy(0,180)")
    time.sleep(0.5)
    check_height = browser.execute_script("return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
    if check_height == temp_height:
        break
    temp_height = check_height

print("解析網頁中.....")

# 讀取網頁
soup = BeautifulSoup(browser.page_source,"html.parser")
techer = soup.find_all('div',{'class':'teacher TeacherItem ProfileItemBase'})
print(len(techer))

print("開始顯示結果")

# 清除雲端原有資料
package ={}
package['clear'] = 'V'
package['sheet'] = ''
r = requests.post("https://script.google.com/macros/s/AKfycbzCtHtve9_BA58bR5x0Kb1Jv9zqelrAV2zwu9l7DSrxbtYjU7Ot-eb4RlAzOQW9hCaVgA/exec",data=package)

# 開始解析網頁
for i in  range(0,len(techer)):
    name = techer[i].find_all('a',{'class':'ignore link-reset'})[0].getText()                                           # 取得教師名字
    price = techer[i].find_all('span',{'class':'currency-converter'})[0].getText()                                      # 取得價錢
    MainLanguage = techer[i].find_all('div',{'class':'text-sc-1b7rn1-0 dQAXQC sc-bdVaJa ksLAur'})[0].getText()          # 主要語言
    Country =  techer[i].find_all('div',{'class':'text-sc-1b7rn1-0 dQAXQC sc-bdVaJa ksLAur'})[1].getText()              # 國家
    url = "https://www.verbling.com/zh-tw" + techer[i].find_all('a',{'class':'ignore link-reset'})[0].get('href')       # 網址
    FinalClass = techer[i].find_all('div',{'class':'text-sc-1b7rn1-0 dQAXQC sc-bdVaJa ksLAur'})[2].getText()            # 完成課堂數
    UseLaunageList = techer[i].find_all('div',{'class':'text-sc-1b7rn1-0 dQAXQC sc-bdVaJa ksLAur'})[3].getText()        # 取得使用語言清單
    # 可能發生無評價的狀況排除
    try:
        Evaluation =  techer[i].find_all('div',{'class':'text-bold text-large'})[0].getText()                           # 評價
    except:
        pass
    
    # 列出詳細資訊
    print(name)
    print(price)
    print(UseLaunageList)
    print(MainLanguage)
    print(Country)
    print(Evaluation)
    print(FinalClass)
    print(url)
    print('-------------------------------------------')
    UpdateToGoogleSheet(sheetName='Verbling',techerName=name,Price=price,language=UseLaunageList,Country=Country,techerStar=Evaluation,FinalClass=FinalClass,techerURL=url)

# =========================================================================================================================================================================
browser.quit()
print("爬取結束")
