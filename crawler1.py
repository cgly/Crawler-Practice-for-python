# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:57:29 2019

@author: Rafael
"""

import requests
import os

root="G://Users//"
url="http://tieba.baidu.com/photo/p?kw=%E6%9D%A8%E8%B6%85%E8%B6%8A&ie=utf-8&flux=1&tid=6064179244&pic_id=1eacd22a2834349b946f3496c7ea15ce36d3be3d&pn=1&fp=2&see_lz=0"
path=root+url.split('&')[-1]
try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("copy success!")
    else:
        print("文件已经存在")
except:
    print("爬取失败")