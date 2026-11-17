# YAML Record Review: Parafrankia sp. EUN1f

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/parafrankia_sp_eun1f.yaml`
- Started UTC: 2026-10-03T19:44:34Z
- Finished UTC: 2026-10-03T19:46:11Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:102897`,
Parafrankia sp. EUN1f. Rank is `SPECIES`, domain `BACTERIA`,
parent `NCBITaxon:2994368`, genetic code 11, grounding `EXACT`,
mapping status `SEEDED`. The record has ten lineage entries, one
GTDB mapping, two source-attributed synonyms, one xref, zero strains,
three attestations and one seed event. It asserts no nomenclature,
strain-genome relationships, explicit phenotypes or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/parafrankia_sp_eun1f.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/parafrankia_sp_eun1f.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison matched identity, rank,
  parent, code and all ten lineage objects; no children were found.
  Complete source-inventory scans, scope/path rows, source counts,
  synonyms and embedded seed reason were checked and agree.
- `just verify-corpus`: Not checked; full-corpus-only. The bounded
  comparisons are not a substitute. Full QC, global provenance/hash
  replay, rendered products and exports were not audited. Primary
  archives and genome FASTAs were not downloaded or verified.
- Ignored-inclusive ID, label and slug searches found no standalone
  target history event. Strict validation checked the embedded event;
  standalone history validation had no target. Graph/product gates
  are not applicable because there is no graph.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18163` supplies the current identity
and the exact synonym Frankia sp. EUN1f. The complete native name
objects at `data/catalog/ncbi_names-0000.jsonl.gz:38169` and
line 38170 classify the former name as equivalent and Parafrankia
sp. EUN1f as scientific. There are no related/broad synonyms or
retirement target in the inventory row.

Inspected live
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102897&retmode=xml)
explicitly confirms the current name, the Frankia equivalent name,
species rank, code and parent.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/102897)
confirms all ten ancestor IDs, including root. The chain is root,
cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes,
Frankiales, Frankiaceae, Parafrankia and unclassified Parafrankia.
The genus is 2994362, not Frankia 1854. Exact grounding is supported;
the isolate-like designation does not override the source species rank.

## Evidence

**GTDB classification.** `data/raw/gtdb_mappings.tsv:1247` and
`gtdb_species.tsv:136885` support
`GTDB:s__Parafrankia_sp000177675`, its source label,
`skos:closeMatch` and count 1. An ignored-inclusive search across
the complete GTDB native catalog returns exactly one species member,
read fully at `data/catalog/gtdb_genomes-0015.jsonl.gz:25180`.
It is representative RS_GCF_000177675.1 and explicitly supplies
taxon/species 102897, EUN1f, GCA_000177675.1, SAMN02441797,
PRJNA224116 and the matching Parafrankia species classification.

The mapping therefore supports the GTDB-attributed exact synonym
Parafrankia sp000177675 and xref under the source mapping policy
in `src/taxonmech/seed.py:437`. It does not replace NCBI's lineage
or create a nomenclatural authority/type-strain claim. The genome
count is a GTDB species membership count, not a culture count.

**NCBI and BV-BRC genome context.** The complete native GenBank
and RefSeq objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:2503`
and `ncbi_refseq-0000.jsonl.gz:2201` explicitly identify
GCA_000177675.1 and GCF_000177675.1 as paired assemblies,
taxon 102897, strain EUN1f, contig-level assembly, BioSample
SAMN02441797 and source-specific projects PRJNA38795 and
PRJNA224116. Their annotation counts differ and were not promoted
to taxon-level biological assertions.

Inspected live
[NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000177675.1/dataset_report)
confirms the current GenBank accession, explicit current RefSeq
partner, source strain, BioSample, project and assembly level.
Pairing was not inferred by prefix substitution. Its nearest ANI
match to another Parafrankia species does not establish identity
with that species or license a nomenclature transfer. BioSample
phenotype attributes were not imported or treated as proof of the
Madin inventory's eight separate assertions.

The complete BV-BRC object at
`data/bvbrc/bvbrc-0000.jsonl.gz:3002` names genome 102897.3,
the former Frankia sp. EUN1f label, current Parafrankia lineage,
GCA_000177675.1, SAMN02441797, PRJNA38795 and ADGX00000000.
Its older display label is consistent with the inspected NCBI
equivalent name, not evidence of a different organism.

