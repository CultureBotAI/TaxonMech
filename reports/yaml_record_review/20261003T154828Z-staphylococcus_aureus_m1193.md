# YAML Record Review: Staphylococcus aureus M1193

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m1193.yaml`
- Started UTC: 2026-10-03T15:43:41Z
- Finished UTC: 2026-10-03T15:48:28Z
- Verdict: needs curation

## Target

Read the complete generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303784`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11. Grounding is `EXACT` and mapping
status `SEEDED`. One GTDB mapping, one GTDB exact synonym, one
equivalence xref, three source attestations and one seed event are
present. Strain count is zero. No strains, genome links, nomenclature,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m1193.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m1193.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten lineage entries. The pinned backbone
  has no children under this target.
- Complete exact-field inventory scans reproduce the GTDB mapping and
  Madin count 2. No direct BacDive, LPSN, GOLD, MediaDive or BactoTraits
  taxon inventory membership was found.
- A fresh complete GTDB census confirms 19,502 distinct species-cluster
  accessions across 4,209 source taxon IDs. One member has target taxon
  1303784. Count reproduction does not establish equivalence.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports, full QC and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation checked the embedded
  event. Graph/product gates are not applicable to the asserted content.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308140` and the complete native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30687` support this exact
Staphylococcus M1193 identity and empty NCBI synonym fields. The PATHS
index has exactly one target row with this slug.

The NCBI browser URL was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303784&retmode=xml)
confirms ID, label, strain rank, Bacteria division, parent 1280, code
11 and full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303784)
confirms strain rank and all ten ancestor IDs including root. Read-only
public API calls succeeded with network escalation after both sandboxed
requests failed DNS resolution. NCBI grounding is supported.

Current NCBI order Caryophanales is retained. Older native BV-BRC/GTDB
NCBI fields use Bacillales, while GTDB's own taxonomy uses
Staphylococcales. Different source hierarchies and ages do not override
the NCBI backbone. Strain membership does not support species equivalence.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308140` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_species.tsv:168198`; `gtdb_mappings.tsv:17472` | Correct species-cluster count, not M1193 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11837` | Count reproduced; no particular trait asserted |

The scope row at `curation/seed_scope.tsv:42162` admits this taxon on
2026-09-12 with three sources. The 2026-09-13T17:54:04Z embedded seed
event preserves that reason and source names without claiming human
review. Counts with different units must not be combined.

The census parsed every `gtdb_genomes-*.jsonl.gz` file for terminal
species exactly `s__Staphylococcus aureus`, excluding aureus_A. Only
RS_GCF_000364085.1 carries taxon 1303784. Its complete object at
`data/catalog/gtdb_genomes-0008.jsonl.gz:30303` retains M1193,
SAMN02596939 and GCA_000364085.1. The representative object at
`data/catalog/gtdb_genomes-0006.jsonl.gz:29983` is
RS_GCF_001027105.1, DSM 20231, taxon 1280, not M1193. The GTDB
taxon page was inaccessible through the web tool; pinned primary
metadata establish cluster scope and target membership.

Complete NCBI native objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:10016`
and `data/catalog/ncbi_refseq-0000.jsonl.gz:8741` supply
GCA/GCF_000364085.1, assembly Stap_aure_M1193_V1, strain M1193,
taxon 1303784 and sample SAMN02596939. They explicitly identify an
identical GenBank/RefSeq pair, scaffold level, 12 contigs, three scaffolds
and 2,873,411 bp including gaps. GenBank project PRJNA192845 and
RefSeq umbrella PRJNA224116 remain distinct source values. BV-BRC's
complete object at `data/bvbrc/bvbrc-0001.jsonl.gz:23830` retains
genome 1303784.3, GCA_000364085.1, PRJNA192845 and the same
strain/sample.

Primary GOLD retains Go0036999 -> Gp0036999 -> Ga0018153, with
GCA_000364085.1, IMG 2545824657, PRJNA192845 and SAMN02596939.
Complete objects are at `data/gold/organisms.jsonl.gz:31293`,
`data/gold/projects.jsonl.gz:25168` and
`data/gold/analyses.jsonl.gz:11528`. The organism has an empty culture
field and only bare designation M1193. Native primary-chain evidence
does not supply a KGX-derived GOLD taxon count; these derivations remain
separate under the documented model.

