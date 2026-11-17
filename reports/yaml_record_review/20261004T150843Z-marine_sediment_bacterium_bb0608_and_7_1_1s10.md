# YAML Record Review: marine sediment bacterium BB0608_AND_7.1_1S10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_1s10.yaml`
- Started UTC: 2026-10-04T15:07:44Z
- Finished UTC: 2026-10-04T15:08:43Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033597, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_7.1_1S10 distinguishes this target from other BB0608 strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_1s10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_1_1s10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded checks do not replace these gates.

## Identity and Grounding

Backbone row 221231 and scientific-name row 30539 in
`data/catalog/ncbi_names-0005.jsonl.gz` match the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033597&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033597)
confirm name and rank; EFetch confirms parent 49928 and code 11. Root-first
lineage is root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928), with matching ranks. Species rank alone does not establish
valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750149.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750149.1),
UID 333384496, one 358-base partial 16S rRNA sequence. Inspected source
qualifiers identify strain BB0608_AND_7.1_1S10, taxon 1033597, genomic DNA,
coastal marine sediment, Australia: Gulf of Carpentaria and June 2008.
Strain is the explicit qualifier, not clone or environmental sample. This
locus is not a genome, culture deposit or independent classification.

Both references were inspected: the Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb cryopreservation study is unpublished; Cornall's
direct submission is dated 2011-04-01. Neither supplies DOI/PMID. Full
manuscript text was not obtained and no phenotype was inferred from its
title. Exact Assembly search returned zero with phrase-not-found/no-items
warnings. The one NAME attestation and snapshot 2026-09-13 agree with the
inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional fields are
appropriate; zero inventoried strains does not mean never cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full designation with dot/underscore variants, including label/slug
forms, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and
`history`. All four matches were inspected: target scope/backbone/name and
one ATB row. Structured recursive SOURCE.json scans found zero matches.
Absence is bounded to these local searches and exact public queries.

ATB row `data/catalog/allthebacteria.tsv.xz:64953` identifies SAMEA1033597,
ERR068082 and ERZ3069005; scientific name and both Sylph fields are
Streptococcus pneumoniae. FASTA is available, assembly/Sylph/HQ filters
PASS and prior-HQ T. Only the sample suffix and AWS URL match the numeric
taxon ID. This supplies no target strain/deposit/genome chain. Exclusion
is identity-based, not quality-based; sample and assembly identities differ.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321583`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:1033597 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13680`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.
