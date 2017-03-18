import os
import json
import sys
localagpath = r'/Users/zhitaoq/Documents/AGPractice/Pyn/'
src = sys.argv[1]
print "read "+src
#res = []
 
def readTagJson(src):
    mdname = localagpath+'.ts/'+ src +'.json'
   # print "addTagJson:"+mdname
    res = []
    try:
        with open(mdname, 'r') as f: 
          #  print "opened"+src
            for line in f.readlines():      
              #  print "read"
                js = json.loads(line[3:])
                 
                for tag in js['tags']:
                    res.append(tag['title'])
                    # [i for i in range(len(string)) if string.startswith('test', i)]
              #  print "towrite"   
                with open(localagpath+src,  'a' ) as wf:
                    wf.seek(0, 0)
                    wf.write('{}'.format(res + '\n'))
                   # print "writed "
    except:
        #print "external exception in readTagJson"
        return ''
    return  res
#readTagJson(src,res,str)
 
print readTagJson(src)