## Completeness

Ignored-inclusive compressed searches by target ID, M1193 and slug
covered all `*.jsonl.gz` files under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
Matching native objects were read in full. Unrelated hits were excluded:

- BacDive 135539 at `data/bacdive/records.jsonl.gz:57844` denotes
  Neisseria elongata subsp. glycolytica, taxon 88719, CIP 104390,
  designation B 8575/M1193. StrainInfo SI-ID69426 at
  `data/straininfo/records.jsonl.gz:56607` links this BacDive ID and
  CIP deposit SI-DP153193, not Staphylococcus M1193.
- StrainInfo SI-ID328625 at `data/straininfo/records.jsonl.gz:255334`
  denotes Neurospora crassa taxon 5141, deposit FGSC 4179,
  SI-DP775337, alias M1193 a. It is not this bacterial strain.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:46100` describes a
  Crocinitomicaceae bacterium, taxon 2026728, GCA_964846625.1.
  The number 1303784 is its genome size, not a taxon match.
- `data/catalog/ncbi_genbank-0032.jsonl.gz:1779` describes
  Streptococcus agalactiae taxon 1311, strain SG-M1193,
  GCA_034344385.1, SAMN20230775, not this Staphylococcus strain.

No target BacDive or StrainInfo native object was found in this bounded
search. The complete BacDive membership scan and singleton subtree
support strain count zero, not a lack of genomes. Native target genome
data exist, but the current model publishes them on source-supported
BacDive strain rows using direct assertions or eligible culture matches.
A bare designation or taxon ID is not a culture-deposit join key.
Native taxon-level genome representation is a separate modeling question,
not permission to fabricate a strain row or copy an unrelated deposit.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, M1193
designation or slug. Compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02596939,
found no target/sample result. These misses are bounded to pinned sources.

There is no same-taxon LPSN inventory mapping. Optional nomenclature and
type flags must not be inherited from the parent species. No DOI, PMID,
gene, locus, regulator, pathway, particular phenotype or transcriptomic
dataset is asserted; iModulonDB is not applicable. Two unspecified Madin
assertions do not establish an experiment or causal graph.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The GTDB exact synonym
  and equivalence xref make `GTDB:s__Staphylococcus_aureus` appear
  identical to strain M1193. The species cluster contains 19,502 genomes
  across many strains, with one target-classified member. Membership
  supports classification, not identity. `src/taxonmech/seed.py:451`
  accepts `skos:closeMatch` as identity without rank/scope checks;
  lines 466-469 emit the unsupported synonym and xref, contrary to
  `src/taxonmech/schema/taxonmech.yaml:180`. Owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate review
  of kg-microbe's source predicate. The count is correct at cluster
  scope, not as a count of M1193 genomes.
- Minor: None found.

## Recommended Edits

1. Make the maintained seeder's equivalence decision rank/scope-aware.
   Preserve GTDB classification and provenance while suppressing the
   unsupported species exact synonym/xref for this strain. Explicitly
   scope the count to the species cluster; do not replace 19,502 with 1
   while retaining species-count semantics.
2. Add a strain/species regression in `tests/test_seed.py`, preserving
   supported same-scope mappings. Review the upstream predicate in
   kg-microbe; do not hand-patch extracted TSVs or guess relation direction.
3. Follow authorized dry-run/canary/regeneration steps after fixing the
   maintained rule. Do not hand-edit YAML, merge name-only matches,
   invent culture joins or promote human review status.

## Follow-up Checks

Run the new regression and
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the emitted record for retained classification, absent unsupported exact
synonym/xref, explicit count scope and unchanged NCBI identity. Repeat
the exact-terminal GTDB census and target-member check. Run
`just verify-corpus` and full QC for regeneration. M1 remains unresolved;
this report did not implement a corrective change.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this report; strict validation wrote its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. No Eukaryota record was re-reviewed;
unrelated eukaryotic source hits were inspected only to exclude homonyms.
