# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:21:16 2019

@author: Rafael
"""

import requests 
from bs4 import BeautifulSoup
import traceback
import re
def getHTMLText(url,code='utf-8'):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=code#r.apparent_encoding
        #print("success!!!")
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
    #从东方财富得到股票列表
    html=getHTMLText(stockURL,'GB2312')
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue
    
    
def getStockInfo(lst,stockURL,fpath):
    count=0
    cun=0
    print(len(lst))
    for stock in lst:
        cun=cun+1
        if cun>10:
            break
        url=stockURL+stock+".html"
        html=getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            
            keyList=stockInfo.find_all('dt')
            valueList=stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key=keyList[i].text
                val=valueList[i].text
                infoDict[key]=val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count=count+1
                print('\r当前速度： {:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count=count+1
            print('\r当前速度： {:.2f}%'.format(count*100/len(lst)),end='')
            continue
  

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file='G:/Users.txt'
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
    
    
main()
