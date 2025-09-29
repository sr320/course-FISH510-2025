# Glossary

A curated list of key terms and definitions relevant to FISH 510 (Data Science / Bioinformatics for Fisheries & Environmental Genomics). Terms are grouped by theme and listed alphabetically within each theme. Feel free to expand.

## Core Concepts
**Algorithm**: A finite sequence of well-defined instructions used to solve a class of problems.
**Annotation (Genome)**: The process of identifying functional elements (genes, regulatory regions, features) in a genome sequence.
**API (Application Programming Interface)**: A defined interface that allows software components or services to communicate programmatically.
**Automation**: Using scripts or workflows to execute repeatable tasks with minimal manual intervention.
**Benchmarking**: Systematic comparison of tools, pipelines, or methods using defined performance metrics.
**Best Practice**: A standardized, evidence-based method shown to produce reliable, reproducible results.
**Bias (Statistical)**: Systematic deviation of an estimator's expected value from the true value.
**Big Data**: Datasets so large or complex that traditional tools struggle with storage, processing, or analysis.
**Command-Line Interface (CLI)**: Text-based interface for interacting with software by typing commands.
**Container**: A lightweight, reproducible software environment packaging code, dependencies, and runtime (e.g., Docker, Apptainer/Singularity).
**Data Lifecycle**: Stages from planning, collection, processing, analysis, sharing, to preservation.
**Data Provenance**: Documentation of the origin, transformations, and handling history of data.
**Data Stewardship**: Responsible management of data assets across their lifecycle.
**Dependency**: External library, package, or tool required for software or analysis to run.
**Environment (Computing)**: A collection of software dependencies and configurations used to run code reproducibly.
**High-Performance Computing (HPC)**: Use of clustered or specialized systems for large-scale or parallel computation.
**Metadata**: Data describing other data (e.g., sample ID, collection date, instrument settings).
**Open Science**: Practices promoting transparency, accessibility, reproducibility, and reuse of research outputs.
**Pipeline**: An ordered sequence of analytical steps transforming raw data into interpretable results.
**Reproducibility**: Ability to obtain the same results using the same data, code, and environment.
**Replication (Scientific)**: Independent repetition of a study, potentially with new data, to confirm findings.
**Scalability**: Capacity of a method or system to handle increasing data volume or complexity without failing.
**Version Control**: Tracking and managing changes to files (e.g., with Git) over time.

## Statistics & Experimental Design
**ANOVA (Analysis of Variance)**: Statistical test comparing means across multiple groups.
**Blocking**: Grouping experimental units sharing similar characteristics to reduce variance.
**Bootstrap**: Resampling method for estimating variability or confidence intervals.
**Confidence Interval (CI)**: Range likely to contain a true parameter value at a specified confidence level.
**Correction for Multiple Testing**: Adjusting p-values to control false positives (e.g., FDR, Bonferroni).
**Effect Size**: Quantitative measure of the magnitude of a phenomenon.
**False Discovery Rate (FDR)**: Expected proportion of false positives among declared significant results.
**Hypothesis (Null / Alternative)**: Statement tested statistically; null often represents no effect.
**Overfitting**: Model capturing noise rather than signal, reducing generalizability.
**p-value**: Probability of observing data as extreme or more so under the null hypothesis.
**Permutation Test**: Non-parametric method using label shuffling to assess significance.
**Power (Statistical)**: Probability of correctly rejecting a false null hypothesis.
**Randomization**: Assigning treatments by chance to reduce bias.
**Replication (Experimental)**: Independent observations collected under the same experimental conditions.

## Bioinformatics & Genomics
**Alignment (Sequence)**: Arranging sequences to identify regions of similarity (local vs global).
**Assembler**: Software that reconstructs longer sequences (contigs, scaffolds) from reads.
**Barcode (Molecular)**: Short sequence tag used to demultiplex pooled samples.
**Base Call**: Assignment of a nucleotide identity during sequencing.
**Coverage (Depth)**: Average number of times a nucleotide position is sequenced.
**De novo Assembly**: Constructing a genome or transcriptome without a reference sequence.
**Demultiplexing**: Sorting reads into sample bins based on barcodes.
**GC Content**: Proportion of nucleotides that are G or C in a sequence.
**Homology**: Shared ancestry between sequences or structures.
**Indel**: Insertion or deletion mutation in a sequence.
**K-mer**: Substring of length k used in indexing, assembly, and error correction.
**Mapping Quality (MAPQ)**: Confidence score for the correctness of a read alignment.
**Ortholog**: Genes in different species derived from a common ancestor via speciation.
**Paralog**: Genes related by duplication within a genome.
**Read**: Raw sequence string produced by a sequencing instrument.
**Reference Genome**: Representative genome assembly used for alignment and annotation.
**SNP (Single Nucleotide Polymorphism)**: Single base position with variation among individuals.
**Structural Variant (SV)**: Large-scale genomic alteration (e.g., inversion, translocation, duplication, deletion).
**Transcriptome**: Complete set of RNA transcripts present in a cell or tissue under specific conditions.
**Variant Calling**: Computational identification of sequence differences relative to a reference.

