# YAML Record Review: uncultured actinobacterium TIHP368-75

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_actinobacterium_tihp368_75.yaml`
- Started UTC: 2026-10-04T06:40:36Z
- Finished UTC: 2026-10-04T06:41:07Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:103334`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, seven ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. TIHP368-75 denotes an
environmental clone, distinct from other TIHP368 clones and numbered deposits.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_actinobacterium_tihp368_75.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_actinobacterium_tihp368_75.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/lineage, synonym, attestation, scope and seed-event
  comparisons passed. Exact type-material, merged-ID and dropped scans found
  no target row; the backbone has no direct children.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global
  term/reference checks, provenance/history/product gates and rendering.
  Focused source comparisons do not replace these gates.

## Identity and Grounding

Backbone row 18443 and scientific-name row 38461 in
`data/catalog/ncbi_names-0000.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103334&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103334)
confirm exact ID, label, species rank, code 11 and parent 35766. All seven
ancestor IDs, labels and ranks agree: root, cellular organisms, Bacteria,
Bacillati, Actinomycetota, Actinomycetes and environmental samples. The last
entry is a no-rank taxonomy grouping, not an independently curated habitat
claim. Species rank does not establish formal nomenclatural publication.

## Evidence

Exact Nuccore search returned one entry, [AB031661.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031661.1),
UID 5869755, a 700-base partial 16S rRNA gene. Source qualifiers name clone
TIHP368-75, taxon 103334, coastal marine sediment and an environmental-sample
flag. This does not establish a culture deposit, genome or clone phenotype.

Both references were inspected: Urakawa, Yoshida, Nishimura and Ohwada's
coastal-sediment community study using 16S rDNA and quinone profiling, marked
unpublished, and Urakawa's direct submission dated 1999-08-25. Neither supplies
a DOI or PMID. Full manuscript text was not obtained; no quinone phenotype
for this clone or publication identifier was inferred from the study title.

Exact Assembly search returned zero with a phrase-not-found/no-items warning.
The one NAME assertion and 2026-09-13 taxonomy snapshot reproduce the pinned
source; assertion count is not a strain census or independent-study count.

## Completeness

Complete exact-ID scans found no BacDive strain, LPSN name, GTDB mapping,
GOLD organism, MediaDive, Madin or BactoTraits entry. Zero inventoried strains
and empty optional fields fit the source-backed environmental clone.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched numeric ID with
digit boundaries and exact label/stem designation across `data/raw`,
`data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`. All 41 matching lines
were inspected. Besides target scope, backbone and scientific name, they concern:

- CIP 103334, Brachybacterium paraconglomeratum 7-11, BacDive 3905, taxon
  173362, LPSN 774153 and StrainInfo 92221's own deposit 58430.
- BacDive 103334, Agromyces sp. ST028659, taxon 51513.
- StrainInfo deposit 103334, ATCC 23870, belonging to SI-ID 38277/BacDive
  13298, taxon 68170. Native strain context says Lentzea aerocolonigenes;
  deposit context retains Lechevalieria aerocolonigenes. Its own-deposit
  nucleotide U09581 is unrelated to this clone; no accession version was added.
- KY103334 on StrainInfo 111516, Derxomyces schimicola, taxon 118575.
- CP103334 in Escherichia coli ZY22049 (GCA_028473865.1), E. coli strain
  103334 (GCA_002075125.1/GCF_002075125.1) and PNUSAE103334
  (historical GCA_023697385.1 and current .2), Pseudomonas aeruginosa
  PSA-BAB-IMI-103334 (GCA_033090715.1), Salmonella PNUSAS103334
  (GCA_008861445.1), Muribaculaceae MGBC103334 (GCA_948692115.1), and a
  Candidatus Altimarinus PELAGICS-MAG-m2-bin103334 assembly (GCA_964663665.1).
- Assembly-statistic matches for Enterobacter roggenkampii GCF_049890955.1
  and GCF_049886935.1, and E. coli GCF_014862665.1.
- ATB SeqKit-sum substrings for SAMEA112851861, SAMEA6145943 and SAMN40353036.
  The first has Neisseria gonorrhoeae source identity and unknown/SYLPH-failed
  classification; the other two have Salmonella enterica identity. Exclusion
  rests on unrelated identity, not a claim that these FASTAs are unavailable.

Recursive structured SOURCE.json searches found two BacDive request-metadata
matches for unrelated BacDive ID 103334. Numeric coincidences and source
groupings establish no target strain/BioSample/assembly identity chain.
These bounded local-source results are not universal absence claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Preserve exact environmental-clone scope. Future evidence-backed fixes
belong in maintained source inputs and `src/taxonmech/extract.py` /
`src/taxonmech/seed.py`; scope is maintained at `curation/seed_scope.tsv:144103`.
Never hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, inspect exact clone/deposit identity
and inventory deltas, run `just seed-canary NCBITaxon:103334 --force`, both
focused validators, `just verify-corpus` and remaining QC gates. No canary
or regeneration was run during this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13422`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page failed; EFetch and Datasets succeeded.
iModulonDB was not applicable to this taxonomy-only record. Only this report
and the documented validation TSV were written for this target; YAML,
maintained inputs, scope, history, status and GitHub remain unchanged.
