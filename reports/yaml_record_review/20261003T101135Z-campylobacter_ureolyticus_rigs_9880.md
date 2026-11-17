# YAML Record Review: Campylobacter ureolyticus RIGS 9880

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_ureolyticus_rigs_9880.yaml`
- Started UTC: 2026-10-03T10:09:35Z
- Finished UTC: 2026-10-03T10:11:35Z
- Verdict: needs curation

## Target

The entire generated TaxonRecord was read. `NCBITaxon:1032069` denotes
RIGS 9880, stored as STRAIN below species 827 in BACTERIA. It carries
ten ancestors, genetic code 11, EXACT grounding, SEEDED mapping status,
two NCBI synonyms, one GTDB mapping/synonym/xref, zero attached strains,
three source attestations and a seed event. The index entry is
`data/taxa/PATHS.tsv:13154`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_ureolyticus_rigs_9880.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_ureolyticus_rigs_9880.yaml`:
  passed, one file and zero errors.
- Structured comparisons matched ID, label, stored rank, parent, code,
  all ten ancestor IDs/labels/ranks/parent links and both NCBI synonyms
  to the pinned inventory. A complete taxonomy scan found no children;
  the BacDive inventory and native search supplied no target strain.
  The zero strain count is consistent with those inputs.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_ureolyticus_rigs_9880.yaml`:
  passed. The record and maintained inputs were not changed.
- `just verify-corpus` was skipped because it is full-corpus-only.
  Full source reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped after an ignored-inclusive
  ID/name/slug search found no separate target artifact in `history/`.
  The embedded seed event was read and included in strict validation.

## Identity and Grounding

The inspected [NCBI page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032069)
supports the identifier, label, two equivalent names, code and ancestry.
It currently reports no rank, not the pinned STRAIN. That discrepancy
does not alone establish an importer bug or a wrong taxon.

The inspected [primary genome announcement](https://journals.asm.org/doi/full/10.1128/genomea.01291-15)
identifies this clinical isolate and explicitly deposits its complete
genome as CP012195. Its DOI is 10.1128/genomeA.01291-15 and its PMID
is 26543122. Only identity and accession evidence were used; incidental
gene/function and clinical assertions were not imported into this review.

A search-result LinkOut to BacDive 2102 is not a RIGS 9880 culture
identity. The inspected [BacDive page](https://bacdive.dsmz.de/strain/2102)
denotes EDMH-1 / DSM 20703 and other deposits, with strain taxon 1121102
and species 827. It supplies no inspected equivalence to RIGS 9880.
Do not attach that type culture through a species-level external link.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220792` and native names at
  `data/catalog/ncbi_names-0005.jsonl.gz:30000` through 30002 support
  the pinned identity and two equivalent-name synonyms.
  `curation/seed_scope.tsv:36139` supports the three-source seed rule.
- `data/raw/gtdb_mappings.tsv:1334` supplies closeMatch and count 16.
  A complete selection over native GTDB JSONL shards reproduced sixteen
  genomes: one at taxon 1032069 and fifteen at species 827. The target
  RS_GCF_001190755.1 at `data/catalog/gtdb_genomes-0007.jsonl.gz:21575`
  is not the representative; RS_GCF_027277485.1 / URMC_785 is.
  Membership in this cluster does not make a species an exact synonym
  of one isolate. Both native `_B` suffixes must remain meaningful.
- `data/raw/madin_taxa.tsv:596` supports one TRAIT_ASSERTION. The
  underlying transformed edge was not replayed, and the count is not
  treated as validated phenotype evidence.
- Full native GenBank `data/catalog/ncbi_genbank-0000.jsonl.gz:43484`
  and RefSeq `data/catalog/ncbi_refseq-0000.jsonl.gz:36419` identify
  GCA_001190755.1 and GCF_001190755.1, latest complete assemblies,
  with RIGS 9880 in their strain fields and SAMN03737995. Preserve
  GenBank PRJNA66811 separately from RefSeq PRJNA224116.
- Native GTDB also carries SAMN03737995, RIGS 9880 and the GenBank
  assembly. Native BV-BRC at `data/bvbrc/bvbrc-0000.jsonl.gz:3137`
  identifies 1032069.3 with GCF_001190755.1, CP012195,
  NZ_CP012195.1, SAMN03737995 and PRJNA66811. These source rows
  corroborate the named isolate without providing a registered culture
  deposit accepted by the current matching contract.
