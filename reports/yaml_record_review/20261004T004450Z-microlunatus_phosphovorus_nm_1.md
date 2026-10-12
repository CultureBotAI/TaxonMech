# YAML Record Review: Microlunatus phosphovorus NM-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microlunatus_phosphovorus_nm_1.yaml`
- Started UTC: 2026-10-04T00:42:57Z
- Finished UTC: 2026-10-04T00:44:50Z
- Verdict: needs curation

## Target

Read all 84 lines of generated `TaxonRecord` NCBITaxon:1032480,
Microlunatus phosphovorus NM-1. It is a `STRAIN` under species
NCBITaxon:29405, with `BACTERIA`, `EXACT`, `SEEDED`, code11, one
GTDB mapping, three synonyms, three attestations and `strain_count: 0`.
No strain listing, genome assertion, nomenclature, general evidence,
phenotype assertion or causal graph is carried. No YAML, source, history
or status was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microlunatus_phosphovorus_nm_1.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microlunatus_phosphovorus_nm_1.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, NCBI names, path, scope and seed event agree. GTDB/Madin fields reproduce their inventories; GTDB semantic scope is the finding below. |
| History | Embedded event matches the maintained scope; no target standalone history entry found in ignored-inclusive searches. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, pages, exports, sequence alignment, ATB FASTA eligibility or a
complete review of the parent species. Focused comparisons do not prove
corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220862`, live
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032480&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032480)
agree on exact identity, `STRAIN`, parent29405 and code11. The full ten
root-first ancestors agree through Bacillati, Actinomycetota,
Actinomycetes, Propionibacteriales, Propionibacteriaceae, Microlunatus
and M. phosphovorus. Complete backbone scans found no children.

Both the indexed and directly fetched legacy
[NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032480)
displayed `no rank`, unlike EFetch/Datasets and the pinned backbone.
This live authority-surface discrepancy is preserved, not called a stale
cache or used to infer a rank change. It does not invalidate the supported
strain scope; either presentation denotes a taxon below species29405.

Native names0005:30146-30148 support the scientific label and both
NCBI equivalent names with NM-1 retained. `data/taxa/PATHS.tsv:13234`,
`curation/seed_scope.tsv:36140` and legacy page row773 agree. The
September13 seed event reproduces the September12 scope reason exactly.

## Evidence

- NCBI contributes one NAME, GTDB four GENOMEs and Madin three
  TRAIT_ASSERTIONs (`data/raw/madin_taxa.tsv:608`). These source units
  are not additive and do not assert three specific phenotypes.
- `data/raw/gtdb_mappings.tsv:1346` maps GTDB species
  `s__Microlunatus_phosphovorus` to strain1032480 with `closeMatch`
  and count4. Row236819 also maps that species to parent29405;
  `gtdb_species.tsv:121253` confirms a species-wide total of four.
  A complete native GTDB species scan found exactly these members:

  | Genome | NCBI taxon | Source isolate/designation |
  | --- | --- | --- |
  | RS_GCF_000270245.1 | 1032480 | NM-1; representative, complete genome |
  | GB_GCA_039811885.1 | 29405 | AS-MICRO-OLR.73; metagenome-derived |
  | GB_GCA_937872995.1 | 29405 | SRR2107183_bin.61_CONCOCT_v1.1_MAG; metagenome-derived |
  | GB_GCA_036723495.1 | 29405 | CTOTU24475; metagenome-derived |

  Native positions are GTDB0008:2389, 0014:26665/47181 and
  0016:14645. The count4 is supported as species-cluster context,
  not four assemblies of NM-1. The public GTDB genome page was
  attempted; native structured metadata supplied the usable evidence.
- [LPSN778152](https://lpsn.dsmz.de/species/microlunatus-phosphovorus)
  concerns the parent species and identifies NM-1 among its type-strain
  designations, including DSM10555, JCM9379 and NBRC101784.
  [BacDive12625](https://bacdive.dsmz.de/strain/12625) independently
  identifies NM-1 but classifies its strain record at species29405.
  Its native row12467 and local inventory agree; there is no exact
  BacDive classification row for target1032480. Thus zero inventoried
  strains on this child is not biological absence of the isolate.
- The native NCBI pair GCA/GCF_000270245.1 explicitly names NM-1,
  taxon1032480, sample SAMD00061117 and the complete genome.
  [Live assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000270245.1/dataset_report)
  confirms current status, the paired GenBank accession, project
  PRJNA66879 and sample. The sample explicitly notes coidentity with
  NBRC101784. Source RefSeq/GTDB project PRJNA224116 is retained
  as its own metadata, not silently replaced by the sequencing project.
- BacDive12625 reports unversioned GCA_000270245, BV-BRC1032480.4
  and IMG650716058. GOLD Go0001114 explicitly names NBRC101784;
  Gp0001114 identifies that organism and sample; Ga0029427 identifies
  that project and GCA_000270245.1 / IMG650716058. These assertions
  are already present under BacDive12625 in
  `data/taxa/bacteria/microlunatus_phosphovorus.yaml`. Their source
  placement follows BacDive's parent-species classification. Go/Gp/Ga
  remain related records, not genome identifiers.
- BV-BRC1032480.4 and the NCBI/GTDB assembly rows use bare `NM-1`
  as their strain field. That string alone is not a CAFI culture-deposit
  join key. The explicit GOLD NBRC chain must not be used to invent
  equivalent provenance in the other databases or duplicate a parent
  strain row onto this child.
- Full exact-target raw scans found no LPSN, GOLD aggregate,
  MediaDive or BactoTraits row for1032480. Native GOLD organism
  evidence and parent-owned genome links are nevertheless present;
  missing an aggregate attestation is not global source absence.
  No gene, regulator, pathway or transcriptomic claim is carried;
  a structured iModulonDB search was not applicable to this review.

## Completeness

The material issue is scope promotion, not proven missing genome data.
The parent-owned BacDive12625 strain and its target-taxonomy genome
assertions were inspected as context, not rereviewed in full. No record
was copied between parent and child. No new StrainInfo or ATB relationship
was inferred from the taxon ID, bare NM-1 name, or parent membership.

Ignored-inclusive identifier, label and slug searches covered raw tables,
all native catalog shards, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo,
ATB strain/genome links and exclusions, curation and history; SOURCE.json
files were JSON-traversed. Exact structured scans found no own NCBI
type-material, merged-ID or dropped row, and the search found no target
standalone history entry on these surfaces. This is not an audit of every
bare NM-1 alias or a global ATB absence claim. Optional graph, definition,
discussion, general evidence and nomenclature need not be invented.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species label is promoted to an exact synonym of a
   single strain.** YAML lines46-49 call `Microlunatus phosphovorus`
   an `EXACT_SYNONYM` of NM-1, while the record's own parent is that
   species and three of the four GTDB members are other, species-level
   metagenome assemblies. The source mapping is useful cluster context
   but does not support whole-species/strain identity. A `closeMatch`
   assertion is being strengthened into an exact name equivalence
   without a rank check. The two NCBI NM-1 equivalent names are sound.

   Maintained owner: `src/taxonmech/seed.py:451` treats every GTDB
   `closeMatch` as identity, and line468 creates the exact synonym.
   `src/taxonmech/extract.py:501` preserves the upstream kg-microbe
   mapping into `data/raw/gtdb_mappings.tsv`; its source predicate and
   species-wide count also need rank-aware review upstream. The
   source mapping/count reproduce correctly, so this is a semantic
   seeding/grounding issue, not a schema failure or generated drift.
   No arbitrary replacement predicate or lineage reconciliation is
   justified by this report alone.

## Recommended Edits

1. In the maintained seeder, prevent a broader GTDB species label from
   becoming an exact synonym of a strain solely because the source
   predicate is `closeMatch`. Preserve the original mapping and its
   provenance as appropriately qualified context; assess the xref's
   intended identity semantics at the same boundary. Retain the two
   exact NCBI strain names.
2. Review the source mapping with the kg-microbe GTDB transform owner.
   Clarify that count4 describes the GTDB species cluster and only one
   listed genome bears NCBITaxon:1032480. Do not simply change count4
   to1 or flip the predicate in the generated file; resolve the
   maintained mapping/count contract first.
3. Leave BacDive classification and parent-owned genome evidence intact.
   Do not hand-edit this YAML, infer a new child strain listing, or
   promote `SEEDED` automatically.

## Follow-up Checks

- Extend `tests/test_seed.py` with a strain child mapped to a GTDB
  species containing additional species-level genomes. Assert that a
  whole-species exact synonym is not emitted and NCBI strain synonyms
  remain. Preserve valid species-level mapping behavior.
- Following authorized maintained changes, run extraction/seed dry
  runs and the NCBITaxon:1032480 canary; inspect the full result,
  then run both focused validators, `just verify-corpus` and `just qc`.
- Recheck the legacy NCBI browser versus EFetch/Datasets rank at refresh;
  preserve the source discrepancy until authoritative state resolves it.
- Verify that any presentation change still exposes parent-owned
  BacDive12625 genome evidence without species/strain conflation or
  cross-database genome-equivalence claims.

## Additional Notes

Native NCBI assembly rows are GenBank0000:5871 and RefSeq0000:4992;
BV-BRC0000:3167; GOLD organisms990/190534, project1017 and analysis19753.
Go0252455 describes a parent-classified NM-1 label but has no collection
identifier and does not supply a new deposit join. A compact structured
GTDB scan re-read all four cluster members after combined terminal output
was truncated. All checks were read-only except this new report and the
validator diagnostic. No GitHub, YAML, source, history or status mutation
occurred. Completed Eukaryota coverage was untouched.
