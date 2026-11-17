# YAML Record Review: uncultured gamma proteobacterium TIHP368-74b

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_74b.yaml`
- Started UTC: 2026-10-04T05:31:07Z
- Finished UTC: 2026-10-04T05:31:53Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103316`, uncultured gamma proteobacterium TIHP368-74b: species rank, BACTERIA, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its only attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_74b.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_74b.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched full backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18425`, name-catalog shard 0000 row 38443, PATHS row 13364 and scope row 144085 agree. Live NCBI Taxonomy EFetch and Datasets confirm exact label, species rank, parent 50423, genetic code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103316&retmode=xml)

Suffix b is retained as part of the exact clone designation. No synonymy or biological equivalence with TIHP368-74a is inferred. Species rank is carried from NCBI, not independently inferred from the short marker or treated as proof of nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869754. Directly resolved AB031660.1 is a 144 bp partial 16S rRNA sequence whose source qualifiers identify taxon:103316, clone TIHP368-74b, environmental_sample and coastal marine sediment. It is a short marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031660.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims or a new taxonomic placement.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count agrees with the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103316, TIHP368-74b/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 39 matching lines and their structured contexts were inspected. Separate SOURCE.json scans found two BacDive request matches and an unrelated StrainInfo byte count. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103316 denotes Leuconostoc pseudomesenteroides strain 39, BacDive 6833, with species taxid 33968 and strain taxid 935295. LPSN 777558, NCBI type-material, GOLD Go0272803 and SI-ID 3524 with own SI-DP 152445 concern that culture. Native BacDive says type strain yes, while the extracted BacDive inventory has flag 0; this unrelated discrepancy was preserved rather than resolved. The NCBI strain synonym, LPSN AB023237 and deposit-linked partial tmRNA record AF375570 do not support TIHP368-74b.

BacDive 103316 itself is Agromyces sp. ST031454/51513. CP103316 belongs to Klebsiella pneumoniae hvKP12/GCA_024762135.1, represented by two BV-BRC records. Other excluded genome collisions include uncultured Elusimicrobium sp. MGBC103316/GCA_948695725.1, uncultured bacterium MarMAG_103316/GCA_977221505.1, Pseudomonas aeruginosa PSA-BAB-IMI-103316/GCA_023904915.1, Shigella sonnei PNUSAE103316/GCA_023827855.1 and Salmonella enterica PNUSAS103316/GCA_016240015.1. Prolixibacteraceae bacterium GCA_964905535.1 has assembly name PELAGICS-MAG-m2-bin103316-CADAX-SM-03sep20 and an isolate string with an additional trailing period; neither is the clone. ATB DRR103316 belongs to E. coli sample SAMD00077724. Unrelated assembly statistics and Haemophilus/Staphylococcus SeqKit-checksum substrings do not establish identity. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Future enrichment should preserve exact environmental-clone identity and represent AB031660.1 only as directly sourced marker evidence. Do not infer a biological relationship to 74a, adjacent accessions, cultivated strains, genomes, type material or phenotypes from naming similarity.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103316 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's type-flag discrepancy is outside this record's scope; future correction would belong to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
