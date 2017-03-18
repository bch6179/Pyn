
import os
import os.path
import sys
from datetime import datetime, timedelta
import platform
import fileinput
 
def tagDate():
    f = sys.argv[1]
    tagStr ='['+sys.argv[2]+'Star]'
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
# f = raw_input("Enter fileName:") 
# response = raw_input("Enter priority NOW ?") 
# if response.upper() != 'N':   
#     tagDate(f, response) 
tagDate()