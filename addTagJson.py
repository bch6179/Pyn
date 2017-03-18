import fileinput,re  
import sys

import os
import json
localagpath = r'/Users/zhitaoq/Documents/AGPractice/Pyn/'
src = sys.argv[1]
tagStr = sys.argv[2]
print "read "+src
#res = []
 
def addTagJson(src, tagStr):
    mdname = localagpath+'.ts/'+ src +'.json'

    print "addTagJson:"+mdname
    toAdd = {"title":tagStr,"type":"sidecar","style":"color: #ffffff !important; background-color: #4986e7 !important;"}
    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():             
                js = json.loads(line[3:])
        with open(mdname,  'w' ) as f:
            js['tags'].append(toAdd)
            json.dump(js, f)         
    except:
        print "outer add exception"
        return  
    return  

addTagJson(src, tagStr)
