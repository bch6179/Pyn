
import os
import os.path
from sys import *
from datetime import datetime, timedelta
import platform
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
def searchTagTS(f, tagStr):
    if  f.startswith('.') or   f.startswith('['): return False
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/.ts/'+ f + '.json'
 
    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():
                if line.find(tagStr) != -1:
                    return True
    except:
        return False
    return searchTag(f, tagStr)
import json
def getTagJson(f):
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/.ts/'+ f + '.json'
    res = []
    try:
        with open(mdname, 'r') as f: 
            for line in f.readlines():             
                js = json.loads(line[3:])
                for sub in js['tags']:
                    res.append(sub['title'])
    except:
        return ''
    return ','.join(res)
def addTagJson(f, tagStr):
    mdname = '/Users/zhitaoq/Documents/AGPractice/Pyn/.ts/'+ f + '.json'
     
    toAdd = {"title":tagStr,"type":"sidecar","style":"color: #ffffff !important; background-color: #4986e7 !important;"}
    try:
        with open(mdname, mode='r', encoding='utf-8') as feedsjson:
            feeds = json.load(feedsjson)
        with open(mdname, mode='w', encoding='utf-8') as feedsjson:
            feeds['tags'].append(toAdd)
            json.dump(feeds, feedsjson)         
    except:
        return  
    return  
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

def mapToGeinus(ag):
    t = os.path.splitext(ag)
    mdname = t[0].split("[")[0] 
    gmap = '/Users/zhitaoq/Documents/AGPractice/Metrics/geniusMap.txt'
    score = 0
    group = 'default'
    type = 'default'
    if  ag.startswith('.') or   ag.startswith('['): return  False
    tagStr = getTagJson(ag)
    if tagStr.find('DP') != -1:
        group = 'DP'
    elif tagStr.find(  'Stack') != -1:
        group = 'Stack'
    elif tagStr.find( 'DFS') != -1:
        group = 'DFS'
    elif tagStr.find('BFS') != -1:
        group = 'BFS'
    elif tagStr.find('LinkedList') != -1:
        group = 'LinkedList'
    elif tagStr.find('Array') != -1:
        group = 'Array'
    elif  tagStr.find('String') != -1:
        group = 'String'
    elif  tagStr.find('HashMap') != -1:
        group = 'HashMap'
        
    if searchTagTS(ag, '5Star'):
        score = 0
    elif searchTagTS(ag, '4tar'):
        score = 1
    elif searchTagTS(ag, '3tar'):
        score = 2 
    elif searchTagTS(ag, '2tar'):
        score = 3  
    elif searchTagTS(ag, '1tar'):
        score = 4
    elif searchTagTS(ag, 'Disable'):
        score = 5
    try:
        print "mapToGeinus"+ag
        with open(gmap, 'a+') as f: 
            f.write('{}	{}	{}	{}	{}		{}\n'.format(mdname, datetime.fromtimestamp(creation_date(ag)), group, tagStr, score, 'Note'))
    except:
        return False
    return False
 
is_windows = platform.system() == 'Windows'
if not is_windows:
    agpath = r'/Users/zhitaoq/Documents/AGPractice/Pyn'
else:
    agpath = r'C:\\Users\\zhiqi\\Documents\\KennyOwn\\AGPractice\\Pyn'
 
os.rename('/Users/zhitaoq/Documents/AGPractice/Metrics/geniusMap.txt', '/Users/zhitaoq/Documents/AGPractice/Metrics/geniusMapBak.txt')
filesTag = os.listdir(agpath)
[mapToGeinus(f) for f in filesTag if f[-2:] == 'py' and (not f.startswith('.') or not f.startswith('['))]