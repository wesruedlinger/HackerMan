#!/usr/bin/env python3

def steg_encode_char(msg, cover):
    '''
    # My Code
    charlist = list(char)
    letList = []
    for x in charlist:
        letList.append(list(format(ord(x), '0>8b')))
    print(cover)
    for i in range(len(cover)):
        coverbinl = list(format(cover[i], '0>8b'))
        coverbinl[-1] = int(str(letList[i]))
        cover[i] = int(''.join(coverbinl), 2)

    print(cover)
    for i in range(len(charlist)):
        coverbinl = list(format(int(cover[i]),'0>8b'))
        coverbinl[-1] = msgbin[i]
        cover[i] = str(int(''.join(coverbinl),2))
    return cover
    '''
#Condenced Code
    coverindex = 0

    for char in msg:
        charbin = format(ord(char), '0>8b')
        for index in range(8):
            coverbinl = list(format(int(cover[coverindex]), '0>8b'))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = str(int(''.join(coverbinl), 2))
            coverindex += 1
    return

def steg_decode_char(stego):
    '''
    # My Code
    binList = []
    msgbit = []
    for n in stego:
        binList.append(format(int(n), 'b'))
    for x in binList:
        msgbit.append(x[-1])
    message = chr(int(''.join(msgbit), 2))
    return message
    '''
#Condenced Code
    msgbits = []
    msg = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
        if len(msgbits) == 8:
            msg.append(chr(int(''.join(msgbits), 2)))
            msgbits = []
    return ''.join(msg)


if __name__ == '__main__':
    pass
