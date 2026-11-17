# YAML Record Review: Saccharopolyspora sp. SPF5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharopolyspora_sp_spf5.yaml`
- Started UTC: 2026-10-03T16:43:15Z
- Finished UTC: 2026-10-03T16:44:51Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303827`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2646250`, genetic code 11, grounding `EXACT`, status
`SEEDED`. It has ten lineage entries, one NCBI NAME attestation,
strain count zero and one embedded seed event. No synonyms,
nomenclature, taxonomy mappings, xrefs, strain/genome links,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/saccharopolyspora_sp_spf5.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/saccharopolyspora_sp_spf5.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and all ten lineage objects. No target children occur. Complete
  exact-field scans find no membership in the seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated-site
  drift, exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308160` agrees on the exact uppercase
SPF5 label, species rank, unclassified-Saccharopolyspora parent, code
and empty synonym fields. The complete native scientific-name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30711` agrees. The ten-entry
root-first lineage matches the pinned NCBI backbone.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303827&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2646250,
code 11 and the full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303827)
confirms rank and all ten ancestor IDs including root. The Pseudonocardiales
and Pseudonocardiaceae placement is supported, without inferred
reconciliation to another taxonomy.

Keep NCBI's species rank and the direct unclassified parent's `NO_RANK`.
SPF5 is not a culture accession or evidence of a named species,
validly published binomial, type strain or functional property.

## Evidence

The NCBITAXON / NCBITaxon:1303827 / 1 NAME attestation matches the
backbone row and its 2026-09-13 taxonomy snapshot. NAME counts source
coverage, not biological strains or genomes. No DOI, PMID, assembly
identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106265` pins the slug.
`curation/seed_scope.tsv:393107` admits the target on 2026-09-13 with
the exact one-source reason reproduced by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is retained;
this report does not grant human-reviewed status.

## Completeness

Ignored-inclusive, case-insensitive searches by ID, label, slug and SPF5
covered `data/raw/`, `curation/` and `history/`, finding only the
backbone and scope rows. Complete exact-field membership scans found
no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
row. There are no descendants to contribute additional strains, so
zero strains is supported at the full BacDive inventory boundary.

A broad native substring search produced many longer SPF names and its
output was truncated. It was not used to establish exhaustive absence.
The search was rerun to completion with whole-token matching, still
case-insensitive and ignored-inclusive, over all compressed native JSONL
files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/` and `data/straininfo/`. Its only match
was the target scientific-name object, with untruncated output.

Inspected examples from the broader search explain the exclusion:
BV-BRC 446.1416 at `data/bvbrc/bvbrc-0020.jsonl.gz:19483` is
Legionella pneumophila SPF590, taxon 446, not SPF5; BV-BRC 1351.8361
at `data/bvbrc/bvbrc-0002.jsonl.gz:28962` is Enterococcus faecalis
EfsPF5, taxon 1351. The complete numeric-hit object
`GCA_023319845.1` at `data/catalog/ncbi_genbank-0021.jsonl.gz:29034`
is Salmonella enterica taxon 28901, with assembly name PDT001303827.1.
None identifies the Saccharopolyspora target. No claim is made to have
read every unrelated object hidden by the initial output truncation.

Additional complete, ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. They found no target
ID, label, slug or SPF5 token. The raw-directory search included all
assembly/genome/related inventories. No eligible culture-deposit or
BioSample source chain was established.

These bounded checks justify empty optional nomenclature, mappings and
genome links; they do not assert that no isolates or sequences exist
elsewhere. No functional gene, regulator, pathway, trait or transcriptomics
dataset is asserted; iModulonDB is not applicable. No causal graph is
required for an identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the exact source spelling, supported backbone
and `SEEDED` status. Future source-backed enrichment belongs in
maintained extraction inputs or `src/taxonmech/extract.py`, with
changed seeding behavior in `src/taxonmech/seed.py` and regression
tests. Do not patch generated YAML or join partial strain labels.

## Follow-up Checks

No finding-specific check remains. New source evidence requires exact
taxon/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Any corpus change also requires
`just verify-corpus` and full QC, neither claimed by this focused pass.

## Additional Notes

Absence checks included ignored files using full structured reads,
`find`, and `rg --no-ignore --hidden`, with `-z` for compressed sources
and `-i -w` for the completed native/overlay token searches. Public
NCBI API reads used network escalation after established sandbox DNS
failures. All process handles were polled to completion.

The only manual write is this new report; strict validation wrote its
standard diagnostic. No record, source, earlier report, history or status
was edited. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
