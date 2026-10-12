# YAML Record Review: uncultured gamma proteobacterium TIHP302-34

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_34.yaml`
- Started UTC: 2026-10-04T04:36:11Z
- Finished UTC: 2026-10-04T04:36:51Z
- Verdict: pass

## Target

The full generated `TaxonRecord` denotes `NCBITaxon:103288`, uncultured gamma proteobacterium TIHP302-34, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`. It carries seven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. NCBITAXON is its sole attestation, 1 NAME with snapshot date 2026-09-13. Its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained upstream source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_34.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_34.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Source/API checks are evidence audits rather than corpus-reproduction gates.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone row `data/raw/ncbitaxon_taxa.tsv:18397`, `data/catalog/ncbi_names-0000.jsonl.gz:38415`, PATHS row 13334 and scope row 144057 agree on this exact clone-named taxon. Live NCBI EFetch and Datasets confirm the preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The environmental-samples ancestor is beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103288&retmode=xml)

Species rank supports inclusion in this repository; it does not imply nomenclatural publication, culture availability or a type strain. No synonym or formal binomial claim is present. Adjacent TIHP302 clone designations do not denote the same taxon.

## Evidence

The pinned backbone/name catalog and live taxonomy support the NCBITAXON NAME attestation and exact grounding. Exact-taxid Nuccore ESearch returned one entry, UID 5869713, whose source qualifiers and reference metadata were inspected. AB031619.1 is a 788 bp partial 16S rRNA sequence with explicit taxon:103288, clone TIHP302-34, environmental_sample and coastal-marine-sediment qualifiers. It is a marker sequence, not an assembly or registered deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031619.1)

The sequence reference metadata attributes an unpublished coastal-community study using 16S and quinone profiling to Urakawa, Yoshida, Nishimura and Ohwada. A separate direct submission is dated 1999-08-25. These entries supply no PMID/DOI; the YAML claims no publication. Neither the study title nor marker metadata establishes a clone-specific metabolic phenotype.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query is consistent with marker-only evidence; it is not a universal claim that an assembly cannot exist under another identifier.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory entry, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Optional strains, mappings and nomenclature are appropriately empty. Zero strain_count follows the BacDive-subtree definition, not a general biological absence claim.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103288, TIHP302-34/underscore spelling and the target stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 22 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; two request matches are in the BacDive identifier namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within those bounds.

Inspected collisions were excluded:

- BacDive 103288 is Agromyces sp. ST000977, taxid 51513. CIP 103288 instead appears on BacDive 138112, Bibersteinia trehalosi 47735, alongside CIP 104864 and NCTC 11549.
- SI-DP 103288 is ATCC 23848 of Escherichia coli 562, in SI-ID 38262. DSM 103288 is the phage deposit 904837 in SI-ID 398153, labeled Escherichia phage vB_EcoM-WFK. Neither is this environmental taxon.
- CP103288 occurs on Pseudarthrobacter sp. NS4 source records, including GCA_024758005.1 and BV-BRC taxid 2973976 entries. KY103288 occurs in the Debaryomyces robertsiae SI-ID 76185 sequence context.
- MGBC103288 is an Alphaproteobacteria 91750 assembly, GCA_948711835.1. Shigella flexneri isolate 103288 is GCA_026020715.1. ATB run DRR103288 belongs to Escherichia coli sample SAMD00077696, not TIHP302-34.

No gene, pathway, resistance, expression-module or causal-graph assertion is present. Empty functional fields are appropriate; iModulonDB is not applicable and its non-use is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and evidence scope.

## Recommended Edits

None required. Future enrichment should preserve the environmental-clone identity and treat AB031619.1 only as marker evidence with its exact source qualifiers. Do not attach the unrelated CIP/BacDive/StrainInfo deposits, assemblies or ATB runs by numeric substring, and do not infer phenotype from the community-study context.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103288 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact sequence/taxon links before adding marker evidence, and run corpus-wide gates before a broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving prior reports.
