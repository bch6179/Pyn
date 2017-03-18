
import os
import os.path
from sys import *
from datetime import datetime, timedelta
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
    mdname = '/mnt/c/Users/zhiqi/Documents/KennyOwn/AGPractice/Pyn/ktag/'+ mdname
    with open(mdname , 'a+') as f: 
        f.write('{}'.format(tagStr + '\n'))
    
def searchTag(f, tagStr):
    t = os.path.splitext(f)
    mdname = t[0].split("[")[0]+'.tag'
    mdname = '/mnt/c/Users/zhiqi/Documents/KennyOwn/AGPractice/Pyn/ktag/' + mdname
    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():
                if line.find(tagStr) != -1:
                    return True
    except:
        return False
    return False

threehour_ago = datetime.now() - timedelta(hours=3)
tenhour_ago = datetime.now() - timedelta(hours=10)

one_days_ago = datetime.now() - timedelta(hours=72)
two_days_ago = datetime.now() - timedelta(days=2)
seven_days_ago = datetime.now() - timedelta(days=7)
eight_days_ago = datetime.now() - timedelta(days=10)

twonine_days_ago = datetime.now() - timedelta(days=22)
thirty_days_ago = datetime.now() - timedelta(days=30)
eighty8_days_ago = datetime.now() - timedelta(days=88)
ninety_days_ago = datetime.now() - timedelta(days=90)

# its win32, maybe there is win64 too?
is_windows = platform.startswith('win')
if not is_windows:#/mnt/c/Users/zhiqi/Documents/KennyOwn/AGPractice/Pyn
    agpath = r'.'
else:
    agpath = r'C:\\Users\\zhiqi\\Documents\\KennyOwn\\AGPractice\\Pyn'
files = os.listdir(agpath)
files_py = [f for f in files if f[-2:] == 'py' or f[-4:] == 'java']
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
        filetime = datetime.fromtimestamp(os.path.getctime(f))
        if filetime < threehour_ago and filetime > tenhour_ago:
            listOfHalf.append(f)
        elif filetime < tenhour_ago and filetime > one_days_ago and "D1" not in f and "W1" not in f and "genius" not in f:
            listOfD1.append(f)
        elif filetime < one_days_ago and filetime > two_days_ago:
            listOfD2.append(f)
        elif filetime < seven_days_ago and filetime > eight_days_ago and "W1" not in f:
            listOfW1.append(f)
        elif twonine_days_ago< filetime < thirty_days_ago :
            listOfM1.append(f)
        elif eighty8_days_ago < filetime <ninety_days_ago  :
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
                    response = raw_input("Done read file?")    
            if response.upper() == "Y":
                tagDate(f, map[i])
            elif response.upper() == "S":
                break

 