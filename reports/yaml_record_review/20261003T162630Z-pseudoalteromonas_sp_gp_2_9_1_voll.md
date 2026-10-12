# YAML Record Review: Pseudoalteromonas sp. Gp-2-9.1-voll

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_gp_2_9_1_voll.yaml`
- Started UTC: 2026-10-03T16:25:16Z
- Finished UTC: 2026-10-03T16:26:30Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`. It denotes `NCBITaxon:1303818`,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:194690`, genetic
code 11, grounding `EXACT`, status `SEEDED`. It carries ten lineage
entries, one NCBI NAME attestation, strain count zero and one embedded
seed event. No synonyms, nomenclature, taxonomy mappings, equivalence
xrefs, strain entries, genome links, experimental claims or causal graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudoalteromonas_sp_gp_2_9_1_voll.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudoalteromonas_sp_gp_2_9_1_voll.yaml`:
  PASS; one file, zero errors. Diagnostic:
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and every lineage object. There are no target children. Exact-field
  scans of all seven other source membership inventories found no target
  membership. PATHS and scope each contain one matching row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no target standalone event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308151` supplies the precise spelling,
species rank, unclassified-Pseudoalteromonas parent, code and empty
synonym fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30702` agrees. The root-first
lineage is the pinned NCBI parent chain, not an inferred placement.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303818&retmode=xml)
confirms identity, species rank, Bacteria division, parent 194690,
code 11 and the full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303818)
confirms rank and all ten ancestor IDs including root. The exact NCBI
grounding is supported.

The designation does not justify converting the source rank to STRAIN,
assigning a named species or claiming a validly published binomial.
`EXACT` grounds this particular NCBI entity, not another member of the
genus. The unclassified parent correctly retains `NO_RANK`.

## Evidence

The NCBITAXON / NCBITaxon:1303818 / 1 NAME attestation matches the
backbone row and its 2026-09-13 taxonomy snapshot. A NAME count is not
evidence for a deposit, genome, phenotype or mechanism. There are no
asserted DOI, PMID, assembly identifiers or experimental quotations to
verify.

`data/taxa/PATHS.tsv:106256` pins the current slug.
`curation/seed_scope.tsv:393098` admits the target on 2026-09-13 with
the one-source reason reproduced in the embedded event. That event is
dated 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES. Its source list and `SEEDED` status agree; no
human review is claimed.

## Completeness

Ignored-inclusive searches by ID, label, slug and Gp-2-9.1-voll covered
`data/raw/`, `curation/`, `history/` and all compressed native JSONL
files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/` and `data/straininfo/`. The only target
native object found was its NCBI scientific name. Full structured
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits membership
scans found no target row. With no descendants, strain count zero is
consistent with the complete BacDive membership boundary.

The native numeric search also returned two unrelated GenBank objects,
both read in full: `GCA_023321795.1` at
`data/catalog/ncbi_genbank-0021.jsonl.gz:29132`, Salmonella enterica
taxon 28901, has the digits in its assembly name; `GCA_013038185.1`
at `ncbi_genbank-0011.jsonl.gz:36307`, E. coli taxon 562, has the
digits in its accession. Neither is target evidence.

Additional ignored-inclusive searches covered `data/atb/`, the complete
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. Two ATB substring hits
were also excluded after reading their rows: SAMN21217572 is E. coli
with the digits in a SeqKit sum; SAMN30567358 is Salmonella enterica
with the digits in SRR21303818. No eligible target association was found.
Raw assembly/genome/related inventories were included in the raw search.

These bounded results justify empty optional mappings, nomenclature,
strains and genome links; they do not assert that no sequences or
biological isolates exist elsewhere. No culture-deposit or BioSample
chain was established. No named gene, regulator, pathway, trait or
transcriptomics dataset is asserted, so iModulonDB is not applicable.
An identity-only record does not require a causal graph.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported NCBI backbone and `SEEDED`
status. Future source-backed enrichment belongs in maintained extraction
inputs or `src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated YAML
or transfer a nearby taxon's evidence.

## Follow-up Checks

No finding-specific check is outstanding. New evidence requires exact
identity/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Any corpus change also requires
`just verify-corpus` and full QC; this focused pass does not claim those
unrun gates passed.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, and `rg --no-ignore --hidden`, using `-z` for compressed sources.
Public NCBI API reads used network escalation after established sandbox
DNS failures. No authentication, paid research or provider credits were
used.

The only manual write is this new report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or review
status was edited. No generator, refresh, GitHub action or cross-repository
write occurred. No Eukaryota record was re-reviewed.
