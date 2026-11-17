# YAML Record Review: Aliarcobacter skirrowii CCUG 10374

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aliarcobacter_skirrowii_ccug_10374.yaml`
- Started UTC: 2026-10-03T21:12:12Z
- Finished UTC: 2026-10-03T21:18:53Z
- Verdict: needs curation

## Target

Read the full 2,119-line generated `TaxonRecord`, `NCBITaxon:1032239`,
Aliarcobacter skirrowii CCUG 10374, rank `STRAIN`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. Its one BacDive strain has
40 assembly, 25 genome-record and 94 related-record assertions. These
counts describe provenance assertions, not distinct biological genomes.
The target is this strain, not parent species `NCBITaxon:28200`.

Maintained owners are the source inventories, `src/taxonmech/seed.py` and
`src/taxonmech/extract.py`. This read-only review changes no generated YAML,
status, source data, prior report or curation history.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aliarcobacter_skirrowii_ccug_10374.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aliarcobacter_skirrowii_ccug_10374.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured inventory comparisons | Backbone, lineage, scope, path index and attestations agree. Full-field multiset equality for 40 assemblies, 24 non-ATB genome records and 94 related records. |
| StrainInfo evidence | All 31 evidence objects agree with native own-deposit eligibility, DOI, taxonomy and explicit sequence-deposit membership. |
| AllTheBacteria evidence | All 17 native metadata fields match the committed row; the entire YAML evidence object matches. Four sample assertions and seven source-chain pairs across four genome crosslinks pass exact structured comparisons. |
| Embedded history | Strict validation passed; the seven-source seed event and scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored and hidden files found no target history entry. |
| Graph and ontology-product gates | Not applicable: no causal graph or curator-added graph nodes occur in the full YAML. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports, full tests, FASTA downloads or checksum
replay. Focused source comparisons are not a substitute for corpus
reproduction. No generator, history writer or status promotion was run.

## Identity and Grounding

The NCBI identifier, label, five equivalent names, parent, genetic code 11
and ten root-first lineage entries match
`data/raw/ncbitaxon_taxa.tsv:220797`. Live EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032239,28200)
corroborate the strain and parent. Native names are in
`data/catalog/ncbi_names-0005.jsonl.gz:30023` and the next five rows.
`data/taxa/PATHS.tsv:13159` and `curation/seed_scope.tsv:7208` agree.
A complete backbone scan found no children of this strain.

Preserve the nomenclatural disagreement: NCBI carries Aliarcobacter,
whereas [LPSN Aliarcobacter skirrowii](https://lpsn.dsmz.de/species/aliarcobacter-skirrowii)
lists name 5967 as a validly published synonym and
[LPSN Arcobacter skirrowii](https://lpsn.dsmz.de/species/arcobacter-skirrowii)
lists name 773370 as the correct name. The 2020 valid combination is not
the earlier invalidly published 2018 name. Parent-name inventory row
`data/raw/lpsn_names.tsv:1137` agrees. Neither source authorizes replacing
the carried NCBI label or lineage.

The LPSN type designations include 449/80, ATCC 51132, CCUG 10374,
CIP 103538, CIP 103588, DSM 7302, LMG 6621 and NCTC 12713; the two CIP
numbers are independently attested, not a spelling correction to infer.
There is no direct LPSN name row for this strain-level taxon. Its NCBI
strain synonyms are supported, but the species-level GTDB exact synonym
and identity xref are over-scoped, as described in M1.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:2090`, native
  `data/bacdive/records.jsonl.gz:2089` and the inspected
  [BacDive 2095 page](https://bacdive.dsmz.de/strain/2095) support designation
  `WCDM 00067, 449/80` and the 12 carried culture identifiers. Reference
  66792 supports GCA_003544835 and GCA_024584055; reference 67770 supports
  GCA_004115735, GCA_008802155 and GCA_900445295. Their IMG/PATRIC
  associations retain the particular source reference rather than becoming
  evidence for every field on the record.
- **Inventory fidelity:** The complete assertion multisets match
  `data/raw/strain_assemblies.tsv` rows 106264-106296 plus
  `data/straininfo/assemblies.tsv` rows 7696-7702;
  `data/raw/strain_genome_records.tsv` rows 85501-85524; and
  `data/raw/strain_related_records.tsv` rows 307464-307533 plus
  `data/straininfo/related_records.tsv.gz` rows 190735-190758.
  The additional ATB record was checked separately against native metadata.
- **NCBI assemblies:** Native GenBank and RefSeq rows support five paired
  current assemblies. Live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_003544835.1,GCF_003544835.1,GCA_004115735.1,GCF_004115735.1,GCA_008802155.1,GCF_008802155.1,GCA_024584055.1,GCF_024584055.1,GCA_900445295.1,GCF_900445295.1/dataset_report)
  confirm the following distinct source chains. Unversioned BacDive and
  StrainInfo accessions remain unversioned in the YAML.

