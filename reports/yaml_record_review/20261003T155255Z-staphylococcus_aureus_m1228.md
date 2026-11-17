# YAML Record Review: Staphylococcus aureus M1228

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m1228.yaml`
- Started UTC: 2026-10-03T15:50:51Z
- Finished UTC: 2026-10-03T15:52:55Z
- Verdict: needs curation

## Target

The entire generated `TaxonRecord` was read. It denotes
`NCBITaxon:1303785`, strain M1228, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11, grounding `EXACT`, status `SEEDED`.
There are ten lineage entries, one GTDB mapping, one GTDB exact synonym,
one equivalence xref, three source attestations and one embedded seed
event. Strain count is zero; no strain list, genome links, nomenclature,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m1228.yaml`:
  PASS, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m1228.yaml`:
  PASS, one file scanned, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison reproduces all ten lineage
  entries, rank, parent and genetic code. The target has no children in
  that backbone. Exact-field full-table scans reproduce GTDB and Madin
  rows and find no direct BacDive, LPSN, GOLD, MediaDive or BactoTraits
  taxon inventory membership.
- A fresh census of every GTDB genome shard yields 19,502 distinct
  accessions for the exact terminal species, 4,209 source taxon IDs and
  one member assigned to taxon 1303785.
- `just verify-corpus`: Not checked, full-corpus-only; no focused
  substitute invented. Full QC, global provenance, rendered products,
  exports and genome sequences were not audited.
- Ignored-inclusive history search found no target entry. No standalone
  history target was available; strict validation checked the embedded
  event. Graph/product gates are not applicable to this graph-free record.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308141` supports this exact ID, name,
rank, parent, code and snapshot 2026-09-13. Native scientific-name object
`data/catalog/ncbi_names-0007.jsonl.gz:30688` agrees. NCBI synonym
fields are empty. The PATHS index has exactly one row for this ID/slug.

The NCBI browser page was inaccessible through the web tool. Current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303785&retmode=xml)
confirms ID, label, strain rank, Bacteria division, parent 1280, code 11
and all non-root lineage names, IDs and ranks, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303785)
confirms rank and all ten ancestor IDs including root. Read-only public
API requests used network escalation after sandbox DNS failure had been
established in the preceding review. NCBI grounding is supported.

Current NCBI order Caryophanales, older BV-BRC/GTDB NCBI order
Bacillales, and GTDB's own order Staphylococcales are distinct source
hierarchies/ages, not a reason to rewrite lineage. The unsupported GTDB
equivalence is separate from the valid NCBI identity.

## Evidence

| Assertion | Inspected source | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308141` | Exact identity and snapshot |
| GTDB 19502 GENOME | `data/raw/gtdb_mappings.tsv:17473`; `gtdb_species.tsv:168198` | Species-cluster count, not strain genome count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11838` | Count reproduced; no named trait claimed |

The scope row at `curation/seed_scope.tsv:42163` admits this record on
2026-09-12 with three sources. The 2026-09-13T17:54:04Z embedded event
matches that reason and the three source names. It does not claim human
review. Counts with different units must not be summed.

The complete GTDB census selected terminal species exactly
`s__Staphylococcus aureus`, excluding aureus_A. Target member
RS_GCF_000364105.1 at `data/catalog/gtdb_genomes-0000.jsonl.gz:6126`
retains taxon 1303785, M1228, SAMN02596940 and GCA_000364105.1.
The representative at `data/catalog/gtdb_genomes-0006.jsonl.gz:29983`
is RS_GCF_001027105.1, DSM 20231, taxon 1280, not M1228. Both
objects were read in full. The GTDB web page was inaccessible; pinned
primary metadata establish membership and cluster scope.

