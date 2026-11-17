# YAML Record Review: Campylobacter volucris

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_volucris.yaml`
- Started UTC: 2026-10-03T20:54:24Z
- Finished UTC: 2026-10-03T20:58:24Z
- Verdict: pass with minor issues

## Target

Read all 1,623 lines of this generated `TaxonRecord`: `NCBITaxon:1031542`,
Campylobacter volucris, `SPECIES`, `BACTERIA`, grounding `EXACT`, status
`SEEDED`. Three BacDive strains carry 27 assembly assertions, 17 genome
assertions and 75 related-record assertions. These are provenance-bearing
assertions, not counts of distinct genomes. One strain is explicitly
classified under descendant `NCBITaxon:580033`.

Review only: no YAML, source, generator, history, status or page changes.
This individual report and the standard validator diagnostic are the
only review outputs.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/campylobacter_volucris.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/campylobacter_volucris.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Source comparisons | Exact backbone, nine-entry lineage, synonyms, scope reason, source counts and complete descendant strain roll-up checked. Full-field multisets match all 27/17/75 assertions against raw and StrainInfo inventories. |
| StrainInfo evidence | All 24 evidence objects checked against the native strain, own eligible deposit, versioned DOI, source taxonomy and explicit sequence/deposit association. |
| Embedded history | Strict validation passed; preserves the historical seven-source scope reason and the currently seeded eight-source inventory list. |
| Standalone history | Not applicable: ignored/hidden-inclusive identifier, label and slug search found no target entry under `history/`. |
| Causal graph and ontology-product gates | Not applicable: no causal graph in the complete YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports or FASTA replay. The bounded
source comparisons are not a substitute for full-corpus reproduction.
No curation or regeneration command ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220747`, live taxonomy EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031542,580033)
agree on the species identity, parent Campylobacter 194, genetic code 11
and root-first lineage. Native name rows 29920-29922 in
`data/catalog/ncbi_names-0005.jsonl.gz` distinguish the includes-name
LMG 24381 from the authority; neither is improperly promoted to an exact
synonym. `data/taxa/PATHS.tsv:13074` uniquely resolves the indexed ID and
slug; `curation/seed_scope.tsv:5451` supplies the historical seed reason.

A complete backbone traversal finds exactly one descendant, strain
580033, at row 137512. The three-strain roll-up equals the complete
BacDive clade inventory, not merely the two directly filed species rows.
The descendant strain retains `classified_as: NCBITaxon:580033`; source
assertions are not relabeled to the parent species indiscriminately.

