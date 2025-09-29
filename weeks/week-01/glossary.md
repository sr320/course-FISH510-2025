# Glossary

FISH 510: Marine Organism Resilience and Epigenetics (Winter 2025)
A living glossary of key concepts, mechanisms, methodologies, and analytical terms used in the study of environmental epigenetics and resilience in marine organisms. Definitions are concise (1–2 sentences). Contributions via pull request are encouraged.

## 1. Core Epigenetic Concepts
**Epigenetics**: Study of heritable (cell or organism-level) changes in gene function not caused by alterations in DNA sequence.  
**Epigenome**: The complete set of epigenetic marks (e.g., DNA methylation, histone modifications, chromatin accessibility) in a cell at a given time.  
**Epigenetic Mechanism**: Molecular process (e.g., DNA methylation, histone modification, non-coding RNA) regulating chromatin state and gene expression.  
**Chromatin**: DNA–protein complex (primarily histones) that packages the genome and modulates accessibility.  
**Nucleosome**: Fundamental chromatin unit—~147 bp of DNA wrapped around a histone octamer.  
**Histone**: Core proteins (H2A, H2B, H3, H4) forming the nucleosome; subject to post-translational modification.  
**Histone Modification**: Chemical alteration (e.g., acetylation, methylation, phosphorylation) of histone tails influencing chromatin structure and transcription.  
**DNA Methylation (5mC)**: Addition of a methyl group to cytosine (often at CpG sites) affecting gene regulation and genome stability.  
**Hydroxymethylcytosine (5hmC)**: Oxidized derivative of 5mC involved in active demethylation and regulatory processes.  
**CpG**: Cytosine-phosphate-Guanine dinucleotide; hotspot for DNA methylation in many eukaryotes.  
**CpG Island**: GC-rich, CpG-enriched genomic region often associated with promoters.  
**Non-CpG Methylation**: Methylation at CHG or CHH contexts (H = A/C/T); more common in plants and some animal tissues.  
**Chromatin Remodeling**: ATP-dependent repositioning or restructuring of nucleosomes altering accessibility.  
**Chromatin Accessibility**: Degree to which DNA is open for binding (often assayed by ATAC-seq).  
**Epiallele**: Genomic locus with distinct, stable epigenetic states among individuals or cells.  
**Epimutation**: Aberrant or spontaneous change in an epigenetic mark that may affect phenotype.  
**Transgenerational Epigenetic Inheritance**: Transmission of epigenetic states across generations beyond direct exposure.  
**Intergenerational Effect**: Parental exposure effect observable in immediate offspring (often still involving direct germline/environment interaction).  
**Developmental Programming**: Early-life epigenetic setting influencing long-term phenotype or stress tolerance.  
**Plasticity (Phenotypic)**: Ability of a genotype to produce different phenotypes across environments.  
**Canalization**: Reduction of phenotypic variation despite environmental or genetic perturbation.  
**Resilience (Biological)**: Capacity to resist, absorb, or recover from environmental stress while maintaining function.  
**Acclimation**: Reversible, non-genetic physiological adjustment to changing environment.  
**Adaptation**: Heritable change improving fitness under specific environmental conditions.  
**Carryover Effect**: Past environmental exposure influencing performance in a future life stage.  

## 2. Environmental Stressors & Marine Context
**Thermal Stress**: Physiological strain caused by elevated or fluctuating temperature regimes.  
**Ocean Acidification (OA)**: Decrease in seawater pH due to CO2 absorption altering carbonate chemistry.  
**Hypoxia**: Reduced dissolved oxygen levels impairing metabolism and survival.  
**Salinity Stress**: Osmotic challenge due to deviation from optimal salinity.  
**pH Fluctuation**: Short-term variability in seawater pH impacting acid-base balance.  
**Oxidative Stress**: Imbalance favoring reactive oxygen species over antioxidant defenses.  
**Multi-stressor Exposure**: Simultaneous or sequential environmental challenges with interactive effects.  
**Sublethal Stress**: Exposure insufficient to cause mortality but influencing physiology or fitness.  
**Environmental Gradient**: Spatial or temporal variation in a key abiotic factor (e.g., pH, temperature).  
**Selective Pressure**: Environmental factor influencing differential survival or reproduction.  

