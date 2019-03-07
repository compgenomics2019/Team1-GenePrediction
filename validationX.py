#! /projects/team1/group2_geneprediction/python3/bin/python3.7
"""
Created on Sat Mar  2 21:14:21 2019

@author: yjk12
"""

import os
import multiprocessing
import argparse
import subprocess
import re

parser = argparse.ArgumentParser(description='blast')
parser.add_argument('-s',required=True,  help = 'input sequences')
parser.add_argument('-b',required=True,  help = 'blast_results')
parser.add_argument('-g',default='still',  help = 'gff_files')
parser.add_argument('-o',required=True,  help = 'output_folder')
args=parser.parse_args()

###blast result is sorted by e-value
path1=args.s
path2=args.b
#path3=args.g

statistic = multiprocessing.Manager().dict()
gms=sorted(os.listdir (path1))
blast=sorted(os.listdir(path2))
if args.g!='still':
    gfffile=sorted(os.listdir(path3))


def modify(aa,bl,gf,ST):      # aa--protein, bl--blast_result, gf--gff
    ###origin predicted protein sequences
    pathA=os.path.join(path1,aa)
    pathB=os.path.join(path2,bl)
    #pathC=os.path.join(path3,gf)
    file1=open(pathA,'r')
    faa=file1.read()
    faa=faa.split('>')[1:]
    
    ###blast result
    file2=open(pathB,'r')
    blastp=file2.read()
    blastp=blastp.split('# BLASTX 2.8.1+\n# Query: ')[1:]
    if len(faa)!=len(blastp):
        print(len(faa)-len(blastp))
        exit('no')
    newlist=[]         # new list that abandaned false positive/novel genes
    newgene=[]         # new list for abandaned genes
    for i in range(len(faa)):
        if re.search('# 0 hits found',blastp[i])==None:
            newlist.append(i)
        else:
            newgene.append(i)
    '''k=0
    for i in range(len(faa)):
        a=int(faa[i].split(' ')[0])
        for j in range(k,len(blastp)):
            b=int(blastp[j].split(' ')[0])        
            if a==b:
                newlist.append(i)
                k=j+1
                break
            elif a<b:
                newgene.append(i)
                break'''
    ### writing known genes
    newprotein=open(args.o+'knownprotein/'+aa,'w')
    for i in newlist:
        newprotein.write('>'+faa[i])
    newprotein.close()
    ### writing novel gene/false positive
    novelgene=open(args.o+'novelgene/'+aa[0:-4]+'novel.faa','w')
    for i in newgene:
        novelgene.write('>'+faa[i])
    novelgene.close()
    #statistic.append(aa[0:-4]+':'+str(len(newlist)/(len(newlist)+len(newgene))))
    statistic[aa[0:-4]]=len(newlist)/(len(newlist)+len(newgene))
    ###gff file   
    '''file3=open(pathC,'r+')          
    gff=file3.read()    
    gff=gff.split('##sequence-region') '''


if __name__=='__main__':
    subprocess.call(['mkdir '+args.o+'knownprotein'],shell=True)
    subprocess.call(['mkdir '+args.o+'novelgene'],shell=True)
    for i in range(0,len(gms),4):
        tlist=[]
        for j in range(4):
          if i+j > len(gms)-1:
              break
          else:
              t=multiprocessing.Process(target=modify,args=(gms[i+j],blast[i+j],0,statistic))               #gfffile[i+j]
              t.start()
              tlist.append(t)
        for k in tlist:
            k.join()
    
    sta=open(args.o+'/statistics.csv','w')
    sta.write('Sample'+','+'Positive rate'+'\n')
    for i,j in statistic.items():
    	sta.write(i+','+str(j)+'\n')
    sta.close()
