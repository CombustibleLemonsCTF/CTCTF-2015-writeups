# CTCTF 2015: Dbftbs Djqifs

### Problem

**Points**: 20

**Description**: 

```
Kyv wcrx zj trgklivu_kyv_wcrx
```

**Hint**: 

```
Step it up
```

### Solution

The hint is the same as the flag from last time. Therefore, the cipher used to encode the flag is probably the Caesar cipher (again). [Decoding](http://rumkin.com/tools/cipher/caesar.php) this ciphertext when `n = 9` gives the message `The flag is captured_the_flag`.

Alternatively, instead of solving the challenge the boring way, you might have noticed that `Kyv wcrx zj` looks a lot like `The flag is`. Making the necessary substitutions, you would have gotten `The flag is *a*t**e*_the_flag`. Then, you could have searched `/usr/share/dict/words` with grep: 

```
[!] sudo grep --ignore-case "^.a.t..e.$" /usr/share/dict/words
Castries
Martinez
bantered
baptized
baptizes
bartered
battened
battered
cactuses
cantered
captives
captured

[ . . . additional output redacted . . . ]
```

**Flag**: `captured_the_flag`

### Other Resources

* None.
