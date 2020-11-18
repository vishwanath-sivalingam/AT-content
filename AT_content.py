# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:29:35 2020

@author: vishu
"""

dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

# AT content
a_count = dna_seq.count('A')
t_count = dna_seq.count('T')

print("length: " + str(len(dna_seq)))
print("AT content: " + str((a_count + t_count)/len(dna_seq)))
