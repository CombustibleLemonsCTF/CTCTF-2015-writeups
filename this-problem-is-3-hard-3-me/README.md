# CTCTF 2015: This problem is 3 hard 3 me!

### Problem

**Points**: 70

**Description**: 

> written by Michael Zhang.  
> 27623b1c6b18181fed122b113027111f  
> flag: cbcb381b203b232233cbcb  

**Hint**: 

> It's not a hash. Don't try to brute-force crack it, because even if you get something, it'll be totally unrelated to the flag.

[Additional hints](https://gist.github.com/failedxyz/86a5f50becdf0d6de7db): 

> this translates roughly to "not a hash lol  " (notice the spaces)  
> 321a124c274c702739704c181a184c4

> Hint 2 for 3 hard: it's based on ASCII.

> base 16, base 2, base 3

### Solution

The solution was surprisingly simple.

The first two hints tell us that each byte (i.e. two hexadecimal digits) translates to a character in the original message. However, the encoding scheme is not ASCII: 

```
[!] python3
Python 3.3.2+ (default, Feb 28 2014, 00:52:16) 
[GCC 4.8.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import binascii
>>> binascii.unhexlify(b'cbcb381b203b232233cbcb')
b'\xcb\xcb8\x1b ;#"3\xcb\xcb'
```

The last hint was the most important. Somehow, we have to use "base 16, base 2, base 3," in that order. Well, the encoded flag is already in hexadecimal, so the "base 16" must mean that we have to convert each character into base 10. Anything in base 2 is valid in base 3, so we can convert each character now in base 10 to "base 2," and then interpret that base 2 string as "base 3."

[Here](solution.py) is the program that we wrote up to get the flag. This is the program's output: 

> Message: ĀϏţuϫlly౼TĒRńĀRy  
> Flag: ஃஃşpóţ÷öňஃஃ

Fun fact: the hexadecimal string that we got in the first hint translates to `ŇoT˽Ā˽НĀŠН˽lol˽`.

Side note: we never got points for this because the scoring system was broken the whole time. To the developers: maybe you should have used [picoCTF's CTF platform](https://github.com/picoCTF/picoCTF-Platform-1), which "has been tested extensively on Ubuntu 12.04 LTS?" Just a thought.

**Flag**: `ஃஃşpóţ÷öňஃஃ`

### Other Resources

* None.
