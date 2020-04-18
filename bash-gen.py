import argparse


args=argparse.ArgumentParser()
args.add_argument("--startNumber","-s",type=int,dest="startNo")
args.add_argument("--endNumber","-e",type=int,dest="endNo")
args.add_argument("--lineCode","-l",type=str,dest="lineCode")
args.add_argument("--outFile","-o",type=str,dest="outFile")
args=args.parse_args()

# print(args)


f = open(args.outFile, "w+")

for i in range(args.startNo,args.endNo+1):
    f.write("{}\n".format(args.lineCode.format(i,i)))

f.close()