| GCA/GCF accession stem, version 1 | Deposit | Assembly | BioSample | Original project |
| --- | --- | --- | --- | --- |
| 003544835 | CCUG 10374 | Complete, ASM354483v1 | SAMN03737956 | PRJNA66827 |
| 004115735 | LMG 6621 | Contig, ASM411573v1 | SAMN07709799 | PRJNA412344 |
| 008802155 | CCUG 10374 | Contig, ASM880215v1 | SAMN12697556 | PRJNA563568 |
| 024584055 | LMG 6621 | Contig, ASM2458405v1 | SAMN25938058 | PRJNA808439 |
| 900445295 | NCTC 12713 | Contig, 57800_A01 | SAMEA104224806 | PRJEB6403 |

- **Source-specific assembly context:** The first four pairs have taxon
  1032239; the NCTC pair has species taxon 28200. Native RefSeq/GTDB
  PRJNA224116 assertions are retained even where the live API reports the
  original project. Compact `NCTC12713` in native assembly/GTDB strain
  fields does not pass the current CAFI deposit matcher; its independent
  BacDive, BV-BRC, GOLD and StrainInfo links remain supported.
- **BV-BRC:** `data/bvbrc/bvbrc-0000.jsonl.gz` rows 3144-3147 support
  PATRIC 1032239.3 through 1032239.6. Row 1704 in shard 0016 supports
  28200.27 through culture field `NCTC:12713`. The accepted whole strain
  values are LMG 6621 and CCUG 10374; `LMG:6621T`, `CCUG culture` and
  compact `NCTC12713` are not silently normalized into extra matches.
- **GOLD:** Complete own-ID searches of
  `data/gold/{organisms,projects,analyses}.jsonl.gz` support
  Go0011290 -> Gp0380739 -> Ga0349706 -> GCA_003544835.1 / IMG 2843847787;
  Go0519044 -> Gp0443179 -> Ga0396092 -> GCA_004115735.1 / IMG 2873822735;
  and Go0468527 -> Gp0342139 -> Ga0317373 -> GCA_900445295.1 / IMG
  2814123187. Both organism strain and collection fields match their own
  deposits. Go0623641 (DSM 7302) and Go0623642 (ATCC 51132) have no
  additional project/analysis chain in the fully searched native files;
  organism-only representation is correct. WRI 449/80 alone does not
  establish another eligible chain.
