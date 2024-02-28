# -*- coding: utf-8 -*-
"""Diffie Hellman_Project_code.ipynb

Automatically generated by Colaboratory.



**SECURE COMMUNICATION**


**SECURING COMMUNICATION THROUGH VARIOUS LAYERS**

1st Process..

Implementing Diffie Hellman Exchange Algorithm
"""

# use Python 3 print function
# this code ensures that the print function works the same in Python 2.x and 3.x
from __future__ import print_function

# Variables Used
P = int(input(' Please enter the value of P.'))
print('  Thanks for entering the value of P as ' + str(P))
g = int(input(' Please enter the value of g.'))
print('  Thanks for entering the value of g as ' + str(g))
 
a = int(input(' \n Please enter the value of a.'))
b = int(input(' Please enter the value of b.'))

# A1 Sends B2 A = g^a mod P
A = (g**a) % P
print( "\n  A1 sends over to B2: " , A )
 
# B2 Sends A1 B = g^b mod P
B = (g ** b) % P
print( "  B2 sends over to A1: " , B )

# A1 computes the Shared Secret: S_A1 = B^a mod P
A1SharedSecret = (B ** a) % P
print( "    \n  A1 Shared Secret: ", A1SharedSecret )
 
# B2 computes the Shared Secret: S_B2 = A^b mod P
B2SharedSecret = (A**b) % P
print( "  B2 Shared Secret: ", B2SharedSecret )

"""2nd PROCESS

Now, 

Vignere Process will happen..


Then Polybius Cipher Process...


Easy to Understand !
"""

# Python code to implement 
# Vigenere Cipher 

# This function generates the 
# key in a cyclic manner until 
# it's length isn't equal to 
# the length of original text 
def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key))

"""WAIT WAIT WAIT..... !


There is more Numbers of line of code.

Hi there, 

This Project will be Useful for you!

you can use it for your college project.

Also for Startups.


Mail me now at **vatshayan007@gmail.com** to get full explained project code, project report, PPT and research paper on this Project
"""

