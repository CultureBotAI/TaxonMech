# YAML Record Review: uncultured gamma proteobacterium TIHP302-38

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_38.yaml`
- Started UTC: 2026-10-04T04:44:02Z
- Finished UTC: 2026-10-04T04:44:42Z
- Verdict: pass

## Target

The full generated `TaxonRecord` denotes `NCBITaxon:103293`, uncultured gamma proteobacterium TIHP302-38, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`. It has seven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. NCBITAXON is the sole attestation, 1 NAME, snapshot 2026-09-13. Its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_38.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_38.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18402`, name-catalog shard 0000 row 38420, PATHS row 13339 and scope row 144062 agree on this exact clone-named taxon. Live NCBI EFetch and Datasets confirm the label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103293&retmode=xml)

The carried species rank supports inclusion without claiming nomenclatural publication, cultivation or type-strain status. No extra synonym or formal binomial identity is asserted.

## Evidence

The pinned backbone/name row and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869718; its source qualifiers and reference metadata were inspected. AB031624.1 is an 819 bp partial 16S rRNA sequence with explicit taxon:103293, clone TIHP302-38, environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not a genome assembly or registered deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031624.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, plus a separate direct submission dated 1999-08-25. The entries supply no PMID/DOI, and the YAML cites no publication. This community context does not establish a clone-specific phenotype.

Exact-taxid Assembly ESearch returned zero entries with a phrase-not-found/no-items warning. This bounded live-query result agrees with the inspected marker-only context; it is not a universal genome-absence claim.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, nomenclature, mappings and functional fields are appropriate. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103293, TIHP302-38/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 36 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; their two BacDive request matches concern that source's own numeric ID. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103293 is an excluded culture collision: Pasteurella dagmatis SDH 953/60, BacDive 11735, strain taxid 667128 under species 754, also ATCC 43325/DSM 22969/NCTC 11617. LPSN 784581, GOLD Go0612126 and StrainInfo SI-ID 41774/own deposit 153711 concern that culture/species. Its type-material and AY702497 sodA evidence do not belong to TIHP302-38. Species-level versus strain-level source classifications were kept distinct.

Other excluded matches include BacDive 103293, Agromyces sp. ST001921/51513; CP103293 in Limosilactobacillus fermentum LfU21 GOLD analysis context; Escherichia coli PNUSAE103293/GCA_023758875.2 and earlier .1; Muribaculaceae MGBC103293/GCA_948687095.1; Flavobacterium PELAGICS-MAG-m2-bin103293/GCA/GCF_964967385.1; and Acidaminobacteraceae MarMAG_103293/GCA_977594355.1. ATB DRR103293 belongs to Escherichia coli sample SAMD00077701. Unrelated GTDB assembly statistics containing these digits are not identity claims.

No gene, resistance, pathway, expression-module or causal-graph assertion is present. iModulonDB is not applicable, not negative evidence; marker context alone does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve the environmental-clone identity and represent AB031624.1 only as directly sourced marker evidence. Do not attach unrelated cultures, type-strain evidence or genomes by numeric substring, and do not infer phenotype from the community-study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103293 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results.

No YAML, maintained input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