## Transcriptomics & Expression Analysis
**Counts Matrix**: Table of gene (or transcript) features by samples with raw or normalized counts.
**Differential Expression (DE)**: Statistical comparison of expression levels between conditions.
**FPKM/TPM**: Normalization metrics for RNA-seq expression accounting for transcript length and depth.
**Normalization**: Adjusting data to remove technical effects (e.g., library size, composition biases).
**rRNA Depletion**: Removal of ribosomal RNA to enrich for mRNA.
**Splice Variant (Isoform)**: Alternative transcript produced via differential splicing.
**UMI (Unique Molecular Identifier)**: Short random sequence enabling duplicate removal and molecule counting.

## Proteomics & Functional Analysis
**Annotation (Functional)**: Assignment of biological function to sequences (e.g., GO terms).
**Domain (Protein)**: Conserved structural or functional unit within a protein.
**GO (Gene Ontology)**: Structured vocabulary describing gene product function, process, and location.
**Pathway Analysis**: Evaluation of enrichment of genes in known biological pathways.

## Ecological & Fisheries Genomics
**Effective Population Size (Ne)**: Size of an idealized population showing equivalent genetic drift.
**Environmental DNA (eDNA)**: Genetic material obtained directly from environmental samples (water, soil) without isolating organisms.
**Genetic Diversity**: Variation in genetic composition within and among populations.
**Hybridization**: Interbreeding between distinct populations or species.
**Local Adaptation**: Population-level genetic differentiation conferring fitness advantages in a particular environment.
**Population Structure**: Non-random distribution of genetic variation across space or groups.
**Selective Sweep**: Reduction in genetic variation due to recent positive selection.
**Stock (Fisheries)**: Managed unit of a harvested species defined by biological or management criteria.

## Data Management & Sharing
**Checksum**: Fixed-length value (hash) verifying file integrity.
**Data Dictionary**: Structured description of variables, formats, and allowable values.
**FAIR Principles**: Guidelines to make data Findable, Accessible, Interoperable, and Reusable.
**Persistent Identifier (PID)**: Stable reference (e.g., DOI) for a digital object.
**README**: Introductory file documenting repository purpose, structure, and usage.

## Software & Workflow Engineering
**CI (Continuous Integration)**: Automated testing and validation of code changes upon commits or pull requests.
**Issue (Tracker)**: A logged task, bug report, or feature request in a version control platform.
**Linter**: Tool that checks source code for stylistic and syntactic issues.
**Makefile**: Declarative file describing build or workflow rules executed by `make`.
**Module (HPC)**: Managed environment package loaded to configure software paths.
**Notebook (Computational)**: Interactive document mixing code, narrative, and outputs (e.g., Jupyter, R Markdown, Quarto).
**Semantic Versioning (SemVer)**: Versioning scheme MAJOR.MINOR.PATCH indicating compatibility and changes.
**Shell Script**: File containing a sequence of shell commands for batch execution.
**Task Runner / Workflow Engine**: Tool orchestrating pipelines (e.g., Snakemake, Nextflow, CWL, WDL).

## Quality Control (QC) & Validation
**Adapter Trimming**: Removal of sequencing adapters from read ends.
**Contamination**: Presence of unintended sequences or samples in data.
**Error Rate**: Frequency of incorrect base calls or measurements.
**Outlier**: Observation inconsistent with the expected distribution of the data.
**Quality Score (Phred)**: Log-scaled score representing base call accuracy probability.
**Technical Replicate**: Repeated measurement of the same biological material capturing assay variation.

## Visualization & Interpretation
**Heatmap**: Matrix-based visualization using color to encode values.
**Manhattan Plot**: Scatter plot of genomic positions vs statistical significance (e.g., GWAS).
**PCA (Principal Component Analysis)**: Dimensionality reduction method projecting variance into orthogonal components.
**Volcano Plot**: Scatter plot of effect size (e.g., log fold change) vs statistical significance.

## Security & Ethics
**Access Control**: Mechanisms restricting who can view or modify resources.
**De-identification**: Removing or masking personal identifiers from datasets.
**IRB (Institutional Review Board)**: Committee overseeing ethical aspects of research involving humans.
**Sensitive Data**: Information requiring restricted handling due to privacy, ethical, or legal constraints.

## Miscellaneous
**Backlog**: Prioritized queue of pending tasks or issues.
**Idempotent**: Operation that yields the same result if executed multiple times without side effects.
**Latency**: Delay between request initiation and completion.
**Throughput**: Amount of data processed in a given time frame.

---
Contributions: Add new terms via pull request. Keep definitions concise (1–2 sentences) and supply citations if specialized.