# YAML Record Review: Pectobacterium sp. IPPBC GR007

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pectobacterium_sp_ippbc_gr007.yaml`
- Started UTC: 2026-10-03T15:13:51Z
- Finished UTC: 2026-10-03T15:15:02Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. Identity is
`NCBITaxon:1303727`, label Pectobacterium sp. IPPBC GR007, rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:2627739`, genetic code 11. Grounding
is `EXACT`, mapping status `SEEDED`, and strain count zero. There is one
NCBI name attestation and one embedded seed event. No synonyms,
nomenclature, mappings, strains, genome links or causal graphs are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pectobacterium_sp_ippbc_gr007.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pectobacterium_sp_ippbc_gr007.yaml`:
  PASS; one file scanned, zero errors. Standard diagnostic written to
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone read confirms identity, rank, parent,
  genetic code and all ten root-first lineage entries. No direct children
  occur in the pinned backbone, so the target subtree is a singleton.
- Complete exact-field scans of BacDive, LPSN, GTDB mappings, GOLD,
  MediaDive, Madin and BactoTraits inventories found no direct target rows.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, rendered products, exports
  and genome sequences were not audited.
- Ignored-inclusive searches of `history/` found no target ID, label or
  slug. Standalone history validation had no target. Strict validation
  checked the embedded event; graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308127` supplies the exact label, species
rank, parent, code and empty synonym fields. The native scientific-name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30675` agrees. The
identifier has exactly one row with this slug in `data/taxa/PATHS.tsv`.

The NCBI browser URL was inaccessible through the web tool, and the first
sandboxed API requests failed DNS resolution. Subsequent read-only public
API requests succeeded. Inspected
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303727&retmode=xml)
confirms the ID, exact scientific name, species rank, Bacteria division,
parent, code and lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303727)
confirms the same name, species rank and ten ancestor IDs including root.

The immediate parent is unclassified Pectobacterium, not directly the
genus. The IPPBC GR007 designation is retained exactly and does not
authorize an invented culture identifier or a change to strain rank.
`EXACT` refers to this NCBI concept, not validly published nomenclature.

## Evidence

The single `NCBITAXON` attestation correctly names 1303727, counts one
`NAME`, and records the pinned 2026-09-13 snapshot. The scope row at
`curation/seed_scope.tsv:393089` includes this taxon with its one-source
NCBI reason. The embedded 2026-09-13T17:54:04Z event reproduces that
reason and does not claim human review. Generic input-directory wording
does not imply that every inventory supplied evidence for this record.

All lineage IDs, labels and ranks match the pinned ancestor chain: root,
cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Enterobacterales, Pectobacteriaceae, Pectobacterium
and unclassified Pectobacterium. The live NCBI responses agree.

Ignored-inclusive compressed ID, full-label and slug searches covered all
`*.jsonl.gz` files in `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/seqcode/`. The relevant hit was
the scientific-name object. One other hit was fully inspected and excluded:
`data/catalog/ncbi_genbank-0066.jsonl.gz:11815` is GCA_982361835.1,
Desulfobulbus oralis, taxon 1986146; 1303727 is its genome size, not its
taxon identity. It cannot support a genome association for this record.

## Completeness

The singleton subtree and empty BacDive inventory membership support
`strain_count: 0`. Empty direct LPSN, GTDB and other source inventories
explain the omitted nomenclature, mappings and non-NCBI attestations.
These are bounded source misses, not claims of biological absence.

Ignored-inclusive compressed searches of `data/atb/` and the full
`data/catalog/allthebacteria.tsv.xz` found no target ID, full label or
slug. No culture-deposit or BioSample key was supplied for a further
supported strain-genome join. Optional fields should not be populated
from a similar designation or genus membership.

No gene, locus, regulator, pathway, phenotype or transcriptomic dataset
is asserted; iModulonDB is not applicable. No DOI, PMID, literature
reference or experimental evidence is cited. Optional evidence and
causal graphs are not required for this NCBI-only identity record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Do not hand-edit the generated YAML or promote its status.
Future authoritative source corrections belong in the source and maintained
extraction workflow, followed by `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`. No owner change is proposed here.

## Follow-up Checks

No corrective edit needs verification. Following a future authorized
source refresh, repeat focused schema/strict validation and explicit
source and lineage comparisons. Run `just verify-corpus` in the complete
regeneration workflow; this review does not prove corpus reproduction.

## Additional Notes

Absence checks included ignored files using complete structured reads,
`find`, or `rg --no-ignore --hidden` with `-z` for compressed sources.
The only manual write is this new report. Strict validation wrote its
standard diagnostic. No YAML, source, prior report, history or status
was edited; no generator, source refresh, paid provider, GitHub mutation
or cross-repository write occurred. Eukaryota was not re-reviewed.
