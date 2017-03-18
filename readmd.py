import glob
import os
import sys
print ('Argument List:'+str(sys.argv[1]))
#os.chdir('/mydir')
for file in glob.glob(sys.argv[1]+'*.md'):
    print(file)
    f = open(file,"r")
    print(f.read())


    ## caller code
#     import subprocess
# import sys
# file_name =  os.path.basename(sys.argv[0])
# mdname = file_name.split("[")[0]
# # mdname = 'getSkyline'
# print(mdname)
# subprocess.Popen("readmd.py"+" "+mdname, shell=True)
 
# from heapq import *