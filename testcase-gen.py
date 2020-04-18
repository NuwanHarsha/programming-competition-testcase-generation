import argparse
import string
import random
import numpy as np

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
args.add_argument("--start","-s",dest="start",type=int)
args.add_argument("--end","-e",dest="end",type=int)
args=args.parse_args()


NN=[1,2,3,4,5,6,7,8,9,10,12,15]

NN=NN[args.start:args.end+1]

for i in range(len(NN)):
    fileName = "{}{:02d}.txt".format(args.fileNamePrefix, args.start+i)
    f = open(fileName, "w+")

    N=NN[i]
    f.write("{}\n".format(N))
    for n in range(N):
        R=ranFloat(10)
        f.write("{:.3f}\n".format(R))

    f.close()


