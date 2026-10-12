# YAML Record Review: Aliarcobacter thereius LMG 24486

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aliarcobacter_thereius_lmg_24486.yaml`
- Started UTC: 2026-10-03T21:21:13Z
- Finished UTC: 2026-10-03T21:25:10Z
- Verdict: needs curation

## Target

Read all 1,512 lines of this generated `TaxonRecord`, `NCBITaxon:1032240`,
Aliarcobacter thereius LMG 24486, rank `STRAIN`, domain `BACTERIA`,
grounding `EXACT`, mapping status `SEEDED`. Its one BacDive strain has
34 assembly, 21 genome-record and 68 related-record assertions. These are
provenance assertions, not counts of distinct biological genomes. The target
is the strain, not its parent species `NCBITaxon:544718`.

Maintained owners are the source inventories, `src/taxonmech/seed.py` and
`src/taxonmech/extract.py`. No generated YAML, source data, status, prior
report or curation history was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aliarcobacter_thereius_lmg_24486.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aliarcobacter_thereius_lmg_24486.yaml` | Passed; one file, zero ERROR rows. Standard diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured inventories | Backbone, full lineage, scope, path index and all attestations agree. Exact full-field multiset equality for 34 assembly, 20 non-ATB genome and 68 related assertions. |
| StrainInfo evidence | All ten evidence objects match native own-deposit eligibility, DOI, source taxonomy and explicit sequence-deposit membership. |
| AllTheBacteria evidence | Native and committed metadata agree on all 17 fields; the entire YAML evidence object matches. Four sample assertions and seven same-source-chain pairs across four genome links pass exact comparisons. |
| Embedded history | Strict validation passed; the six-source seed event and scope reason agree. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored and hidden files found no target entry under `history/`. |
| Graph and ontology-product gates | Not applicable: the full YAML contains no causal graph or curator-added graph nodes. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
rendered-page freshness, exports, full tests, FASTA downloads and checksum
replay. Focused comparisons do not substitute for full-corpus reproduction.
No generator, history writer or status promotion was run.

## Identity and Grounding

The identifier, label, four NCBI equivalent names, parent, genetic code 11
and all ten root-first lineage entries match
`data/raw/ncbitaxon_taxa.tsv:220798`. Live EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032240,544718)
corroborate the strain and parent. Native names in
`data/catalog/ncbi_names-0005.jsonl.gz` rows 30029-30033,
`data/taxa/PATHS.tsv:13160` and `curation/seed_scope.tsv:10792` agree.
A complete backbone scan found no children of this strain.

