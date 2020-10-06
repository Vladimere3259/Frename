#!/usr/bin/python3

import os
import sys

wd = os.getcwd().split('/')[-1]

print len(sys.argv)

content_list = []

for content in os.listdir("."): 
    content_list.append(content)
content_list.sort()
x = 0

if len(sys.argv) > 1 :
    x = int(sys.argv[1])
    
for i in content_list :
    if(".jpg" in i or ".JPG" in i) :
        
        y = '{:04d}'.format(x)
        print ("mv -v \""+i+"\" \"" + wd + " " + y + ".jpg\"")

        x+=1
        
