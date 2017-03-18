import fileinput,re  
import sys
import json
def  addJsonTag2(file_name,pattern,value=""):  
    fh=fileinput.input(file_name,inplace=True)  
    for line in fh:  
        replacement='{"tags":[' +  '{"title":'+value+',"type":"sidecar","style":"color: #ffffff !important; background-color: #4986e7 !important;"},'
        line=re.sub(pattern,replacement,line)  
        sys.stdout.write(line)  
    fh.close()  
def addTagJson(f, tagStr):
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/.ts/'+ f +'.json'
     
    toAdd = {"title":tagStr,"type":"sidecar","style":"color: #ffffff !important; background-color: #4986e7 !important;"}
    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():             
                js = json.loads(line[3:])
        with open(mdname,  'w' ) as f:
            js['tags'].append(toAdd)
            json.dump(js, f)         
    except:
        return  
    return  
 
addTagJson('wiggleSequence.py',  '5Star')