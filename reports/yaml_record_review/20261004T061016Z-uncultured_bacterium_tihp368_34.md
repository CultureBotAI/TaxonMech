# YAML Record Review: uncultured bacterium TIHP368-34

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_bacterium_tihp368_34.yaml`
- Started UTC: 2026-10-04T06:09:33Z
- Finished UTC: 2026-10-04T06:10:16Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103332`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four lineage entries, zero strains, one
NCBITAXON NAME attestation and one seed event. The target is environmental
clone TIHP368-34, not a deposited strain or genome.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_bacterium_tihp368_34.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_bacterium_tihp368_34.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, ancestor-chain, synonym, attestation, scope and
  seed-event comparisons passed. Exact type-material, merged and dropped
  scans found no target rows; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not establish these broader invariants.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18441` and native scientific-name row
38459 in `data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML.
Live NCBI EFetch and Datasets confirm [taxon 103332](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103332),
label, species rank, parent 48479 and code 11. The entire root-first lineage
and ranks match: root (1), cellular organisms (131567), Bacteria (2),
environmental samples (48479). No phylum, genus or nomenclatural validity
was inferred from this unresolved NCBI classification.

## Evidence

Exact Nuccore search returned one source, [AB031649.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031649.1),
UID 5869743, an 811-base partial 16S rRNA gene. Inspected source qualifiers
identify clone TIHP368-34, taxon 103332, environmental sampling and coastal
marine sediment. Both references were inspected: an unpublished
Urakawa/Yoshida/Nishimura/Ohwada community study and Urakawa's 1999-08-25
direct submission. Neither provides a DOI or PMID; no identifier was guessed.
The locus does not establish a culture, genome or physiological property.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME attestation and snapshot date 2026-09-13 match the inventory;
this count is neither a strain census nor an independent-experiment count.

## Completeness

Complete exact-ID scans found no target BacDive strain, LPSN name, GTDB
mapping, GOLD organism, MediaDive, Madin or BactoTraits row. Empty optional
slots and zero strains reproduce the inspected inputs.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the numeric ID
with digit boundaries, label and stem across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`,
`data/atb`, `curation` and `history`: 25 matching lines. Separate recursive
structured SOURCE.json scans returned two BacDive request-list references.
Inspected non-target contexts include:

- CIP 103332: Brachybacterium conglomeratum strain 3-8, taxon 47846,
  BacDive 3907, LPSN 774147, SI-ID 126056 and own SI-DP 58415. The native
  BacDive non-type status concerns that culture, not TIHP368-34.
- BacDive 103332: Agromyces sp. ST026904(HKI), GT20044002, taxon 51513.
  KY103332 is associated with Derxomyces pseudohuiaensis, SI-ID 107531.
- CP103332 occurs on E. coli ZY22049 genome record 562.122164,
  GCA_028473865.1. E. coli PNUSAE103332 has GCA_023693765.1;
  Pseudomonas PSA-BAB-IMI-103332 and Salmonella PNUSAS103332 are also
  distinct strains, not this clone.
- MGBC103332 is an uncultured Muribaculaceae bacterium,
  GCA_948616945.1; MarMAG_103332 has GCA_977587185.1. Matching numeric
  suffixes do not establish identity or assembly equivalence.
- A GTDB contig statistic and ATB checksum for sample SAMN44075049 do not
  supply a target identity chain. That ATB row retains its Staphylococcus
  source label, unknown derived classification, SYLPH failures and ENA
  submission error; no target link was inferred regardless of FASTA status.

These searches establish bounded local-source coverage, not universal absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and stated checks.

## Recommended Edits

None. Preserve the clone identity, unresolved lineage and zero-strain state.
Future supported corrections belong in maintained inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:144101`. Never hand-edit generated YAML.

## Follow-up Checks

Following an authorized source correction, inspect exact evidence and the
inventory delta, run `just seed-canary NCBITaxon:103332 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run in this review.

## Additional Notes

Unique target path: `data/taxa/PATHS.tsv:13404`. The seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets
succeeded. iModulonDB was not applicable to this taxonomy-only record.
Only this new report and the documented validation TSV were written; YAML,
source inputs, scope, history, status and GitHub state remain unchanged.
