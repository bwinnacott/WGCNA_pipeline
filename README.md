# Weighted Gene Co-expression Network Analysis (WGCNA) and Functional Annotation Pipeline
### UO in collaboration with InVivo Biosystems
### Authors: Tucker Bower, Kate Roth, Brendan Winnacott
### Mentors: Dr. Adam Saunders, Dr. Trisha Brock

## Project Summary

This pipeline utilizes *C. elegans* gene expression data to perform a network analysis of co-expressed genes and identify gene clusters (modules) significantly correlated with experimental treatments. This method evaluates changes in expression patterns with a higher, systems-level approach than traditional differential gene expression analysis. The genes, modules, and pathways identified in this analysis serve to inform and guide future research. 

## Table of contents

1. [Getting Started](#Getting_Started)
2. [Input Data](#Input_Data)
3. [Data Cleanup](#Data_Cleanup)
4. [Data Pre-processing](#Data_Pre-Processing)
5. [Running WGCNA](#Running_WGCNA)
6. [GO Module Enrichment](#GO_Module_Enrichment)
7. [Glossary](#Glossary)

## Getting_Started

#### Hardware Requirements
* System memory: 32 GB minimum
  * Memory usage increases with size and number of input datasets, WGCNA parameters
#### Software
R/4.0.2
Rstudio 1.0 or newer
OSX (Currently, pipeline appears **inoperable** on Linux/Windows based machines)

Clone all files from github repo:

> git clone https://github.com/2020-bgmp/group-projects-invivo-fall-project/ 

## Input data
A minimum of 15 samples is recommended for WGCNA. Therefore, if you have N experimental samples, you must find 15-N samples from public databases.

## Data_Cleanup
Fully cleaned and prepped datasets will be provided on Google Drive for a basic analysis. If not incorporating new data, skip directly to [Running WGCNA](#Running_WGCNA)

For the incorporation of new literature datasets, follow the [Dataset_Cleanup_Tutorial.Rmd](https://github.com/2020-bgmp/group-projects-invivo-fall-project/blob/master/dataset_cleanup_tutorial/Dataset_Cleanup_Tutorial.Rmd) instructions. 

Each dataset could have a unique format and require a hands-on approach to conform to the structure of existing data. Irregularities in gene naming conventions, gene number, and data frame structure can all lead to incompatibility of datasets for WGCNA. 

## Data_Pre-Processing

## Running_WGCNA

## GO_Module_Enrichment

## Glossary

Module: A cluster of highly interconnected genes 

Eigengene: The first principle component of a module. This value is representative of the module as a whole

Module Membership: A metric of correlation between a given gene and its module's eigengene 

Gene Significance: A metric of biological significance of a given gene to its pathway 

Hub Gene: A highly connected gene with a high module membership and gene significance

Trait: Experimental condition. Can represent a pool of biological replicates
