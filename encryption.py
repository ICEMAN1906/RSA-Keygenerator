import math
import random
#i=9
"""
Author:Aaron Brown
4/20/2024
 generate keys
"""
def RSA_KeyGenerator():
    """
    generates keys

    returns public and private keys
    """

    with open("primeNumbers.txt",'r') as pnl:
        plaintextlist=pnl.readlines()
    plaintextlist=[int(line.strip()) for line in plaintextlist]

    random1=random.randint(1,400)
    random2=random.randint(1,400)
    p=plaintextlist[random1]
    q=plaintextlist[random2]
    n=p*q
    e= 65537

    if n < 65537:
        e=17

    Lambda=math.lcm(q-1, p-1)
    d= 2
    while True:
        if (d*e) % Lambda == 1: #loop until de%lambda
            break
        d+=1

    publickey=(hex(n),hex(e))
    privatekey=(hex(n),hex(d))

    return publickey,privatekey

RSA_KeyGenerator()

public,privatekey=RSA_KeyGenerator()
print("Public key hexadecimal", public)
print("Private key hexadecimal", privatekey)
