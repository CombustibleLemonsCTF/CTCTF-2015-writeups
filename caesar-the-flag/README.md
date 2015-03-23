# CTCTF 2015: Caesar the Flag

### Problem

**Points**: 10

**Description**: 

```
Csbjogvdl jt bo ftpufsjd qsphsbnnjoh mbohvbhf opufe gps jut fyusfnf njojnbmjtn. Uif mbohvbhf dpotjtut pg pomz fjhiu tjnqmf dpnnboet boe bo jotusvdujpo qpjoufs. Ju jt eftjhofe up dibmmfohf boe bnvtf qsphsbnnfst, boe xbt opu nbef up cf tvjubcmf gps qsbdujdbm vtf. Ju xbt dsfbufe jo 1993 cz Vscbo Nümmfs. Bozxbzt, uif gmbh jt tufq_ju_vq
```

**Hint**: 

None given.

### Solution

As the title suggests, the problem description is the ciphertext of a [cipher](http://en.wikipedia.org/wiki/Caesar_cipher) where each letter is shifted by `n` positions. For example, if `n = 1`, then "A" would become "B," "B" would become "C," and so on. Because the letters loop around, there are only 25 possibilities in the solution space, making this cipher very easy to crack. Only one of them is likely to contain English.

Using [this tool](http://rumkin.com/tools/cipher/caesar.php), we got the flag when `n = 25`.

**Flag**: `step_it_up`

### Other Resources

* None.
