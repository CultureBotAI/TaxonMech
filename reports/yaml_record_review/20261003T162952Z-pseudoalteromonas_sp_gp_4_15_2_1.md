# YAML Record Review: Pseudoalteromonas sp. Gp-4-15.2.1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_gp_4_15_2_1.yaml`
- Started UTC: 2026-10-03T16:28:51Z
- Finished UTC: 2026-10-03T16:29:52Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303820`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:194690`, genetic code 11, grounding `EXACT`, status `SEEDED`.
Ten lineage entries, one NCBI NAME attestation, strain count zero and one
embedded seed event are present. No nomenclature, synonyms, mappings,
equivalence xrefs, strain/genome entries, experimental evidence or causal
graph is asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudoalteromonas_sp_gp_4_15_2_1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_gp_4_15_2_1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, code,
  parent and all ten lineage entries. There are no target children.
  Complete exact-field scans found no membership in the seven other
  source inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated-site
  drift, exports and nucleotide content were not audited.
- Ignored-inclusive history searches found no target standalone event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308153` reproduces the target spelling,
rank, code, unclassified-Pseudoalteromonas parent and empty synonym
fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30704` agrees. Every lineage
object matches its pinned NCBI backbone row.

The NCBI browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303820&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 194690,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303820)
confirms rank and all ten ancestor IDs including root. Grounding is
supported for this exact source entity.

Keep NCBI's species rank and its `NO_RANK` unclassified parent. An
isolate-like designation does not justify changing rank, treating it as
a culture accession or assigning a named species. No validly published
binomial or equivalence to another Gp designation is implied.

## Evidence

The NCBITAXON / NCBITaxon:1303820 / 1 NAME attestation matches the
backbone row and the 2026-09-13 snapshot. One NAME is a source count,
not a biological strain or genome count. No DOI, PMID, accession,
functional assertion or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106258` fixes the target slug.
`curation/seed_scope.tsv:393100` admits it on 2026-09-13 with the exact
one-source reason carried in the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list are consistent with the YAML.
`SEEDED` is preserved; no human-review status is claimed.

## Completeness

Ignored-inclusive searches by ID, label, slug and Gp-4-15.2.1 covered
`data/raw/`, `curation/`, `history/` and all compressed native JSONL
catalogs under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/` and `data/straininfo/`. Only the NCBI
scientific-name object was target evidence. Exact membership scans of
the complete BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventories found no row for this taxon. With no descendants, zero
listed strains is supported at the BacDive inventory boundary.

One unrelated native numeric hit was fully read and excluded:
`GCA_023324885.1` at `data/catalog/ncbi_genbank-0021.jsonl.gz:29272`
is Salmonella enterica taxon 28901, strain SC-H1910-0053, whose
assembly name is PDT001303820.1. Those digits do not establish a
taxonomy link to this record.

Additional ignored-inclusive searches covered the complete
`data/catalog/allthebacteria.tsv.xz`, `data/atb/` and StrainInfo link,
assembly, exclusion and compressed related-record tables. The sole ATB
substring hit, SAMN30567377 with run SRR21303820, is Salmonella
enterica; its full row was read and excluded. No target source chain
was found. Raw assembly/genome/related inventories were included in the
raw-directory search.

No eligible culture-deposit or BioSample association was established.
This does not assert that the organism lacks sequences or isolates
outside the checked sources. Optional nomenclature, mappings and genome
links are appropriately empty at that boundary. No gene, locus,
regulator, pathway, trait or transcriptomics dataset is asserted;
iModulonDB is not applicable. A causal graph is not required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported identity and lineage, and keep
`SEEDED`. Future source-backed enrichment belongs in maintained
extraction inputs or `src/taxonmech/extract.py`, with changed seeding
behavior in `src/taxonmech/seed.py` and regression tests. Do not patch
generated YAML or borrow neighboring taxa's evidence.

## Follow-up Checks

No finding-specific check is outstanding. New evidence requires exact
identity/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Corpus changes also require
`just verify-corpus` and full QC. This focused verdict does not claim
those unrun corpus-wide checks passed.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden`, with `-z` for compressed sources.
Read-only NCBI requests used network escalation after established
sandbox DNS failures. No paid research or provider credits were used.

The only manual write is this new report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, source refresh, GitHub mutation or
cross-repository write occurred. No Eukaryota record was re-reviewed.
