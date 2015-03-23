# CTCTF 2015: 8675309

### Problem

**Points**: 70

**Description**: 

```
84433 33355524 444777794466683399877775554445533844 4447777
```

**Hint**: 

```
Numbers... phone numbers?
```

### Solution

Many of the digits in the numbers we were given repeat, some of them up to four times. If we separate them, we get this: 

```
8:44:33 333:555:2:4 444:7777:9:44:666:8:33:99:8:7777:555:444:55:33:8:44 444:7777
```

Perhaps this is an encoding scheme where each group of digits represents a word? Fortunately, this is where the hint about the phone numbers becomes useful. Phone keypads map characters to digits so that you can have phone numbers with words in them to make them more memorable, like `555-NOPE`, which translates to `555-6673`.

The repeated digits represent what position on that key the letter is. That is, for the `1` button, `1` would map to `A`, `11` would map to `B`, and `111` would map to `C`. If we apply this decoding algorithm to the phone numbers, we get a message: `THE FLAG ISWHOTEXTSLIKETH IS`.

**Flag**: `WHOTEXTSLIKETHIS`

### Other Resources

* None.
