# Quality-Guided Fusion of Semantic Network-Flow Views for Forensic Intrusion Analysis

**Research repository:** `Quality-Guided-Forensic-Fusion`  
**Associated manuscript:** *Quality-Guided Fusion of Semantic Network-Flow Views for Forensic Intrusion Analysis*  
**Status:** Research artifact; public-release and independent reproduction checks are pending.

## Overview

This repository contains the research code, selected experimental artifacts, and documentation supporting a study of **quality-guided fusion of semantic network-flow views for forensic intrusion analysis**. The workflow examines network-flow evidence through multiple representations and investigates how view quality can inform evidence fusion and subsequent intrusion analysis.

The repository is intended to make the experimental workflow inspectable and to support reproduction where source data, dependencies, and execution environments are available. **The presence of a script or saved result does not by itself establish that a reported experiment has been independently reproduced.**

## Repository contents

The publication copy retains the original experimental folder organization where files are included:

```text
Quality-Guided-Forensic-Fusion/
├── Code/                         # Data preparation, modeling and evaluation scripts
├── Data/                         # Included data files and metadata, where redistributable
├── Results/                      # Included experiment outputs and reports
├── SASP/                         # Additional framework-specific experimental artifacts
├── tools/                        # Repository checks and maintenance utilities, if installed
├── README.md
├── CITATION.cff                  # Citation metadata, after author/DOI verification
├── requirements.txt              # Preliminary dependencies; verify before reproduction
├── .gitignore
├── DATA_AVAILABILITY.md
├── REPRODUCIBILITY.md
├── EXPERIMENTS.md
├── EXTERNAL_STORAGE.md
├── LARGE_FILES_MANIFEST.csv
├── COPY_MANIFEST.csv
└── EXCLUDED_FILES_MANIFEST.csv
```

Some documentation or manifest files may be absent until the corresponding repository preparation step has been completed. The directory tree above is a **target layout**, not a guarantee that every listed file is present in a particular checkout.

## Experimental workflow

The existing code inventory identifies the following **candidate** entry points:

| Stage | Candidate script |
|---|---|
| Dataset acquisition | `Code/01_phase1_acquire_datasets.py` |
| File integrity verification | `Code/02_phase2_step1_file_verification.py` |
| Dataset cleaning | `Code/03_phase2_step2_clean_datasets.py` |
| Baseline modeling | `Code/04_experiment_01_baseline_models.py` |
| Original-feature evaluation | `Code/05_experiment_02_1_original_features.py` |
| Semantic/multi-view evidence representation | `Code/06_experiment_02_2_forensic_evidence_representation.py` |
| Fusion framework validation | `Code/07_experiment_03_ferf_validation.py` |
| Ablation experiments | `Code/08_experiment_04_ablation.py` |
| Cross-dataset evaluation | `Code/09_experiment_05_cross_dataset_validation.py` |
| Computational efficiency | `Code/10_experiment_06_computational_efficiency.py` |
| Statistical analysis | `Code/11_experiment_07_statistical_analysis.py` |
| Final result compilation | `Code/12_experiment_08_final_results.py` |

**Important:** Several scripts have corrected or alternative versions. These filenames were identified from a repository inventory, not from a verified end-to-end execution. Review `EXPERIMENTS.md` and `REPRODUCIBILITY.md`, inspect script parameters and paths, and identify the exact versions associated with the manuscript before running the pipeline or interpreting its outputs.

## Getting started

### 1. Obtain the repository

Clone the published repository using its verified GitHub address, or download the corresponding tagged release. The GitHub URL will be added here after publication.

### 2. Create a Python environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The supplied `requirements.txt` was assembled from inferred imports and **has not been validated as a pinned, complete reproduction environment**. Check the original environment and package versions before executing experiments. Individual scripts may also depend on system utilities or dataset-specific tooling.

### 3. Obtain the required data

