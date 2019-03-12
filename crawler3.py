# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:56:38 2019

@author: Rafael
"""
#淘宝爬取商品价格名称
import requests
import re

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        r.enconding=r.apparent_encoding
        return r.text
    except:
        return ""
   
def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("error") 

def printGoodList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for i in ilt:
        count=count+1
        print(tplt.format(count,i[0],i[1]))
   
def main():
    goods='书包'
    depth=10
    start_url='https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'+goods
    infoList=[]
    for i in range(depth):
        try :
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)
    
    
main()