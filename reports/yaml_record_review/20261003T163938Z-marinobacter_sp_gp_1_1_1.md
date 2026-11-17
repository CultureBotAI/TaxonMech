# YAML Record Review: Marinobacter sp. Gp-1-1.1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marinobacter_sp_gp_1_1_1.yaml`
- Started UTC: 2026-10-03T16:38:26Z
- Finished UTC: 2026-10-03T16:39:38Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303825`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:83889`, genetic code 11, grounding `EXACT`, status `SEEDED`.
It carries ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event. No synonyms, nomenclature, mappings,
equivalence xrefs, strain/genome links, experimental claims or causal
graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marinobacter_sp_gp_1_1_1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marinobacter_sp_gp_1_1_1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  genetic code and all ten lineage objects. No target children occur.
  Complete exact-field scans find no target membership in the seven other
  source inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated-site
  drift, exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308158` supplies the exact label, species
rank, unclassified-Marinobacter parent, code and empty synonym fields.
The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30709` agrees. The ten-entry
root-first lineage matches the pinned NCBI backbone.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303825&retmode=xml)
confirms identity, species rank, Bacteria division, parent 83889,
code 11 and the full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303825)
confirms rank and all ten ancestor IDs including root. The Pseudomonadales
order and Marinobacteraceae family agree in the pinned and live sources.
Exact grounding to this NCBI entity is supported.

Keep NCBI's species rank and the direct unclassified parent's `NO_RANK`.
The designation is not a culture accession, evidence of a validly
published binomial or permission to assign a named species. Do not
infer habitat, phenotype or type status from the genus or designation.

## Evidence

The NCBITAXON / NCBITaxon:1303825 / 1 NAME attestation matches the
backbone row and its 2026-09-13 taxonomy snapshot. NAME is a source
count, not a strain or genome count. No DOI, PMID, assembly identifier
or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106263` pins the slug.
`curation/seed_scope.tsv:393105` admits the target on 2026-09-13 with
the exact one-source reason reproduced in the embedded seed event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and the NCBITAXON source list agree. `SEEDED` is
retained; this automated review does not grant human-reviewed status.

## Completeness

Ignored-inclusive searches by ID, label, slug and Gp-1-1.1 covered raw
inventories, curation, history and all compressed native JSONL catalogs
under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. Only the scientific-name object
was native target evidence. Complete exact-field BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin and BactoTraits membership scans found no target
row. Zero descendants and zero BacDive membership support strain count
zero at the complete inventory boundary.

The broad numeric search returned unrelated source objects, all read in
full and excluded on their own identity fields:

| Accession or record | Actual identity | Inspected native locations |
| --- | --- | --- |
| GCA_001303825.1; BV-BRC 1703359.3; GOLD Ga0111181 | Gemmatimonas sp. SM23_52, NCBI taxon 1703359 in NCBI/BV-BRC | `data/catalog/ncbi_genbank-0000.jsonl.gz:48886`; `data/bvbrc/bvbrc-0005.jsonl.gz:18188`; `data/gold/analyses.jsonl.gz:61166` |
| GCA_041303825.1; BV-BRC 2026762.103 | Micrococcales bacterium PPR_0130, taxon 2026762 | `data/catalog/ncbi_genbank-0037.jsonl.gz:38658`; `data/bvbrc/bvbrc-0011.jsonl.gz:13731` |
| GCA/GCF_051303825.1; RS_GCF_051303825.1 | Klebsiella pneumoniae TB083-B, taxon 573 | `data/catalog/ncbi_genbank-0047.jsonl.gz:18852`; `ncbi_refseq-0007.jsonl.gz:35744`; `gtdb_genomes-0006.jsonl.gz:2207` |
| GCA_023326245.1 | Salmonella enterica, taxon 28901; assembly name PDT001303825.1 | `data/catalog/ncbi_genbank-0021.jsonl.gz:29340` |
| GCA_901303825.1 | Streptococcus pneumoniae, taxon 1313 | `data/catalog/ncbi_genbank-0057.jsonl.gz:25767` |

Digits in assembly accessions and names do not establish a Marinobacter
taxon association. GOLD's matching accession points to the Gemmatimonas
analysis, not this record; no project-chain inference was needed to
exclude that explicitly different organism.

Further ignored-inclusive searches covered `data/atb/`, the complete
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. The sole ATB numeric
hit, SAMN30567365 with run SRR21303825, is Salmonella enterica; its
full row was read and excluded. No eligible target association was
found. Raw assembly/genome/related tables were included in the raw search.

No culture-deposit or BioSample source chain was established. Empty
optional nomenclature, mappings and genome links are supported at the
checked boundary, not proof that no isolates or sequences exist elsewhere.
No gene, regulator, pathway, trait or transcriptomics dataset is asserted;
iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported NCBI backbone and `SEEDED`
status. Future source-backed enrichment belongs in maintained extraction
inputs or `src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated YAML
or use numeric substrings as join keys.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
identity/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Any corpus change also requires
`just verify-corpus` and full QC; this focused pass does not claim those
unrun corpus-wide gates passed.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, and `rg --no-ignore --hidden`, using `-z` for compressed sources.
Public read-only NCBI API requests used network escalation after
established sandbox DNS failures. The only manual write is this report;
strict validation wrote its standard diagnostic. No record, source,
prior report, history or status was edited. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. Eukaryota
was not re-reviewed.
