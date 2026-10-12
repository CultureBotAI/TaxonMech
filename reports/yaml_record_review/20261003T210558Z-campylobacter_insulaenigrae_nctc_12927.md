# YAML Record Review: Campylobacter insulaenigrae NCTC 12927

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_insulaenigrae_nctc_12927.yaml`
- Started UTC: 2026-10-03T21:00:22Z
- Finished UTC: 2026-10-03T21:05:58Z
- Verdict: needs curation

## Target

Reviewed the complete 1,114-line generated `TaxonRecord` for
`NCBITaxon:1031564`, Campylobacter insulaenigrae NCTC 12927: rank `STRAIN`,
domain `BACTERIA`, grounding `EXACT`, mapping status `SEEDED`. One BacDive
strain carries 14 assembly assertions, 11 genome-record assertions and 51
related-record assertions. These are source-bearing assertions, not counts
of distinct biological genomes.

This strain is distinct from its parent species, `NCBITaxon:260714`.
Maintained owners include `src/taxonmech/seed.py`, `src/taxonmech/extract.py`
and source inventories. This review writes only this report and the standard
validator diagnostic; it does not edit generated YAML or curation history.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/campylobacter_insulaenigrae_nctc_12927.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/campylobacter_insulaenigrae_nctc_12927.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured comparisons | Backbone, complete lineage, source attestations, path index and seed reason agree with their inventories. All 14/11/51 strain assertions match raw plus StrainInfo inventories as full-field multisets. |
| StrainInfo evidence | All 19 evidence objects match native eligible deposits, DOI, status, source taxonomy and explicit same-deposit sequence links. Live API metadata corroborate them. |
| Embedded history | Strict validation passed; the seven-source seed event and scope reason match the inventories. |
| Standalone history | Not applicable: ignored-inclusive identifier, label and slug searches found no target entry under `history/`. |
| Causal graph and ontology-product gates | Not applicable: no causal graph in the complete target YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports, FASTA replay and the full test suite. Focused
source comparisons are not substitutes for full-corpus reproduction. No
generator, curation-status promotion or history writer was run. Passing
structural checks does not resolve the semantic issue in M1.

## Identity and Grounding

The strain identifier, label, parent, four NCBI synonyms, genetic code 11 and
all ten root-first lineage entries match `data/raw/ncbitaxon_taxa.tsv:220749`.
Live taxonomy EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031564)
confirm this identity. A complete backbone scan found no child taxa.
`data/taxa/PATHS.tsv:13078`, `curation/seed_scope.tsv:7205` and native name
rows 29924-29928 in `data/catalog/ncbi_names-0005.jsonl.gz` agree.

The parent-name inventory `data/raw/lpsn_names.tsv:16011` and inspected
[LPSN species page](https://lpsn.dsmz.de/species/campylobacter-insulaenigrae)
identify name 774381, Foster et al. 2004, with CCUG 48653 and DSM 17739 as
type deposits. The original paper's
[abstract, PMID 15545485](https://pubmed.ncbi.nlm.nih.gov/15545485/)
explicitly identifies NCTC 12927 and CCUG 48653 as the type strain;
DOI `10.1099/ijs.0.63147-0` matches that paper. This is contextual
species nomenclature, not justification for equating the strain with the
species or adding a direct species-name identity xref. No direct LPSN row
targets 1031564; leaving strain-level nomenclature empty follows the model.

NCBI Epsilonproteobacteria and GTDB Campylobacteria are source-specific
classifications. The NCBI lineage should not be replaced by GTDB taxonomy.
The GTDB species-level exact synonym and identity xref are over-scoped: M1.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:2110`, native
  `data/bacdive/records.jsonl.gz:2109` and the inspected
  [BacDive record](https://bacdive.dsmz.de/strain/2132) support BacDive 2132
  and CCUG 48653, CIP 108590, DSM 17739 and NCTC 12927. Native genome
  reference 66792 supports both unversioned GCAs, IMG 2630968444 and
  8119573457, and PATRIC 1031564.3 and 260714.7. That reference is scoped
  to these genome assertions, not the entire taxon record.
- **Inventory fidelity:** Raw assembly rows 106680-106691 plus StrainInfo
  assembly rows 7751-7752 reproduce all 14 assembly assertions. Raw genome
  rows 85840-85850 reproduce all 11 genome assertions. Raw related rows
  308530-308563 plus compressed StrainInfo related rows 191286-191302
  reproduce all 51 related assertions. The files are respectively
  `data/raw/strain_assemblies.tsv`, `data/straininfo/assemblies.tsv`,
  `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`
  and `data/straininfo/related_records.tsv.gz`. Separate source fields
  remain separate provenance, not duplicate biological genomes.
- **BV-BRC:** Native `data/bvbrc/bvbrc-0000.jsonl.gz:3085` supports
  1031564.3, GCA_000816185.1, SAMN03248541 and PRJNA66785 via the whole
  `strain` value NCTC 12927. Native `bvbrc-0015.jsonl.gz:794` supports
  260714.7, GCA_900637885.1, SAMEA48403168 and PRJEB6403 via the whole
  `culture_collection` value NCTC:12927. Species-level taxonomy in the
  latter source does not invalidate its explicit deposit evidence.
- **GOLD:** Native organism row 9951, project rows 9812 and 604100 and
  analysis rows 43594 and 448064 establish Go0011328 -> Gp0011328 ->
  Ga0069264 and Go0011328 -> Gp0818766 -> Ga0668061 in
  `data/gold/{organisms,projects,analyses}.jsonl.gz`. Both organism fields
  name NCTC 12927 and support the two assemblies, IMG IDs and corresponding
  sample/project pairs. Organism rows 459875-459877 explicitly identify
  DSM 17739, CIP 108590 and CCUG 48653 as Go0629310, Go0629311 and
  Go0629312. Complete own-ID searches found no additional project/analysis
  chains for those three organisms; their organism-only assertions are
  appropriately retained.
- **NCBI and GTDB:** Native GenBank `ncbi_genbank-0000.jsonl.gz:30777`,
  RefSeq `ncbi_refseq-0000.jsonl.gz:26739` and GTDB
  `gtdb_genomes-0014.jsonl.gz:20707`, all under `data/catalog/`, support
  GCA/GCF_000816185.1, NCTC 12927 and SAMN03248541. Live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000816185.1,GCF_000816185.1,GCA_900637885.1,GCF_900637885.1/dataset_report)
  confirm both current complete assembly pairs, ASM81618v1 and 52683_H03,
  their sample IDs and deposited strain identifiers. The native RefSeq and
  GTDB PRJNA224116 assertions are retained alongside GenBank/GOLD
  PRJNA66785, although the live API now reports the original project for
  both paired accessions. Unversioned source accessions remain unversioned.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:91891` and the
  [live SI-ID 133636 record](https://api.straininfo.dsmz.de/v2/data/strain/max/133636)
  support DOI `10.60712/SI-ID133636.3`, BacDive 2132, published status and
  available deposits 380556 (NCTC), 381725 (CCUG), 532309 (CIP) and
  674830 (DSM). Each is nondeprecated and nonerroneous. The four native
  deposit taxonomies are 260714; preserving them does not assert that the
  species and strain are identical. `data/straininfo/strain_links.tsv`
  rows 79628-79631 reproduce the four eligible culture matches.
- **Own-deposit sequences:** Both StrainInfo assembly links explicitly
  name NCTC deposit 380556. Nine marker associations likewise name their
  own eligible deposits; none is inferred through group membership.
  NCBI nuccore EFetch definitions and features confirm DSM 17739
  [AB543242.1](https://www.ncbi.nlm.nih.gov/nuccore/AB543242.1) (dnaJ),
  CCUG 48653 [JX912518.1](https://www.ncbi.nlm.nih.gov/nuccore/JX912518.1)
  (16S), and NCTC 12927 AJ620504.1 and DQ174183.1 (16S), DQ174240.1
  (rpoB), KF855249.1 (phosphoramidate cytidylyltransferase), KF855258.1
  (type I glutamine amidotransferase), KF855267.1 (phosphate kinase) and
  [KF855286.1](https://www.ncbi.nlm.nih.gov/nuccore/KF855286.1) (atpA).
  These checks validate accession metadata and source association, not
  biochemical function, sequence equivalence or expression.
- **Attestations:** Raw inventories reproduce NCBI NAME 1, BacDive STRAIN
  1, MediaDive MEDIUM 2, GOLD ORGANISM 1, MADIN TRAIT_ASSERTION 4 and
  BACTOTRAITS TRAIT_ASSERTION 4. Relevant row numbers are 2110, 91, 406,
  582 and 66 in their respective source inventories. The media IDs are
  429 and 693. GTDB mapping row 1312 reproduces count 21, but this is the
  species cluster's count, not 21 genomes established as this strain.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 keys and no Campylobacter
  dataset. No organism-matched gene query applies. This is not negative
  evidence about the marker annotations.

## Completeness

Ignored-inclusive compressed searches covered all native `data/catalog/`,
`data/bacdive/`, `data/bvbrc/` and `data/gold/` files using the target
taxon, species/strain names, whole CCUG/CIP/DSM/NCTC/LMG designations and
both own BioSamples. Complete structured inventory scans checked the
backbone, direct source rows, culture identifiers, type material, merged IDs,
dropped records and StrainInfo evidence. Additional ignored-inclusive
catalog/GOLD/BV-BRC/SeqCode searches found no C708/93 alias hit. These are
bounded source checks, not a claim to have replayed all generators.

Native GCA/GCF_900637885.1 and GTDB RS_GCF_900637885.1 exist at
`data/catalog/ncbi_genbank-0057.jsonl.gz:11422`,
`ncbi_refseq-0009.jsonl.gz:43012` and `gtdb_genomes-0003.jsonl.gz:24741`.
Their compact NCTC12927 field is rejected by the guarded whole-deposit
normalizer in `src/taxonmech/genome_sources.py:83`; spaced or colon-separated
NCTC 12927 is accepted. Their lack of NCBI/GTDB-derived strain assertions
therefore follows existing join policy, while BacDive, BV-BRC, GOLD and
StrainInfo independently preserve the second assembly. A species name or
GTDB cluster must not be used to bypass that policy.

StrainInfo also has available LMG 22716 deposit 383925 and an explicitly
LMG-linked AM924135 marker. The BacDive collection field contains only the
four listed deposits, not LMG. The NCBI LMG synonym is not itself a
source-qualified BacDive collection entry. Excluding this fifth deposit and
its marker follows the current overlay boundary; do not transfer AM924135
to NCTC through group membership or silently relabel LMG as BacDive evidence.

AllTheBacteria correctly contributes no assembly. Own sample SAMEA48403168
has `NOT_PROCESSED`, FASTA flag 0 at native catalog row 668093 and committed
`data/atb/assemblies.tsv:1552`; exclusion row 1030 records
`assembly_unavailable`. SAMN03248541 has no row in the fully searched native
catalog or committed ATB data. A different species-labelled ATB sample,
SAMN03567962, is not an own-deposit match. Taxonomy alone cannot supply one.

The optional strain medium count is absent because its BacDive inventory
value is zero; the two taxon-level MediaDive attestations do not establish
a missing strain-specific count. Phenotype assertions and causal graphs are
not required additions to this identity/provenance record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: a species-cluster mapping is promoted to strain identity.**
Target lines 46-49 declare `Campylobacter D insulaenigrae` an
`EXACT_SYNONYM`; line 63 adds `GTDB:s__Campylobacter_D_insulaenigrae` as an
identity xref. The source mapping at lines 39-44 and attestation at
1077-1082 are species-cluster observations. A complete native cluster
census found 21 members: one filed under NCBI strain 1031564 and twenty
under species 260714. The latter include NCTC 12928 and other different
strain identifiers. Thus neither the species identity nor all 21 genomes
can be equated to NCTC 12927.

The maintained owner is `src/taxonmech/seed.py:451`: it treats any
`skos:closeMatch` as identity without a rank check, then writes the xref and
exact synonym. `src/taxonmech/extract.py:755` copies the whole species
cluster count to the mapped taxon. The raw mapping faithfully records its
upstream predicate; preserving that provenance does not justify promoting
it to exact identity. This is one scope defect with several manifestations,
not an invalid strain identifier or a blocker.

## Recommended Edits

1. In `src/taxonmech/seed.py`, make GTDB identity promotion rank-aware.
   Do not turn a species mapping into an exact synonym or identity xref
   on this `STRAIN` record. Preserve the source mapping with an explicit
   species-cluster scope note unless the maintained mapping policy itself
   is changed with evidence.
2. Clarify the cluster count's scope in generated mappings/attestations.
   Do not relabel 21 as this strain's genome count. Any future count change
   belongs in the maintained extraction/counting policy, with documented
   handling of deposit matches and assembly versions; it is not a hand
   edit of `data/raw/gtdb_mappings.tsv` or this YAML.
3. Add a strain-versus-species regression to `tests/test_seed.py` retaining
   the supported NCBI strain synonyms, all 14/11/51 provenance assertions,
   and legitimate species-level GTDB identity behavior. After approval for
   curation, use the documented dry run and
   `just seed-canary NCBITaxon:1031564`; do not patch generated output.

## Follow-up Checks

Run the focused seed regression, both recorded single-file validators, and
repeat the native 21-member cluster census. Verify that GTDB species
identity promotion is absent for this strain while the scoped source
mapping remains intelligible. Recompare the complete 14/11/51 assertion
multisets and all 19 StrainInfo evidence objects after regeneration.

Before any bulk release, run the documented full-corpus reproduction,
strict validation, provenance/QC and rendered-product gates. No focused
replacement for `just verify-corpus` was invented. Retry the unavailable
live GTDB tree if release-current classification is required; the finding
already follows from the inspected pinned native metadata.

## Additional Notes

- The strain is biologically a type strain, corroborated by the original
  abstract, NCBI type-material rows 105636-105639 for the parent species,
  native BacDive and both live BioSamples. Nevertheless the current
  `is_type_strain` slot is expressly tied to LPSN names of the record's own
  taxon (`src/taxonmech/schema/taxonmech.yaml:477`). The seeder gathers only
  record-local LPSN type designations, so this strain-level record omits
  the flag. This is a known representation boundary, not evidence that
  the strain is non-type, and is not counted as a separate defect under
  the current contract. Ancestor-qualified type evidence would require
  an explicit schema/policy decision and exact deposit grounding.
- Preserve an upstream StrainInfo conflict: its NCTC deposit 380556 has
  `typeStrain: false`, while the live group flag and the CCUG/CIP/DSM
  deposits are true. Native group projection omits the group type flag.
  The YAML does not copy this conflicting NCTC flag. Do not use it to
  override primary type-material evidence.
- Native BacDive includes additional 16S rows with descriptions naming
  NCTC 12927 but different taxon IDs. They were not promoted to YAML.
  The reviewed StrainInfo markers have explicit own-deposit support and
  independently checked nuccore metadata; co-listing is not sufficient.
- Raw GOLD ORGANISM 1 is the snapshot inventory count. The newer native
  organism view includes both NCTC Go0011328 and DSM Go0629310 under
  1031564. Those views were not silently conflated, and the native DSM
  organism evidence is already represented in the related records.
- The original paper's abstract was read, not its full text or erratum.
  No clinical, cultivation or biosafety conclusion is made. The live GTDB
  tree request failed; native pinned metadata were successfully inspected.
  Public reads required network permission; no paid research was used.
- Only this target was judged in this review. Candidate rows for other
  strains were screened for identity boundaries, not reviewed as records.
  Eukaryota records and all existing reports were left untouched.
