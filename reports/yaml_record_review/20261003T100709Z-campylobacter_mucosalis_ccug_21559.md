# YAML Record Review: Campylobacter mucosalis CCUG 21559

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_mucosalis_ccug_21559.yaml`
- Started UTC: 2026-10-03T10:00:43Z
- Finished UTC: 2026-10-03T10:07:09Z
- Verdict: needs curation

## Target

The full 921-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1032067`, stored as `STRAIN` under species 202 in BACTERIA,
with ten ancestors, code 11, EXACT grounding and SEEDED mapping status.
It has three NCBI synonyms, one GTDB mapping/synonym/xref, two BacDive
entries, four source attestations and an embedded seed event. Its index
entry is `data/taxa/PATHS.tsv:13153`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_mucosalis_ccug_21559.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_mucosalis_ccug_21559.yaml`:
  passed, one file and zero errors.
- Structured comparisons matched ID, label, stored rank, parent, code,
  all ten ancestor IDs/labels/ranks/parent links and three NCBI synonyms
  to the pinned inventory. The complete corresponding inventories have
  no child taxa and exactly the two listed BacDive classifications.
- Exact multiset comparisons matched every attached assembly, genome
  record and related-record assertion to raw plus StrainInfo inventories,
  including decoded evidence objects and conflict flags. BacDive 143851
  has 0/0/20 assertions in those fields; 143850 has 7/3/27.
- `just straininfo-query --strain SI-ID92187 --evidence --limit 10`:
  passed, four matched deposits. Its displayed output was truncated;
  full native records and exact committed-link comparisons were also
  inspected. `just straininfo-query --strain SI-ID125612 --evidence --limit 10`:
  passed, three matched deposits, with output inspected in full.
  Query validation checks source/configuration/hashes with
  `reproduce=False`; it is not full source replay.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_mucosalis_ccug_21559.yaml`:
  passed. No taxon record or maintained input changed.
- `just verify-corpus` was skipped because it is full-corpus-only.
  Generated pages and full source reproduction were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: an ignored-inclusive ID/name/slug
  search of `history/` found no separate target artifact. The embedded
  event was read and covered by strict validation.

## Identity and Grounding

The inspected [NCBI record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032067)
supports the target identifier, label, ancestry, code and two equivalent
CCUG-name expansions. It now reports no rank, not the pinned STRAIN,
and explicitly calls the ATCC 49352 name a heterotypic synonym rather
than an equivalent name. The target itself is identifiable; not all
of its attached identity assertions are supported at that same scope.

