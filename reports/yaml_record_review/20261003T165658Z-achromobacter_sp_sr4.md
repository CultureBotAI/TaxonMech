# YAML Record Review: Achromobacter sp. SR4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/achromobacter_sp_sr4.yaml`
- Started UTC: 2026-10-03T16:54:58Z
- Finished UTC: 2026-10-03T16:56:58Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303833`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2626865`, genetic code 11, grounding `EXACT`, status
`SEEDED`. Ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event are present. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/achromobacter_sp_sr4.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/achromobacter_sp_sr4.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  genetic code and all ten lineage objects. No target children occur.
  Complete exact-field scans find no target membership in the seven other
  source inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308166` supplies the exact Achromobacter
SR4 label, species rank, unclassified-Achromobacter parent, code and
empty synonym fields. The full scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30717` agrees. Every root-first
ancestor matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303833&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2626865,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303833)
confirms rank and all ten ancestor IDs including root. Betaproteobacteria,
Burkholderiales and Alcaligenaceae agree in pinned and live sources.
Exact grounding to this NCBI entity is supported.

Keep NCBI's species rank and the direct unclassified parent's `NO_RANK`.
SR4 is a reused bare designation, not a unique collection accession.
It supplies no basis for assigning a named species, type status,
validly published binomial or phenotype to this record.

## Evidence

The NCBITAXON / NCBITaxon:1303833 / 1 NAME attestation matches the
backbone row and its 2026-09-13 taxonomy snapshot. NAME describes
source coverage, not a biological strain or genome count. No DOI,
PMID, assembly identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106271` pins the slug.
`curation/seed_scope.tsv:393113` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is retained;
no human-review status is claimed or granted.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SR4 covered raw inventories, curation and history.
Full exact-field scans found no direct BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits membership for this target. There are
no descendants to contribute BacDive strains, supporting the zero count.

Two complementary ignored-inclusive native searches covered all compressed
JSONL catalogs under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/` and `data/straininfo/`:

- Target ID, full label and slug matches were read as full objects.
  Only the scientific-name object was target evidence. Numeric matches
  were genome-size fields in unrelated assemblies, described below.
- The complete SR4 token search was parsed through ripgrep JSON output
  and native JSON objects. It returned 76 matched lines. Identity fields
  were inspected for every match without output truncation; Achromobacter
  matches were emitted in full. The only Achromobacter object was the
  target name. Other objects were excluded by their explicit organism,
  taxonomy, deposit or project identity. This was not a full review of
  those other records or their biological claims.

Important bare-designation collisions and exclusions include:

| Source evidence | Different identity and reason for exclusion |
| --- | --- |
| BacDive 16844, `data/raw/bacdive_strains.tsv:16660`; full native object `data/bacdive/records.jsonl.gz:16659` | Thermoanaerobacter siderophilus, taxon 106578, deposit DSM 12299. Its SR4 genome taxon 880478 and type flag do not concern Achromobacter. |
| StrainInfo identity/deposit fields, `data/straininfo/records.jsonl.gz:37130` | SI-ID 49268, own deposit SI-DP 163114 / DSM 12299, Thermoanaerobacter siderophilus taxon 106578. |
| Native NCBI, GTDB and BV-BRC identity fields for GCA/GCF_000517725.1 | Streptococcus sp. SR4, taxon 1161417, not Achromobacter. NCBI objects are at `data/catalog/ncbi_genbank-0000.jsonl.gz:16961` and `ncbi_refseq-0000.jsonl.gz:14092`. |
| Native identity fields for GCA/GCF_012641475.1 | Flammeovirga agarivorans SR4, taxon 2726742, including `data/catalog/ncbi_genbank-0011.jsonl.gz:17896`; its old Flammeovirga sp. SR4 name is likewise distinct. |
| Native identity fields for GCA/GCF_020295515.1 | Pectobacterium versatile SR4, taxon 2488639, including `data/catalog/ncbi_genbank-0018.jsonl.gz:33806`. |
| Native identity fields at `data/catalog/ncbi_genbank-0018.jsonl.gz:33697` | GCA_020293345.1, E. coli isolate SR4, taxon 562. |
| StrainInfo identity/deposit fields at `data/straininfo/records.jsonl.gz:2459` and line 153964 | Pectobacterium atrosepticum Graham SR4/1 and Tetraselmis SR4.BC 103/2 are different records. The latter was excluded as a source hit, not re-reviewed as a Eukaryota YAML. |

Other inspected native identity fields name Halomonas, Polaromonas,
Micromonospora, Desulfovibrio, Priestia and longer SR4-prefixed names in
several genera, including Lacticaseibacillus SR4-4, SR4-8 and SR4-9.
Those explicit identities do not establish a target association. The
raw Thermoanaerobacter assembly/genome/related rows are attached to
BacDive 16844 and its own GOLD chain, not this target.

GOLD's SR4 organism/project/analysis identity fields likewise name
Thermoanaerobacter, Streptococcus, Flammeovirga or Pectobacterium.
The full project object at `data/gold/projects.jsonl.gz:505417`,
Gp0674088, describes an environmental sediment-community project,
PRJNA671745 / SAMN17154527, with no organism GOLD ID. A project
sample named SR4 is not an identified Achromobacter culture.

Full numeric-match objects were also excluded:
GCA_000435375.1 at `data/catalog/ncbi_genbank-0000.jsonl.gz:13297`,
its GTDB object at `gtdb_genomes-0004.jsonl.gz:6169` and historical
RefSeq object at `ncbi_refseq_historical-0000.jsonl.gz:4046` identify
Clostridium sp. CAG:798, taxon 1262841, with total length 1303833.
GCA_965326725.1 at `ncbi_genbank-0064.jsonl.gz:17357` identifies
Clostridia bacterium taxon 2044939, with ungapped length 1303833.
Lengths do not supply taxon-ID matches.

Additional complete ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. The one ATB match,
SAMN02344625 at catalog line 1020562, has source name Streptococcus
sp. SR4 and classification Streptococcus salivarius. Its full row was
read and excluded; neither name supports an Achromobacter association.
No eligible target deposit/BioSample chain was established.

Empty optional nomenclature, mappings and genome links are justified
at the checked source boundary, not proof that no isolates or sequences
exist elsewhere. No gene, regulator, pathway, trait or transcriptomics
dataset is asserted; iModulonDB is not applicable. No causal graph is
required for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep the supported backbone and `SEEDED` status.
Future enrichment belongs in maintained extraction inputs or
`src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML, join bare SR4 labels across conflicting taxa or interpret numeric
assembly fields as taxon references.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
Achromobacter identity and primary deposit/sample provenance, followed
by authorized dry-run/canary steps and both focused validators after
regeneration. Any corpus change also requires `just verify-corpus` and
full QC, neither claimed by this focused pass.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w`, with structured JSON
inspection for the larger SR4 result set. Projections were used only
to inspect explicit identities of unrelated source hits, not in place
of reading the entire target YAML or its positive source evidence.
Public NCBI requests used network escalation after established sandbox
DNS failures. All search processes completed.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. No Eukaryota record was re-reviewed.
