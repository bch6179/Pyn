
import os
import os.path
from sys import *
from datetime import datetime, timedelta
import platform
import subprocess
def reTag():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and ('.py' or '.java' in f)]
    for f in files:
        t = os.path.splitext(f)
        mdname = t[0].split("[")
 
        ouf = open(mdname[0]+'.tag','a+')
        content = ouf.readlines()
        ouf.seek(0,0)
        s = ''
       
        for t1 in mdname[1:]:
            s = s + '['+t1 +'\n'
        ouf.write('{}'.format(s))

def tagDate(f, tagStr):
    t = os.path.splitext(f)
    # newname = t[0]+tagStr+t[1]
    # os.rename(f, newname)
    # fnames = in glob.glob(t[0]+'*'+'.md'):
    # mdfile = ''
    # for f in fnames:
    #     try:
    #         mdfile = open(f, 'r')
    #     except:
    #         mdfile = open(f, 'w')
    # if mdfile == '':
    mdname = t[0].split("[")[0]+'.tag'
    mdname = agpath+'ktag/'+ mdname
    print mdname
    with open(mdname , 'a+') as f: 
        f.write('{}'.format(tagStr + '\n'))
 
def foo(ag):
    t = os.path.splitext(ag)
    mdname = t[0].split("[")[0] 
    gmap = agpath+dirMap[typeResponse]+'ktag/geniusdir.txt'
    try:
        with open(gmap, 'a+') as f: 
            f.write('{}	{}			{}		{}\n'.format(mdname, mdname, 0, 'Note'))
    except:
        return False
    return False


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    path_to_file = agpath+path_to_file
    print "path_to_file:"+path_to_file
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            if platform.system() == 'Linux':
                return stat.st_ctime
            else:
                return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            print "Exception creation_date"
            return stat.st_mtime
def modifiy_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_mtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
def mapToGeinus(ag):
    t = os.path.splitext(ag)
    mdname = t[0].split("[")[0] 
    gmap = agpath+'../Metrics/geniusMap.txt'
    priority = 0
    if searchTagTS(ag, '5Star'):
        priority = 5
    elif searchTagTS(ag, '4tar'):
        priority = 4
    elif searchTagTS(ag, '3tar'):
        priority = 3 
    elif searchTagTS(ag, '2tar'):
        priority = 2  
    elif searchTagTS(ag, '1tar'):
        priority = 1
    elif searchTagTS(ag, 'Disable'):
        priority = 0
    try:
        print "mapToGeinus"+ag
        with open(gmap, 'a+') as f: 
            f.write('{}	{}			{}		{}\n'.format(mdname, datetime.fromtimestamp(creation_date(ag)), 0, 'Note'))
    except:
        return False
    return False
def searchTag(f, tagStr):
    t = os.path.splitext(f)
    mdname = t[0].split("[")[0]+'.tag'
    mdname = agpath+'ktag/' + mdname
    #print "searchTag filename:"+mdname

    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():
                if line.find(tagStr) != -1:
                    return True
    except:
        return False
    return False
def searchTagTS(f, tagStr):
    mdname = f + '.json'
    mdname = agpath+'/.ts/' + mdname
    #print "searchTagTS filename:"+mdname

    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():
                if line.find(tagStr) != -1:
                    return True
    except:
        return False
    return False
import fileinput,re  
import sys
def addTagJson(f, tagStr):
    mdname = agpath+'.ts/'+ f +'.json'

    #print "addTagJson:"+mdname
    toAdd = {"title":tagStr,"type":"sidecar","style":"color: #ffffff !important; background-color: #4986e7 !important;"}
    try:
        with open(mdname, encoding='utf-8-sig') as rf: 
            js = json.load(rf)
        with open(mdname,  'w' ) as tf:
            js['tags'].append(toAdd)
            json.dump(js, tf)         
    except:
      #  print "add exception"
        return
    return  
def readTagJson(src):
    mdname = agpath+'.ts/'+ src +'.json'
    print "In readTagJson:"+mdname
    res = []
    try:
        with open(mdname, encoding='utf-8-sig') as rf: 
            js = json.load(rf)
            print js
            for tag in js['tags']:
                res.append(tag['title'])
            print res
        with open(agpath+src,  'w' ) as wf:
            wf.write('{}'.format(res + '\n'))
    except:
        print "exception in readTagJson",sys.exc_info()[0]
    return  res

pattern = r'\s{"tags":[\s'
threehour_ago = datetime.now() - timedelta(hours=3)
tenhour_ago = datetime.now() - timedelta(hours=10)

one_days_ago = datetime.now() - timedelta(hours=30 )
two_days_ago = datetime.now() - timedelta(days=5    )
seven_days_ago = datetime.now() - timedelta(days=7)
eight_days_ago = datetime.now() - timedelta(days=25)

