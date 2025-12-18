# VARACS
Visualization Analysis of RNA-seq, ATAC-seq, Chip-seq and Single cell RNA-seq.

**VARACS** is a visualization and analysis framework for high-throughput sequencing data, including  
**RNA-seq, ATAC-seq, ChIP-seq, and single-cell RNA-seq**.

This repository provides reproducible scripts and visualization pipelines for transcriptomic and epigenomic analyses.

---

## Overview

VARACS is designed to streamline downstream analysis and visualization of bulk and single-cell sequencing data.  
It integrates commonly used bioinformatics methods into modular and reusable scripts.

Supported data types:
- Bulk RNA-seq
- ATAC-seq
- ChIP-seq
- Single-cell RNA-seq (scRNA-seq)

---

## Repository Structure

VARACS/
├── README.md                  # Project documentation
├── scripts/                   # Analysis and visualization scripts
│   ├── rnaseq_analysis.R
│   ├── atacseq_analysis.R
│   ├── chipseq_analysis.R
│   ├── scrnaseq_analysis.R
│   └── visualization_utils.R
├── figures/                   # Generated figures
├── data/                      # Example or processed datasets
├── results/                   # Output files
└── docs/                      # Additional documentation

---

## Key Features

- Differential expression analysis for RNA-seq
- Chromatin accessibility profiling (ATAC-seq)
- ChIP-seq peak visualization and annotation
- Single-cell RNA-seq clustering, trajectory, and marker analysis
- Publication-ready visualizations

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/JackNg88/VARACS.git
cd VARACS

2. Install dependencies

R packages:

install.packages(c("Seurat", "ggplot2", "dplyr", "DESeq2", "Signac"))

Python packages (optional):

pip install scanpy pandas matplotlib anndata

3. Run analysis scripts

Rscript scripts/scrnaseq_analysis.R


⸻

Applications

VARACS has been applied to:
	•	Stem cell reprogramming studies
	•	Chromatin dynamics during cell fate transitions
	•	Cancer and ageing-related transcriptomic analyses
	•	Multi-omics data integration

⸻

License

This project is licensed under the MIT License.

---

## Contact

If you have any questions, issues, or suggestions regarding this repository,  
please feel free to contact:

**Jian Wu**  
📧 Email: Jian.Wu@mpi-bn.mpg.de

---