**GOLD chain and culture boundary.** Complete primary objects at
`data/gold/organisms.jsonl.gz:3915`, `projects.jsonl.gz:3943`
and `analyses.jsonl.gz:15955` preserve
Go0004420 -> Gp0004420 -> Ga0025097. The organism explicitly
names EUN1f and 102897, the project supplies PRJNA38795 and
SAMN02441797, and the analysis supplies GCA_000177675.1,
ADGX00000000 and IMG 2506381019. The analysis has an empty
direct organism field but one explicit project leading to Go0004420.

The organism's culture-collection field is empty. The pinned CAFI
matcher returns an empty normalized identifier for bare EUN1f, and
the complete BacDive inventory supplies no target strain or child
strain. Consequently the supported native chain does not establish
an eligible culture-deposit genome link in this YAML.

The absent GOLD attestation is also consistent with the current
pipeline: taxon attestations come from KGX, while primary workbook
objects support strain-linked relationships
(`docs/HARMONIZATION.md:44`). Native census presence alone is not
a missing KGX-derived target field.

**Attestations and history.** The inventories support NCBITAXON
1 NAME, GTDB 1 GENOME and MADIN 8 TRAIT_ASSERTION. Madin's
row is `data/raw/madin_taxa.tsv:543`; its count is coverage metadata,
not eight asserted phenotypes. Units are not summed. The NCBI
snapshot note is 2026-09-13.

`data/taxa/PATHS.tsv:11535` pins the slug;
`curation/seed_scope.tsv:31674` admits the taxon on 2026-09-12
with the three-source reason. The event at 2026-09-13T17:54:04Z
correctly retains seed_from_sources, SEEDED_FROM_SOURCES, the
three sorted source names and that exact reason. `SEEDED` remains
appropriate; this review does not change status.

## Completeness

Absence checks included ignored files. Digit-bounded ID, label,
slug, EUN1f and GTDB identifier searches covered raw inventories,
curation, history, native catalog/BacDive/BV-BRC/GOLD/SeqCode/
StrainInfo projections, ATB and StrainInfo TSV/compressed overlays,
and the full ATB catalog. Searches include the former name through
the EUN1f alias. All nine relevant native objects were read in full.
Eighteen foreign native candidates were parsed and screened by
typed identifiers, names and matching key paths, not assigned
foreign-record verdicts.

Complete source-inventory scans found no target BacDive, LPSN,
GOLD KGX, MediaDive or BactoTraits entry. The three StrainInfo
overlay matches, read in full, belong to Corynebacterium amycolatum
43765 through CIP 102897, SI-ID67958 and SI-DP150060. They are
not Parafrankia. Other native numeric matches include Arthrobacter
BacDive 102897, Leptospira deposit 102897, Chlorella NBRC 102897,
unrelated sequence accessions, isolate names and assembly statistics.

The two complete ATB matches at
`data/catalog/allthebacteria.tsv.xz:6771` and line 2000721 are
Escherichia coli sample SAMD00077305 with run DRR102897, and
Klebsiella pneumoniae sample SAMN17906424 with a numeric checksum
substring. Neither is target evidence. No full-catalog entry matched
EUN1f, its GTDB species or SAMN02441797. Further ignored-inclusive
raw/ATB/StrainInfo TSV/compressed searches for both assembly
accessions, the BioSample and all three GOLD IDs found no target
overlay row. This is a local snapshot boundary, not a claim that
no public assembly exists.

No consequential missing eligible representation was found.
Optional nomenclature and strain links should remain empty without
the required evidence. iModulonDB is not applicable: no gene,
regulator, pathway, stress response or expression dataset is asserted;
a Madin source count alone supplies no specific biological claim
to query. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Retain the current and equivalent names, GTDB source
mapping, typed genome context and strict culture-deposit boundary.
Future enrichment belongs in maintained source and overlay pipelines
before `src/taxonmech/seed.py` may emit links. GOLD attestation
changes belong in its KGX inventory pipeline. Do not patch generated
YAML, infer a culture accession from EUN1f or transfer adjacent
species nomenclature.

## Follow-up Checks

No corrective check is required. An authorized refresh should recheck
the exact name equivalence, GTDB membership, whole eligible culture
identifiers and explicit organism/project/assembly/sample chains,
then rerun both focused validators. Corpus-wide reproduction and
publication assurance also require `just verify-corpus` and full QC,
neither performed here.

## Additional Notes

The GTDB genome page was inaccessible through the web tool. The
complete pinned primary GTDB object supports the source mapping;
live NCBI taxonomy and assembly metadata supplied independent
identity checks. Live status of every external source and genome
contents was not audited.

Only this new report was manually written. Strict validation wrote
its usual diagnostic. No YAML, source, prior report, history or
status was changed. No generator, refresh, paid research, GitHub
action or cross-repository edit occurred. Eukaryota was not re-reviewed.