- Native GOLD organism `data/gold/organisms.jsonl.gz:10418`
  identifies Go0011841 with taxon 1032069 and strain RIGS 9880, but
  an empty culture-collection field. Project
  `data/gold/projects.jsonl.gz:10276` connects Gp0011841 to that
  organism, PRJNA66811 and SAMN03737995. Analysis
  `data/gold/analyses.jsonl.gz:51889` follows Gp0011841 to Ga0081792,
  IMG 2654587774 and GCA_001190755.1. Its organism field is empty,
  not contradictory. The explicit project chain is retained natively,
  but a BacDive/eligible-deposit anchor for publishing strain links was
  not found. Go/Gp/Ga, BioSample and BioProject are not genomes.

## Completeness

Ignored-inclusive ID/name/slug and RIGS-accession searches covered raw,
curation, history, ATB and StrainInfo inventories. Decompressed native
catalog, BacDive, BV-BRC, GOLD and StrainInfo JSONL.GZ searches were
also completed. Broad numeric hits were inspected structurally; unrelated
genome-size and longer strain-number matches were rejected.

No prior report stem, separate history artifact, target BacDive culture
or native RIGS 9880 StrainInfo record was found in those bounded sources.
No accepted link for the assembly, BioSample or GOLD chain was found in
committed raw/ATB/StrainInfo TSV/YAML/JSON or StrainInfo TSV.GZ
inventories, including ignored files. The full ATB TSV.XZ was not
inspected, so no global ATB-absence claim is made.

The zero strain count means no BacDive classification in this subtree,
not no isolate or genome. Current policy correctly rejects a bare strain
designation as a culture-deposit join key; do not bypass that guard.
The genome evidence is retained in native catalogs but not exposed in
this record. Missing optional nomenclature, graph and type-strain fields
are not independently defects for this non-type isolate.

The GTDB live species page was unavailable. Native metadata support the
cluster and accession checks; every remote auxiliary accession was not
independently revalidated. iModulonDB is not applicable to this taxon/count
record: no gene or expression claim is present, and none was inferred
from the genome paper.

## Findings

- **Blocker:** None found; the NCBI target identity resolves correctly.
- **Major (1): GTDB species membership becomes exact strain identity.**
  The sixteen-genome species becomes an EXACT_SYNONYM and identity-style
  xref of RIGS 9880. Native Campylobacter_B and ureolyticus_B suffixes
  are also flattened. Owners: `src/taxonmech/seed.py:451`, its synonym
  emission and `tests/test_seed.py`; review upstream kg-microbe GTDB
  mapping semantics consumed by `src/taxonmech/extract.py`. Preserve
  the cluster count and source classification rather than forcing one
  genome or mechanically reversing the mapping predicate.
- **Minor (1): Rank-source discrepancy.** The live authority reports
  no rank while the inventory reports STRAIN. Owners:
  `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`, after
  checking the native pinned node rather than assuming a parser defect.
- **Minor (2): Confirmed genome context is not visible on the record.**
  Independent native assembly/genome sources and an inspected primary
  paper support RIGS 9880, but the current BacDive/deposit-only
  publication contract exposes none of those identifiers here. This is
  a representation/navigation limitation, not permission to invent a
  deposit or evidence of lost native data. Owners: harmonization design,
  the seeder/templates and, for any new maintained representation,
  `src/taxonmech/schema/taxonmech.yaml`. Existing strict deposit joins
  in `src/taxonmech/genome_sources.py` should remain intact.

## Recommended Edits

Do not edit generated YAML. Make GTDB identity promotion rank/scope-aware
and preserve native suffixes. Verify the pinned rank before refreshing
the source. Consider source-qualified native-genome context for an
uncollected isolate through a separately designed maintained surface;
do not create a fake BacDive strain, move a species' type culture here,
or loosen culture-identifier matching. Keep the explicit GOLD chain and
typed identifiers distinct if such context is later published.

## Follow-up Checks

- Inspect the archive pinned by `conf/ncbi_taxdump.yaml`. An
  ignored-inclusive checkout filename search did not locate that archive
  or nodes.dmp; no absence outside this checkout is claimed.
- For any new genome-context representation, test a bare isolate with
  explicit primary assembly evidence separately from registered deposit
  joins. Retain all source fields and distinguish evidence association
  from cross-database genome equivalence.
- After separately authorized fixes, run focused seeder/source-link
  tests, the normal input refresh, `just seed-canary NCBITaxon:1032069`,
  both target validators and full `just verify-corpus`. Verify rendering
  if presentation changes.

## Additional Notes

No curation status, history, source inventory or taxon YAML was changed.
No paid research, outbound messages or GitHub mutation occurred.
Eukaryota was not reviewed.
