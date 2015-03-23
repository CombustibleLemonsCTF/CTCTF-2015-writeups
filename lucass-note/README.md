# CTCTF 2015: Lucas's Note

### Problem

**Points**: 75

**Description**: 

>   
> note.txt

**Hint**: 

> lucas is a pretty cool dude

### Solution

Lucas numbers are part of a recursive integer sequence where `L_n = L_{n - 1} + L_{n - 2}`; this is essentially a Fibonacci sequence with different seed values. Instead of starting with `0` and `1`, Lucas numbers start with `2` and `1`, giving us the sequence `2, 1, 3, 4, 7, 11, 18, 29, . . . `.

What does this have to do with the flag and the file of text that we got? Well, suppose that you combined the characters whose indices were Lucas numbers. We wrote [this program](lucas.py) to do that.

**Flag**: `LUCASNUMBERSAREPRETTYCOOL`

### Other Resources

* None.
