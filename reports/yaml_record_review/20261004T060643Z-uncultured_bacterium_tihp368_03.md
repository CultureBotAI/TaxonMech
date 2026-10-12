# YAML Record Review: uncultured bacterium TIHP368-03

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_tihp368_03.yaml`
- Started UTC: 2026-10-04T06:06:01Z
- Finished UTC: 2026-10-04T06:06:43Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103330`, `SPECIES`,
`BACTERIA`, `EXACT`, `SEEDED`, genetic code 11, four lineage entries, zero
strains, one NCBITAXON NAME attestation and one seed event. The target is
environmental clone TIHP368-03, not a culture-deposit record.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_bacterium_tihp368_03.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_bacterium_tihp368_03.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event
  comparisons passed. No direct children or exact type-material, merged-ID
  or dropped entries were found in the respective full source scans.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  The focused checks do not prove those broader invariants.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18439` and scientific-name row 38457 in
`data/catalog/ncbi_names-0000.jsonl.gz` support the exact ID and label.
Live NCBI EFetch and Datasets agree on [taxon 103330](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103330),
rank, parent 48479 and code 11. The entire lineage is root (1), cellular
organisms (131567), Bacteria (2), environmental samples (48479), with the
same ranks. No missing phylum or genus was guessed, and species rank was not
interpreted as evidence of valid publication.

## Evidence

Exact Nuccore search returned one source, [AB031629.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031629.1),
UID 5869723, a 764-base partial 16S rRNA gene. Inspected source qualifiers
explicitly give clone TIHP368-03, taxon 103330, environmental sampling and
coastal marine sediment. The two references are an unpublished
Urakawa/Yoshida/Nishimura/Ohwada community study and Urakawa's direct
submission dated 1999-08-25. Neither contains a DOI or PMID; none was guessed.
No strain, genome or phenotype was inferred from this locus.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME attestation, 2026-09-13 snapshot and seed-event text match their
inventories. A name count is not a count of strains or independent evidence.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits row for this taxon. The empty
optional slots and zero strain count are supported by the inspected inputs.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the numeric ID
with digit boundaries, label and stem across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`, returning 36 lines. Recursive structured
SOURCE.json checks added two BacDive request-list references. None of the
following numeric collisions supplies a target association:

- CIP 103330 is Tetragenococcus solitarius, BacDive 5256, species 71453,
  strain taxon 1223494, SI-ID 10345 and own SI-DP 40516. Native BacDive type
  status and LPSN 782433 concern that organism. The retained Enterococcus
  solitarius name in other source fields and deprecated LPSN 775985 was not
  silently rewritten or transferred to the target.
- Its AJ387921, EU021309, EU021372, EU021407 and EU021425 own-deposit loci
  are not genomes and do not concern TIHP368-03. SI-DP 103330 is instead
  ATCC 23868, Pseudomonas savastanoi, SI-ID 38276, taxon 29438.
- BacDive 103330 identifies Agromyces sp. STI10627(IMET), 655L, taxon 51513;
  KY103330 is associated with Derxomyces mrakii, SI-ID 65610.
- CP103330 occurs on E. coli ZY22049 genome record 562.122164,
  GCA_028473865.1. MGBC103330 is a Muribaculaceae bacterium,
  GCA_948667105.1; MarMAG_103330 has GCA_977612335.1. Other suffix matches
  concern Pseudomonas, Shigella and Salmonella strains, not the target clone.
- GTDB statistic matches and an ATB checksum for Salmonella sample
  SAMN05978527 are not identity evidence. No eligible target BioSample
  chain or assembly-equivalence claim was inferred.

These bounded local searches do not establish universal absence of evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record and the documented checks.

## Recommended Edits

None. Preserve the environmental-clone identity and unresolved placement.
Future supported corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained in
`curation/seed_scope.tsv:144099`. Do not hand-edit the generated record.

## Follow-up Checks

After an authorized source correction, inspect the exact identity chain and
inventory delta; run `just seed-canary NCBITaxon:103330 --force`, both focused
validators, `just verify-corpus` and remaining QC gates. No canary or
regeneration was run during this review.

## Additional Notes

Unique target path: `data/taxa/PATHS.tsv:13390`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed, but EFetch and Datasets
succeeded. iModulonDB was not applicable to this taxonomy-only record.
YAML, source inputs, scope, history, status and GitHub state are unchanged;
only this report and the documented strict-validation TSV were written.
