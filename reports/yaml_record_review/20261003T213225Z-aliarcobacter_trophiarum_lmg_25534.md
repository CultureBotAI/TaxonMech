# YAML Record Review: Aliarcobacter trophiarum LMG 25534

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aliarcobacter_trophiarum_lmg_25534.yaml`
- Started UTC: 2026-10-03T21:26:45Z
- Finished UTC: 2026-10-03T21:32:25Z
- Verdict: needs curation

## Target

Read all 1,377 lines of the generated `TaxonRecord`, `NCBITaxon:1032241`,
Aliarcobacter trophiarum LMG 25534, rank `STRAIN`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. Its one BacDive strain carries
25 assembly, 16 genome-record and 60 related-record assertions. These
are provenance assertions, not distinct biological genome counts. The
target is this strain, not parent species `NCBITaxon:708186`.

Maintained owners are the source inventories and taxonomy import/seeding
code. This read-only review changes no generated YAML, source data,
curation status, history or earlier report.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aliarcobacter_trophiarum_lmg_25534.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aliarcobacter_trophiarum_lmg_25534.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured inventory comparisons | Backbone, complete lineage, scope, path index and attestations agree. Exact full-field multisets match for 25 assembly, 15 non-ATB genome and 60 related assertions. |
| StrainInfo evidence | All 17 objects match native eligible deposits, statuses, DOI, source taxonomy and explicit sequence-deposit membership. |
| AllTheBacteria evidence | Native and committed metadata agree on all 17 fields. Entire YAML evidence object, four sample assertions and seven same-source-chain pairs across four genome crosslinks pass exact comparisons. |
| Embedded history | Strict validation passed; the six-source seed event and scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored and hidden files found no target entry under `history/`. |
| Graph and ontology-product gates | Not applicable: no causal graph or curator-added graph nodes in the full YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports, full tests, FASTA downloads or checksum
replay. Focused comparisons do not substitute for corpus reproduction.
No generator, history writer or status promotion was run. Passing schema
validation does not resolve either identity finding.

## Identity and Grounding

The identifier, label, parent, genetic code 11 and ten root-first lineage
entries match `data/raw/ncbitaxon_taxa.tsv:220799`. Live EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032241,708186)
corroborate the strain and parent. Native names are in
`data/catalog/ncbi_names-0005.jsonl.gz` rows 30034-30038;
`data/taxa/PATHS.tsv:13161` and `curation/seed_scope.tsv:10793` agree.
A complete backbone scan found no children of this strain.

All four NCBI synonym strings reproduce the source, but source fidelity is
not proof of biological strain equivalence. In particular,
`Arcobacter sp. 122/3-38/R-39970` conflicts with independent evidence for
the non-type strain LMG 25535; see M2. The primary identifier and deposit
set still consistently identify LMG 25534, so this is not a wholesale
wrong-record identification.

Preserve a separate nomenclatural difference: NCBI carries Aliarcobacter;
[LPSN Aliarcobacter trophiarum](https://lpsn.dsmz.de/species/aliarcobacter-trophiarum)
lists name 5969 as a validly published synonym, while
[LPSN Arcobacter trophiarum](https://lpsn.dsmz.de/species/arcobacter-trophiarum)
lists name 789024 as the correct name. The 2020 valid combination differs
from the invalidly published 2018 version. Parent-name inventory row
`data/raw/lpsn_names.tsv:1139` agrees; no direct LPSN name maps to this
strain taxon. Type designations include 64, 64/2-45d5/R-39974,
CCUG 59229, DSM 25469 and LMG 25534. Do not rewrite the carried NCBI
name or lineage to reconcile these classifications.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:2096`, native
  `data/bacdive/records.jsonl.gz:2095` and the inspected
  [BacDive 2101 page](https://bacdive.dsmz.de/strain/2101) support designation
  `64, 64/2-45d5/R-39974` and the four carried deposits: CCUG 59229,
  CIP 110286, DSM 25469 and LMG 25534. Native reference 66792 supports
  all three unversioned GCA records, IMG 2847262524/2858249781 and
  PATRIC 1032241.5/.6/.7. The public page and raw inventory supply the
  collection list, which the native compact projection does not retain.
- **Inventory fidelity:** Full assertion multisets match
  `data/raw/strain_assemblies.tsv` rows 106424-106445 plus
  `data/straininfo/assemblies.tsv` rows 7719-7721;
  `data/raw/strain_genome_records.tsv` rows 85619-85633; and
  `data/raw/strain_related_records.tsv` rows 307825-307870 plus
  `data/straininfo/related_records.tsv.gz` rows 190837-190850.
  The additional ATB record was independently checked.
- **NCBI assemblies:** Native GenBank/RefSeq rows and live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_003355515.1,GCF_003355515.1,GCA_004116585.1,GCF_004116585.1,GCA_024584015.1,GCF_024584015.1/dataset_report)
  confirm six current accessions, each with strain LMG 25534 and taxon
  1032241, in the three paired chains below. Native RefSeq/GTDB
  PRJNA224116 remains a source-specific assertion; the live paired-assembly
  API instead supplies original projects. Source-unversioned accessions
  remain unversioned.

