# 081

```bash
┌──(kali💀kali)-[~/…/CTF/hackmyvm/challenges/81]
└─$ cat message.txt -A                                
 ^I   ^I  $
  ^I^I    $
 ^I  ^I^I^I $
 ^I ^I ^I  $
 ^I ^I^I^I^I^I$
 ^I ^I ^I^I^I$
  ^I^I    $
 ^I ^I  ^I $
 ^I ^I  ^I $
 ^I ^I^I  ^I$
 ^I ^I^I^I^I^I$
 ^I   ^I^I^I$
 ^I ^I ^I ^I$
 ^I ^I^I  ^I$
  ^I^I ^I ^I$
 ^I ^I^I^I^I^I$
$
$
$
^I   $
   ^I^I$
  ^I^I ^I$
^I   $
    ^I$
^I ^I $
^I ^I$
  ^I^I ^I$
   $
^I^I^I^I^I$
^I^I^I^I^I$
^I $
^I ^I ^I^I$
  ^I^I ^I$
$
$
$
   ^I   ^I^I^I$
^I$
      ^I^I    $
^I$
     ^I ^I ^I  $
^I$
     ^I ^I ^I  $
^I$
      ^I^I ^I  $
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I ^I ^I  $
^I$
      ^I^I ^I  $
^I$
     ^I  ^I ^I^I$
^I$
      ^I^I  ^I^I$
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I    ^I^I$
^I$
      ^I^I ^I  $
^I$
     ^I ^I  ^I $
^I$
      ^I^I  ^I^I$
^I$
     ^I ^I^I^I^I^I$
^I$
      ^I^I    $
^I$
     ^I   ^I^I $
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I ^I  ^I^I$
^I$
      ^I^I    $
^I$
     ^I  ^I^I ^I$
^I$
     ^I   ^I ^I$
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I    ^I $
^I$
     ^I ^I ^I ^I$
^I$
      ^I^I ^I ^I$
^I$
      ^I^I   ^I$
^I$
     ^I  ^I^I^I $
^I$
      ^I^I  ^I^I$
^I$
      ^I^I ^I ^I$
^I$
      ^I^I ^I ^I$
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I     ^I$
^I$
     ^I ^I  ^I $
^I$
      ^I^I    $
^I$
     ^I ^I ^I ^I$
^I$
     ^I  ^I^I^I $
^I$
     ^I   ^I  $
^I$
     ^I ^I^I^I^I^I$
^I$
     ^I  ^I   $
^I$
      ^I^I  ^I^I$
^I$
     ^I ^I  ^I $
^I$
      ^I^I  ^I^I$
^I$
      ^I^I^I ^I $
^I$
      ^I ^I  ^I$
^I$
```
![sublime](img/sublime.png)
```
Sublime output shows some morse code 
challenge  has three parts 
```
```
The caret "^" followed by "I" reperesents tab character . 
dollar signs at the end of each line is point to end of line 
so we got some tabs and spaces 
only two chracter repeated so we can assume that might be binaries
lets conver it .
```

# First Part

```bash
┌──(kali💀kali)-[~/…/CTF/hackmyvm/challenges/81]
└─$ cat message.txt | sed -e "s/ /0/g" -e "s/\t/1/g"
01000100
00110000
01001110
01010100
01011111
01010111
00110000
01010010
01010010
01011001
01011111
01000111
01010101
01011001
00110101
01011111



1000
00011
001101
1000
00001
1010
101
001101
000
11111
11111
10
101011
001101



0001000111
1
000000110000
1
000001010100
1
000001010100
1
000000110100
1
000001011111
1
000001010100
1
000000110100
1
000001001011
1
000000110011
1
000001011111
1
000001000011
1
000000110100
1
000001010010
1
000000110011
1
000001011111
1
000000110000
1
000001000110
1
000001011111
1
000001010011
1
000000110000
1
000001001101
1
000001000101
1
000001011111
1
000001000010
1
000001010101
1
000000110101
1
000000110001
1
000001001110
1
000000110011
1
000000110101
1
000000110101
1
000001011111
1
000001000001
1
000001010010
1
000000110000
1
000001010101
1
000001001110
1
000001000100
1
000001011111
1
000001001000
1
000000110011
1
000001010010
1
000000110011
1
000000111010
1
000000101001
1
00 
```

```
From first part we got these :
01000100
00110000
01001110
01010100
01011111
01010111
00110000
01010010
01010010
01011001
01011111
01000111
01010101
01011001
00110101
01011111
```
> D0NT_W0RRY_GUY5_
# Second Part
```
1000
00011
001101
1000
00001
1010
101
001101
000
11111
11111
10
101011
001101
```
```
Second part is not like binaries so
from sublime i thought it might be morse code 
we can conver one,s to '-' and zero,s to '.' 
to get a correct flag
```

```bash
┌──(kali💀kali)-[~/…/CTF/hackmyvm/challenges/81]
└─$ cat second  | sed -e 's/1/-/g'  -e  's/0/./g'
-...
...--
..--.-
-...
....-
-.-.
-.-
..--.-
...
-----
-----
-.
-.-.--
..--.-
```
# Second Flag
>B 3 _ B 4 C K _ S 0 0 N ! _ 