twonine_days_ago = datetime.now() - timedelta(days=26)
thirty_days_ago = datetime.now() - timedelta(days=40)
eighty8_days_ago = datetime.now() - timedelta(days=88)
ninety_days_ago = datetime.now() - timedelta(days=90)

# its win32, maybe there is win64 too?
is_windows = platform.system() == 'Windows'
if platform.system() == 'Windows':
    agpath = r'C:\\Users\\zhiqi\\Documents\\KennyOwn\\AGPractice\\'
elif platform.system() == 'Linux':
    agpath = r'/mnt/c/Users/zhiqi/Documents/KennyOwn/AGPractice/'
else:
     agpath = r'/Users/zhitaoq/Documents/AGPractice/'
dirMap = {}
dirMap['p'] = 'Pyn/'
dirMap['n'] = "KeyNotes/"



listOfD1 = []
listOfD2 = []
listOfW1 = []
listOfM1 = []
listOf3M = []
listOfHalf = []
debug = False
if debug:
    typeResponse = 'p'
else: 
    if version_info > (3,0):
        typeResponse = input("Choose Pyn or Note task")
    else:
        typeResponse = raw_input("Choose Pyn or Note task")
blacklist = ['FSM', 'js', 'winvscode','addTagInJson.py']
blacklist
if typeResponse.upper()  in "PN": 
        
    agpath += dirMap[typeResponse]

    files = os.listdir(agpath)
    files_py = [f for f in files if not f.startswith('.') and not f.startswith('[') and f not in blacklist and f[:-2] != '.m' and f[:-3] != '.md']

    #filesTag = os.listdir(agpath)
    #[mapToGeinus(f) for f in filesTag]

    for f in files_py:
        print "filename: "+f

        try:
            filetime = datetime.fromtimestamp(creation_date(f))
        except:
            print "exception"
            

        if filetime < threehour_ago and filetime > tenhour_ago:
            listOfHalf.append(f)
            foo(f)

        elif filetime < tenhour_ago and filetime > one_days_ago and "D1" not in f and "W1" not in f and "genius" not in f:
            listOfD1.append(f)
        elif two_days_ago < filetime < one_days_ago  :
            listOfD2.append(f)
        elif filetime < seven_days_ago and filetime > eight_days_ago and "W1" not in f:
            listOfW1.append(f)
        elif thirty_days_ago  < filetime < eight_days_ago :
            listOfM1.append(f)
        elif thirty_days_ago > filetime > ninety_days_ago  :
            listOf3M.append(f)

    print("short of today")
    for f in listOfHalf:
        print(f)

    print("one day ago")
    for f in listOfD1:
        print(f)
    print("two day ago")
    for f in listOfD2:
        print(f)
    print("7 day ago COUNT: ",len(listOfW1))
    for f in listOfW1:
        print(f)
    print("21 day ago COUNT: ",len(listOfM1))

    for f in listOfM1:
        print(f)
    # print("9021 day ago")
    # for f in listOf3M:
    #     print(f)
    map = {0:"[D1]", 1:"[W1]", 2:"[M1]", 3:"[M3]"}            
    for i, sublist in enumerate([listOfD1, listOfW1, listOfM1, listOf3M]):
        print("Beginning review files of "+ map[i], "count:",len(sublist))
        print()
        for f in sorted(sublist):
            if 'tag' in f: continue
            if not searchTag(f, map[i]):
                print(f)
                #readTagJson(f)
                print datetime.fromtimestamp(creation_date(f))
                command1 = "/Applications/Visual\ Studio\ Code.app/Contents/MacOS/Electron"
                print "switch "+agpath+f
                command2="/Applications/tagspaces.app/Contents/MacOS/tagspaces"
                #os.system(command2+' '+agpath+f)
                os.system('python /Users/zhitaoq/Documents/AGPractice/Pyn/readTagJson.py '+f)
                os.system(command1+' '+agpath+f)

                if debug:
                    response = 'Y'
                else: 

                    if version_info > (3,0):
                        response = input("Done read file? ")
                    else:
                        response = raw_input(" Done read file?")    
                        

                if response.upper() == "Y":
                    try:
                        tagDate(f, map[i])
                        response = raw_input("Enter priority NOW ?") 
                        if response.upper() != 'N':   
                            tagDate(f, response+'Star') 
                            #addTagJson(f,response+'Star')
                            os.system('python /Users/zhitaoq/Documents/AGPractice/Pyn/addTagJson.py '+f+ ' '+response+'Star')
                    except:
                        print "exception"
                elif response.upper() == "S":
                    break

 