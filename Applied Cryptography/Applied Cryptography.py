# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:09:00 2020
@author: shane
"""

from binascii import hexlify, unhexlify
from itertools import combinations 
import numpy as np


#-------------------------------
# -- Get lines from text file --
#-------------------------------
def get_lines():
    # 1. Reading text file to import data
    file = open("R00150873.txt", "r") 
    
    # 2. Putting data into an array of lines
    lines = [line.strip().split(' ') for line in file]

    # 3. Split data into ciphertexts given, and what we wish to decrypt
    ciphertexts_given = list( lines[i][0] for i in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29] )
    ciphertext_to_decrypt = lines[len(lines)-1][0]
    
    return ciphertexts_given, ciphertext_to_decrypt

#-------------------------------
# -- Padding the key --
#-------------------------------
def pad_string(string, length):
    return (string * (int(length/len(string))+1))[:length]


#------------------
# -- XOR strings --
#------------------
def xor_strings( s1, s2 ):

    s1_ord = []
    s2_ord = []
    result = []
    res_chr = []
    
    for i in range(len(s1)):
        #Get decimal value of each character in s1 and s2
        s1_ord += [ord(s1[i])]
        s2_ord += [ord(s2[i])]
        
        #Then xor both decimal values at each index
        result += [ s1_ord[i] ^ s2_ord[i]]
        
        #With decimal value we can now get new characther
        res_chr += chr(result[i])
        
    return res_chr


#----------------------
# -- XOR hex strings --
#----------------------
def xor_hex_strings(s1,s2):
    
    global spaces
    
    s1_unhex = unhexlify(s1)
    s1_normal = str(s1_unhex,'latin_1')
    
    s2_unhex = unhexlify(s2)
    s2_normal = str(s2_unhex,'latin_1')
    
    s1_ord = []
    s2_ord = []
    result = []
    res_chr = []
    
    for i in range(len(s1_normal)):
        #Get decimal value of each character in s1 and s2
        s1_ord += [ord(s1_normal[i])]
        s2_ord += [ord(s2_normal[i])]
        
        #Then xor both decimal values at each index
        result += [ s1_ord[i] ^ s2_ord[i]]
        
        #With decimal value we can now get new characther
        res_chr += chr(result[i])
        
        #Check if result is a character to find spaces
        if result[i] >= 65 and result[i] <=90 or result[i] >= 97 and result[i] <=122:
            spaces[i] += 1

    return res_chr
        
            


# Step 1. Get lines from my text file
ciphertexts_given, ciphertext_to_decrypt = get_lines()

# Step 2. Make all ciphers the same length
ciphertexts_given = [cipher[:len(ciphertext_to_decrypt)] for cipher in ciphertexts_given]

# Step 3. Make a empty key
key = [0] * len(ciphertext_to_decrypt)

#Looping through ciphertexts_given
for c1 in ciphertexts_given:
    
    spaces = [0] * len(ciphertext_to_decrypt)
    spaces_str = ' ' * len(ciphertext_to_decrypt)
    res = xor_strings(str(unhexlify(c1),'latin_1'),spaces_str)

    #Looping through ciphertexts_given
    for c2 in ciphertexts_given:
        #As long as its not xoring the same ciphers
        if c1 != c2:
            #XOR the ciphers
            xor_hex_strings(c1,c2)
            
            
    #For each guessed space
    for i in range(len(spaces)):
        #If the number of spaces in guessed index is greater than x
        if spaces[i] >= len(ciphertexts_given) * 0.5:
            key[i] = str(hexlify(bytes(res[i],'latin_1')).decode('utf-8'))
           
        
        
#Put to key into a string
key_str = ''.join([str(x) for x in key])

#Pad the key
padded_key = pad_string(key_str,len(ciphertext_to_decrypt))

#Decrypt cipher
res = xor_hex_strings(ciphertext_to_decrypt,padded_key)  
res = ''.join([str(x) for x in res]) 

print(res)
        












