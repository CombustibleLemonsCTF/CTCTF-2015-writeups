# CTCTF 2015: Kelvin's Favorite Colors

### Problem

**Points**: 40

**Description**: 

```
Frogs are known to have excellent eyesight. Being a designer, Kelvin the Frog also has excellent taste for colors. Here's a list of his favorite colors.
```

**Hint**: 

```
What does the # do?
```

### Solution

Ordinarily, the `#` would signal that the following characters were part of a hexadecimal RGB color code. Each color in the code, red, green, and blue, would be assigned an integer value from `0` to `255`, or `0` to `FF` in hexadecimal. For example, the first color, `#466c61`, has a red value of `70`, a green value of `108`, and a blue value of `97`.

However, in this case, the hexadecimal values in the text file also represent an ASCII string. Using Python, you can merge the hexadecimal strings as one and decode it as ASCII.

```python
[!] python3
Python 3.3.2+ (default, Feb 28 2014, 00:52:16) 
[GCC 4.8.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> hexed = ''
>>> with open('colors.txt', 'r') as f:
...     for line in f:
...             hexed += line.strip()[1:]
... 
>>> hexed
'466c61673a2020746861745f7761735f657a'
>>> import binascii
>>> binascii.unhexlify(hexed.encode('utf-8'))
b'Flag:  that_was_ez'
```

**Flag**: `that_was_ez`

### Other Resources

* None.