| GCA/GCF accession stem, version 1 | Assembly | BioSample | Original project |
| --- | --- | --- | --- |
| 003355515 | Complete, ASM335551v1 | SAMN03737959 | PRJNA66831 |
| 004116585 | Contig, ASM411658v1 | SAMN07767218 | PRJNA412344 |
| 024584015 | Contig, ASM2458401v1 | SAMN25938061 | PRJNA808439 |

- **Native genome sources:** GenBank shard/row locations are 0002/32430,
  0003/9690 and 0022/38590; RefSeq locations are 0001/48161, 0002/12307
  and 0004/22282 under `data/catalog/`. GTDB shard/row pairs 0002/35339,
  0007/43699 and 0012/47949 retain the corresponding whole LMG deposit
  matches. BV-BRC shard 0000 rows 3151-3153 support the three PATRIC
  records through `strain`; `LMG culture` in the first culture field is
  correctly excluded as a deposit key.
- **GOLD:** Full own-ID searches of
  `data/gold/{organisms,projects,analyses}.jsonl.gz` confirm Go0011289
  through Gp0380738 -> Ga0349697 -> GCA_003355515.1 / IMG 2847262524,
  and through Gp0443177 -> Ga0396115 -> GCA_004116585.1 / IMG 2858249781.
  Both organism strain and collection fields independently match LMG.
  Native organism rows are 9915, 445376 and 445377; projects 268317 and
  314816; analyses 209556 and 250378. DSM organism Go0614654 and CCUG
  organism Go0614655 have no additional project/analysis chain in these
  complete files, so organism-only representation is correct.
