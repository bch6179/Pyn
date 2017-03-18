
import os
import os.path
from sys import *
from datetime import datetime, timedelta
import platform

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
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/ktag/'+ mdname
    with open(mdname , 'a+') as f: 
        f.write('{}'.format(tagStr + '\n'))
 
def foo(ag):
    t = os.path.splitext(ag)
    mdname = t[0].split("[")[0] 
    gmap = '/Users/zhitaoq/Documents/AGPractice/Pyn/ktag/geniusdir.txt'
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
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
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
    gmap = '/Users/zhitaoq/Documents/AGPractice/Pyn/Metrics/geniusMap.txt'
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
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/ktag/' + mdname
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
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/.ts/' + mdname
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

pattern = r'\s{"tags":[\s'
threehour_ago = datetime.now() - timedelta(hours=3)
tenhour_ago = datetime.now() - timedelta(hours=10)

one_days_ago = datetime.now() - timedelta(hours=24)
two_days_ago = datetime.now() - timedelta(days=2)
seven_days_ago = datetime.now() - timedelta(days=7)
eight_days_ago = datetime.now() - timedelta(days=10)

twonine_days_ago = datetime.now() - timedelta(days=22)
thirty_days_ago = datetime.now() - timedelta(days=40)
eighty8_days_ago = datetime.now() - timedelta(days=88)
ninety_days_ago = datetime.now() - timedelta(days=90)

# its win32, maybe there is win64 too?
is_windows = platform.system() == 'Windows'
if not is_windows:
    agpath = r'/Users/zhitaoq/Documents/AGPractice/Pyn'
else:
    agpath = r'C:\\Users\\zhiqi\\Documents\\KennyOwn\\AGPractice\\Pyn'
files = os.listdir(agpath)
files_py = [f for f in files if f[-2:] == 'py' or f[-4:] == 'java']

filesTag = os.listdir(agpath)
#[mapToGeinus(f) for f in filesTag]



listOfD1 = []
listOfD2 = []
listOfW1 = []
listOfM1 = []
listOf3M = []
listOfHalf = []
debug = False
if debug:
    response = 'Y'
else: 
    if version_info > (3,0):
        response = input("Finish task now?")
    else:
        response = raw_input("Finish task now?")
if response.upper() == "Y":
    for f in files_py:
        filetime = datetime.fromtimestamp(creation_date(f))
        if filetime < threehour_ago and filetime > tenhour_ago:
            listOfHalf.append(f)
            foo(f)

        elif filetime < tenhour_ago and filetime > one_days_ago and "D1" not in f and "W1" not in f and "genius" not in f:
            listOfD1.append(f)
        elif two_days_ago < filetime < one_days_ago  :
            listOfD2.append(f)
        elif filetime < two_days_ago and filetime > eight_days_ago and "W1" not in f:
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
print("7 day ago")
for f in listOfW1:
    print(f)
print("21 day ago")
for f in listOfM1:
    print(f)
print("9021 day ago")
for f in listOf3M:
    print(f)
map = {0:"[D1]", 1:"[W1]", 2:"[M1]", 3:"[M3]"}            
for i, sublist in enumerate([listOfD1, listOfW1, listOfM1, listOf3M]):
    print("Beginning review files of "+ map[i])
    print()
    for f in sorted(sublist):
        if 'tag' in f: continue
        if not searchTag(f, map[i]):
            print(f)
            if debug:
                response = 'Y'
            else: 
                if version_info > (3,0):
                    response = input("Done read file?")
                else:
                    response = raw_input(" Done read file?")    
            if response.upper() == "Y":
                
                tagDate(f, map[i])
                response = raw_input("Enter priority NOW ?") 
                if response.upper() != 'N':   
                    tagDate(f, response+'Star') 
                    addTagJson(f,response+'Star')
            elif response.upper() == "S":
                break

 