# YAML Record Review: Achromobacter sp. SR5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/achromobacter_sp_sr5.yaml`
- Started UTC: 2026-10-03T16:58:43Z
- Finished UTC: 2026-10-03T17:02:46Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303834`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2626865`, genetic code 11, grounding `EXACT`, and mapping
status `SEEDED`. Ten lineage entries, one NCBI NAME attestation,
zero strains and one embedded seed event are present. No synonyms,
nomenclature, taxonomy mappings, equivalence xrefs, strain/genome links,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/achromobacter_sp_sr5.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/achromobacter_sp_sr5.yaml`:
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

`data/raw/ncbitaxon_taxa.tsv:308167` supplies the exact Achromobacter
SR5 label, species rank, unclassified-Achromobacter parent, genetic code
and empty synonym fields. The complete scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30718` agrees. Every root-first
ancestor matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303834&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2626865,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303834)
confirms rank and all ten ancestor IDs including root. Betaproteobacteria,
Burkholderiales and Alcaligenaceae agree in pinned and live sources.
Exact grounding to this NCBI entity is supported.

Keep NCBI's species rank and the direct unclassified parent's `NO_RANK`.
SR5 is a reused bare designation, not a unique collection accession.
It does not establish a named species, type status, validly published
binomial or phenotype for this record.

## Evidence

The NCBITAXON / NCBITaxon:1303834 / 1 NAME attestation matches the
backbone row and its 2026-09-13 taxonomy snapshot. NAME describes
source coverage, not a biological strain or genome count. No DOI,
PMID, assembly identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106272` pins the slug.
`curation/seed_scope.tsv:393114` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is retained;
no human-review status is claimed or granted.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SR5 covered raw inventories, curation and history.
Full exact-field scans found no direct BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits membership for this target. There are
no descendants to contribute BacDive strains, supporting the zero count.

Two complementary ignored-inclusive native searches covered all compressed
JSONL catalogs under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/` and `data/straininfo/`:

- Target ID, full label and slug returned only the complete NCBI
  scientific-name object described above.
- The complete SR5 token search was parsed through ripgrep JSON output
  and native JSON objects. It returned 61 matched lines. Identity fields
  were inspected for every match without output truncation; objects
  containing Achromobacter were emitted in full. The only such object
  was the target name. Other objects were excluded by their explicit
  organism, taxonomy, deposit or project identity. This was not a full
  review of those other records or their biological claims.

Important bare-designation collisions and exclusions include:

| Source evidence | Different identity and reason for exclusion |
| --- | --- |
| BacDive 2712, `data/raw/bacdive_strains.tsv:2613`; full native object `data/bacdive/records.jsonl.gz:2612` | Clostridium sporogenes, taxon 1509, designation SR 5 / SR5, with deposits DSM 1664, ATCC 19404 and NCTC 532. It is explicitly not a type strain. Its genome accessions belong to Clostridium, not Achromobacter. |
| StrainInfo identity/deposit fields, `data/straininfo/records.jsonl.gz:1974` | SI-ID 1974, BacDive 2712, Clostridium sporogenes taxon 1509. Its own ATCC 19404, NCTC 532 and DSM 1664 deposits and unversioned GCA_001573855 / GCA_011019475 do not establish a target association. |
| StrainInfo identity/deposit fields, `data/straininfo/records.jsonl.gz:30807` | SI-ID 42592, BacDive 13713, Paracoccus aminovorans taxon 34004, aliases SR5 / DM-82, own JCM 7685 and DSM 8537 deposits. Its markers and unversioned GCA_900005615 / GCA_900113565 concern Paracoccus. |
| Native NCBI, GTDB and BV-BRC identity fields for GCA/GCF_000241785.1 | Aliivibrio fischeri SR5, taxon 1088719, including `data/catalog/ncbi_genbank-0000.jsonl.gz:4596` and `ncbi_refseq-0000.jsonl.gz:3909`; the older Vibrio fischeri name is also distinct. |
| Native identity fields for GCA/GCF_020295605.1 | Pectobacterium brasiliense SR5, taxon 180957, including `data/catalog/ncbi_genbank-0018.jsonl.gz:33810` and `ncbi_refseq-0003.jsonl.gz:42969`. |
| Native identity fields for GCA_011754295.1 and its historical RefSeq counterpart | Lactobacillus sp. L. sR5, taxon 2717813, including `data/catalog/ncbi_genbank-0010.jsonl.gz:24455`. |
| Native identity fields at `data/catalog/ncbi_genbank-0009.jsonl.gz:41690` | GCA_011074085.2, Salmonella enterica serovar Inverness FL_UFL-SR5, taxon 913074. The older .1 object is likewise not Achromobacter. |
| Native identity fields at `data/catalog/ncbi_genbank-0026.jsonl.gz:29569`, line 29570 and line 29572 | Lacticaseibacillus rhamnosus taxon 47715, isolates SR5-6, SR5-5 and SR5-9, accessions GCA_028579135.1, GCA_028579145.1 and GCA_028579195.1. |

Other inspected NCBI name fields and raw rows identify Methylomonas
scandinavica SR5, taxon 85583; Streptococcus sp. SR5, taxon 1161418;
and SR5 designations or longer prefixed names in several other genera.
Those explicit identities do not establish an Achromobacter association.

GOLD organism/project/analysis identity fields similarly identify
Aliivibrio (Go0014273), Streptococcus (Go0020640), Methylomonas
(Go0024946), Clostridium (Go0254650) or Lactobacillus (Go0541262).
The full project object at `data/gold/projects.jsonl.gz:505418`,
Gp0674089, describes an environmental sediment-community project,
PRJNA671745 / SAMN17154528, with no organism GOLD ID. A project
sample named SR5 is not an identified Achromobacter culture.

Additional complete ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. No ID, full-label,
slug or SR5 token match occurred in that boundary. No eligible target
deposit/BioSample chain was established.

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
YAML or join bare SR5 labels across conflicting taxa.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
Achromobacter identity and primary deposit/sample provenance, followed
by authorized dry-run/canary steps and both focused validators after
regeneration. Any corpus change also requires `just verify-corpus` and
full QC, neither claimed by this focused pass.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w`, with structured JSON
inspection for the larger SR5 result set. Projections were used only
to inspect explicit identities of unrelated source hits, not in place
of reading the entire target YAML or its positive source evidence.
Public NCBI requests used network escalation after established sandbox
DNS failures. All search and validation processes completed.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. No Eukaryota record was re-reviewed.