The directly refreshed [LPSN page](https://lpsn.dsmz.de/species/campylobacter-volucris)
confirms name 788696, Debruyne et al. 2010, valid publication, current-name
status, its medical-name recommendation and all three type deposits:
CCUG 57498, DSM 25354 and LMG 24380. The marker is FM883694. Raw LPSN
row 25821 agrees. The medical-name wording is a source nomenclatural
status, not a clinical or biosafety recommendation by this review.

Both GTDB mappings retain the inventory's `skos:broadMatch`, and neither
is promoted to a species identity xref or exact synonym. Cluster counts
15 and one are supported, but the explanatory text for the one-member
cluster overstates what those data show; see N1.

## Evidence

- **BacDive and type material:** Raw strain rows 2119, 77613 and 77614
  and native rows 2118, 77612 and 77613 in
  `data/bacdive/records.jsonl.gz` support BacDive 2141, 155372 and
  155373. The inspected authority pages for
  [2141](https://bacdive.dsmz.de/strain/2141),
  [155372](https://bacdive.dsmz.de/strain/155372) and
  [155373](https://bacdive.dsmz.de/strain/155373) corroborate their
  collection identifiers. Native explicit type flags are yes/no/no;
  NCBI type-material rows 1549-1555 and LPSN support only strain 2141's
  collection group as type. Generic page labels are not substituted for
  explicit type evidence.
- **Per-strain fidelity:** BacDive 2141 has 18 assembly, 11 genome and
  42 related assertions; 155372 has 9/6/25; 155373 has 0/0/8. Raw
  assembly rows 106830-106845 and 62358-62365, genome rows 85970-85980
  and 48147-48152, and related rows 308935-308968 and 198433-198452
  match all raw-source objects. StrainInfo assembly rows 7769-7770 and
  5074, and gzip related rows 191467-191474 and 124980-124992, account
  for the remainder. Source versions, levels and evidence fields were
  compared without deduplicating independent assertions.
- **Genome identities:** The supported assembly pairs are
  GCA/GCF_008245045.1, complete ASM824504v1 from type deposit LMG 24380;
  GCA/GCF_008801985.1, contig ASM880198v1 from type deposit CCUG 57498;
  and GCA/GCF_000816345.1, complete ASM81634v1 from non-type LMG 24379.
  Native GenBank rows are `ncbi_genbank-0007.jsonl.gz:8385`, the same
  file at 34887, and `ncbi_genbank-0000.jsonl.gz:30783`. RefSeq rows are
  `ncbi_refseq-0002.jsonl.gz:29738`, that file at 31852, and
  `ncbi_refseq-0000.jsonl.gz:26745`. Live
  [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_008245045.1,GCF_008245045.1,GCA_008801985.1,GCF_008801985.1,GCA_000816345.1,GCF_000816345.1/dataset_report)
  corroborates all six current accessions, pairs, strains, levels,
  names and samples. BacDive/StrainInfo unversioned accessions remain
  unversioned rather than being silently rewritten.
- **Samples and projects:** LMG 24380 uses SAMN12636418/PRJNA562226;
  CCUG 57498 uses SAMN12697566/PRJNA563568; LMG 24379 uses
  SAMN03248550/PRJNA66783. Native RefSeq and GTDB instead retain the
  RefSeq umbrella PRJNA224116. Live Datasets assembly-info blocks expose
  the original sequencing projects even for GCF records. This source/
  API distinction is preserved, not treated as an identity mismatch.
- **BV-BRC:** Native `data/bvbrc/bvbrc-0000.jsonl.gz:3071` and the next
  row support PATRIC 1031542.11 and 1031542.12 through explicit LMG and
  CCUG strain/culture fields. `bvbrc-0025.jsonl.gz:10801` supports
  PATRIC 580033.3 through its LMG 24379 strain field. Its culture field
  says only LMG culture and correctly does not create a second deposit
  assertion. Other species genomes have distinct bare strain names and
  are not joined to these deposits.
- **GOLD:** Eligible native organisms Go0172330, Go0032730,
  Go0614533, Go0011842 and Go0172333 occur at organism rows 110602,
  27887, 445259, 10419 and 110605. The LMG 24380 chain is
  Go0172330 -> Gp0653239 -> Ga0560023, at project row 487832 and
  analysis row 366473, supplying IMG 8111628605. The LMG 24379 chain
  is Go0011842 -> Gp0011842 -> Ga0069346, at project row 10277 and
  analysis row 43658, supplying IMG 2630968854. Both analyses have
  empty direct organism fields and reach the organism through their
  explicit projects. Repeated chromosome/plasmid entries in Ga0560023's
  GenBank JSON point to the same assembly. Full native searches found
  no project/analysis chain for the other three eligible organisms.
- **GTDB:** Full native species-cluster search finds 15 volucris members,
  14 filed as NCBI 1031542 and one as descendant 580033. Representative
  RS_GCF_008245045.1 is at `gtdb_genomes-0016.jsonl.gz:27409`; the
  CCUG type assembly is at `gtdb_genomes-0000.jsonl.gz:46038`, and the
  descendant genome at `gtdb_genomes-0017.jsonl.gz:28715`. The sole
  volucris_A member is representative RS_GCF_008011665.1 at
  `gtdb_genomes-0012.jsonl.gz:32618`, strain 2016D-0084, NCBI 1031542.
  Raw mapping rows 1310-1311 reproduce the two species mappings; row
  297627 separately maps the main cluster to descendant 580033. Both
  public GTDB tree requests failed, so this is pinned-native evidence,
  not a successful live authority lookup.
- **StrainInfo:** Native rows 23172, 290945 and 22639 and live records
  [28765](https://api.straininfo.dsmz.de/v2/data/strain/max/28765),
  [381547](https://api.straininfo.dsmz.de/v2/data/strain/max/381547) and
  [22639](https://api.straininfo.dsmz.de/v2/data/strain/max/22639)
  support DOI versions 28765.3, 381547.2 and 22639.2 respectively.
  The seven available deposits are LMG 24380/841858,
  CCUG 57498/855444, DSM 25354/913980, LMG 24379/874032,
  CCUG 57497/917700, LMG 24381/841857 and CCUG 57499/916440.
  All have nondeprecated collections and nonerroneous own relations.
  Every sequence points explicitly to its asserted deposit; equivalent
  cultures do not inherit sequences without that evidence. Overlay
  strain-link rows 79683-79685 and 52704-52707 agree.
- **Marker accessions:** NCBI Nuccore EFetch verifies all seven markers:
  FM883693.1/1504 bases, FM883694.1/1482 and FM883695.1/1485 are the
  respective LMG 24379, 24380 and 24381 16S records; FM883696.1,
  FM883697.1 and FM883698.1 are their 555-base partial hsp60 genes;
  KF855304.1 is the 1506-base LMG 24379 atpA coding sequence. Deposit,
  definition and feature metadata agree. NCBI uses strain taxon 580033
  for the LMG 24379 sequences; StrainInfo uses species taxon 1031542
  on its deposits. The YAML retains that source-level difference.
- **Publications:** Crossref verifies
  [DOI 10.1099/ijs.0.013748-0](https://doi.org/10.1099/ijs.0.013748-0),
  the 2010 species description at pages 1870-1875, and
  [DOI 10.1099/ijs.0.028779-0](https://doi.org/10.1099/ijs.0.028779-0),
  the 2010 notification list at pages 2511-2512. The complete inspected
  [PMID 19767353 abstract](https://pubmed.ncbi.nlm.nih.gov/19767353/)
  explicitly separates the three LMG isolates and designates LMG 24380,
  equivalent to CCUG 57498, as type. Full articles were not reviewed.
- **Attestations:** Complete inventories support NCBI NAME 1, LPSN NAME
  1, principal GTDB GENOME 15 with the additional cluster disclosed,
  clade BacDive STRAIN 3, direct MediaDive MEDIUM 2, direct GOLD ORGANISM
  12, direct Madin TRAIT_ASSERTION 7 and direct BactoTraits
  TRAIT_ASSERTION 8. Relevant aggregate rows are 90, 405, 581 and 65.
  The GOLD species count excludes descendant Go0011842; organism
  inventory inspection confirms 12 direct plus one descendant record.
  Counts and units are not added into a biological trait census.

## Completeness

The complete descendant traversal and BacDive inventory support exactly
three listed strains, with no cap. LMG 24381's empty genome slots are
correct under the checked inventories; its two markers and own deposit
links are present. The broader NCBI/GTDB species genomes, including MON,
2014D, 2016D and Ca_G strain names, do not establish deposit matches to
these three strains. GOLD's additional bare aliases likewise are not
grounds for inferred culture joins.

Ignored/hidden-inclusive compressed searches covered all `data/catalog/`,
`data/bacdive/`, `data/bvbrc/` and `data/gold/` files using species and
descendant IDs, label, all culture identifiers, samples and explicit GOLD
chains. Matched records were inspected structurally; unrelated numeric
collisions in genome statistics were excluded. This establishes a local
snapshot boundary, not an exhaustive public genome census.

There is no eligible ATB link for a target strain. Native
`data/catalog/allthebacteria.tsv.xz:1670174` and committed
`data/atb/assemblies.tsv:6851` retain SAMN12636418 as NOT_PROCESSED with
no FASTA; exclusion row 2899 correctly records `assembly_unavailable`.
Full ignored-inclusive searches found neither SAMN12697566 nor
SAMN03248550 in the ATB catalog, and no target strain links. Other
available species-labeled or sylph-classified ATB samples are different
samples and cannot be transferred by taxonomy.

All three raw BacDive rows report zero linked media, so optional
strain-level medium counts are omitted. Direct MediaDive independently
counts media 429 and 693. Neither is a species-wide growth claim. No
phenotype, medium recipe or causal graph is required to fill optional
slots. The iModulonDB structured adapter returned 28 dataset keys and no
Campylobacter coverage; no hsp60/atpA expression context was transferred
from another organism.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**N1 - Minor: unsupported other-taxon pooling explanation for volucris_A.**
The second mapping's note at record lines 71-72 says its GTDB species
also maps to other NCBI taxa. Its complete native cluster contains only
RS_GCF_008011665.1, NCBI 1031542, and the complete raw mapping inventory
contains only this species mapping for volucris_A. Thus its count one
and source broadMatch are faithfully retained, but the generic prose
claims a pooling relationship absent from the inspected source evidence.
The main cluster does include descendant 580033, which is a different
NCBI identifier within this species, not evidence about volucris_A.

Maintained owner: `src/taxonmech/seed.py:463` unconditionally emits the
other-NCBI-taxa explanation for broadMatch. The inventory at
`data/raw/gtdb_mappings.tsv:1311`, produced through
`src/taxonmech/extract.py:755`, carries the source predicate and cluster
count but does not justify that additional statement. Do not patch the
generated YAML or change its mapping predicate solely to repair wording.

## Recommended Edits

1. In a later authorized code/curation change, make broadMatch prose in
   `src/taxonmech/seed.py` neutral about cluster composition unless the
   contributing NCBI taxa have been established. Preserve the two source
   mappings, 15/1 counts and absence of GTDB identity xrefs/synonyms.
2. Add a focused case to `tests/test_seed.py` for a one-member,
   one-NCBI-taxon broadMatch cluster, alongside the existing pooled
   mapping tests. Generate this target with
   `just seed-canary NCBITaxon:1031542` only after the maintained fix.

## Follow-up Checks

- Run `uv run pytest tests/test_seed.py` after adding the regression;
  verify the corrected note does not claim unsupported other-taxon
  membership and that existing mapping identity safeguards remain.
- Repeat both target validators and the per-strain 18/11/42,
  9/6/25 and 0/0/8 source comparisons. Preserve the descendant's
  `classified_as`, the own-deposit sequence links and ATB exclusion.
- Run full `just verify-corpus` and `just qc` before publishing an
  authorized regenerated corpus; those remain unrun in this review.

## Additional Notes

There is a source conflict not imported into the YAML: native and live
StrainInfo deposit 841857 marks LMG 24381 as type, while the live strain
group 22639 says false, CCUG 57499 says false, and LPSN plus the original
description select LMG 24380. The native projection omits the group-level
type flag but retains deposit flags. The record correctly derives its
type assertion from the LPSN designation set and does not mark LMG 24381
as type. Reconciliation of the upstream StrainInfo discrepancy would
require a separate authorized source-curation task, not a YAML flag change.

The type-strain BacDive source also co-lists FM883693 from LMG 24379.
The YAML does not copy that marker onto the type strain; explicit
StrainInfo deposit evidence places it under BacDive 155372 instead.
Taxonomy differences between NCBI Campylobacterota/Epsilonproteobacteria,
LPSN's phylum placement and GTDB Campylobacter_D do not authorize
rewriting the carried NCBI lineage.

Merged-ID rows 87306-87307 redirect 580032 and 580034 to 1031542;
580033 remains the live descendant. The scope reason's historical seven
sources is preserved rather than rewritten to the current eight-source
seed list. No prior report or Eukaryota record was modified. The full
corpus review remains in progress.
