# YAML Record Review: uncultured bacterium TIHP302-14

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_tihp302_14.yaml`
- Started UTC: 2026-10-04T06:03:03Z
- Finished UTC: 2026-10-04T06:03:56Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103328`, `SPECIES`,
`BACTERIA`, `EXACT`, `SEEDED`, genetic code 11, four ancestors, zero strains
and one NCBITAXON NAME attestation. This denotes environmental clone
TIHP302-14, not a deposited culture or a genome.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_bacterium_tihp302_14.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_bacterium_tihp302_14.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete target/backbone, parent-chain, synonym, attestation, scope and
  seed-event comparisons passed. Exact type-material/merged/dropped scans
  returned no target rows; no direct children were present in the backbone.
- Not checked: full-corpus reproduction, `just qc`, tests, global term and
  reference checks, history/provenance/product gates and rendering. Focused
  source comparisons are not substitutes for those checks.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18437` and scientific-name row 38455
in `data/catalog/ncbi_names-0000.jsonl.gz` agree with the full YAML. Public
NCBI EFetch and Datasets confirm [taxon 103328](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103328),
its label, species rank, code 11 and parent 48479. The full root-first chain
is 1/root, 131567/cellular organisms, 2/Bacteria, 48479/environmental samples,
with the same ranks. No phylum or genus was inferred from nearby records.
The species rank is NCBI's classification, not evidence of valid publication.

## Evidence

Exact Nuccore search returned one entry, inspected in full for source and
reference fields: [AB031600.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031600.1),
UID 5869694, a 739-base partial 16S rRNA gene. It names clone TIHP302-14,
taxon 103328, environmental sampling and coastal marine sediment. Its
Urakawa/Yoshida/Nishimura/Ohwada community-study reference is unpublished;
the second reference is Urakawa's direct submission dated 1999-08-25.
Neither supplies a DOI or PMID. No citation identifier or phenotype was
invented, and this locus was not treated as an assembly.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME attestation and September 13, 2026 snapshot correctly describe
the source inventory, not a count of strains or independent studies.

## Completeness

Complete exact-ID scans found no target BacDive, LPSN, GTDB mapping, GOLD,
MediaDive, Madin or BactoTraits inventory row. Zero strains and empty optional
slots match these inputs.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched ID, label and stem
through `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`:
120 matching lines. Recursive structured SOURCE.json searches added two
BacDive request-list references and one SeqCode checksum substring, none
establishing a target association. Distinct source contexts were preserved:

- CIP 103328 belongs to Yersinia mollaretii, taxon 33060, BacDive 138647,
  GOLD Go0298784, SI-ID 70663 and its own SI-DP 156307.
- BacDive 103328 is Agromyces sp. ST028168, taxon 51513.
- SI-DP 103328 is ATCC 23866, Planobispora rosea, taxon 35762, SI-ID 319092,
  BacDive 16575. Its AF051395 locus association does not concern this clone.
- CP103328 is associated with Bacillus taxon 1423 strain KC14-1 and
  GCA_030863625.1. MGBC103328 is Bacteroides acidifaciens, GCA/GCF_948743225.1;
  MarMAG_103328 is associated with GCA_977632725.1. Matching numeric suffixes
  do not establish clone or assembly identity.
- Mycena and Mycenella taxon IDs beginning 103328, NPDC103328_429_C02,
  PELAGICS-MAG-m2-bin103328, unrelated pathogen strain names, sample/run
  accessions, genome statistics and checksums are not exact target matches.
  No ATB BioSample-to-strain evidence chain was established.

These are bounded local-source findings, not a universal absence claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and stated validation scope.

## Recommended Edits

None. Preserve the unresolved bacterial placement and zero-strain state.
Future evidence-backed changes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:144097`. Do not hand-edit generated YAML.

## Follow-up Checks

Following an authorized source change, inspect the exact target evidence and
inventory delta, run `just seed-canary NCBITaxon:103328 --force`, both focused
validators, `just verify-corpus` and the remaining QC gates. No canary was run.

## Additional Notes

Unique path entry: `data/taxa/PATHS.tsv:13384`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible, but EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. No YAML, maintained input, scope, history, status or GitHub mutation
was made; only this report and the documented validation TSV were written.
