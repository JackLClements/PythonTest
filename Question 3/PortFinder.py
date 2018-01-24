# -*- coding: utf-8 -*-
"""
@author: Jack L. Clements
"""

import os.path
import re
import collections

def getPort(fPath): #reads port no. from file
    p = re.compile('[0-9a-fA-F]+') #regex for port structure
    test = open(fPath, 'r')
    port = p.search(test.readline()).group() #seperate port from header token
    test.close()
    return port

#Simple traversal, works on all OS
def traverse(fPath, cnt):
    if os.path.exists(fPath):
        pathContents = os.listdir(fPath)
        for files in pathContents:
            if os.path.isfile(os.path.join(fPath, files)):
                if os.path.splitext(files)[1] == '.inform':
                    port = getPort(os.path.join(fPath, files))
                    cnt[port] += 1
                
            if os.path.isdir(os.path.join(fPath, files)): #use join over + \\ to avoid creating a new string
                traverse(os.path.join(fPath, files), cnt)
        return cnt
    else:
        print ' dir. does not exist'

#UNIX Traversal, works with symbolic links

def isVisited(fPath, visitedNodes): #Checks if node/branch has been visited
    for nodes in visitedNodes:
        if nodes == fPath:
            return True
    return False

def unixTraverse(fPath, visitedFiles, cnt): 
    #same as old algorithm but w/ a list of all visited nodes
    if os.path.exists(fPath):
        pathContents = os.listdir(fPath)
        for files in pathContents:
            newPath = os.path.join(fPath, files)
            if isVisited(newPath, visitedFiles) == False:
                if os.path.islink(newPath):
                    realPath = os.path.realpath(newPath)
                    newPath = realPath #replace path, essentially branch before scanning directory
                if os.path.isfile(newPath):
                    visitedFiles.append(newPath)
                    if os.path.splitext(files)[1] == '.inform':
                        port = getPort(os.path.join(fPath, files))
                        cnt[port] += 1
                if os.path.isdir(newPath): #use join over + \\ to avoid creating a new string
                    visitedFiles.append(newPath)
                    unixTraverse(newPath, visitedFiles, cnt)
        return cnt
    else:
        print ' dir. does not exist'


def main():
    cnt = collections.Counter() #Used collections data structure to save space on printing lists
    l = []
    currentDir = os.getcwd()
    unixTraverse(os.path.join(currentDir, 'Test Data'), l, cnt) 
    print l
    print cnt
    
if __name__ == '__main__':
    main()
    
