import argparse
import string
import random

def ranCap():
    upper_alphabet = string.ascii_uppercase
    return random.choice(upper_alphabet)

def ranSim():
    lowe = string.ascii_lowercase
    return random.choice(lowe)

def ranWord(l):
    a=""
    for _ in range(l):
        a=a+ranCap()
    return a


def ranInt(x):
    return random.randint(0,x-1)

def ranFloat(x):
    return random.random()*x

def ranSign():
    if random.random()>0.5:
        return 1.0
    else:
        return -1.0


args=argparse.ArgumentParser()
args.add_argument("--fileNamePrefix","-fnp",dest="fileNamePrefix")
args=args.parse_args()


NN=[2,5,10,20,30,50,100,150,200,500]

for i in range(len(NN)):
    fileName = "{}{:02d}.txt".format(args.fileNamePrefix, i + 1)
    f = open(fileName, "w+")


    E=ranFloat(1000)
    C=ranFloat(1000)*ranFloat(0.9)
    N=NN[i]
    S=ranFloat(100)


    f.write("{} {} {} {}\n".format(C,E,N,S))

    for n in range(N):
        f.write("{} {}\n".format(ranFloat(E),ranFloat(100)*ranSign()))

    f.close()