- **GTDB genomes:** Four deposit-backed native genome records retain
  their own assembly, sample and project evidence. The complete pinned
  `s__Aliarcobacter_skirrowii` cluster has 44 genomes: 35 assigned NCBI
  taxon 28200, four 1032239, one 165434, one 2021861, two 2321116 and one
  1977087. This cluster census is not a count of 44 genomes established as
  CCUG 10374. The live GTDB tree request failed; native evidence was
  available and inspected.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:979` and the
  [live SI-ID 979 API record](https://api.straininfo.dsmz.de/v2/data/strain/max/979)
  support version DOI `10.60712/SI-ID979.3`, BacDive 2095 and published
  status. All eight own deposits are available, nondeprecated and
  nonerroneous: SI-DP 3960 LMG, 3961 CCUG, 3962 CIP 103538, 115207 ATCC,
  128231 DSM, 148609 CIP 103588, 342786 NCTC and 898564 CECT. They carry
  species taxon 28200 and type-strain evidence. Complete structured
  scanning of all 314,470 native records found no other own-deposit group;
  JCM 33358 is only a group alias, not an SI-DP to which sequences may
  be transferred.
- **Own-deposit sequences:** Seven SI assembly associations are supported:
  GCA_003544835 and GCA_008802155 explicitly name CCUG; GCA_004115735
  and GCA_024584055 explicitly name both CCUG and LMG; GCA_900445295
  explicitly names NCTC. Eight additional sequence accessions have explicit
  own-deposit membership and verified live NCBI Nuccore metadata: ATCC
  [AB104484.1](https://www.ncbi.nlm.nih.gov/nuccore/AB104484.1), rpoB/rpoC,
  and [DQ059471.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ059471.1), cpn60;
  LMG [EF667145.1](https://www.ncbi.nlm.nih.gov/nuccore/EF667145.1),
  hypothetical protein/flaA/flaB,
  [EU669897.1](https://www.ncbi.nlm.nih.gov/nuccore/EU669897.1), rpoB,
  [FN600703.1](https://www.ncbi.nlm.nih.gov/nuccore/FN600703.1), 23S rRNA,
  [GU291962.1](https://www.ncbi.nlm.nih.gov/nuccore/GU291962.1), gyrB,
  and [X80385.1](https://www.ncbi.nlm.nih.gov/nuccore/X80385.1), 23S rRNA;
  CCUG [L14625.1](https://www.ncbi.nlm.nih.gov/nuccore/L14625.1), 16S rRNA.
  StrainInfo's `gene` vocabulary for FN600703 does not imply protein coding.
- **AllTheBacteria:** Native row 2243829 in
  `data/catalog/allthebacteria.tsv.xz` exactly matches all 17 fields of
  `data/atb/assemblies.tsv:8554`. Snapshot genome
  `atb.assembly:202505.SAMN25938058` is r0.2, PASS/PASS, with an available
  FASTA, run SRR18076130 and analysis ERZ26086475. SeqKit sum, sylph name,
  AWS URL, OSF URL and archive filename are preserved. The four exact
  BioSample assertions in `data/atb/strain_links.tsv:3423` are already
  present on this strain. Genome-link rows 14826-14829 contain seven
  verified same-source-chain pairs across GTDB RS_GCF_024584055.1,
  GCA/GCF_024584055.1 and PATRIC 1032239.6, without a Cartesian join.
  Live [ENA run XML](https://www.ebi.ac.uk/ena/browser/api/xml/SRR18076130)
  and [ENA analysis XML](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26086475)
  confirm the shared sample SRS12049019 / SAMN25938058 and the run link.
  Shared BioSample is not assembly or sequence equivalence.
- **Attestations:** Structured comparisons reproduce NCBI NAME 1, GTDB
  GENOME 44, BacDive STRAIN 1, MediaDive MEDIUM 2 (693 and J256), GOLD
  ORGANISM 2, MADIN TRAIT_ASSERTION 2 and BACTOTRAITS TRAIT_ASSERTION 8.
  Raw mapping/attestation rows are GTDB 1339, BacDive 2090, MediaDive 97,
  GOLD 418, MADIN 601 and BACTOTRAITS 71. Counts have distinct source
  units and are not summed. The older GOLD attestation count is not a
  census of every organism in the separately pinned native catalog.
- **iModulonDB:** The resolved shared `kg-microbe-sources imodulondb datasets`
  adapter returned 28 dataset keys, none for Aliarcobacter or Arcobacter.
  No organism-matched marker query applies; this is not negative evidence
  about these genes or the strain.

## Completeness

Ignored-inclusive searches covered native catalog, BacDive, BV-BRC, GOLD,
SeqCode and history using the taxon ID, species names, label, slug and
deposit candidates. Structured full-inventory scans covered type material,
merged/dropped IDs, source assertions and StrainInfo own-deposit eligibility.
No additional eligible genome association was found within these pinned
source boundaries. Bare names, numerical substring coincidences, separate
cluster members and SeqCode nomenclatural entries are not genome evidence.

The full 3,227,665-row native ATB catalog was scanned for all five own
BioSamples. SAMEA104224806 has no available FASTA and is correctly excluded
as `assembly_unavailable`. SAMN03737956 has a FASTA but `META_FAIL` and is
correctly excluded as `metadata_identity_flags:META_FAIL`. SAMN07709799
and SAMN12697556 are absent from that complete scan and committed metadata.
Only SAMN25938058 is eligible. The native/committed rows and exclusions
agree; absence was not inferred from a gitignore-filtered search.

All 12 culture strings reproduce BacDive, but CAFI accepts only nine as
deposit keys. `CIP 1035838T`, `WDCM 00067` and `WRI 449/80` remain source
strings without becoming joins. Neither their spelling nor `WCDM 00067`
in the designation is silently repaired. JCM's group alias does not supply
missing StrainInfo sequences. Current policy leaves record-local LPSN
nomenclature and `is_type_strain` absent here; that omission is not a claim
that the biological strain is non-type. Phenotypes, media recipes and causal
graphs are not required additions to this identity/provenance record.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: a GTDB species identity is promoted onto one strain.**
Target lines 46-49 make `Aliarcobacter skirrowii` an `EXACT_SYNONYM`, and
line 66 makes `GTDB:s__Aliarcobacter_skirrowii` an identity xref. The native
44-member cluster spans six NCBI taxa and includes other strains, such as
17-1208-2, L402 and CECT 9299. Its species name and total cannot establish
exact CCUG 10374 identity.

Maintained owner: `src/taxonmech/seed.py:451` treats `skos:closeMatch` as
identity without a rank check and emits the exact synonym and xref.
`src/taxonmech/extract.py:755` copies a cluster-wide genome count into the
mapping. Preserve the upstream mapping predicate as an observation while
preventing unsupported identity promotion and explaining count scope.
These manifestations are one scope defect, not a wrong NCBI identifier,
invalid YAML or rejection of the deposit-backed genome links.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   Suppress the species exact synonym and identity xref on this strain;
   retain supported NCBI strain synonyms and explicitly scoped mappings.
2. Identify 44 as a species-cluster count. Any alternative count policy
   belongs in the maintained extractor with explicit provenance semantics,
   not a hand edit of the raw mapping or generated YAML.
3. Add strain-versus-species regression coverage in `tests/test_seed.py`,
   preserving valid species identity behavior and all 40/25/94 assertions.
   After curation authorization, use the documented dry run and
   `just seed-canary NCBITaxon:1032239` before bulk regeneration.

## Follow-up Checks

Run the focused seed regression and both recorded single-file validators.
Repeat the 44-member native GTDB census; confirm removal of the unsupported
identity promotion without losing deposit-backed associations. Recheck all
31 SI evidence objects and the four ATB sample assertions/seven same-chain
pairs. Retain both ATB exclusions and the alias/full-accession boundaries.
Full corpus reproduction, strict validation, provenance/QC and rendered
products remain release gates, not checks claimed by this review.

## Additional Notes

- The type flag contract at `src/taxonmech/schema/taxonmech.yaml:477` and
  the seeder use LPSN designations for this record's own name. Copying
  ancestor or other-source type evidence requires an explicit policy
  extension; the eight SI deposit type flags were not transferred silently.
- Live SAMN25938058 host metadata differ from earlier lamb-associated
  CCUG/NCTC sample context. Preserve that sample-specific source difference;
  no host phenotype is asserted in this YAML or inferred by this review.
- MG195899 and DQ464344 are not SI own-deposit sequence assertions in the
  inspected group. Their occurrence in other sources is not authorization
  to add them as StrainInfo evidence.
- The ENA file MD5 and ATB SeqKit sum are different quantities. No FASTA,
  sequence equivalence, mutable AWS object freshness or download hash was
  tested. Full literature texts and protein annotations were not reanalysed;
  the strain-version DOI was verified at the source API.
- Only this target was judged. Candidate rows are not reviews of their
  YAML records. Eukaryota and previous reports were untouched.
