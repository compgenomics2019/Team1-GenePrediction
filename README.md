Computational Genomics Gene prediction pipeline
===============================================
This pipeline is designed by team2-group1, to predict genes of the samples from team1 using a number of Gene prediction tools. This pipeline is used to generate a merged result from several tools.

Requirements
---------------------
[python3](https://www.python.org/) \
Latest [Perl](http://www.perl.org/get.html) \
[bedtools](https://bedtools.readthedocs.io/en/latest/content/installation.html) \
[samtools](http://www.htslib.org/download/) \

bedtools and samtools are required for the union of GeneMarkS-2 and Prodigal results \
All required tools need to be installed properly and added to $PATH

Getting started
----------------
`-f` :Path to file input directory (Required) \
`-p` :Run Prodigal prokaryotic mRNA gene prediction tool \
`-g` :Run GeneMarkS-2 prokaryotic mRNA gene prediction tool \
`-nc` :Run Aragorn and Barrnap to predict tRNA/tmRNA and rRNA (respectively)

Default behavior will still require `-f` and will run both Prodigal and GeneMarkS-2 with Bedtools \
Example usage: `./geneprediction_pipeline_t1.py -f <input_dir>` 


Blast ( For validation )
---------------------
### Requirement
Version_5 database (required) \
taxonomic_id list (required) \
[EDirect](https://www.ncbi.nlm.nih.gov/books/NBK179288/) command-line utility (required) \
Latest [Perl](http://www.perl.org/get.html) (required)\
[python3](https://www.python.org/) (required)\
[blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download) (required)

The validation part assume that all the requirements are installed and the tools should be added to $PATH.


### Quick start
For downloading database:\
Use ```./update_blastdb.pl --blastdb_version 5 --showall``` to see the option. \
Use ```./update_blastdb.pl --blastdb_version 5 [Database] --decompress ``` to download. \
\
For getting the taxonomy_idlist:\
Use ```get_species_taxids.sh -n [organism]```\
\
For blastp (amino acid):   
```./blastp.py -d [queried_fold] -t [taxonomy_idlist] -o [outputfolder]``` \
or blastx (DNA seqs):\
```./blastx.py -d [queried_fold] -t [taxonomy_idlist] -o [outputfolder]``` 
### Description of argument
For blastp.py or blastx.py: \
`-d` :the folder that contains only fasta files you want to validate. \
`-t` :the taxonomy_idlist for specific organism. \
`-o` :the output folder for your outputs. 

For validationP.py or validationX.py: \
`-s` :the folder that contains only fasta files you want to validate. \
`-b` :the folder that contains only blast results for your fasta files. \
`-o` :the output folder for your outputs. 
### Description of output
There will be two folders in your output folder:\
`knownprotein/` : The fasta files in this folder have got rid of the sequences that do not have hit in blast.\
`novelgene/` : The fasta files in this folder do not have hit in blast.
