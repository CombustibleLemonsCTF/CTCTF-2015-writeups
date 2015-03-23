# CTCTF 2015: They said EasyCTF was Easy

### Problem

**Points**: 25

**Description**: 

![](easysteg.jpg)

**Hint**: 

> Hint

### Solution

As in any forensics challenge, we ran this image through the `strings` command, which grabs the printable fragments of the file and writes them to standard output. Most of the output is part of the image and irrelevant, but, hidden at the very end, is the flag.

```
[!] strings easysteg.jpg 
Exif
Adobe Photoshop CS6 (Windows)
2015:03:01 19:37:51
Adobe_CM
Adobe
b34r
7GWgw
AQaq"
dEU6te

[ . . . output condensed . . . ]

yl}~+#
G*  a
He43
h@4 
}e7^
file.headers.are.important......flag:this_steg_was_waaay_too_easy_to_find
```

**Flag**: `this_steg_was_waaay_too_easy_to_find`

### Other Resources

* None.
