import random

def TAKE8(own, opp):
    if (len(own)%256 == 0):
        return 1
    return 0

def TAKE6(own, opp):
    if (len(own)%64 == 0):
        return 1
    return 0

def TAKE4(own, opp):
    if (len(own)%16 == 0):
        return 1
    return 0

def TAKE2(own, opp):
    if (len(own)%4 == 0):
        return 1
    return 0

def TAKE1(own, opp):
    if (len(own)%2 == 0):
        return 1
    return 0

def RAND8(own, opp):
    if (random.randint(0,256) == 0):
        return 1
    return 0

def RAND6(own, opp):
    if (random.randint(0,64) == 0):
        return 1
    return 0

def RAND4(own, opp):
    if (random.randint(0,16) == 0):
        return 1
    return 0

def RAND2(own, opp):
    if (random.randint(0,4) == 0):
        return 1
    return 0

def RAND1(own, opp):
    if (random.randint(0,2) == 0):
        return 1
    return 0

def TF0C0 (own, opp):
    if (len(own) == 0):
        return 0
    return opp[-1]

def TF8C0(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 0
    return opp[-1]

def TF6C0(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 0
    return opp[-1]

def TF4C0(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 0
    return opp[-1]

def TF2C0(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 0
    return opp[-1]

def TF8C2(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 1
    return opp[-1]

def TF6C2(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 1
    return opp[-1]

def TF4C2(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 1
    return opp[-1]

def TF2C2(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 1
    return opp[-1]

def TF8C4(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 1
    return opp[-1]

def TF6C4(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 1
    return opp[-1]

def TF4C4(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 1
    return opp[-1]

def TF2C4(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 1
    return opp[-1]

def TF8C6(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 1
    return opp[-1]

def TF6C6(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 1
    return opp[-1]

def TF4C6(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 1
    return opp[-1]

def TF2C6(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 1
    return opp[-1]

def TF8C8(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 1
    return opp[-1]

def TF6C8(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,64) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 1
    return opp[-1]

def TF4C8(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,16) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 1
    return opp[-1]

def TF2C8(own, opp):
    if (len(own) == 0):
        return 0
    if (random.randint(0,4) == 0):
        return 0
    if (random.randint(0,256) == 0):
        return 1
    return opp[-1]
