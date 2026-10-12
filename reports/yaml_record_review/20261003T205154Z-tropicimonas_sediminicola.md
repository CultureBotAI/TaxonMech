# YAML Record Review: Tropicimonas sediminicola

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/tropicimonas_sediminicola.yaml`
- Started UTC: 2026-10-03T20:45:51Z
- Finished UTC: 2026-10-03T20:51:54Z
- Verdict: pass with minor issues

## Target

Read all 704 lines of this generated `TaxonRecord`: `NCBITaxon:1031541`,
Tropicimonas sediminicola, rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`. Its one BacDive strain carries ten
assembly assertions, eight genome-record assertions, including one
AllTheBacteria entry, and 26 related-record assertions. These totals count
source assertions, not distinct biological genomes.

This is a read-only review. Future corrections belong in maintained source
inputs and transforms, not generated YAML. Only this individual report
and the standard validator diagnostic were written.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/tropicimonas_sediminicola.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/tropicimonas_sediminicola.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Backbone, nine-entry lineage, synonyms, seed reason and all eight source attestations checked against complete inventories. Exact full-field multiset equality for all ten assembly, seven non-ATB genome and 26 related-record assertions. |
| StrainInfo evidence | All three evidence objects match the native strain, eligible own deposit, DOI, statuses, deposit taxonomy and explicitly deposit-linked genome. |
| ATB evidence | All 17 native metadata columns match the committed row; YAML metadata and all seven sample-evidence objects agree. Five genome crosslinks retain 13 supported genome/sample evidence pairs. |
| Embedded history | Strict validation passed; the seed event agrees with the eight-source scope reason. |
| Standalone history | Not applicable: ignored/hidden-inclusive identifier, label and slug search found no target entry under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the complete record has no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports, genome FASTA downloads or
sequence-digest replay. The bounded source comparisons are not substitutes
for those checks. No generator, history writer or status promotion ran.

## Identity and Grounding

The species identifier, label, parent `NCBITaxon:599652`, genetic code 11,
lineage labels and ranks match `data/raw/ncbitaxon_taxa.tsv:220746` and live
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031541).
Taxonomy EFetch also confirms the authority and includes-name represented
as related synonyms. Native name rows 29917-29919 in
`data/catalog/ncbi_names-0005.jsonl.gz` support these distinctions. A full
backbone scan finds no children. `data/taxa/PATHS.tsv:13073` resolves this
identifier and slug uniquely in the index; `curation/seed_scope.tsv:4038`
preserves the eight-source inclusion reason.

