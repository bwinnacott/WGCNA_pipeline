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
#### Software Requirements
* R/4.0.2
* Rstudio 1.0
* OSX (Currently, pipeline appears **inoperable** on Linux/Windows based machines)
* Clone all files from github repo:

> git clone https://github.com/2020-bgmp/group-projects-invivo-fall-project/ 

### First Steps
* If incorporating new literature data from a new dataset/source, begin with [data cleanup](Data_Cleanup)
* If merging cleaned data, begin with [data pre-processing](Data_Pre-processing)
* If running WGCNA with cleaned and processed data (available on Google Drive), begin by [running WGCNA](Running_WGCNA)

## Input data
A minimum of 15 samples is recommended for WGCNA. Therefore, if you have N experimental samples, you must find 15-N samples from public databases.

## Data_Cleanup
For the incorporation of data from a new dataset/source, follow the [Dataset_Cleanup_Tutorial.Rmd](https://github.com/2020-bgmp/group-projects-invivo-fall-project/blob/master/dataset_cleanup_tutorial/Dataset_Cleanup_Tutorial.Rmd) instructions. 

Each dataset could have a unique format and require a hands-on approach to conform to the structure of existing data. Irregularities in gene naming conventions, gene number, and data frame structure can all lead to incompatibility of datasets for WGCNA. 

## Data_Pre-processing

To merge datasets, remove rRNA genes, and create the design matrix, follow the [pre-processing for WGCNA tutorial](https://github.com/2020-bgmp/group-projects-invivo-fall-project/blob/master/WGCNA/pre-processing_for_WGCNA.Rmd). 

## Running_WGCNA

To generate co-expression modules using WGCNA, follow the [WGCNA module generation tutorial](https://github.com/2020-bgmp/group-projects-invivo-fall-project/blob/master/WGCNA/WGCNA_module_generation.Rmd). Make sure to adjust the following parameters to suit the needs of your analysis:

Parameter Name | Explanation
------------ | -------------
* gene_ids  |  Gene naming convention used in expression data. Can be external_gene_name, wormbase_gene, transcript_stable_ID, etc.
* softPower | Threshold of correlation. Set to the lowest value that exceeds 0.9 on the scale-free topology index (scale independence plot)
* minModuleSize | Minimum number of genes per module. Vary to adjust number of modules generated
* MEDissThres | Merging threshold. This value "cuts" the branches of the module tree (METree) at the specified value. Any branches below this value will be merged. Useful for removing redundant/similar modules
* CorThreshold | Correlation threshold for selecting modules with a minimum of this correlation value for further analysis


## GO_Module_Enrichment

## Glossary

Module: A cluster of highly interconnected genes 

Eigengene: The first principle component of a module. This value is representative of the module as a whole

Module Membership: A metric of correlation between a given gene and its module's eigengene 

Gene Significance: A metric of biological significance of a given gene to its pathway 

Hub Gene: A highly connected gene with a high module membership and gene significance

Trait: Experimental condition. Can represent a pool of biological replicates
