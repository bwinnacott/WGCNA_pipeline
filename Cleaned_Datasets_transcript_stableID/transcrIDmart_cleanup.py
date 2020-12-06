#!/usr/bin/env python

import argparse
import re

def get_args():
    parser = argparse.ArgumentParser(description="converts transcript stable ID to gene synonym")
    parser.add_argument("-f", "--file", help="tsv from biomart containing Stable Gene ID, Transcript Stable ID, Gene name", required=True, type=str)
    return parser.parse_args()

# store args
args = get_args()
martfile = args.file

# gene id: [transcript id, gene name]
ID_dict = {}

in_mart = open(martfile, "r")
out_mart = open("celegans_cleaned_mart_ensembl.102.tsv", "w")

for line in in_mart:
    line = line.strip()
    split_ln = re.split("\t", line)
    geneID = split_ln[0]
    transcrID = split_ln[1]
    genename = split_ln[2]

    if geneID not in ID_dict:   # if the gene ID is not in the dictionary add the row to the ID dictionary
        ID_dict[geneID] = [transcrID, genename]

counter = 0
for k,v in ID_dict.items():
    split_transcr = re.split("\.", v[0])    # split transcript ID by .
    
    if len(split_transcr) == 3:       # if transcript ID has version number i.e. the last 1 in T13A10.10a.1
        if split_transcr[1].endswith("a".lower()):      # if the transcript ID has an "a" as in T13A10.10a.1 following the number 10, remove the a, then write out
            split_transcr2 = re.findall(r"((\d+)(\w))", split_transcr[1])   # split 10a to extract just 10
            new_transc = split_transcr[0] + "." + split_transcr2[0][1]      # piece together new transcript ID T13A10 + . + 10 = T13A10.10
            counter+=1
            out_mart.write(k +"\t"+ new_transc +"\t"+ v[1] + "\n")      # write out all 3 IDs tab separated
            
            
        else:   # else the transcript ID looks like F07C3.7.1
            new_transc = split_transcr[0] + "." + split_transcr[1]      # F07C3 + . + 7 = F07C3.7
            out_mart.write(k +"\t"+ new_transc +"\t"+ v[1] + "\n")      # write out all 3 IDs tab separated
            
    else:
        out_mart.write(k +"\t"+ v[0] +"\t"+ v[1] + "\n")
    

in_mart.close()
out_mart.close()

print(counter)
print("Unique gene IDs:", len(ID_dict))