The inspected [LPSN page](https://lpsn.dsmz.de/species/tropicimonas-sediminicola)
confirms name 790190, the 2012 authority, valid publication, current-name
status, Hordt et al. 2020 emendation and marker JF748735. The local
nomenclature faithfully copies `data/raw/lpsn_names.tsv:27170`, but its
type-deposit list omits one authority-listed collection identifier; see N1.

The GTDB `skos:closeMatch`, count one and species xref are supported by
`data/raw/gtdb_mappings.tsv:1309`, the LPSN inventory link and the native
representative type genome. GTDB uses Rhodobacteraceae where NCBI uses
Roseobacteraceae. The record correctly retains NCBI's lineage rather than
silently replacing it with GTDB classification.

## Evidence

- **BacDive:** `data/raw/bacdive_strains.tsv:52946`, native
  `data/bacdive/records.jsonl.gz:52945` and the inspected
  [BacDive strain page](https://bacdive.dsmz.de/strain/130633) support M97,
  DSM 29339, JCM 17731, KACC 15544 and type-strain status. Native reference
  66792 supplies unversioned GCA_900188335, IMG 2681813518 and BV-BRC
  1031541.3 at contig level; the public references section identifies
  66792 as automated DiASPora annotation, not an experimental paper.
- **Inventory fidelity:** Raw assembly rows 16083-16091 and
  `data/straininfo/assemblies.tsv:1606` account for all ten assertions.
  Raw genome-record rows 12537-12543 account for the seven non-ATB
  assertions. Raw related-record rows 47366-47389 plus StrainInfo gzip
  rows 26166-26167 account for all 26 related assertions. All fields,
  accession versions, source fields and provenance objects match.
- **BV-BRC:** `data/bvbrc/bvbrc-0000.jsonl.gz:3069` supplies genome
  1031541.3, GCA_900188335.1, SAMN05421757 and PRJEB21423. Both explicit
  culture-collection and strain fields contain DSM 29339 and support
  separate, retained assertions for the same deposit.
- **GOLD:** Native organism rows 37234, 448992 and 448993 in
  `data/gold/organisms.jsonl.gz` identify DSM Go0044395, KACC Go0618318
  and JCM Go0618319. The actual sequencing chain is DSM organism
  Go0044395 -> project Gp0131681 -> analysis Ga0111647, supported by
  `data/gold/projects.jsonl.gz:79613` and
  `data/gold/analyses.jsonl.gz:61441`. It supplies GCA_900188335.1,
  IMG 2681813518, SAMN05421757 and PRJNA329778. The analysis reaches its
  organism through its explicit project, not its empty direct-organism
  field. Full native searches found no project/analysis chain for the
  other two organisms; their organism links are correctly not promoted
  to additional assemblies.
- **NCBI assemblies:** Native
  `data/catalog/ncbi_genbank-0056.jsonl.gz:45846` and
  `ncbi_refseq-0009.jsonl.gz:33088`, corroborated by live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_900188335.1,GCF_900188335.1/dataset_report),
  support the current GCA/GCF_900188335.1 pair, DSM 29339, type material,
  contig level and BioSample. The snapshot associates GenBank with
  PRJEB21423 and RefSeq with PRJNA224116; the BioSample itself links to
  PRJNA329778. Those different source scopes must remain separate.
- **GTDB:** `data/catalog/gtdb_genomes-0006.jsonl.gz:1585` identifies
  RS_GCF_900188335.1 as the sole exact-species cluster member and
  representative, with DSM 29339, both assembly accessions, BioSample
  and PRJNA224116. The public GTDB tree request failed; this check uses
  the pinned native metadata, not an asserted successful live lookup.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:301977`,
  `data/straininfo/strain_links.tsv:10198` and the live
  [SI-ID 404088 record](https://api.straininfo.dsmz.de/v2/data/strain/max/404088)
  agree on DOI `10.60712/SI-ID404088.3`, BacDive 130633 and published
  status. DSM 29339 is the available own deposit SI-DP 911201, with
  nondeprecated collection, nonerroneous relation and NCBI 1031541.
  GCA_900188335 is explicitly linked to that deposit, with genome type,
  contig level and matching description. M97, JCM and KACC group
  designations are not invented additional SI-DP objects.
- **ATB metadata:** The whole sample SAMN05421757 matches native
  `data/catalog/allthebacteria.tsv.xz:1172714` and all 17 columns of
  `data/atb/assemblies.tsv:4589`. Release 2025-05, dataset 661k, run
  SRR4235391, ERZ26866015, SeqKit sum, PASS flags, available-FASTA flag,
  supplied S3 URL and OSF archive metadata all agree. The snapshot-scoped
  identifier `atb.assembly:202505.SAMN05421757` is correctly separate
  from BioSample, NCBI assembly and ENA analysis identifiers.
- **ATB provenance:** `data/atb/strain_links.tsv:536` preserves exactly
  the seven YAML BioSample assertions: two BV-BRC, two GOLD, one GTDB
  and two NCBI. Genome-link rows 2329-2333 preserve respectively one
  GTDB, two IMG, six GCA, two GCF and two PATRIC evidence pairs. Every
  genome and sample assertion exists in the target, retains its exact
  culture match and follows its own source identifier or GOLD organism/
  project chain. All five relationships are `shares_biosample`; none
  asserts sequence equivalence. The full exclusions table has no row
  for this sample.
- **ENA authority:** The public
  [ERZ26866015 analysis XML](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26866015)
  confirms sample SAMN05421757/SRS1686651 and run SRR4235391. ENA run
  metadata independently confirms the sample, species, taxon and
  PRJNA329778. The ATB reassembly study PRJEB89175 is separate context,
  not a replacement for the original sequencing projects. ENA's file
  MD5 and ATB's SeqKit sum are different digest types; no equality was
  inferred or sequence file downloaded.
- **Publications and marker:** Crossref verifies the original
  [species-description DOI](https://doi.org/10.1099/ijs.0.037929-0),
  2012 volume 62 pages 2424-2429, and the
  [notification-list DOI](https://doi.org/10.1099/ijs.0.049288-0),
  2013 volume 63 pages 6-7. The complete inspected
  [PMID 22140172 abstract](https://pubmed.ncbi.nlm.nih.gov/22140172/)
  establishes M97 as the proposed species' type strain and explicitly
  equates KACC 15544 with JCM 17731. Nuccore EFetch confirms
  [JF748735.1](https://www.ncbi.nlm.nih.gov/nuccore/JF748735.1), a
  1,390-base partial 16S rRNA sequence from M97, type material of taxon
  1031541. It is not a genome assembly. Full articles and detailed
  emendation content were not reviewed; the emendation attribution is
  supported by LPSN, not incorrectly assigned to the original article.
- **Attestations:** Complete raw-table reads support NCBI NAME 1,
  LPSN NAME 1, GTDB GENOME 1, BacDive STRAIN 1, GOLD ORGANISM 3,
  MediaDive MEDIUM 2, Madin TRAIT_ASSERTION 16 and BactoTraits
  TRAIT_ASSERTION 26. Relevant aggregate rows are GOLD 404, MediaDive
  89, Madin 580 and BactoTraits 64. These are inventory counts, not
  interchangeable units or claims that every strain has every trait.

## Completeness

The one listed BacDive strain equals `strain_count: 1`; it is not capped.
All supported culture-deposit and genome/sample assertions in the checked
inventories are represented. NCBI type-material rows 1541-1548 and culture
mapping rows 75879, 103252 and 113322 corroborate all three collection
identifiers. Complete merged-ID and dropped-record inventories have no
target row.

Ignored/hidden-inclusive compressed searches covered all `data/catalog/`,
`data/bacdive/`, `data/bvbrc/` and `data/gold/` files using the taxon,
species label, culture identifiers and sample; GOLD chain identifiers
were checked as well. Actual field values were inspected after matching.
Substring collisions in unrelated accession numbers or SeqKit hashes
were rejected. The ATB full catalog has one relevant species/sample row;
it is present, not an inferred association from a species name. These
searches establish completeness within the local snapshots, not an
exhaustive census of future or unqueried public records.

The native BacDive projection has no culture-medium section and its raw
strain row reports zero linked media, so the optional strain-level
`medium_count` is omitted. MediaDive independently counts two associations,
514 and J118. The live BacDive page's DSM medium 514 association does not
make these differently scoped snapshot fields contradictory. No medium
recipe, physiological trait or causal graph is required by this record.

The structured iModulonDB `datasets` adapter returned 28 keys and none for
Tropicimonas. No matching organism/dataset was available; this is not
negative biological evidence. No expression-module context was transferred
from another taxon.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**N1 - Minor: incomplete LPSN type-strain designation list.** The
`nomenclature[0].type_strain_designations` list at record lines 48-50
contains DSM 29339 and JCM 17731 but omits `kgmicrobe.strain:KACC-15544`.
The inspected [LPSN entry](https://lpsn.dsmz.de/species/tropicimonas-sediminicola)
and original-paper abstract explicitly support that collection deposit.
The same omission is already present in `data/raw/lpsn_names.tsv:27170`;
the BacDive strain's collection list correctly includes it. This is a
nonblocking nomenclatural completeness gap, not a wrong taxon or false
type-strain flag.

Maintained owner: the upstream LPSN culture-designation transform supplying
`data/transformed/lpsn/edges.tsv`, consumed by
`src/taxonmech/extract.py:420`, then the inventory handoff above and
`src/taxonmech/seed.py:405`. The seeder copies the supplied designations;
do not patch the generated YAML. An ignored-inclusive file inventory of
the configured older kg-microbe checkout found no LPSN transform/data
files, so the exact upstream loss point was not inspected locally.

## Recommended Edits

1. Correct or refresh the maintained upstream LPSN type-deposit evidence
   for name 790190 to retain `kgmicrobe.strain:KACC-15544`, preserving
   DSM and JCM. Locate the active upstream checkout before choosing the
   transform implementation to edit; do not synthesize a collection ID
   from bare M97 or alter the already-correct BacDive deposit list.
2. In a later authorized curation change, run `just extract-inventory-dry`,
   inspect the target row, and publish the intended inventory refresh.
   Follow the documented dependent ATB and StrainInfo refresh checks,
   then use `just seed-canary NCBITaxon:1031541` before any bulk seed.
   No such curation or regeneration was performed during this review.

## Follow-up Checks

- Confirm the three authority-backed collection designations survive
  upstream extraction and target regeneration; retain the source's
  identity, current-name status and type-strain evidence.
- Repeat both exact target validation commands listed above. Recheck
  the 10/8/26 assertion totals, all three StrainInfo evidence objects
  and seven ATB sample chains to detect collateral provenance changes.
- Run full `just verify-corpus` and `just qc` after authorized publication
  of regenerated products; neither has been represented here as a
  completed target-only gate.

## Additional Notes

Live NCBI Datasets exposes PRJEB21423 in the assembly-info block for both
GCA and GCF. The pinned RefSeq assembly summary and GTDB row retain
PRJNA224116, while BioSample and the GOLD project retain PRJNA329778.
This source/API distinction is preserved, not treated as three competing
identities or grounds for rewriting the source-specific assertions.

The record's authority combines the original description and later
emendation, while its publication list contains the original description
and notification references. The list is not claimed to be an exhaustive
emendation bibliography; no additional unsupported publication finding
is assigned.

This review did not modify any prior report, taxon record, source inventory,
history entry, generated page, branch or worktree. The parallel session
was reported closed, and the existing single worktree remained in use.
Eukaryota reviews were left untouched. The corpus-wide review goal remains
in progress.
