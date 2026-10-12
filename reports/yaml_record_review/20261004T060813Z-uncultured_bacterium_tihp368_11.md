# YAML Record Review: uncultured bacterium TIHP368-11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_tihp368_11.yaml`
- Started UTC: 2026-10-04T06:07:26Z
- Finished UTC: 2026-10-04T06:08:13Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103331`, rank `SPECIES`,
domain `BACTERIA`, grounding `EXACT`, status `SEEDED`, code 11, four lineage
entries, zero strains, one NAME attestation and one seed event. This is
environmental clone TIHP368-11, not a deposited strain or assembly.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_bacterium_tihp368_11.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_bacterium_tihp368_11.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full target/backbone, lineage, synonym, attestation, scope and seed-event
  comparisons passed. The pinned backbone has no direct children; exact
  type-material, merged and dropped scans found no target row.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons are not substitutes for those gates.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18440` and scientific-name row 38458
in `data/catalog/ncbi_names-0000.jsonl.gz` agree with the record. Live NCBI
EFetch and Datasets confirm [taxon 103331](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103331),
the label, species rank, parent 48479 and genetic code 11. All ancestors
match: root (1), cellular organisms (131567), Bacteria (2), environmental
samples (48479), with their original ranks. No more specific placement was
inferred and no valid-publication claim was added.

## Evidence

Exact Nuccore search returned one entry, [AB031633.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031633.1),
UID 5869727, a 766-base partial 16S rRNA gene. Its inspected qualifiers give
clone TIHP368-11, taxon 103331, an environmental sample and coastal marine
sediment. Its references are the unpublished Urakawa/Yoshida/Nishimura/Ohwada
community study and Urakawa's direct submission of 1999-08-25. Neither
reference provides a DOI or PMID; none was guessed. A partial locus does not
establish a cultured strain, genome or physiological property.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The single NCBITAXON NAME attestation, snapshot 2026-09-13 and seed-event text
faithfully reproduce the source inventory; the count is not an experiment or
strain count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits inventory entry for this taxon.
Zero strains and unpopulated optional fields are supported within these inputs.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries, label and stem across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`: 27 lines. Separate recursive structured
SOURCE.json scans returned two BacDive request-list references. Inspected
numeric collisions were kept separate:

- BacDive 103331 is Agromyces sp. ST026900(HKI), GT20044001, taxon 51513,
  explicitly non-type in that source.
- Native SI-ID 2269 / SI-DP 9290 identifies CIP 103331 as Enterococcus
  pseudoavium, taxon 44007, with BacDive cross-reference 5325. KY103331 is
  associated with Derxomyces nakasei, SI-ID 180184, not TIHP368-11.
- CP103331 occurs on E. coli ZY22049 genome record 562.122164,
  GCA_028473865.1. E. coli PNUSAE103331 has GCA_023695325.1; their numeric
  suffixes do not identify the environmental clone.
- MGBC103331 is an uncultured Clostridia bacterium, GCA_948676835.1;
  MarMAG_103331 is a different uncultured bacterium, GCA_977601475.1.
  Pseudomonas PSA-BAB-IMI-103331, Salmonella PNUSAS103331 and GOLD's
  NPDC103331_431_E07 project/analysis names do not supply a target identity
  chain. GOLD project/analysis records are not themselves genome identifiers.
- GTDB assembly-statistic matches and ATB checksum hits for Klebsiella
  sample SAMN10734714 and Salmonella sample SAMN46192234 are not taxon or
  strain matches. No target BioSample association or assembly equivalence
  was inferred.

These are bounded local-source findings, not a claim of universal absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and stated checks.

## Recommended Edits

None. Preserve the clone identity, carried lineage and zero-strain state.
Future supported corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained in
`curation/seed_scope.tsv:144100`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect the exact source identity
chain and inventory delta, then run `just seed-canary NCBITaxon:103331 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run during this review.

## Additional Notes

Unique target path: `data/taxa/PATHS.tsv:13401`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. No YAML, maintained input, scope, history, status or GitHub state
changed; only this new report and the documented validation TSV were written.
