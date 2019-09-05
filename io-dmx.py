#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import numpy as np

#读取文件存入数组
f = 'K13800-2-test.txt'
with open(f,'r+', encoding='utf-8') as f:    
 list = [i[:-1].split(',') for i in f.readlines()]
 print(list)
f.close()

                                    ##创建中桩文件##
#建立中桩文件文件并创建文件头
f = open('K13800-2-test.dmx', 'w')
f.write('HINTCAD5.83_DMX_SHUJU'+"\n")

#循环找到“BEGIN”
for i in range(len(list)):
    if list[i][0].strip()=='BEGIN':
        print(list[i][1])
        first = list[i][1]
        first1 = first.split(":")
        f.write("    "+str(first1[0]) + " ")
    elif list[i][0].strip()=='0.000':
        print(list[i][1])
        f.write(str(list[i][1] + "\n"))
f.close()

 
                                   ##创建纬地里程文件##
f = open('test1.hdm', 'w')
f.write('HINTCAD5.83_HDM_SHUJU'+"\n")

key=[]#创建BEGIN位置索引列表

for j in range(len(list)):
    if list[j][0].strip()=="BEGIN":
        key.append(j)
        #print(key[0])
        first = list[j][1]
        first1 = first.split(":")
        f.write(str(first1[0]) + " "+"\n")
   
  
f.close()




