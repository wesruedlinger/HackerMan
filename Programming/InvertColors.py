#!/usr/bin/env python3

def invert(l):
    #Condenced Script
    '''
    for n in range(len(l)):
        l[n] = str(255 - int(l[n]))
    '''
    #My Script
    invert = []
    for i in l:
        invert.append(str(255 - int(i)))
    print(invert)
    tmp = l[0]
    l[0] = l[-1]
    l[-1] = tmp
    return

def inverted(l):
    newl = []
    for n in l:
        newl.append(str(255 - int(n)))
    return newl

if __name__ == '__main__':
    invert([123, 0, 456])

#Give a color as a list of rgb decimal values. The return is those colors inverted for the purpose of stegnography.
