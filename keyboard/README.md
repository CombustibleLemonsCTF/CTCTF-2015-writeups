# CTCTF 2015: Keyboard

### Problem

**Points**: 35

**Description**: 

```
ZY DHPUKYEHAURP, A JBSJKZKBKZYY DZURQH ZJ A TQKRYF YW QYDYFZYE SP MRZDR BYZKJ YW UVAZYKQOK AHQ HQUVADQF MZKR DZURQHKQOK, ADDYHFZYE KY A HQEBVAH JPJKQT; KRQ "BYZKJ" TAP SQ JZYEVQ VQKKQHJ (KRQ TYJK DYTTYY), UAZHJ YW VQKKQHJ, KHZUVQKJ YW VQKKQHJ, TZOKBHQJ YW KRQ ASYNQ, AYF JY WYHKR. WYH KRQ WVAE, ZK'J CQQUZKDVQAY
```

**Hint**: 

```
Keyboard... substitution?
```

### Solution

This is essentially a substitution cipher challenge. To make things easier, we used [quipquip](http://quipqiup.com/), which analyzes which English words could possibly make up the ciphertext. The highest ranked solution for this ciphertext was: 

```
IO CRYPTOGRAPHY, A SUBSTITUTIOO CIPHER IS A METHOD OF EOCODIOG BY WHICH UOITS OF PLAIOTEXT ARE REPLACED WITH CIPHERTEXT, ACCORDIOG TO A REGULAR SYSTEM; THE 'UOITS' MAY BE SIOGLE LETTERS (THE MOST COMMOO), PAIRS OF LETTERS, TRIPLETS OF LETTERS, MIXTURES OF THE ABOVE, AOD SO FORTH. FOR THE FLAG, IT'S ~EEPITCLEAO
```

The last sentence, `FOR THE FLAG, IT'S ~EEPITCLEAO`, is what we are looking for. However, the most glaring error for the whole text is that the `N`s were incorrectly interpreted as `O`s. The last sentence is now `FOR THE FLAG, IT'S ~EEPITCLEAN`. We inferred that the `~` is probably a `K`, which gives us the flag.

**Flag**: `KEEPITCLEAN`

### Other Resources

* None.