Preserve the source naming difference: NCBI carries Aliarcobacter thereius;
[LPSN Aliarcobacter thereius](https://lpsn.dsmz.de/species/aliarcobacter-thereius)
lists name 5968 as a validly published synonym, while
[LPSN Arcobacter thereius](https://lpsn.dsmz.de/species/arcobacter-thereius)
lists name 788114 as the correct name. The valid 2020 combination is
distinct from the invalidly published 2018 version. Parent-name inventory
row `data/raw/lpsn_names.tsv:1138` agrees; no direct LPSN name row maps to
this strain taxon. This difference does not authorize rewriting NCBI's
carried name or lineage.

LPSN lists CCUG 56902, DSM 23385 and LMG 24486 alongside designation
16389 and an additional LMG 22486. Only the first three collection deposits
are carried by this BacDive strain and independently supported by NCBI and
StrainInfo. The extra LPSN number is not silently imported as a join key;
see Additional Notes. The unsupported species-level exact synonym is M1.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:2094`, native
  `data/bacdive/records.jsonl.gz:2093` and the inspected
  [BacDive 2099 page](https://bacdive.dsmz.de/strain/2099) support designation
  `strain 16389` and deposits CCUG 56902, DSM 23385 and LMG 24486.
  Native genome reference 66792 supplies four unversioned GCA accessions,
  two IMG identifiers and four PATRIC identifiers, with their individual
  assembly names, levels and taxonomy. The native projection has no
  collection-list section; the raw inventory and public page supply that
  part of the deposit check.
- **Inventory fidelity:** Exact assertions reproduce
  `data/raw/strain_assemblies.tsv` rows 106353-106382 plus
  `data/straininfo/assemblies.tsv` rows 7711-7714;
  `data/raw/strain_genome_records.tsv` rows 85567-85586; and
  `data/raw/strain_related_records.tsv` rows 307663-307724 plus
  `data/straininfo/related_records.tsv.gz` rows 190803-190808. The additional
  ATB genome was checked separately.
- **NCBI assemblies:** Native GenBank/RefSeq catalogs and live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001695395.1,GCF_001695395.1,GCA_004214815.1,GCF_004214815.1,GCA_005818985.1,GCF_005818985.1,GCA_024584025.1,GCF_024584025.1/dataset_report)
  confirm all eight current accessions and the four paired assembly chains
  below. Native RefSeq/GTDB PRJNA224116 remains a source-specific assertion
  even though the live API reports each original project. Unversioned
  BacDive and StrainInfo accessions are not assigned an invented version.

| GCA/GCF accession stem, version 1 | Deposit | Assembly | BioSample | Original project |
| --- | --- | --- | --- | --- |
| 001695395 | LMG 24486 | Scaffold, ASM169539v1 | SAMN03654041 | PRJNA283692 |
| 004214815 | LMG 24486 | Complete, ASM421481v1 | SAMN03737958 | PRJNA66829 |
| 005818985 | DSM 23385 | Contig, ASM581898v1 | SAMN11638433 | PRJNA542783 |
| 024584025 | LMG 24486 | Contig, ASM2458402v1 | SAMN25938059 | PRJNA808439 |

- **Taxonomy and native locations:** The DSM assembly pair carries species
  taxon 544718; the LMG pairs carry strain taxon 1032240. GenBank locations
  are shard 0001 row 15844, shard 0003 row 13107, shard 0004 row 39811 and
  shard 0022 row 38591 under `data/catalog/ncbi_genbank-*.jsonl.gz`.
  Corresponding RefSeq locations are shard 0001 row 5252, shard 0002
  rows 13701 and 21884, and shard 0004 row 22283.
- **BV-BRC:** `data/bvbrc/bvbrc-0000.jsonl.gz` rows 3148-3150 support
  PATRIC 1032240.3, 1032240.8 and 1032240.9; shard 0021 row 39961
  supports 544718.59. All own strain fields are supported. The first
  culture field `LMG 24486T` is correctly rejected as an unsupported full
  accession; its separate `LMG 24486` strain field is accepted. Both strain
  and culture fields independently match 1032240.8 and 544718.59.
- **GOLD:** Full own-ID searches of
  `data/gold/{organisms,projects,analyses}.jsonl.gz` verify
  Go0010354 -> Gp0374769 -> Ga0336799 -> GCA_001695395.1 / IMG 2876158629,
  and Go0612671 -> Gp0817989 -> Ga0667657 -> GCA_005818985.1 / IMG
  8118118232. Both organism strain and collection fields support each
  deposit match. Gp0010354 has PRJNA66829 but no native BioSample or
  downstream analysis; it is correctly represented without inventing
  another genome chain. CCUG organism Go0612672 has no project/analysis
  chain in these complete files and remains organism-only. Organism rows
  are 9094, 443416 and 443417; project rows 8959, 262366 and 603358;
  analysis rows 196786 and 447660.
- **GTDB genomes:** Native GTDB shard/row pairs 0013/30127, 0011/26701,
  0002/46336 and 0016/18364 support the four own-deposit genome links.
  The complete `s__Aliarcobacter thereius` cluster has ten genomes: three
  with NCBI strain taxon 1032240 and seven with species taxon 544718.
  DSM 23385 is an independently supported own deposit, but the remaining
  cluster members include 440, DU22, 452, 17CS1191_2, 17CS1200_2 and
  CHK160-9197. Those are not evidence for LMG 24486 identity.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:232598` and the
  [live SI-ID 302813 API record](https://api.straininfo.dsmz.de/v2/data/strain/max/302813)
  support DOI `10.60712/SI-ID302813.3`, BacDive 2099 and published status.
  Available, nondeprecated and nonerroneous own deposits are SI-DP 844447
  LMG 24486, 844448 CCUG 56902 and 904536 DSM 23385, each with source
  species taxon 544718 and type-strain evidence. Complete structured
  scanning of all 314,470 native records found exactly this eligible group
  for the three carried deposits.
- **Sequence scope:** The three LMG assembly accessions explicitly name
  SI-DP 844447; GCA_005818985 explicitly names DSM deposit 904536.
  CCUG has no own sequence in this group and receives no sequence by
  transfer. The four assemblies, three deposit records and three
  strain-association records explain all ten SI evidence objects. Native
  and live SI show no gene/rRNA sequence in this group. BacDive/LPSN's
  AY314753 is not a missing StrainInfo assertion.
- **AllTheBacteria:** Native catalog row 2243830 agrees with
  `data/atb/assemblies.tsv:8555` on all 17 fields. Snapshot assembly
  `atb.assembly:202505.SAMN25938059` is r0.2, PASS/PASS, with an available
  FASTA, run SRR18076129 and analysis ERZ26086479. The composite supplied
  scientific name, sylph name, SeqKit sum, AWS/OSF URLs and archive filename
  are preserved. Four BioSample assertions in
  `data/atb/strain_links.tsv:3424` exactly match this strain's related
  records. Genome-link rows 14830-14833 contain seven verified same-source
  pairs across GTDB RS_GCF_024584025.1, GCA/GCF_024584025.1 and PATRIC
  1032240.9. Live [ENA run XML](https://www.ebi.ac.uk/ena/browser/api/xml/SRR18076129)
  and [ENA analysis XML](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26086479)
  corroborate sample SRS12049020 / SAMN25938059 and the run link. Shared
  BioSample is not assembly or sequence equivalence.
- **Attestations:** NCBI NAME 1, GTDB GENOME 10, BacDive STRAIN 1,
  MediaDive MEDIUM 1 (693), MADIN TRAIT_ASSERTION 2 and BACTOTRAITS
  TRAIT_ASSERTION 13 reproduce their inventories. Relevant raw rows are
  GTDB 1340, BacDive 2094, MediaDive 98, MADIN 602 and BACTOTRAITS 72.
  The raw GOLD attestation inventory has no target row; supplemental native
  GOLD links are a separate source surface, not a reason to invent an
  attestation count. Distinct source units are not summed.
- **iModulonDB:** Not applicable to the record's claims: it asserts no
  named gene, marker, regulator, pathway, stress response, phenotype or
  transcriptomic dataset. No expression-module query or negative biological
  inference was made.

## Completeness

Ignored-inclusive compressed searches covered all native catalog, BacDive,
BV-BRC, GOLD and SeqCode files using names, target identity and whole
deposit candidates. Complete structured scans covered source inventories,
type material, merged/dropped IDs and SI own-deposit eligibility. No further
eligible own-deposit genome association was found in these pinned sources.
Different strain members, LMG 24487 and bare 16389 records were not joined.
SeqCode name records 3073 and 24431 are nomenclatural leads, not genomes.

The complete 3,227,665-row native ATB catalog and committed metadata were
checked against all four own BioSamples. Only SAMN25938059 occurs;
SAMN03654041, SAMN03737958 and SAMN11638433 are absent from that full
scan. No own-sample exclusion row occurs in the complete exclusion inventory.
No other ATB association is required by the pinned source evidence.

The record-local LPSN/type flag omission follows current policy, not a
biological claim of non-type status. NCBI parent type-material rows
232097-232105, BacDive, all three SI deposits and live BioSamples support
type status in their own scopes. Raw BacDive medium count zero and the
taxon-level MEDIUM attestation are separate fields. Optional phenotypes
and a causal graph do not need to be invented.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: GTDB species identity is promoted onto one strain.**
Target lines 46-49 make `Aliarcobacter thereius` an `EXACT_SYNONYM`;
line 63 emits `GTDB:s__Aliarcobacter_thereius` as an identity xref.
The ten-member species cluster includes six other strains beyond the
four genomes supported through LMG/DSM deposits. Its species name and
cluster-wide count cannot establish exact identity with LMG 24486.

Maintained owner: `src/taxonmech/seed.py:451` treats `skos:closeMatch` as
identity without checking rank, then adds the synonym and xref.
`src/taxonmech/extract.py:755` supplies the cluster-wide genome count.
Preserve the upstream predicate as source mapping evidence while preventing
exact-identity promotion across species/strain scope. These are aspects of
one defect, not an invalid NCBI identifier or a failure of the deposit links.

## Recommended Edits

1. Make GTDB identity promotion rank-aware in `src/taxonmech/seed.py`.
   Suppress this species exact synonym and identity xref on the strain,
   preserving supported NCBI synonyms and explicitly scoped mappings.
2. Explain the cluster scope of count ten. Any alternative counting policy
   belongs in the maintained extractor with explicit provenance semantics,
   not manual changes to raw mappings or generated YAML.
3. Add strain-versus-species regression coverage in `tests/test_seed.py`,
   retaining valid species identity behavior and all 34/21/68 assertions.
   After curation authorization, use the documented dry run and
   `just seed-canary NCBITaxon:1032240` before bulk regeneration.

## Follow-up Checks

Run the focused seed regression and both single-file validators. Repeat the
native ten-member GTDB census and confirm that the unsupported identity
promotion is removed without losing any deposit-backed assertion. Recheck
all ten SI evidence objects and all four ATB sample assertions/seven
same-source-chain pairs. Full corpus reproduction, provenance/QC and
rendered products remain release gates, not checks claimed by this review.

## Additional Notes

- LPSN's additional LMG 22486 conflicts with native GOLD Go0212315, which
  labels that deposit Burkholderia cepacia, taxon 292. This is a source
  conflict outside the target's carried three deposits, not permission to
  merge those cultures. The linked live LMG catalog page was inaccessible
  through the web tool. No correction to either source is asserted here.
- `is_type_strain` at `src/taxonmech/schema/taxonmech.yaml:477` is defined
  against this record's own LPSN name. Ancestor-qualified or other-source
  type evidence requires an explicit policy extension, not silent transfer.
- Live BioSamples have differing dates and isolation-source descriptions,
  including the later pork sample. No single isolation narrative was
  inferred and none is asserted in this YAML.
- The live GTDB tree request failed; the full pinned native cluster was
  inspected. Source paper titles/identifiers are contextual, not literature
  claims carried by this YAML. Full papers, FASTAs and protein annotations
  were not reanalysed. The SI version DOI was verified at its source API.
- ENA file MD5 is not the ATB SeqKit sum. Mutable AWS object freshness and
  sequence equivalence were not tested. Only this target was judged;
  candidate rows are not reviews of their YAML. Eukaryota was untouched.
