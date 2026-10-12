# YAML Record Review: Sulfitobacter sp. Gp-4-5.2.1-voll

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sulfitobacter_sp_gp_4_5_2_1_voll.yaml`
- Started UTC: 2026-10-03T16:41:22Z
- Finished UTC: 2026-10-03T16:42:33Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303826`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:196795`, genetic code 11, grounding `EXACT`, status `SEEDED`.
It has ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event. No synonyms, nomenclature, mappings,
equivalence xrefs, strain/genome links, experimental claims or causal
graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sulfitobacter_sp_gp_4_5_2_1_voll.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/sulfitobacter_sp_gp_4_5_2_1_voll.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and all ten lineage objects. No target children occur. Complete
  exact-field scans find no membership in the seven other source
  inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308159` matches the exact label, species
rank, unclassified-Sulfitobacter parent, code and empty synonym fields.
The complete scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30710` independently agrees.
Every root-first ancestor matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303826&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 196795,
code 11 and the full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303826)
confirms rank and all ten ancestor IDs including root. Alphaproteobacteria,
Rhodobacterales and Roseobacteraceae agree in pinned and live sources.
Exact grounding to this NCBI entity is supported.

Preserve NCBI's species rank and its direct unclassified parent's
`NO_RANK`. The Gp designation is not a culture accession or evidence
for a named species, validly published binomial, type strain or phenotype.

## Evidence

The NCBITAXON / NCBITaxon:1303826 / 1 NAME attestation matches the
backbone row and the 2026-09-13 snapshot. NAME counts source coverage,
not biological strains or genomes. No DOI, PMID, assembly accession
or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106264` pins the slug.
`curation/seed_scope.tsv:393106` admits the target on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. The record remains `SEEDED`;
this review does not claim human sign-off.

## Completeness

Ignored-inclusive searches by ID, label, slug and Gp-4-5.2.1-voll
covered raw inventories, curation, history and all compressed native
JSONL catalogs under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/` and `data/straininfo/`. Only the target
scientific-name object was native target evidence. Complete exact-field
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits membership
scans found no row. Zero descendants and zero BacDive membership support
the uncapped strain count of zero.

Two numeric GenBank hits were read in full and excluded:
`GCA_023327945.1` at `data/catalog/ncbi_genbank-0021.jsonl.gz:29425`
is Salmonella enterica taxon 28901, with assembly name PDT001303826.1;
`GCA_013038265.1` at `ncbi_genbank-0011.jsonl.gz:36311` is E. coli
taxon 562, isolate WFJW09. Neither is this Sulfitobacter taxon.

Additional ignored-inclusive searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. The sole ATB substring
hit, SAMN30567362 with run SRR21303826, is Salmonella enterica; its
full row was read and excluded. No target association or eligible
culture-deposit/BioSample source chain was found. Raw assembly/genome/
related inventories were included in the raw-directory search.

Empty optional nomenclature, mappings and genome links are justified at
the checked source boundary, not evidence that no isolates or sequences
exist elsewhere. No gene, regulator, pathway, trait or transcriptomics
dataset is asserted; iModulonDB is not applicable. No causal graph is
required for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported NCBI identity, lineage and
`SEEDED` status. Future source-backed enrichment belongs in maintained
extraction inputs or `src/taxonmech/extract.py`, with changed seeding
behavior in `src/taxonmech/seed.py` and regression tests. Do not patch
generated YAML or borrow a neighboring taxon's evidence.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
taxon/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Corpus changes also require
`just verify-corpus` and full QC, neither claimed by this focused pass.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, and `rg --no-ignore --hidden`, with `-z` for compressed sources.
Read-only NCBI API requests used network escalation after established
sandbox DNS failures. The only manual write is this new report; strict
validation wrote its standard diagnostic. No record, source, earlier
report, history or status was changed. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. No Eukaryota
record was re-reviewed.
