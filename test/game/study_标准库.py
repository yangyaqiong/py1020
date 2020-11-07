#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# # os.mkdir("testdir")
# # print(os.listdir("./"))
# # os.removedirs("testdir")
# # print(os.getcwd())
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f=open("b/test.txt","w")
#     f.write("hello world!")
#     f.closed
# print(os.listdir("./"))
# import time
# # print(time.asctime())
# # print(time.time())
# # print(time.localtime())
# # print(time.strftime("%Y年%m月%d日 %H:%M",time.localtime()))
# nowtime=time.time()
# qiantian = nowtime - 60*60*24*2
# qiantian1=time.localtime(qiantian)
# print(time.strftime("%Y年%m月%d日 %H:%M:%S",qiantian1))
# import urllib.request
# import urllib.response
# reponse=urllib.request.urlopen("http://www.baidu.com")
# print(reponse.status)
# print((reponse.read()))
# print(reponse.headers)
import math
print(math.ceil(4.6))
print(math.floor(6.9))
print(math.sqrt(9))
