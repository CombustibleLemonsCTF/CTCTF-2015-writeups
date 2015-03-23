# CTCTF 2015: His name is Jay Mo

### Problem

**Points**: 25

**Description**: 

None given.

**Hint**: 

> unitedjaymo

### Solution

This is a recon problem of Jay Mo, one of the organizers of this competition. If we google his online handle, `unitedjaymo`, we get his personal website, GitHub, and Twitter, among other things. His website turns up nothing of interest with regard to finding the flag, but his GitHub profile turns up [two suspicious commits](https://github.com/unitedjaymo/unitedjaymo.github.io/commits?author=unitedjaymo) named "This isn't CSS" and "His name is Jay Mo."

In the commit "[His name is Jay Mo](https://github.com/unitedjaymo/unitedjaymo.github.io/commit/8a69038b9219a379519e65924f25da8033e94bb3)," which is the name of this challenge, we can see that he added a CSS comment containing the flag in the source of `index.html`.

**Flag**: `that's_my_name`

### Other Resources

* None.
