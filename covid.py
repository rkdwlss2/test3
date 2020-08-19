from selenium import webdriver
from itertools import count
import time
from bs4 import BeautifulSoup
result = []

def CoVIDStock(result):
    url = 'https://finance.naver.com/sise/sise_group_detail.nhn?type=theme&no=108'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    time.sleep(4)
    for stock in count():
        driver.execute_script('store.getList(%s)'%str(stock+1))
#         time.sleep(2)
#         rcv_data = driver.page_source
#         soupData = BeautifulSoup(rcv_data, 'html.parser')
#         print("굽네 치킨 [%s] 크롤링 " % str(page+1))
#         for storelist in soupData.findAll('tbody', {'id':"store_list"}):
#             for store in storelist:
#                 tr_tag = list(store.strings)
#                 if tr_tag[0] == '등록된 데이터가 없습니다.':
#                     print("크롤링 종료")
#                     return result
#                 store_name = tr_tag[1]
#                 store_address = tr_tag[6]
#                 store_sido_gu = store_address.split()[:2]
#                 store_phone = tr_tag[3]
#                 if store_phone != '':
#                     result.append([store_name]+ store_sido_gu+[store_address]+[store_phone])
#
#
#
CoVIDStock(result)
#
# import pandas as pd
# goobne_table = pd.DataFrame(result, columns=['store','sido', 'gungu', 'address','phone'])
# goobne_table.to_csv("goobne.csv", encoding="cp949", index=True)
#
# print("굽네 치킨 주소 저장 완료")
