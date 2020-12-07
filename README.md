# Weighted Gene Co-expression Network Analysis (WGCNA) and Functional Annotation Pipeline
### UO in collaboration with InVivo Biosystems
### Authors: Tucker Bower, Kate Roth, Brendan Winnacott
### Mentors: Dr. Adam Saunders, Dr. Trisha Brock

## Project Summary

This pipeline utilizes *C. elegans* gene expression data to perform a network analysis of co-expressed genes and identify gene clusters (modules) significantly correlated with experimental treatments. This method evaluates changes in expression patterns with a higher, systems-level approach than traditional differential gene expression analysis. The genes, modules, and pathways identified in this analysis serve to inform and guide future research. 

## Table of contents

1. [Hardware & Software Requirements](#Hardware_&_Software_Requirements)
2. [Input Data](#Input_Data)
3. [Data Cleanup](#Data_Cleanup)
4. [Data Pre-processing](#Data_Pre-Processing)
5. [Running WGCNA](#Running_WGCNA)
6. [GO Module Enrichment](#GO_Module_Enrichment)
7. [Glossary](#Glossary)






## Hardware_&_Software_Requirements

#### Hardware
System memory: 32 GB minimum
Memory usage increases with size and number of input datasets, WGCNA parameters
#### Software
R/4.0.2
Rstudio 1.0 or newer
OSX (Currently, pipeline appears **inoperable** on Linux/Windows based machines)

Clone all files from github repo:

> https://github.com/2020-bgmp/group-projects-invivo-fall-project/
## Input data
A minimum of 15 samples is recommended for WGCNA. Therefore, if you have N experimental samples, you must find 15-N samples from public databases.
## Data_Cleanup


## Data_Pre-Processing
## Running_WGCNA
## GO_Module_Enrichment
## Glossary

Module: A cluster of highly interconnected genes \

Eigengene: The first principle component of a module. This gene is representative of the gene expression profiles within its module \

Module Membership: A metric of correlation between a given gene and its module's eigengene \

Gene Significance: A metric of biological significance of a given gene to its pathway \

Hub Gene: A highly connected gene \

Trait: Experimental condition. Can represent a pool of biological replicates
