# Data Availability

This repository supports the manuscript **Quality-Guided Fusion of Semantic Network-Flow Views for Forensic Intrusion Analysis**.

## Data sources

The original experiment inventory contains paths referencing BoT-IoT, CICIDS2017, CSE-CIC-IDS2018, and UNSW-NB15. These are third-party research datasets; their original licenses, download conditions, and citation requirements apply. Inclusion of a dataset name in the folder structure does not mean that the full dataset is redistributed here.

## Included and excluded files

The GitHub staging workflow uses a **25 MiB (26,214,400-byte)** per-file threshold. `LARGE_FILES_MANIFEST.csv` is populated from the **original source inventory** and identifies files above this threshold. `COPY_MANIFEST.csv` identifies **candidate files within the size limit**, not verified copies. `EXCLUDED_FILES_MANIFEST.csv` records size-based exclusions and additional publication exclusions, where known.

Large files were planned to remain outside GitHub, with a Taif University SharePoint folder proposed for storage. **External accessibility has not been verified**. See `EXTERNAL_STORAGE.md`.

## Access and reuse

Before release, confirm: (1) each dataset's provenance and permitted redistribution, (2) whether any packet captures or logs contain sensitive data, (3) which large files can be accessed by independent reviewers, and (4) whether data are persistently archived. Do not present a private SharePoint location as public access.

## Data citation

Cite the original dataset publications and providers in addition to the associated paper. Insert exact verified dataset references in the final release documentation.
