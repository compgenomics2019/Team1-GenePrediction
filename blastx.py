#! /projects/team1/group2_geneprediction/python3/bin/python3.7

import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='blast')
parser.add_argument('-d',required=True,  help = 'input dir')
parser.add_argument('-t',required=True,  help = 'taxidlist')
parser.add_argument('-o',required=True,  help = 'outputfolder')
args=parser.parse_args()




def dirname(path):
    #if
    for filename in os.listdir(path):
        dirlist.append(os.path.join(path,filename))
        name.append(filename)
        
if __name__ == '__main__':
    dirlist=[]
    name=[]
    dirname(args.d)
    subprocess.call(['mkdir '+args.o],shell=True)
    print(args.d,args.t) 
    for i in range(len(dirlist)):
        subprocess.call(['blastx -evalue 1e-6 -db swissprot_v5 -max_target_seqs 1 -outfmt 7 -taxidlist '+args.t+' -out '+args.o+'/'+name[i][0:-4]+'.txt ' +'-query '+dirlist[i]],shell=True)
