#!/usr/bin/python

import random
import string

posibles = string.ascii_letters + string.digits + string.punctuation

def RandomPasswordGenerator(passLen=10):
    cadena = ""
    for i in range(passLen):
        if not (chr in string.ascii_letters for chr in cadena):
            cadena += random.choice(string.ascii_letters)
        elif not (chr in string.digits for chr in cadena):
            cadena += random.choice(string.digits)
        elif not (chr in string.puctuation for chr in cadena):
            cadena += random.choice(string.punctuation)
        else:
            cadena += random.choice(posibles)
    return cadena
