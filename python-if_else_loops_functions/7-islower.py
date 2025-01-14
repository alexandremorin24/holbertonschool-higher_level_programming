#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

# Autre facon de faire :
# def islower(c):
#    return 97 <= ord(c) <= 122
# Retourne True si la condition est respectée, sinon False
