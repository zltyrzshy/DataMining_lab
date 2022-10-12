# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:40:45 2021

@author: 66952
"""

import json
 
json_file = open('out2.json', 'r' , encoding='utf-8')
doc_file = open('../Frequent Itemset Mining/resource/out.csv', 'w', encoding='utf-8')
print('read')
json_str = json_file.read()
print('load')
ls = json.loads(json_str)
print('write')
i=0
print(len(ls))
for l in ls:
    i=i+1
   
    #print(i)
    if i < 341326:
       if len(l) > 10:
          l = l[:9]
       while(True):
            if len(l) < 10:
               l.append('?')
            else:
               break
 
 
       assert len(l) == 10
       content = ','.join(str(author) for author in l)
       content = content.replace(r'"','')
       content = content.replace(r"'",'')
       content = content.replace(r" ",'')
       # print(content)
       print(content,file=doc_file)
    else:
        break
    
json_file.close()
doc_file.close()