- **GTDB scope:** The complete pinned species cluster has four genomes:
  three assigned NCBI strain taxon 1032241 and one assigned species taxon
  708186. The fourth is CECT 7650, GCA/GCF_004115865.1, not an own
  carried deposit. Its BioSample SAMN07767229 and GOLD Go0260057 chain
  do not belong to this record. The live GTDB tree request failed;
  the complete native cluster was inspected.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:286420` and the
  [live SI-ID 368756 API record](https://api.straininfo.dsmz.de/v2/data/strain/max/368756)
  verify version DOI `10.60712/SI-ID368756.3`, BacDive 2101, published
  status and four available, nondeprecated, nonerroneous deposits:
  SI-DP 852915 LMG, 863702 CCUG, 870813 CIP and 915503 DSM. All carry
  source species taxon 708186 and type-strain evidence. Complete structured
  scanning of 314,470 native records found only this eligible group for
  the four carried deposits.
- **Own-deposit sequences:** All three SI assembly sequences and all six
  marker sequences explicitly name LMG deposit 852915. Other deposits
  receive their own SI strain/deposit associations, not transferred
  sequences. Live NCBI Nuccore metadata verify
  [FR682116.1](https://www.ncbi.nlm.nih.gov/nuccore/FR682116.1), partial
  rpoB, 435 bases; [FR682118.2](https://www.ncbi.nlm.nih.gov/nuccore/FR682118.2),
  partial gyrB, 665 bases;
  [HF935055.1](https://www.ncbi.nlm.nih.gov/nuccore/HF935055.1), partial
  ciaB, 255 bases; [HF935057.1](https://www.ncbi.nlm.nih.gov/nuccore/HF935057.1),
  partial cj1349, 551 bases; and
  [MG195901.1](https://www.ncbi.nlm.nih.gov/nuccore/MG195901.1) /
  [MG196030.1](https://www.ncbi.nlm.nih.gov/nuccore/MG196030.1), partial
  16S/23S rRNA, 1506/2912 bases. The first four have source taxon 1032241;
  the rRNAs carry species taxon 708186 and LMG 25534T. The source headline
  `LM 25534` on HF935055 is retained, while its actual NCBI source features
  explicitly say strain LMG 25534 and collection LMG:25534. The join does
  not depend on silently rewriting that headline.
- **AllTheBacteria:** Native catalog row 2243832 and
  `data/atb/assemblies.tsv:8557` agree on all 17 fields. Assembly
  `atb.assembly:202505.SAMN25938061` is r0.2, PASS/PASS, with an available
  FASTA, run SRR18076127 and analysis ERZ26086489. Composite source name,
  sylph name, SeqKit sum, AWS/OSF URLs and archive filename are preserved.
  Four exact sample assertions at `data/atb/strain_links.tsv:3425` already
  occur on this strain. Genome-link rows 14834-14837 contain seven verified
  same-source pairs across GTDB RS_GCF_024584015.1, GCA/GCF_024584015.1
  and PATRIC 1032241.7. Live
  [ENA run XML](https://www.ebi.ac.uk/ena/browser/api/xml/SRR18076127) and
  [ENA analysis XML](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26086489)
  confirm sample SRS12049022 / SAMN25938061 and the explicit run link.
  Shared sample does not establish sequence or assembly equivalence.
- **Attestations:** NCBI NAME 1, GTDB GENOME 4, BacDive STRAIN 1,
  MediaDive MEDIUM 1 (693), MADIN TRAIT_ASSERTION 4 and BACTOTRAITS
  TRAIT_ASSERTION 15 reproduce their distinct source units. Relevant raw
  rows are GTDB 1341, BacDive 2096, MediaDive 99, MADIN 603 and
  BACTOTRAITS 73. No raw GOLD attestation row maps to this target;
  supplemental native GOLD associations are a separate evidence surface.
- **iModulonDB:** Ran
  `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets`.
  After a sandbox DNS failure, the public network retry returned 28 dataset
  keys, none for Aliarcobacter or Arcobacter. No organism-matched gene
  search applies. This absence is not negative gene or phenotype evidence.

## Completeness

Ignored-inclusive compressed searches covered all native catalog, BacDive,
BV-BRC, GOLD and SeqCode files using taxon names, target/deposit identifiers
and the specific isolate aliases. Full structured scans covered source
inventories, type material, merged/dropped IDs and SI eligibility. No
additional eligible own-deposit genome association was found in those
bounded pinned sources. SeqCode name entries 3074/24432 are not genomes.

The full 3,227,665-row native ATB catalog was checked against all three own
BioSamples. SAMN03737959 has a FASTA and a sylph PASS but retains
`META_FAIL`: native row 1097525 agrees with
`data/atb/assemblies.tsv:3787`, and exclusion row 2074 records the identity
filter. Earlier HQ status does not override that filter. SAMN07767218 is
absent from the full native/committed scan. Only SAMN25938061 is eligible.

All four carried deposits pass CAFI full-accession matching. Bare aliases,
CECT 7650 and other LMG deposits do not become join keys. The public
BacDive page calls 2101 an isotype of 132895; the pinned latter record is
species-mapped, carries no genome sequences and is not an additional
own-deposit genome link. Do not merge BacDive records from that status alone.

Record-local LPSN/type flag omission follows current policy, not a claim of
biological non-type status. NCBI parent type-material rows 259381-259391,
BacDive, all four SI deposits and live BioSamples provide type evidence in
their own scopes. Optional phenotype and graph fields need not be added.

## Findings

Counts: 0 blocker, 2 major, 0 minor.

**M1 - Major: species-level GTDB identity is promoted onto one strain.**
Target lines 46-49 make `Aliarcobacter trophiarum` an `EXACT_SYNONYM`,
and line 63 emits `GTDB:s__Aliarcobacter_trophiarum` as an identity xref.
The four-member native cluster contains the separate CECT 7650 strain;
its species name and whole-cluster count cannot establish exact LMG 25534
identity. Maintained owner: `src/taxonmech/seed.py:451` performs rank-blind
`skos:closeMatch` identity promotion; `src/taxonmech/extract.py:755`
copies the cluster-wide count. Keep the source mapping distinct from exact
identity and describe its count scope.

**M2 - Major: an exact NCBI synonym conflicts with a different isolate.**
Target lines 53-55 attach `Arcobacter sp. 122/3-38/R-39970` as an exact
synonym of LMG 25534. This faithfully reproduces the pinned names row and
live NCBI taxonomy, but independent strain evidence contradicts the implied
identity. Native SI row 290331 and the
[live SI-ID 380030 record](https://api.straininfo.dsmz.de/v2/data/strain/max/380030)
assign De Smet 122, 3-38 and R-39970 to non-type LMG 25535 / CCUG 59230,
not type strain LMG 25534 / CCUG 59229. The inspected
[original species-description abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.022665-0)
distinguishes isolates 64 and 122 and explicitly identifies type strain 64
as LMG 25534. Their species membership does not make them the same strain.

This is an unresolved upstream source-identity conflict, not grounds to
replace the record's correct primary identifier or transfer LMG 25535 data.
The import owner is `src/taxonmech/ncbi_taxdump.py:91`, which assigns NCBI
`synonym`/`equivalent name` classes to `EXACT_SYNONYM`; inventory emission
is in `src/taxonmech/extract.py:741` and consumption in `seed.py:381`.
The source assertion needs NCBI/collection resolution or a separately
authorized, explicit harmonization decision. No blanket demotion of all
NCBI synonyms or silent generated-YAML correction is justified.

## Recommended Edits

1. Fix M1 with rank-aware GTDB identity promotion in `src/taxonmech/seed.py`
   and focused `tests/test_seed.py` coverage. Preserve species-level
   identity behavior and legitimate deposit-backed genome links. Explain
   count four as the species-cluster total.
2. Route M2's evidence to the upstream NCBI taxonomy/collection owners
   for resolution after authorization; this review sends no message.
   Once corrected upstream, refresh the pinned taxonomy through the
   maintained extraction path and regenerate. Any interim source-qualified
   conflict handling must be explicitly designed in maintained import/
   harmonization code with a targeted regression, not an ad hoc YAML edit
   or a global change to synonym semantics.
3. Preserve all 25/16/60 source assertions, the four carried deposits and
   the SI/ATB match boundaries. After curation authorization, use the
   documented dry run and `just seed-canary NCBITaxon:1032241` before
   any bulk regeneration.

## Follow-up Checks

For M1, run the focused seed regression, both single-file validators and
the four-member native cluster census. For M2, recheck the primary species
description, both SI strain groups and the corrected NCBI names assertion;
confirm LMG 25535 is not treated as a deposit of this record. Do not call
the conflict resolved merely because the YAML validates or reproduces.
Recheck all 17 SI evidence objects, FR682118's actual current version,
the four ATB sample assertions/seven source-chain pairs and the META_FAIL
exclusion. Full corpus reproduction, provenance/QC and rendered products
remain release gates.

## Additional Notes

- The NCBI synonym conflict is separate from NCBI/LPSN genus preference
  and from the GTDB rank error. NCBI's label, parent and lineage remain
  carried source classification.
- Live FR682118 resolves to version 2, not version 1. The YAML's
  unversioned accession correctly reflects SI and should not be patched
  to a guessed version. No sequence alignment or functional assay was run.
- FN650333 is BacDive's separate 16S sequence for strain 64 and is not
  an SI own-deposit sequence in this snapshot. A further identity lead,
  FN650332, currently says strain 123 in NCBI; it was not used to assert
  equivalence with strain 122, R-39970 or the target.
- The original species-description abstract was inspected, not its full
  paper or all supplemental tables. The SI DOI and source sequence metadata
  were verified. Annotation labels such as ciaB and cj1349 are not direct
  experimental proof of invasion or binding by this strain.
- The type-flag contract at `src/taxonmech/schema/taxonmech.yaml:477`
  uses this record's own LPSN name. Ancestor/other-source type evidence
  requires an explicit policy extension rather than silent transfer.
- ENA file MD5 differs from ATB's SeqKit sum. Mutable AWS object freshness,
  FASTA hashes and sequence equivalence were not checked. Only this target
  was judged; neighboring source rows are identity candidates, not reviews
  of their YAML. Eukaryota and prior reports were untouched.
