# YAML Record Review: marine sediment bacterium BB0608_AND_6.2_5G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_5g0.yaml`
- Started UTC: 2026-10-04T15:00:28Z
- Finished UTC: 2026-10-04T15:01:24Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033593, species, Bacteria,
EXACT/SEEDED, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact strain designation
BB0608_AND_6.2_5G0 separates this record from neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_5g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_5g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded checks are not substitutes for these gates.

## Identity and Grounding

Backbone row 221227 and scientific-name row 30535 in
`data/catalog/ncbi_names-0005.jsonl.gz` support the YAML identity. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033593&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033593)
confirm the exact label and rank; EFetch confirms parent 49928 and code 11.
Root-first lineage is root (1), cellular organisms (131567), Bacteria (2),
unclassified Bacteria (49928), with matching ranks. Species rank alone
does not establish valid publication or finer placement.

## Evidence

Exact Nuccore search returned one [JF750138.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750138.1)
record, UID 333384485, containing 513 bases of partial 16S rRNA. Inspected
source qualifiers explicitly identify strain BB0608_AND_6.2_5G0, taxon
1033593, genomic DNA, coastal marine sediment, Australia: Gulf of
Carpentaria and June 2008. Strain is the source qualifier, not clone or
environmental sample; the sequence is not a genome or culture-deposit
identifier and does not independently establish classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's cryopreservation study is marked unpublished, and
Cornall's direct submission is dated 2011-04-01. Neither supplies DOI/PMID;
full manuscript text was not obtained and no phenotype was inferred from
its title. Exact Assembly search returned zero with phrase-not-found and
no-items warnings. The attestation is one NAME from snapshot 2026-09-13,
matching the inventory, not one experiment.

## Completeness

Complete exact-ID scans found no target entries in BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin or BactoTraits inventories. Optional slots can
remain empty; zero inventoried strains does not mean never cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and complete designation with dot/underscore variants, covering
label/slug forms, across `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. All four matches were inspected: target
scope/backbone/scientific name and one ATB row. Structured recursive
SOURCE.json scans found zero matches. Absence is bounded to these searches.

ATB row `data/catalog/allthebacteria.tsv.xz:64949` identifies SAMEA1033593,
ERR064659 and ERR085918, ERZ3068999; scientific name and both Sylph fields
are Streptococcus pneumoniae. FASTA is available, assembly/Sylph/HQ filters
PASS and prior-HQ T. Only the sample suffix and its AWS URL match the taxon
number. This supplies no target strain/deposit/genome chain. Exclusion is
identity-based, not quality-based; sample identity is not assembly identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321579`. Generated YAML must not be hand-edited.

## Follow-up Checks

After an authorized fix, verify exact identity and inventory deltas, run
`just seed-canary NCBITaxon:1033593 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13676`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the documented validation TSV were written; YAML,
maintained inputs, scope, status, history and GitHub were not changed.
