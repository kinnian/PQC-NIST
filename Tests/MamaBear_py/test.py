import math
import numpy
import os
import _pysha3 # Bibliotheque pour la fonction cSHAKE256 utilisee par la fonction de hachage 


# Constantes de MamaBear

D = 312
x = 2**10
N = x**D - x**(D/2) - 1
d = 3
sigma2 = 1/2
clar = x**(D/2)
l = 4


## Fonctions auxilliaires

def encode_string(S):
    return bytearray([len(len(S)), len(S)]) + S

def bytepad(X, w):
    z = bytearray([len(w), w]) + X
    while (len(z)%0) != 0:
        z = z + b'0'
    while ((len(z)/8)%w) != 0:
        z = z + b'0 0 0 0 0 0 0 0'
    return z

def h(p, data, L):
    pblock = bytearray([1,40,24,32,0,32,10,56,1,3,63,4,18,1])
    XX = pblock + bytearray([0,p]) + data
    LL = 8*L
    NN = b""
    SS = b"ThreeBears"
    return keccak_512(bytepad(encode_string(NN) + encode_string(SS), 136) + XX + b'0 0', LL)

def uniform(seed, i, j):
    B = h(0, seed + bytearray([d*j+i]), len(bytearray([])))
# TODO decoder B en temps qu'element de Z/NZ
    return B

def noise(p, seed, i):
    B = h(p, seed + bytearray(i), D)
    for j in range(0,D):
        sample = B[j]
        digit[j] = 0
        for k in range(0, math.ceil(2*sigma2)):
            v = 64*min(1, (2*sigma2 - k))
            digit[j] = digit[j] + round((sample + v)/256) + round((sample - v)/256)
            sample = (sample*4) % 256
    for j in range(0,D):
        digit[j] = (digit[j]*x**j)%N
    return numpy.sum(digit)

def extract(b, S, i):
    if i % 2 == 0:
        j = i/2
    else:
        j = D-(i+1)/2
# TODO ecrire S comme element de [0,N-1]
    return round(S*2**b/(x**(j+1)))

def step(R,s):
    b = len(R)
    s_0 = s[0]
    for i in range(b):
        l[i] = (s ^ (s_0*R))[i]
    return l

def step_i(i, R, s):
    for j in range(i):
        s = step(R,s)
    return s

def o_mult(a,b):
    s = 0
    for i in range(9):
        s = s ^ (bytearray(b)[8-i]*step_i(i, Q, a))
    return s

def o_pwr(k, a):
    for i in range(k):
        b = o_mult(a,b)
    return b


## Melas FEC encode

def syndrome_18(B):
    n = len(B)
    P = b'0x46231'[:19]
    s = 0
    for i in range(0, n):
        s = step(P, s ^ B[i])
    return s

def fecEncode_18(B):
    return B + syndrome_18(B)


## Melas FEC decode

def fecDecode_18(B):
    n = len(B)
    s = syndrome_18(B)
    Q = b'0x211'[:10]
    c = o_mult(step_i(9, Q, s), step_i(9, Q, reverse(s)))   # TODO what is reverse??
    r = step_i(17, Q, o_pwr(510, c))
    s_0 = step_i(511-n, Q, s)

    halfTraceTable = [36,10,43,215,52,11,116,244,0]
    halfTrace = 0
    for i in range(9):
        halfTrace = halfTrace ^(r[i]*bytearray(halfTraceTable[i])[:9])

    (e_0, e_1) = (o_mult(s_0, halfTrace), o_mult(s_0, halfTrace) ^ s_0)

    for i in range (n-18):
        if (step_i(i, Q, e_0) == b'1'[:9]) | (step_i(i, Q, e_1) == b'1'[:9]):
            B[i] = B[i] ^ 1

    return B[:(n-18-1)]



## Keypair Generation

def getPubKey(sk):
    for i in range(d):
        a[i] = noise(1, sk, i)

    matrixSeed = h(1,sk, 24)
    for i in range(d):
        for j in range(d):
            M[i][j] = uniform(matrixSeed, i, j)

    for i in range(d):
        A[i] = noise(1, sk, d+i) + numpy.sum(M[i]*a*clar) # TODO multiplication de vecteurs composant par composant

    pk = (matrixSeed, A)
    return pk

def keypair():
    sk = os.urandom(40)
    return (sk, getPubKey(sk))


## Encapsulation

def encapsDet(pk, seed):
    (matrixSeed, A) = pk # lol so not gonna work

    for i in range (d):
        b[i] = noise(2, matrixSeed + seed + b'0', i)

    for i in range(d):
        for j in range(d):
            M[i][j] = uniform(matrixSeed, i, j)

    for i in range(d):
        B[i] = noise(2, seed, d+i) + numpy.sum(M[i]*b*clar) # TODO same as before

    C = noise(2, seed, 2*d) + numpy.sum(A*b*clar)   # TODO same
    pt = seed

    encpt = fecEncode(bit(pt))   # TODO mettre pt en bit string
    for i in range(len(encpt)):
        encr[i] = (extract(4, C, i) + 8*encpt) % 16

    ss = h(2, matrixSeed + pt + b'0', 32)
    capsule = (B, encr[:len(pt)-1], b'0')   # TODO check "nibbles"

    return (ss, capsule)

def encapsulate(pk):
    seed = os.urandom(32)
    return encapsDet(pk, seed)


## Decapsulation

def decapsulate(sk, capsule):
    for i in range(d):
        a[i] = noise(1, sk, i)
    (B, encr, iv) = capsule

    C = noise(2, 2*d) + numpy.sum(B*a*clar)
    for i in range(len(encr)):
            encoded_seed[i] = round((2*encr[i] - extract(5, C, i))/2**l)

    seed = fecDecpde(encoded_seed)

    (shared_secret, capsule_) = encapsDet(getPubKey(sk), seed)

    if (capsule_ != capsule):
        return "Fail!"
    else:
        return shared_secret
