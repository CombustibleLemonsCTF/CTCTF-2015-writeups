# CTCTF 2015: Vulnerable Server

### Problem

**Points**: 60

**Description**: 

```
written by Michael Zhang.
http://vulnserver-failedxyz.c9.io/
```

**Hint**: 

```
You might want to look up SQL injection.
```

### Solution

For this problem, the flag is the `admin`'s password. When we deliberately enter a wrong password, we get: 

```
Nope. SELECT * FROM users WHERE username='admin' AND password='notpassword'
```

Because there is no filtering in place, we can alter the query and the conditions to get a binary outcome to deduce the password.

Short solution: we wrote [this script](client.py).

**Flag**: `i_h0pe_u_didnt_do_this_manually_lol`

### Other Resources

* None.