## 3. Genomic & Regulatory Features
**Promoter**: Region upstream (or proximal) to a transcription start site influencing initiation.  
**Enhancer**: Distal regulatory element increasing transcription of target genes in a context-dependent manner.  
**Gene Body Methylation (GBM)**: Methylation within transcribed regions; in some taxa associated with constitutive expression.  
**Differentially Methylated Cytosine (DMC)**: Single CpG (or site) showing statistically significant methylation difference between groups.  
**Differentially Methylated Region (DMR)**: Contiguous genomic region with coordinated methylation change.  
**Regulatory Element**: DNA sequence modulating transcription factor binding and gene expression.  
**Non-coding RNA (ncRNA)**: RNA molecules (miRNA, lncRNA, piRNA) with regulatory functions but not translated.  
**Small RNA**: Short regulatory RNA class (e.g., miRNA, siRNA) influencing post-transcriptional regulation.  
**Long Non-coding RNA (lncRNA)**: >200 nt RNA with roles in chromatin remodeling, scaffolding, or transcriptional regulation.  

## 4. Experimental Techniques & Assays
**WGBS (Whole Genome Bisulfite Sequencing)**: Base-resolution genome-wide DNA methylation profiling using bisulfite conversion.  
**RRBS (Reduced Representation Bisulfite Sequencing)**: Enrichment-based bisulfite method focusing on CpG-rich fragments.  
**Bisulfite Conversion**: Chemical treatment converting unmethylated cytosines to uracils for methylation inference.  
**OxBS / TAB-seq**: Modified bisulfite strategies distinguishing 5mC from 5hmC.  
**MBD-seq / MeDIP-seq**: Enrichment-based methods capturing methylated DNA via binding proteins or antibodies.  
**ChIP-seq**: Chromatin immunoprecipitation sequencing identifying protein or histone modification binding sites.  
**CUT&RUN / CUT&Tag**: Targeted chromatin profiling techniques with lower background than traditional ChIP-seq.  
**ATAC-seq**: Assay for Transposase-Accessible Chromatin mapping open chromatin regions.  
**RNA-seq**: Sequencing-based transcript quantification for expression analysis.  
**Small RNA-seq**: Sequencing library targeting regulatory small RNAs (e.g., miRNAs).  
**qPCR / RT-qPCR**: Quantitative amplification used for validation of expression or enrichment.  
**ddPCR (Digital Droplet PCR)**: Partitioned amplification enabling absolute quantification of target molecules.  
**LC-MS/MS (Histone PTM Profiling)**: Mass spectrometry approach to quantify histone post-translational modifications.  
**Multi-omics Integration**: Combined analysis of datasets (e.g., methylome + transcriptome + proteome) to infer regulatory interactions.  

## 5. Bioinformatics & Data Processing
**Read Alignment**: Mapping sequencing reads to a reference genome or assembly.  
**Bisulfite Aligner**: Specialized aligner (e.g., Bismark) accounting for C-to-T conversions.  
**Reference Genome / Draft Assembly**: Baseline sequence used for mapping; draft may contain gaps or scaffolding uncertainties.  
**Coverage (Depth)**: Average number of reads covering a genomic position; influences confidence in methylation calls.  
**Conversion Rate**: Proportion of unmethylated cytosines successfully converted during bisulfite treatment (quality metric).  
**Beta Value / Methylation Proportion**: Fraction of reads at a cytosine supporting methylation (mC / total).  
**Filtering (Coverage Threshold)**: Removal of sites with insufficient read depth to reduce noise.  
**Batch Effect**: Unwanted variation associated with processing groups (e.g., lane, date).  
**Normalization**: Adjusting data to reduce technical bias while preserving biological signal.  
**Feature Annotation**: Assigning genomic features (promoter, exon, intergenic) to coordinates.  
**Genome Annotation**: Identification of genes, transcripts, and functional elements in a sequence assembly.  
**Pipeline (Workflow)**: Ordered, reproducible sequence of computational steps.  
**Containerization**: Packaging software and dependencies for reproducible execution (e.g., Docker, Apptainer).  

## 6. Statistical & Analytical Concepts
**Experimental Unit**: The smallest entity that can be independently assigned a treatment.  
**Replication (Biological)**: Independent samples capturing natural variation.  
**Technical Replicate**: Repeat measurement of the same biological material capturing assay variance.  
**Randomization**: Allocation of samples to treatments without systematic bias.  
**Blocking**: Grouping similar experimental units to control nuisance variation.  
**Power (Statistical)**: Probability of detecting a true effect given design parameters.  
**False Discovery Rate (FDR)**: Expected proportion of false positives among declared significant tests.  
**Multiple Testing Correction**: Adjustment (e.g., Benjamini-Hochberg) controlling error inflation.  
**Effect Size**: Magnitude of a measured difference or association.  
**Overdispersion**: Greater variance than expected under a nominal distribution (e.g., binomial), relevant for methylation counts.  
**Gene-by-Environment Interaction (GxE)**: Differential phenotypic effect of genotype across environmental conditions.  
**Heritability (h²)**: Proportion of phenotypic variance attributable to additive genetic variance.  
**Reaction Norm**: Pattern of phenotypic expression of a genotype across environments.  

