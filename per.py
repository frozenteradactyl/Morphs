from string import ascii_lowercase
from sets import Set
import random

#Property of John Andrew Summers, MS
#this defines the morphological corollary to "D" in 'I=DI'

# s is the set of morphemes
s = Set([])

# t is the set of words
t = Set([])

# v is the list of morpheme maps (depths)
v = []

sock = ""
chi = []
count_morph = 0
count_mor = 0

def open_words():
    global t
    foo_string = "vic/vee.txt"
    ld = open(foo_string, "r")
    coo = ld.readlines()
    coo = map(lambda s: s.strip(), coo)
    for ii in coo:
        t.add(ii)

def set_morph():
    global chi
    global s
    global count_mor
    for kk in ascii_lowercase:
         foo_string = "morph_data/" + kk + ".txt"
         ld = open(foo_string, "r")
         coo = ld.readlines()
         coo = map(lambda s: s.strip(), coo)
         for ii in coo:
             s.add(ii)
    for t in s:
        count_mor = count_mor + 1
        chi.insert(count_mor, t)

def chunk():
    global s
    global t
    global v
    global chi
    global count_morph
    global sock
    for i in t:
        for j in s:
            if j in i:
                # print "morph_index: " + str(chi.index(j))
                sock = sock + str(chi.index(j)) + " "
                count_morph = count_morph + 1
        print "Word: " + i
        print "Morph map: " + sock
        v.append(sock)
        sock = ""
        
    print "morphs: " + str(len(s))
    print "words: " + str(len(t))
    print "morphs in words: " + str(count_morph)
    # print v

set_morph()
open_words()
chunk()
