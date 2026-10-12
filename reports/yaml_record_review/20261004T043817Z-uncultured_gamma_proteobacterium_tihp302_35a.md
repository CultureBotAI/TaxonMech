# YAML Record Review: uncultured gamma proteobacterium TIHP302-35a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_35a.yaml`
- Started UTC: 2026-10-04T04:37:35Z
- Finished UTC: 2026-10-04T04:38:17Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103289`, uncultured gamma proteobacterium TIHP302-35a. Its rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It has seven root-first ancestors, zero BacDive strains and a sole NCBITAXON attestation of 1 NAME, snapshot 2026-09-13. The seed event is dated 2026-09-13T17:54:04Z.

Future fixes belong to maintained source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_35a.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_35a.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Native-source and live API checks are evidence audits, not corpus-reproduction substitutes.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18398`, `data/catalog/ncbi_names-0000.jsonl.gz:38416`, PATHS row 13335 and scope row 144058 agree on this exact target. Live NCBI EFetch and Datasets confirm the preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The environmental-samples parent sits below Gammaproteobacteria and is not a genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103289&retmode=xml)

The species rank is source-carried and supports repository inclusion; it does not assert valid nomenclatural publication, cultivation or a type strain. The complete clone suffix 35a is preserved. No synonym, type-strain or formal binomial claim is made.

## Evidence

The pinned backbone/name row and live taxonomy support the NCBITAXON NAME attestation and exact grounding. Exact-taxid Nuccore ESearch returned one record, UID 5869714, and its source qualifiers and reference metadata were inspected. AB031620.1 is a 468 bp partial 16S rRNA sequence with explicit taxon:103289, clone TIHP302-35a, environmental_sample and coastal-marine-sediment qualifiers. It is a marker sequence, not a genome assembly or registered deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031620.1)

The reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, plus a separate direct submission dated 1999-08-25. No PMID/DOI appears in those entries, and the YAML cites no publication. A community-study title does not establish clone-specific metabolic or quinone activity.

Exact-taxid Assembly ESearch returned zero entries with a phrase-not-found/no-items warning. This bounded result agrees with the inspected marker-only context; it is not evidence that no genome could exist under another identifier.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory entry, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Optional strains, mappings, nomenclature and functional fields are appropriately empty. Zero strain_count is the BacDive-subtree count, not a universal biological absence claim.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103289, TIHP302-35a/underscore spelling and the full target stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 37 matched lines and their structured contexts were inspected. SOURCE.json files were separately scanned; their two BacDive request matches concern that database's own numeric ID. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within those bounds.

Inspected namespace/subsequence collisions were kept separate:

- BacDive 103289 is Agromyces sp. ST000955(HKI), GT19991135, taxid 51513.
- CIP 103289 belongs to Mannheimia haemolytica G 1, taxid 75985, BacDive 137240, with NCTC 10643. Its GOLD Go0224079 and StrainInfo SI-ID 69229/own SI-DP 152599 also refer to that culture, not TIHP302-35a.
- DSM 103289 is phage deposit 908458 in SI-ID 401515, labeled Escherichia phage vB_EcoM_WfaE185. The source strain record's broad Viruses taxonomy is not a link to this bacterium.
- CP103289 occurs in Cellulomonas sp. NS3 source records, including GCA_024757985.1 and BV-BRC taxid 2973977. KY103289 occurs in Debaryomyces robertsiae SI-ID 178463.
- Pediococcus acidilactici SRCM 103289 is GCA/GCF_004054355.1; Alistipes MGBC103289 is GCA_948682575.1; Escherichia coli PNUSAE103289 is GCA_023670685.1; Listeria monocytogenes FLAG-103289 is GCA_050885305.1.
- ATB DRR103289 belongs to Escherichia coli sample SAMD00077697. Unrelated GTDB assembly statistics containing 103289 are not taxon-ID assertions.

No gene, pathway, resistance, expression-module or causal-graph assertion is present. iModulonDB is not applicable, not negative evidence; marker context alone does not justify functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and evidence scope.

## Recommended Edits

None required. Future enrichment should preserve the exact environmental-clone identity and retain AB031620.1 as marker evidence only, with its source taxon/clone qualifiers. Do not transfer unrelated culture, GOLD, StrainInfo, genome or ATB links through matching digits, and do not infer a phenotype from the study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103289 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm sequence identity at its authority before adding marker evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Sequence-source and reference metadata were inspected without claiming access to unpublished study results.

No YAML, maintained input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, and earlier reports were preserved.
