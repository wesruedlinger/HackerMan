#!/usr/bin/env python3

def read_pgm(filename):
    '''My code
    f = open(filename, 'r')
    content = f.read().split()
    header = content[0:4]
    pixels = content[5:]
    f.close()
    combined = (header, pixels)

    return combined
    '''
    #Condenced Code
    with open(filename, 'r') as fp:
        content = fp.read()
    content = content.split()
    return (content[0:4], content[4:])


def write_pgm(filename,content):
    #Condenced Code
    with open(filename, 'w') as fp:
        for p in content[0] + content[1]:
            fp.write('{}\n'.format(p))
    pass

def invert(content):
    '''My code
    for i in content[1]:
        invert = 255 - int(i)
    print(invert)
    #old = content[1]
    #new = 255 - old
    return
    '''
    #Condenced Code
    for pixelindex in range(len(content[1])):
        content[1][pixelindex] = 255 - str(int(content[1][pixelindex]))
    pass


if __name__ == '__main__':

    pass
