from Bio import SeqIO
import Bio.Data
import sys

input = open(sys.argv[1],'r')
output = open(sys.argv[2],'w+')
for i in SeqIO.parse(input, "fasta"):
    output.write(">"+i.name+"\n")

    output.write(str(i.seq.translate(table="Bacterial"))+"\n")