Consult `DATA_AVAILABILITY.md`, `EXTERNAL_STORAGE.md`, and `LARGE_FILES_MANIFEST.csv`. Large experimental files were intentionally excluded from the GitHub staging copy. Restore them to the expected relative paths **only when their provenance, license, and access permissions permit it**.

### 4. Inspect the workflow before execution

Review the relevant source file and its path/configuration assumptions. Do not run the full numbered sequence without first resolving alternative script versions, dataset paths, resource requirements, and expected outputs.

## Data and large-file policy

The original experimental directory was inventoried at approximately **109.68 GB** across **3,489 files**. The GitHub staging process was configured to omit files **larger than 25 MiB** and to record those exclusions in `LARGE_FILES_MANIFEST.csv`. Additional files may be excluded for safety or publication reasons.

Excluded experimental files remain in the original local `Experiments/` directory; a separate SharePoint location has been proposed for large-file access. **Availability through SharePoint is not guaranteed**: access permissions, long-term persistence, and reviewer accessibility must be checked independently.

The source-data collections referenced in the experimental structure include **BoT-IoT, CICIDS2017, CSE-CIC-IDS2018, and UNSW-NB15**. The inclusion of their names here does not imply that their complete datasets are redistributed in this repository or that their third-party licenses permit redistribution.

## Results and scientific interpretation

The `Results/` directory contains the selected outputs included in the publication copy. To connect any reported result to a manuscript table or figure, verify:

- the exact script revision and configuration;
- input dataset version, partitioning, and preprocessing;
- random seeds and software/hardware environment;
- output filenames and checksums; and
- consistency between generated metrics and the final manuscript.

Until these checks are completed, saved artifacts should be treated as **research outputs requiring verification**, not as independently certified results.

## Reproducibility and provenance

See:

- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — preliminary execution order and unresolved verification tasks.
- [`EXPERIMENTS.md`](EXPERIMENTS.md) — experiment-to-script index.
- [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) — data sources, restrictions, and access.
- [`EXTERNAL_STORAGE.md`](EXTERNAL_STORAGE.md) — external storage details.
- [`LARGE_FILES_MANIFEST.csv`](LARGE_FILES_MANIFEST.csv) — files excluded due to the size threshold.
- [`COPY_MANIFEST.csv`](COPY_MANIFEST.csv) and [`EXCLUDED_FILES_MANIFEST.csv`](EXCLUDED_FILES_MANIFEST.csv) — staging provenance, when generated.

The public copy should not include credentials, confidential information, or restricted packet captures.

## License

**License selection must be finalized before release.** The intended options discussed for original research materials are **Creative Commons Attribution 4.0 International (CC BY 4.0)** or **CC0 1.0 Universal**. For original executable software, a dedicated software license (such as MIT) is generally more appropriate than a Creative Commons content license.

Do **not** assume that the selected license applies to third-party datasets, software, or materials. Those retain their respective terms. Add the final `LICENSE` file and state the exact scope of each license here after confirming ownership and permissions.

## Citation

If you use this research artifact, please cite the associated paper and the archived software release once its bibliographic details and DOI are available. `CITATION.cff` should contain verified authors, title, version, repository address, and DOI; do not cite placeholders as final metadata.

**Paper:** *Quality-Guided Fusion of Semantic Network-Flow Views for Forensic Intrusion Analysis*  
**Repository:** `Quality-Guided-Forensic-Fusion`  
**DOI:** Pending verified Zenodo release.

## Release checklist

Before creating a GitHub release and Zenodo archive, confirm that (1) the chosen source files correspond to the manuscript, (2) dependencies and reproduction commands have been tested, (3) datasets and included artifacts may legally be shared, (4) external-file access has been tested, (5) manifests accurately describe the release, (6) no sensitive files remain, and (7) licensing and citation metadata are final.

---

*This README documents the repository structure and intended use based on the available inventory. It does not assert that the full pipeline has been independently executed or that all external datasets are publicly accessible.*
