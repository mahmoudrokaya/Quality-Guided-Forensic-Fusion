# Reproducibility Guide

**Status: preliminary.** The source inventory establishes filenames and folder structure but does not verify that the full workflow executes successfully or reproduces the final manuscript metrics.

## Environment

1. Install a Python version compatible with the actual source code.
2. Create a fresh environment and install packages from `requirements.txt`.
3. Record exact dependency versions (`python -m pip freeze > environment_freeze.txt`) after a successful run.
4. Review all scripts for hard-coded Windows paths, required executables, GPU needs, and dataset-specific configurations.

## Candidate experimental sequence

| Stage | Candidate source file |
|---|---|
| Data acquisition | `Code/01_phase1_acquire_datasets.py` |
| File integrity | `Code/02_phase2_step1_file_verification.py` |
| Cleaning | `Code/03_phase2_step2_clean_datasets.py` |
| Baselines | `Code/04_experiment_01_baseline_models.py` |
| Original features | `Code/05_experiment_02_1_original_features.py` |
| Semantic evidence | `Code/06_experiment_02_2_forensic_evidence_representation.py` |
| Fusion validation | `Code/07_experiment_03_ferf_validation.py` |
| Ablation | `Code/08_experiment_04_ablation.py` |
| Cross-dataset | `Code/09_experiment_05_cross_dataset_validation.py` |
| Efficiency | `Code/10_experiment_06_computational_efficiency.py` |
| Statistics | `Code/11_experiment_07_statistical_analysis.py` |
| Results compilation | `Code/12_experiment_08_final_results.py` |

These are **candidate** entry points, not tested commands. Some steps have alternative or corrected script versions; select and document the versions used for the paper before attempting reproduction.

## Input restoration

Consult `DATA_AVAILABILITY.md`, `EXTERNAL_STORAGE.md`, and `LARGE_FILES_MANIFEST.csv`. Restore authorized data to the original relative paths as required by the scripts.

## Verification checklist

- Document exact scripts, arguments, random seeds, train/test splits, and preprocessing.
- Verify participant/flow/file separation and any leakage controls relevant to the study.
- Compare newly generated metrics with the manuscript tables and figures.
- Record checksums for external inputs and generated outputs.
- Archive an environment specification and a tagged source release.

Do not claim that results are independently reproduced until these checks have been completed.