Two culture groups must remain distinguishable. The inspected
[NCTC 11418 page](https://www.culturecollections.org.uk/nop/product/campylobacter-mucosalis-3)
associates CCUG 21559 with original reference 124/73 and serotype A.
The inspected [NCTC 11419 page](https://www.culturecollections.org.uk/nop/product/campylobacter-mucosalis-4)
instead associates CCUG 21560 and ATCC 49352 with reference 982/76
and serotype B. The respective
[CCUG 21559](https://www.ccug.se/strain?id=21559) and
[CCUG 21560](https://www.ccug.se/strain?id=21560) pages support this
distinction, although some older Lawson aliases overlap. These are
identity clues, not a new phenotype curation or proof that one source's
ATCC accession must be a typographical error.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220791`, native names at
  `data/catalog/ncbi_names-0005.jsonl.gz:29996` through 29999 and
  `curation/seed_scope.tsv:21756` support the pinned baseline and seed
  rationale. The ATCC name's native class is `synonym`; the two CCUG
  expansions have `equivalent name`. `ncbi_taxdump.py` promotes both
  classes to EXACT_SYNONYM, losing the distinction relevant here.
- `data/raw/gtdb_mappings.tsv:1333` supports count seven. A complete
  native cluster selection reproduced seven members: one target
  RS_GCF_004803775.1 and six genomes at species 202, including ATCC
  49353, ATCC 49354, ATCC 43264, ATCC 43265 and DSM 21682 records.
  RS_GCF_013372205.1, not the target genome, is the representative.
  Species membership does not establish identity with CCUG 21559.
  The native Campylobacter_A suffix is flattened in the emitted synonym.
- `data/raw/bacdive_strains.tsv:66133` and 66134 reproduce both entries.
  The full native records at `data/bacdive/records.jsonl.gz:66132` and
  66133 explicitly supply strain taxon 1032067 and species taxon 202;
  `src/taxonmech/bacdive_v2.py` prefers the strain match. Thus the
  conflicting placement is already in source data, not a fabricated
  culture accession from the seeder. Both native type-strain flags are no.
- Native BacDive 143850, version DOI
  `10.13145/bacdive143850.20260601.11`, has CCUG 21559, LMG 8265 and
  NCTC 11418. Its genome fields supply unversioned GCA_004803775 and
  BV-BRC 1032067.3. The inspected
  [BacDive page](https://bacdive.dsmz.de/strain/143850) was an older
  2025 version, agreeing on these identity/genome fields; the native
  pinned record supplies the stated 2026 version.
- Native BacDive 143851, version DOI
  `10.13145/bacdive143851.20251217.10`, instead has CCUG 21560,
  ATCC 49352, LMG 8266 and NCTC 11419, without a native genome field.
  The inspected [live page](https://bacdive.dsmz.de/strain/143851)
  also has ATCC 49352 in its culture header but ATCC 49353 in its
  StrainInfo-derived names panel. Its AF550660 entry is a 16S sequence,
  not a genome, and does not resolve the accession conflict.
- Native GenBank `data/catalog/ncbi_genbank-0003.jsonl.gz:39946`,
  RefSeq `ncbi_refseq-0002.jsonl.gz:18496`, GTDB
  `gtdb_genomes-0010.jsonl.gz:47897` and BV-BRC
  `data/bvbrc/bvbrc-0000.jsonl.gz:3136` agree on CCUG 21559, taxon
  1032067, SAMN03737981 and the versioned GCA/GCF_004803775.1 pair.
  Preserve the unversioned BacDive/StrainInfo accession separately.
  GenBank/BV-BRC PRJNA66809 and RefSeq/GTDB PRJNA224116 are different
  project associations, not assembly identities. BV-BRC additionally
  supplies CP012542. Seven assembly assertions are not seven distinct
  biological genomes; three genome-record assertions include separate
  source evidence for BV-BRC 1032067.3 and the GTDB genome accession.
- Native GOLD organism rows 10412, 189356, 189361, 189362, 189365,
  189368 and 189369 in `data/gold/organisms.jsonl.gz` support retained
  Go0011834, Go0251274, Go0251279, Go0251280, Go0251283, Go0251286
  and Go0251287 via the explicit deposit fields. Project row 10270 in
  `data/gold/projects.jsonl.gz` connects Gp0011834 to Go0011834 and
  PRJNA66809. GOLD Go/Gp and project/sample identifiers remain related
  records, not genomes. Repeated evidence through two source fields
  is preserved as separate assertions, not counted as separate cultures.
- `data/raw/madin_taxa.tsv:595` supports four transformed
  TRAIT_ASSERTION rows. Individual Madin source edges were not replayed;
  their count is not a validation of four biological phenotypes.

Full native StrainInfo records at `data/straininfo/records.jsonl.gz:69880`
and 90774 identify versions `10.60712/SI-ID92187.2` and
`10.60712/SI-ID125612.2`. All listed own deposits are available,
non-erroneous and assigned species taxon 202. The inspected sequence
associations are deposit-specific:

| Own deposit | Native record | Sequence support and local result |
| --- | --- | --- |
| CCUG 21559 / SI-DP6431 | SI-ID92187 | GCA_004803775, DQ174175, DQ174232 and KF855292; retained on BacDive 143850 only. |
| ATCC 49352 / SI-DP6430 | SI-ID92187 | AB292471 and AF550660; matched to BacDive 143851, with `bacdive_reference_conflict: true` retained. |
| LMG 8265 / SI-DP6429; NCTC 11418 / SI-DP6433 | SI-ID92187 | Deposit/strain references only; no sequence transfer from CCUG 21559. |
| CCUG 21560 / SI-DP52015 | SI-ID125612 | DQ174176 and DQ174233; retained on BacDive 143851. |
| LMG 8266 / SI-DP52013; NCTC 11419 / SI-DP52017 | SI-ID125612 | Deposit/strain references only. |
| ATCC 49353 / SI-DP52014 | SI-ID125612 | AF550661 and GCA_012978735; no matching BacDive own deposit in the checked inventory, so not attached here. |

SI-ID92187 points to BacDive 143850 while its ATCC 49352 own deposit
matches the other BacDive culture. Four retained ATCC-related assertions
carry that conflict flag: two sequences and the deposit/strain references.
SI-ID125612 instead has ATCC 49353 as an own deposit and ATCC 49352 only
as an alias. Reciprocal alternative-record references and aliases cannot
transfer sequence evidence. The query and committed overlay respect that
rule; this does not settle the underlying biological identity dispute.

Independent native GenBank, RefSeq, GTDB and BV-BRC rows also associate
GCA/GCF_012978735.1, SAMN04010563 and BV-BRC 202.13 with ATCC 49353 at
species 202. That supports the source accession's existence, not a
new equivalence between ATCC 49352, ATCC 49353 and CCUG 21560.

## Completeness

The record preserves both classified BacDive entries, all seven culture
accessions and every expected inventory-backed link. Missing LPSN
nomenclature, causal graph, medium counts and type flags are not defects
merely because optional fields exist. Do not remove a classified strain
or invent an alias to make the sources appear consistent.

Ignored-inclusive searches covered target ID/name/slug in reports,
history, curation and committed inventories. Compressed native catalog,
BacDive, BV-BRC, GOLD and StrainInfo records were also searched/read.
There was no prior target report. Exact ATCC 49353 searches found no
deposit in the BacDive inventory or committed StrainInfo strain links.
There is no group-level exclusion row for SI-ID125612 because its other
deposits match; this is not evidence that ATCC 49353 was matched.

SAMN03737981 and SAMN04010563 searches of committed ATB TSV/YAML/JSON
surfaces found no link. The full ATB TSV.XZ was not inspected; no
claim of global ATB absence is made. ATCC pages, the GTDB species page,
NCBI assembly/nucleotide pages and attempted ENA nucleotide pages were
unavailable to the web tool. Their contents were not inferred. Native
source records support the accession checks; current remote sequence
records and every DOI were not independently revalidated.

The iModulonDB structured runner was not on PATH. An ignored-inclusive
search of sibling `pyproject.toml` files found references but no claw
runner in that bounded scope; this is not a global installation claim.
The iModulonDB page returned no readable content. No covered dataset
was verified. Gene/16S titles here establish accession type/provenance,
not inferred function, pathway, expression or phenotype evidence.

## Findings

- **Blocker:** None found; the target NCBI identifier resolves correctly.
- **Major (1): A GTDB species becomes exact strain identity.** A
  seven-genome species mapping produces an EXACT_SYNONYM and
  identity-style xref for one strain, and destroys the native `_A`
  suffix. `src/taxonmech/seed.py:451` treats closeMatch as identity
  without a rank/scope guard. Owners: that seeder, `tests/test_seed.py`
  and the upstream kg-microbe GTDB transform consumed by
  `src/taxonmech/extract.py`. Retain cluster membership and count seven;
  neither a count of one nor a mechanically reversed SKOS predicate
  resolves the scope error.
- **Major (2): Conflicting culture identities are exposed as exactness.**
  The ATCC 49352 name is an exact synonym despite NCBI's heterotypic
  distinction. Two different CCUG/NCTC culture groups are filed under
  this strain node by BacDive, while StrainInfo disagrees on the own
  ATCC deposit and four links carry a cross-BacDive conflict flag.
  Primary CCUG/NCTC pages themselves support 49352 for the second
  group, so silently changing it to 49353 would not resolve all sources.
  Owners: upstream collection/NCBI/BacDive/StrainInfo identity records,
  `src/taxonmech/ncbi_taxdump.py:95`, `src/taxonmech/bacdive_v2.py`
  and source-qualified presentation in the seeder/templates. An
  evidence-backed curator overlay would require a separately designed
  maintained input. Preserve the correct own-deposit constraints in
  `src/taxonmech/straininfo_links.py`; they are not the cause of this
  identity conflict.
- **Minor (1): Rank-source discrepancy.** Current NCBI reports no rank
  while the pinned inventory reports STRAIN. The importer normalizes
  the native rank directly, so the live discrepancy alone does not
  prove a parser defect. Owners: `conf/ncbi_taxdump.yaml` and
  `src/taxonmech/ncbi_taxdump.py` after inspecting the pinned node.

## Recommended Edits

Do not edit generated YAML. Add rank/scope-aware GTDB synonym/xref
handling and preserve native suffixes. Preserve NCBI name classes and
avoid treating a plain source synonym as unconditional strain equivalence;
test the heterotypic versus equivalent-name distinction explicitly.

Keep both BacDive source claims and all conflict flags visible until
primary deposit/deposition evidence resolves the 49352/49353 placement.
Route any corrected identities through the owning source and maintained
transform, not an ad hoc YAML alias. Do not transfer ATCC 49353 sequences
to CCUG 21560 through an alias, alternative StrainInfo ID or species ID.
Investigate the pinned rank separately. No record curation is performed
by this review.

## Follow-up Checks

- Inspect the archive pinned by `conf/ncbi_taxdump.yaml` for the rank
  and exact native synonym class. An ignored-inclusive checkout filename
  search did not locate the pinned archive or nodes.dmp; no absence
  outside the checkout is claimed.
- Reconcile ATCC's primary deposit evidence with NCTC/CCUG histories,
  BacDive taxon matches and both StrainInfo own-deposit versions before
  reclassifying a culture. Recheck the sequence deposition records
  directly when accessible; the two source groups must not be merged
  solely through their shared taxon or overlapping older aliases.
- After separately authorized changes, run focused seeder, NCBI
  taxdump and StrainInfo link tests, normal input refresh and
  `just seed-canary NCBITaxon:1032067`. Inspect the written record,
  rerun both target validators, then full `just verify-corpus`.
  Check rendering if source-conflict presentation changes.

## Additional Notes

Source attestations remain in distinct units: one NAME, seven GTDB
GENOME records, two BACDIVE STRAIN records and four MADIN
TRAIT_ASSERTION records. No totals across these units were inferred.
No paid research, outbound messages, GitHub mutation, history addition
or review-status promotion occurred. Eukaryota was not reviewed.
