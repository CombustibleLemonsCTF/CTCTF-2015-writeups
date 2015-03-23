# CTCTF 2015: Just Keep Going

### Problem

**Points**: 50

**Description**: 

```
Just keep going…
persevere.txt
Rot13->b64->repeat, should be automated for good results.
```

**Hint**: 

```
nope
```

### Solution

The problem description tells us exactly how to reverse the contents of the file. [`This file`](persevere.txt) contains the output of `base64`, which makes binary data safe to export as ASCII text, and `rot13`, which is just the Caesar cipher with `n = 13`. However, instead of automation, we just copied and pasted a long chain of commands and pipes and then adjusted the it until we got the flag.

```
[!] cat persevere.txt | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d | rot13 | base64 -d
```

**Flag**: `isnt_automation_great`

### Other Resources

* None.
