#!/usr/bin/env python

import argparse
import re

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--file", help="tsv from biomart containing Stable Gene ID, Transcript Stable ID, Gene name", required=True, type=str)
    return parser.parse_args()

# store args
args = get_args()
martfile = args.file


ID_dict = {}

in_mart = open(martfile, "r")
out_mart = open("celegans_cleaned_mart_ensembl.102.tsv", "w")

for line in in_mart:
    line = line.strip()
    split_ln = re.split("\t", line)
    geneID = split_ln[0]
    transcrID = split_ln[1]
    genename = split_ln[2]

    if geneID not in ID_dict:
        ID_dict[geneID] = [transcrID, genename]


for k,v in ID_dict.items():
    split_transcr = re.split("\.", v[0])
    
    if len(split_transcr) == 3:
        new_transc = split_transcr[0] + "." + split_transcr[1]
        out_mart.write(k +"\t"+ new_transc +"\t"+ v[1] + "\n")
    
    else:
        out_mart.write(k +"\t"+ v[0] +"\t"+ v[1] + "\n")
    

in_mart.close()
out_mart.close()


print("Unique gene IDs:", len(ID_dict))



