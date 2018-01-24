# -*- coding: utf-8 -*-
"""
@author: Jack L. Clements
"""

import re
def W1(testData): #A task that iterates through test data per-regex statement
    print 'Task W1:'
    p = re.compile('ABC')
    for string in testData:
        print string
        m = p.search(string)
        if m:
            print 'MATCH'
        else:
            print 'NO MATCH'
    
def W2(testData): 
    print 'Task W2:'
    p = re.compile('^A(B|C|D|X)C$')
    for string in testData:
        print string
        m = p.search(string)
        if m:
            print 'MATCH'
        else:
            print 'NO MATCH'

def W3(testData): 
    print 'Task W3:'
    p = re.compile('^(ABC){1}\n')
    for string in testData:
        print string
        m = p.search(string)
        if m:
            print 'MATCH'
        else:
            print 'NO MATCH'

def W4(testData): 
    print 'Task W4:'
    p = re.compile('^(A(.)*B)$')
    for string in testData:
        print string
        m = p.search(string)
        if m:
            print 'MATCH'
        else:
            print 'NO MATCH'

def W5(testData): 
    print 'Task W5:'
    p = re.compile('^(A(OX|XO)*B)$')
    for string in testData:
        print string
        m = p.match(string)
        if m:
            print 'MATCH'
        else:
            print 'NO MATCH'

def main():
    array = ['ABC', 'AXC', 'ABBBC', 'ABC\n', 'AteststringB', 'AXOXOOXOXOXB', 'AB', 'AOXB'] #test data
    W1(array)
    W2(array)
    W3(array)
    W4(array)
    W5(array)
    
if __name__ == '__main__':
    main()