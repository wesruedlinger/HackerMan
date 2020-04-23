#!/usr/bin/env python3

def steg_encode_char(char, cover):
    msgbin = format(ord(char), '0>8b')

    for i in range(0,8):
        coverbinl = list(format(int(cover[i]),'0>8b'))
        coverbinl[-1] = msgbin[i]
        cover[i] = str(int(''.join(coverbinl),2))
    return cover

''' Condenced Code
    charbin = format(ord(char), '0>8b')
    for index in range(8):
        coverbinl = list(format(int(cover[index], '0>8b'))
        coverbinl[-1] = charbin[index]
        cover[index] = int(''.join(coverbinl), 2))
'''

def steg_decode_char(stego):
    binList = []
    msgbit = []
    for n in stego:
        binList.append(format(int(n), 'b'))
    for x in binList:
        msgbit.append(x[-1])
    message = chr(int(''.join(msgbit), 2))
    return message

''' Condenced Code
    msgbits = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
    return chr(int(''.join(msgbits), 2))
'''

if __name__ == '__main__':

    cover = ['250','251','252','251','250','249','248','249']
    steg_encode_char('a',cover)
    print(steg_decode_char(cover))
