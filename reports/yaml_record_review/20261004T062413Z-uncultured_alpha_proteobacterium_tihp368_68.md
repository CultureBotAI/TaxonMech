# YAML Record Review: uncultured alpha proteobacterium TIHP368-68

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_alpha_proteobacterium_tihp368_68.yaml`
- Started UTC: 2026-10-04T06:23:32Z
- Finished UTC: 2026-10-04T06:24:13Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103333`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, seven ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. TIHP368-68 denotes an
environmental clone; it is distinct from other TIHP368 clones.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_alpha_proteobacterium_tihp368_68.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_alpha_proteobacterium_tihp368_68.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans
  found no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not replace these gates.

## Identity and Grounding

Backbone row 18442 and scientific-name row 38460 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103333&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103333)
confirm the exact ID, label, species rank, code 11 and parent 47925.
All seven ancestor IDs, labels and ranks agree: root, cellular organisms,
Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria and environmental
samples. The latter is a no-rank taxonomy grouping, not an independently
curated habitat observation. Species rank does not imply formal publication.

## Evidence

Exact Nuccore search returned one entry, [AB031658.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031658.1),
UID 5869752, a 724-base partial 16S rRNA gene. Inspected source qualifiers
give clone TIHP368-68, taxon 103333, coastal marine sediment and an
environmental-sample flag. This is not evidence for a culture deposit,
assembled genome or independently verified phenotype.

Both sequence references were inspected: Urakawa, Yoshida, Nishimura and
Ohwada's coastal-sediment community study using 16S rDNA and quinone
profiling, marked unpublished, and Urakawa's direct submission dated
1999-08-25. Neither supplies a DOI or PMID. Full manuscript text was not
obtained. No quinone phenotype for this clone or publication identifier
was inferred from the community-study title.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME attestation and 2026-09-13 taxonomy snapshot accurately
reproduce the pinned NCBI source; this is not an independent-study count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero inventoried
strains and empty optional fields fit the source-backed environmental clone.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the numeric ID
with digit boundaries and exact label/stem designation across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`. All 31 matched lines
were inspected. Besides target scope, backbone and name, matches concern:

- CIP 103333, Brachybacterium faecium 6-10, BacDive 3902, species 43669,
  strain 446465, LPSN 774148 and StrainInfo 92763's own deposit 149337.
  Native BacDive and StrainInfo contexts establish this unrelated identity.
- BacDive 103333, Agromyces sp. ST026907(HKI), GT20044003, taxon 51513.
- CP103333 in Escherichia coli ZY22049 (GCA_028473865.1), E. coli
  PNUSAE103333 (GCA_023694305.1), Pseudomonas aeruginosa PSA-BAB-IMI-103333
  (GCA_033090755.1), Salmonella PNUSAS103333 (GCA_008795355.1), Shigella
  flexneri isolate 103333 (GCA_026021275.1), Oscillospiraceae MGBC103333
  (GCA_948714875.1) and uncultured bacterium MarMAG_103333 (GCA_977586535.1).
- Coordinate or assembly-statistic matches for archaeal assemblies
  GCA_001940755.1 and GCA_001940705.1, Caulobacter GCF_009905535.1 and
  Enterobacter roggenkampii GCF_050772235.1; an ATB checksum for
  Clostridioides difficile sample SAMN32115901.

Recursive structured SOURCE.json searches found two BacDive request-metadata
matches for the unrelated BacDive ID 103333. No numeric coincidence, shared
source grouping or neighboring clone establishes a target strain/BioSample/
assembly identity chain. These are bounded local-source results, not
universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve the exact environmental-clone scope. Future evidence-backed
corrections belong in maintained source inputs and `src/taxonmech/extract.py`
/ `src/taxonmech/seed.py`; scope is maintained at
`curation/seed_scope.tsv:144102`. Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect clone/deposit identity and
inventory deltas, run `just seed-canary NCBITaxon:103333 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13411`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets
succeeded. iModulonDB was not applicable to this taxonomy-only record.
Only this report and the documented validation TSV were written for this
target; YAML, maintained inputs, scope, history, status and GitHub remain
unchanged.