Complete native NCBI objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:10017`
and `data/catalog/ncbi_refseq-0000.jsonl.gz:8742` support the identical
GCA/GCF_000364105.1 pair, assembly Stap_aure_M1228_V1, strain M1228,
taxon 1303785 and SAMN02596940. They describe 28 contigs, three
scaffolds and 2,836,019 bp including gaps. GenBank PRJNA192846 and
RefSeq umbrella PRJNA224116 remain distinct source project values.
BV-BRC `data/bvbrc/bvbrc-0001.jsonl.gz:23831` supports genome
1303785.3, GCA_000364105.1, PRJNA192846 and the same strain/sample.

Primary GOLD's complete objects at `data/gold/organisms.jsonl.gz:31294`,
`data/gold/projects.jsonl.gz:25169` and
`data/gold/analyses.jsonl.gz:11522` preserve
Go0037000 -> Gp0037000 -> Ga0018147, IMG 2545824651,
GCA_000364105.1, PRJNA192846 and SAMN02596940. The culture field
is empty and M1228 is a bare designation. Native GOLD evidence does not
create a KGX-derived GOLD taxon count; these derivations remain separate.

## Completeness

Ignored-inclusive compressed searches by ID, designation and slug covered
all JSONL shards under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/seqcode/`; matching complete
objects were read. The unrelated M1228 object at
`data/catalog/ncbi_genbank-0021.jsonl.gz:45098` describes Enterobacter
hormaechei taxon 158836, GCA_023675595.1, SAMN28668708. It cannot
supply evidence for this Staphylococcus strain.

No target BacDive or StrainInfo native object was found in that bounded
search. Full BacDive membership and the singleton subtree support strain
count zero, not a lack of genomes. Native genome evidence exists, but
the documented model attaches genome links to supported BacDive strain
rows through explicit source assertions or eligible culture-deposit
matches. Neither a bare designation nor a taxon ID is a deposit join key.
Do not fabricate a strain row or borrow the unrelated isolate's evidence.

Ignored-inclusive searches of raw strain assembly/genome/related tables,
StrainInfo link/assembly/exclusion tables and history found no target ID,
M1228 designation or slug. Compressed searches of `data/atb/` and the
complete `data/catalog/allthebacteria.tsv.xz`, additionally using
SAMN02596940, found no target/sample result. Misses are bounded to
pinned sources, not biological absence claims.

No same-taxon LPSN inventory row supports nomenclature or type flags;
the parent's nomenclature must not be copied down. No DOI, PMID, named
phenotype, gene, regulator, pathway or transcriptomics dataset is asserted.
iModulonDB is not applicable. Unspecified Madin counts do not establish
experimental or causal claims.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The exact synonym
  Staphylococcus aureus and equivalence xref
  `GTDB:s__Staphylococcus_aureus` identify the 19,502-genome species
  cluster with strain M1228, although just one cluster member has its
  taxon ID. Membership supports classification, not identity.
  `src/taxonmech/seed.py:451` treats `skos:closeMatch` as identity
  without checking rank/scope, and lines 466-469 emit the synonym/xref,
  contrary to the true-equivalence contract at
  `src/taxonmech/schema/taxonmech.yaml:180`. Maintained fix owners:
  `src/taxonmech/seed.py`, `tests/test_seed.py`; separately review the
  upstream kg-microbe predicate. The count is numerically correct at
  species-cluster scope, not as a count of M1228 genomes.
- Minor: None found.

## Recommended Edits

1. Make the maintained seeder's equivalence rule rank/scope-aware.
   Retain GTDB classification and provenance but suppress this unsupported
   exact synonym and equivalence xref. Explicitly scope the count to the
   species cluster; do not substitute 1 while retaining cluster semantics.
2. Add a strain/species regression in `tests/test_seed.py`, preserving
   supported same-scope mappings. Review the source predicate upstream;
   do not hand-patch extracted TSVs or guess relation direction.
3. After authorization, follow dry-run/canary/regeneration steps. Do not
   hand-edit YAML, invent culture joins or promote human review status.

## Follow-up Checks

Run the new regression with
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
classification, count scope, synonym/xref suppression and unchanged NCBI
identity. Repeat the exact-terminal cluster/member census. Run
`just verify-corpus` and full QC for regeneration. M1 remains unresolved;
this review made no corrective record change.

## Additional Notes

Absence checks used full structured reads, `find`, or
`rg --no-ignore --hidden`, adding `-z` for compressed sources. The only
manual write is this new report; strict validation wrote its standard
diagnostic. No source, record, prior report, history or status was edited.
No generator, source refresh, paid research, GitHub mutation or
cross-repository write occurred. No Eukaryota record was re-reviewed.
