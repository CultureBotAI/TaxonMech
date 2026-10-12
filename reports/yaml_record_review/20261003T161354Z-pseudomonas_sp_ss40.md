# YAML Record Review: Pseudomonas sp. SS40

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_ss40.yaml`
- Started UTC: 2026-10-03T16:12:33Z
- Finished UTC: 2026-10-03T16:13:54Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303815`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:196821`, genetic code 11, grounding `EXACT`, status `SEEDED`.
Ten lineage entries, one NCBI NAME attestation, strain count zero and
one embedded seed event are present. No synonyms, nomenclature, taxonomy
mappings, equivalence xrefs, strain rows, genome links, experimental claims
or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_ss40.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_ss40.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and all ten lineage entries. The target has no children in the
  pinned backbone. Complete exact-field inventory scans find no direct
  BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits taxon
  membership. The PATHS index and scope each have one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive searches found no target standalone history entry;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308148` supports the ID, scientific name,
species rank, parent, code 11 and empty synonym fields. The complete
native name object at `data/catalog/ncbi_names-0007.jsonl.gz:30697`
agrees.

The NCBI browser page was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303815&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 196821,
code 11 and full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303815)
confirms rank and all ten ancestor IDs including root. Read-only public
API calls used network escalation after established sandbox DNS failures.

The parent is NCBI's unclassified Pseudomonas grouping, rank `NO_RANK`.
Preserve this exact chain and species rank rather than interpreting the
SS40 designation as a different rank or a named-species identification.
`EXACT` grounds the NCBI entity; it does not assert a validly published
binomial or equivalence to another organism using SS40.

## Evidence

The NCBITAXON / NCBITaxon:1303815 / 1 NAME attestation matches
the 2026-09-13 backbone row and native name object. One NAME is a source
count, not an experimental observation, strain count or genome count.
No DOI, PMID, source accession or experimental quotation is present.

`curation/seed_scope.tsv:393096` admits the taxon on 2026-09-13 with
one source. The same reason and source name appear in the event dated
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES. The event is consistent with `SEEDED` and makes
no human-review claim.

## Completeness

Ignored-inclusive searches used the target ID, full label, slug and SS40
across `data/raw/`, `curation/`, `history/` and all compressed JSONL
files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/`. Matching native objects were read
in full. The following unrelated uses of SS40 were excluded:

- Obesumbacterium sp. SS40, taxon 1867554, has a separate backbone
  row at `data/raw/ncbitaxon_taxa.tsv:488250`, scope row at
  `curation/seed_scope.tsv:545484` and native name object at
  `data/catalog/ncbi_names-0011.jsonl.gz:27040`.
- Streptococcus suis SS40, taxon 1307, has the identical
  GCA/GCF_900052855.1 pair and sample SAMEA1566052. Complete objects
  at `data/catalog/ncbi_genbank-0056.jsonl.gz:35197`,
  `data/catalog/ncbi_refseq-0009.jsonl.gz:23272`,
  `data/catalog/gtdb_genomes-0014.jsonl.gz:44449` and
  `data/bvbrc/bvbrc-0001.jsonl.gz:27775` identify that organism, not
  this Pseudomonas taxon. Its BV-BRC genome is 1307.700. The separate
  GOLD chain Go0142798 -> Gp0148231 -> Ga0130552, IMG 2734482692,
  appears at `data/gold/organisms.jsonl.gz:82055`,
  `data/gold/projects.jsonl.gz:93688` and
  `data/gold/analyses.jsonl.gz:76800`.
- Salmonella enterica SS40, taxon 28901, is represented by BV-BRC
  28901.38976 at `data/bvbrc/bvbrc-0017.jsonl.gz:6426` and
  GCA_049944295.1 at `data/catalog/ncbi_genbank-0046.jsonl.gz:4181`,
  sample SAMN47997955 and project PRJNA1251116.
- GOLD Gp0054055 at `data/gold/projects.jsonl.gz:38416` describes
  a Sargasso Sea microbial-community sample SS40-2, SAMN09092767,
  PRJNA464480, not an isolate identity for this record.

No target BacDive strain, LPSN inventory name, GTDB mapping/genome,
NCBI assembly, BV-BRC genome, GOLD organism, SeqCode name or StrainInfo
native object was established in the checked catalogs. Full BacDive
membership and the singleton subtree support strain count zero, not
biological absence or absence of sequences elsewhere. The unrelated
strain names cannot supply a culture-deposit or genome join.

Additional ignored-inclusive searches of StrainInfo link, assembly and
exclusion TSVs, its compressed related-record table, `data/atb/` and the
complete `data/catalog/allthebacteria.tsv.xz` found no target ID, label,
slug or SS40 match. Raw assembly/genome/related tables were covered by
the raw-directory search. No target BioSample or eligible source chain
was discovered. These misses are bounded to pinned sources.

The optional nomenclature, synonym, mapping and strain fields are
correctly empty at this source boundary. No named gene, locus, regulator,
pathway, trait or transcriptomics dataset is asserted; iModulonDB is not
applicable. No phenotype, type status or causal graph should be inferred
from the genus or from another organism sharing SS40.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required by this review. Preserve NCBI's identity and classification.
Future source-backed enrichment belongs to maintained extraction inputs
or `src/taxonmech/extract.py`, with changed derivations in
`src/taxonmech/seed.py` and regression coverage. Do not hand-edit generated
YAML, merge designation-only matches or promote human-review status.

## Follow-up Checks

No finding-specific follow-up is outstanding. Future evidence must first
resolve exact identity and any deposit/sample/genome chain. Use authorized
dry-run/canary steps and rerun both focused validators after regeneration.
Any corpus change also requires `just verify-corpus` and full QC. This
focused passing verdict does not imply the unrun corpus-wide checks passed.

## Additional Notes

The only manual write is this report; strict validation wrote its standard
diagnostic. Absence checks included ignored files using full structured
reads, `find`, and `rg --no-ignore --hidden`, with `-z` for compressed
sources. No record, source, prior report, history or status was edited.
No generator, source refresh, paid research, GitHub mutation or
cross-repository write occurred. No Eukaryota record was re-reviewed.
