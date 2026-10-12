# YAML Record Review: uncultured bacterium TIHP302-29

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_tihp302_29.yaml`
- Started UTC: 2026-10-04T06:04:36Z
- Finished UTC: 2026-10-04T06:05:21Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103329`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero strains, one NCBITAXON NAME
attestation and one seed event. It denotes environmental clone TIHP302-29.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_bacterium_tihp302_29.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_bacterium_tihp302_29.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Structured comparisons passed for identity, complete lineage, synonyms,
  attestations, scope and seed-event text. Exact type-material, merged and
  dropped scans found no target rows; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, history/provenance/product gates and rendering.
  Focused source checks do not substitute for these gates.

## Identity and Grounding

Backbone row 18438 and native scientific-name row 38456 in
`data/catalog/ncbi_names-0000.jsonl.gz` match the YAML. Public NCBI EFetch
and Datasets confirm [taxon 103329](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103329),
the exact label, species rank, genetic code 11 and parent 48479. All four
ancestors and ranks agree: root, cellular organisms, Bacteria, environmental
samples. Unresolved placement is correctly retained; no phylum or genus
was inferred. NCBI species rank does not imply valid nomenclatural publication.

## Evidence

Exact Nuccore search returned one record, [AB031615.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031615.1),
UID 5869709, a 700-base partial 16S rRNA gene. Inspected source qualifiers
explicitly identify TIHP302-29, taxon 103329, an environmental sample and
coastal marine sediment. References comprise the unpublished
Urakawa/Yoshida/Nishimura/Ohwada community study and Urakawa's 1999-08-25
direct submission. No DOI or PMID is supplied by either reference, and none
was inferred. This is clone/locus evidence, not a strain deposit or genome.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME attestation reproduces the pinned NCBI inventory and snapshot
date 2026-09-13, not a count of cultures or independent experiments.

## Completeness

Complete exact-ID scans found no target BacDive, LPSN, GTDB mapping, GOLD,
MediaDive, Madin or BactoTraits rows. Empty optional fields and zero strains
are supported within these source inventories.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the numeric ID
with digit boundaries, label and stem throughout `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`: 36 matching lines. Separate recursive
SOURCE.json scans found two BacDive request-list references and a timestamp
fraction, not target attestations. Inspected source contexts distinguish:

- CIP 103329: Enterococcus raffinosus, species 71452, BacDive 5326 with
  strain-level classification 1218093, LPSN 775981, GOLD Go0252021, SI-ID
  10344 and own SI-DP 40510. The source type status and five own-deposit
  nucleotide-locus associations do not transfer to this environmental clone.
- BacDive 103329: Agromyces sp., taxon 51513, designation
  STH00154(ZIMET), ST 00985, GT19991136; HKI-0154 is not TIHP302-29.
- KY103329: Derxomyces mrakii, SI-ID 65609. CP103329 occurs on E. coli
  ZY22049 genome record 562.122164, assembly GCA_028473865.1.
- MGBC103329: uncultured Muribaculaceae bacterium, GCA_910576935.1;
  MarMAG_103329: a different uncultured bacterium, GCA_977609915.1.
  Pseudomonas PSA-BAB-IMI-103329, Shigella PNUSAE103329 and Salmonella
  PNUSAS103329 also have distinct taxonomy and assemblies. GTDB numeric
  statistic matches are not identity evidence.

No target ATB strain/sample chain was established by these bounded searches.
Absence from the inspected inputs does not prove universal biological absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and documented scope.

## Recommended Edits

None. Preserve the clone identity, unresolved lineage and zero-strain state.
Any future supported correction belongs in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144098`. Never hand-edit the generated YAML.

## Follow-up Checks

For a later authorized source correction, inspect the exact identity chain
and inventory delta, run `just seed-canary NCBITaxon:103329 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run in this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13387`. Seed event remains
2026-09-13T17:54:04Z. The Taxonomy Browser request failed; EFetch and Datasets
succeeded. iModulonDB was not applicable to this taxonomy-only YAML. No
phenotype, gene-function or expression claim was added from unrelated locus
hits. Only this new report and the documented strict-validation TSV were
written; YAML, maintained inputs, scope, history, status and GitHub are unchanged.
