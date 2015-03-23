# CTCTF 2015: Vulnerable Server

### Problem

**Points**: 60

**Description**: 

> written by Michael Zhang.  
> http://vulnserver-failedxyz.c9.io/

**Hint**: 

> You might want to look up SQL injection.

### Solution

For this problem, the flag is the `admin`'s password. When we deliberately enter a wrong password, we get: 

```
Nope. SELECT * FROM users WHERE username='admin' AND password='notpassword'
```

Because there is no filtering in place, we can alter the query and the conditions to get a binary outcome to deduce the password. Here is the necessary algorithm: 

1. Loop over all of the valid characters (i.e. the alphanumeric characters as well as the underscore).
2. Given a current character of the loop, create a query that tests whether the username is `admin` and whether the password starts with the current password plus the current character.
3. Send the query to the server.
4. If the query returns a success, then add the current character to the current password, and go back to step 1 to loop start over.
5. Otherwise, continue to the next character at step 2.
6. If there are no more characters to loop over, then you have the full password.

We wrote [this script](client.py) to automate the guessing process. 

**Flag**: `i_h0pe_u_didnt_do_this_manually_lol`

### Other Resources

* None.