## 7. Marine Life History & Development
**Gametogenesis**: Formation and maturation of gametes (eggs, sperm).  
**Embryogenesis**: Early developmental phase from fertilization to larval stages.  
**Larval Stage**: Dispersive, often planktonic life phase preceding settlement.  
**Metamorphosis**: Transition from larval to juvenile/adult form involving morphological and regulatory shifts.  
**Settlement**: Process by which a larva adopts a benthic or sessile lifestyle.  
**Maternal Effect**: Influence of maternal phenotype or provisioning on offspring traits.  
**Paternal Effect**: Influence of paternal factors (e.g., sperm epigenome) on offspring phenotype.  

## 8. Resilience & Evolutionary Dynamics
**Epigenetic Variation**: Diversity in epigenetic marks among individuals or populations.  
**Standing Genetic Variation**: Pre-existing genomic diversity enabling adaptive response.  
**Adaptive Potential**: Capacity of a population to evolve in response to selection.  
**Selective Sweep**: Reduction in variation following fixation of an advantageous allele.  
**Local Adaptation**: Enhanced fitness of a population in its native environment relative to non-local populations.  
**Fitness**: Reproductive success and contribution to subsequent generations.  
**Tolerance Threshold**: Environmental magnitude beyond which performance declines sharply.  

## 9. Data Stewardship & Reproducibility
**Metadata**: Structured descriptors of samples, protocols, instruments, and processing steps.  
**Data Provenance**: Traceable lineage of data transformations.  
**Checksum**: Hash value verifying data integrity.  
**FAIR Principles**: Guidelines to ensure data are Findable, Accessible, Interoperable, Reusable.  
**Version Control**: System (e.g., Git) tracking file changes over time.  
**Open Science**: Practices promoting transparency, accessibility, and reuse of research outputs.  
**Notebook (Computational)**: Interactive, documented analysis environment (e.g., Jupyter, R Markdown, Quarto).  

## 10. Ethical & Societal Considerations
**De-identification**: Removal or masking of personal or sensitive identifiers.  
**Sensitive Species Data**: Location or biological data requiring restricted dissemination to prevent exploitation.  
**Benefit Sharing**: Equitable distribution of advantages arising from biological or genomic research.  
**Indigenous Knowledge (IK)**: Culturally embedded environmental knowledge systems; requires respectful, consent-based integration.  

## 11. Quality Control (QC)
**Adapter Trimming**: Removal of sequencing adapters from read ends.  
**Quality Score (Phred)**: Log-scaled probability that a base call is incorrect.  
**Contamination**: Presence of exogenous or unintended DNA sequences in a dataset.  
**Outlier Sample**: Sample deviating markedly from cohort distribution (may reflect biology or artifact).  
**Conversion Efficiency (Bisulfite)**: Proportion of unmethylated cytosines converted; low efficiency biases methylation upward.  
**Duplication Rate**: Fraction of reads representing PCR or optical duplicates.  

## 12. Visualization & Interpretation
**Heatmap**: Matrix visualization encoding values (e.g., methylation proportions) via color gradients.  
**Volcano Plot**: Scatter plot of effect size vs significance (e.g., log2 fold change vs -log10 p-value).  
**PCA (Principal Component Analysis)**: Ordination method summarizing major axes of variance.  
**Manhattan Plot**: Genomic coordinate vs statistical metric plot (adapted for epigenome scans).  
**Genome Browser Track**: Visual representation of aligned reads or features across genomic coordinates.  

## 13. Miscellaneous & Operational
**Pipeline Orchestration**: Automated coordination of multi-step analyses (e.g., Snakemake, Nextflow).  
**Container**: Reproducible software environment encapsulating dependencies.  
**Module (HPC)**: Managed environment configuration enabling software loading.  
**Idempotent Step**: Analysis step producing identical results upon re-execution without side effects.  
**Backlog**: Prioritized list of pending tasks or enhancements.