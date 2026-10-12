# YAML Record Review: Novipirellula rosea

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/novipirellula_rosea.yaml`
- Started UTC: 2026-10-03T20:40:48Z
- Finished UTC: 2026-10-03T20:43:53Z
- Verdict: pass with minor issues

## Target

Reviewed all 566 lines of this generated `TaxonRecord`: `NCBITaxon:1031540`,
Novipirellula rosea, rank `SPECIES`, domain `BACTERIA`, grounding `EXACT`,
mapping status `SEEDED`. One BacDive strain carries nine assembly
assertions, five genome-record assertions and 26 related-record assertions.
These are source assertions, not distinct biological genome counts.

Future corrections belong in maintained source inputs and transforms,
not generated YAML. This read-only review creates its individual report
and the standard validator diagnostic, without curation or history changes.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/novipirellula_rosea.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/novipirellula_rosea.yaml` | Passed; one file, zero ERROR rows. Diagnostic: `reports/instance_validation_failures.tsv`. |
| Structured source comparisons | Exact backbone, ten-entry lineage, source names, counts and seed reason checked; full-field multiset equality for all 9/5/26 strain assertions against raw and StrainInfo inventories. |
| StrainInfo evidence | Both evidence objects verified against the native record, eligible DSM deposit, statuses, DOI and deposit-scoped optional taxonomy. See Additional Notes for a corrected review-helper assumption. |
| Embedded history | Strict validation passed; seed event preserves the source inventories and historical scope reason. |
| Standalone history | Not applicable: identifier, label and slug searches including ignored/hidden files found no target history under `history/`. |
| Causal graph and ontology-product gates | Not applicable: the complete YAML has no causal graph. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered-page freshness, exports and FASTA replay. Focused
checks do not substitute for these gates. No generator, history writer
or status promotion was run.

## Identity and Grounding

The identifier, label, species rank, parent `NCBITaxon:2795426`, genetic
code 11 and complete root-first lineage match
`data/raw/ncbitaxon_taxa.tsv:220745`. Live taxonomy EFetch and
[NCBI taxonomy metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1031540)
confirm the current identity and three source names. Native name rows
29913-29916 in `data/catalog/ncbi_names-0005.jsonl.gz` distinguish the two
NCBI synonyms from the historical includes-name. The complete backbone
scan finds no children. `data/taxa/PATHS.tsv:13072` and
`curation/seed_scope.tsv:26073` agree with the identifier and slug.

The inspected [LPSN current-name page](https://lpsn.dsmz.de/species/novipirellula-rosea),
refreshed directly after an older browser cache response, supports name
19023, the 2021 combination, valid publication, current-name status and
JF748734. The [basionym page](https://lpsn.dsmz.de/species/rhodopirellula-rosea)
confirms name 791939 and the homotypic relationship. Raw rows 3621 and
28727 in `data/raw/lpsn_names.tsv` agree with those identities. Retaining
the historical name as a conservative LPSN related synonym is not an
unsupported identity claim. The type-deposit list is incomplete; see N1.

The principal GTDB identity is supported by the LPSN link and the native
representative type genome. The second GTDB member is an environmental
assembly, not another JCM deposit association. Its alternative NCBI
classification is preserved below rather than used to rewrite this lineage.

## Evidence

- **BacDive strain:** `data/raw/bacdive_strains.tsv:52848`, native
  `data/bacdive/records.jsonl.gz:52847` and the inspected
  [BacDive page](https://bacdive.dsmz.de/strain/130534) support LHWP3,
  DSM 29889, JCM 17759, KACC 15560 and type-strain status. Native reference
  124043 supplies unversioned GCA_039541335 at scaffold level. Source
  accession versions are preserved, not silently harmonized.
- **Inventory fidelity:** Raw assembly rows 15449-15457, genome-record
  rows 12031-12035 and related-record rows 45711-45734 exactly match
  every raw-source assertion. The two additional StrainInfo rows at
  `data/straininfo/related_records.tsv.gz:25642` and the next row account
  for the complete related-record total.
- **BV-BRC:** Native `data/bvbrc/bvbrc-0000.jsonl.gz:3068` supplies
  genome 1031540.3, GCA_039541335.1, SAMD00645724 and PRJDB10510 through
  both explicit JCM strain and culture-collection fields. Both normalize
  to the same eligible deposit while retaining their distinct provenance.
- **GOLD:** Native organism rows 449444-449446 preserve KACC Go0618774,
  JCM Go0618775 and DSM Go0618776 separately. The full native project/
  analysis identifier search finds the JCM chain Go0618775 -> Gp0829362 ->
  Ga0674979 at `data/gold/projects.jsonl.gz:608764` and
  `data/gold/analyses.jsonl.gz:451166`. It supplies IMG 8129873741,
  GCA_039541335.1, SAMD00645724 and PRJDB10510. No project or analysis
  for the other three species-level GOLD organisms was found within those
  complete files. Historical Rhodopirellula source labels are retained.
- **NCBI genome:** Native
  `data/catalog/ncbi_genbank-0036.jsonl.gz:5286` and
  `ncbi_refseq-0006.jsonl.gz:3232`, corroborated by live
  [NCBI genome metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039541335.1/dataset_report),
  support the current GCA/GCF_039541335.1 pair, JCM 17759, type material,
  scaffold assembly ASM3954133v1 and BioSample. GenBank's PRJDB10510
  remains separate from RefSeq/GTDB PRJNA224116.
- **GTDB scope:** Raw mapping `data/raw/gtdb_mappings.tsv:1308` retains
  the source `skos:closeMatch` and cluster count two. Native
  `data/catalog/gtdb_genomes-0006.jsonl.gz:15993` identifies the JCM type
  genome as representative. The second exact-cluster member at
  `gtdb_genomes-0013.jsonl.gz:42526` is GB_GCA_963976545.1, an uncultured
  metagenome filed under NCBI taxon 666712, with isolate
  ERR2762116_binner12_Refined_17 and sample SAMEA115300705. The cluster
  count is supported; there is no basis for joining that member to JCM,
  KACC or DSM, and the YAML correctly does not do so.
- **StrainInfo:** Native `data/straininfo/records.jsonl.gz:302368`, overlay
  `data/straininfo/strain_links.tsv:9977` and the live
  [SI-ID 404479 record](https://api.straininfo.dsmz.de/v2/data/strain/max/404479)
  support DOI `10.60712/SI-ID404479.3`, BacDive 130534, published status
  and the available, nondeprecated, nonerroneous DSM deposit 911625.
  It is the sole own deposit. JCM 17759, KACC 15560 and LHWP3 are group
  designations, not additional SI-DP objects. Neither native nor live
  record provides a sequence or assembly to transfer.
- **Deposit taxonomy:** The SI strain group carries NCBI 1031540 and
  current LPSN 19023, but its DSM deposit carries only basionym LPSN
  791939 and no NCBI ID. `src/taxonmech/straininfo_links.py:190` deliberately
  uses the deposit's optional `taxon.ncbi`. The YAML's two SI assertions
  therefore correctly omit `taxon_id`; the group ID is not substituted.
- **Publications:** The full abstract of
  [PubMed 31853689](https://pubmed.ncbi.nlm.nih.gov/31853689/) and
  [Crossref metadata](https://api.crossref.org/works/10.1007/s10482-019-01374-5)
  verify the reclassification paper, DOI and placement of LHWP3 in the
  new genus. Its discussion of other strains and rpoB thresholds is not
  transferred into a phenotype or mechanism claim. The full original
  description abstract, [PubMed 23812809](https://pubmed.ncbi.nlm.nih.gov/23812809/),
  independently supports LHWP3 = KACC 15560 = JCM 17759. The cited
  [validation-list DOI](https://api.crossref.org/works/10.1099/ijsem.0.004688)
  resolves, but its Crossref date differs from LPSN's chronology; see
  Additional Notes. Full articles were not read.
- **Marker:** Inspected [JF748734.1](https://www.ncbi.nlm.nih.gov/nuccore/JF748734.1)
  metadata confirm a 1,459-base partial 16S sequence from LHWP3, taxon
  1031540, with explicit type material under the basionym. It remains
  an unversioned source accession under nomenclature, not a genome count
  or invented StrainInfo sequence assertion. No alignment was performed.
- **Attestations:** Complete inventory scans corroborate NCBI NAME 1,
  LPSN NAME 1, GTDB GENOME 2, BacDive STRAIN 1 and GOLD ORGANISM 4.
  Direct MediaDive, MADIN and BactoTraits target rows are absent from
  the inspected complete inventories. Counts alone imply no phenotype.
- **iModulonDB:** The resolved `culturebotai-claw/.venv/bin/kg-microbe-sources
  imodulondb datasets` adapter returned 28 keys, none covering Novipirellula
  or Rhodopirellula. No organism-matched marker query applies; this is not
  negative biological evidence.

## Completeness

The BacDive strain listing is complete for the local species subtree, not
capped. Ignored-inclusive compressed searches covered native catalog,
BacDive, BV-BRC, GOLD, SeqCode and StrainInfo data using current/historical
names, LHWP3 context, whole culture identifiers and typed current/retired
taxon IDs. Complete structured scans covered raw inventories, type material,
merged IDs and dropped rows. The merge row at
`data/raw/ncbi_merged_ids.tsv:23126` resolves old 1649552 to 1031540; it
does not supply another extant strain. No extra eligible own-deposit genome
association was identified in those boundaries.

GOLD Go0618773 at native organism row 449443 has only the bare designation
LHWP3. It contributes to the species organism count but not an eligible
deposit join. KACC and DSM organism links correctly stop at organism scope
because no corresponding project/analysis chain was found in the complete
native identifier search. The environmental GTDB member is likewise not
a missing cultured-strain genome.

Ignored-inclusive searches covered `data/atb/` and the complete compressed
`data/catalog/allthebacteria.tsv.xz` using current/historical names, slug,
all three culture IDs, both relevant samples and typed target identities.
No target ATB match was found in those sources. This is not a statement of
global genome absence. SeqCode name entries support name discovery only.

The raw BacDive inventory has medium count zero, so the optional count is
omitted. The live BacDive page displays a DSM medium association, but this
review does not reinterpret an upstream inventory count as a complete live
cultivation census or add a direct MediaDive attestation. Optional mechanism
and phenotype fields need not be invented for this identity record.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**N1 - Minor: the nomenclatural type-deposit list omits KACC 15560.** YAML
line 51 lists only JCM 17759. Both inspected LPSN pages, the original
description's full abstract and NCBI type-material rows 1537-1538 identify
KACC 15560 as another registered deposit of LHWP3. The deposit is already
correctly listed under the BacDive strain at YAML line 93 and in its
GOLD organism assertions. Identity, type status and existing genome links
remain supported.

Maintained owner: the LPSN source transform feeding
`data/raw/lpsn_names.tsv:3621` and basionym row 28727. Both raw rows omit
KACC. `src/taxonmech/extract.py:420` gathers transformed type-deposit edges,
and `src/taxonmech/seed.py:405` faithfully copies their inventory. Inspect
the upstream KGX edge set to locate the earlier loss point; those upstream
edges were not inspected in this review. Do not patch generated YAML or
invent a registered culture identifier for LHWP3.

## Recommended Edits

1. In a later curation change, retain KACC 15560 in the maintained LPSN
   type-deposit evidence/transform and re-extract. Trace the actual upstream
   edges before deciding whether the correction belongs in kg-microbe or
   TaxonMech extraction. Do not import DSM into LPSN nomenclature merely
   from BacDive/StrainInfo co-occurrence.
2. Add a focused extraction regression for multiple registered type
   deposits and a seeder regression confirming their retention without
   changing supported source links or the deposit-scoped missing SI taxon.
3. Regenerate only through the documented workflow after an authorized
   implementation and tests. No such edits or regeneration occurred here.

## Follow-up Checks

- Run focused extraction/seeding tests; inspect
  `just seed --only NCBITaxon:1031540`, then an authorized
  `just seed-canary NCBITaxon:1031540` and its diff.
- Rerun both target validators and full-field source comparisons. Confirm
  JCM and KACC appear in nomenclature while all 9/5/26 source assertions,
  accession versions and deposit provenance remain unchanged.
- Shared transform changes require full tests, corpus reproduction,
  provenance and generated-product checks in their own curation workflow.
- Recheck the live GTDB authority page when accessible; its browser request
  failed. The assessment here uses inspected pinned native members, not
  an unread live taxonomy page.
- Resolve the validation-list date discrepancy at the publication source
  before any proposed change to nomenclatural dates; do not overwrite the
  LPSN authority from aggregator metadata alone.

## Additional Notes

The ad hoc SI comparison initially expected every assertion to have the
group's NCBI taxon ID and stopped with a missing-key error. Inspection of
the native deposit and `straininfo_links.py` established the actual
deposit-scoped optional contract. The read-only helper was corrected in
memory and both evidence objects passed. No repository validator or source
code was altered, and the missing field is not a record defect.

Live SI's group-level type flag is false while the DSM deposit flag is
true. The record does not assert a group-level type flag; its local strain
type is supported independently by BacDive, nomenclature and the original
description. No type property is transferred solely through group membership.

Crossref reports a 2019 date for DOI 10.1099/ijsem.0.004688, while refreshed
LPSN identifies validation list 198 in 2021. The DOI/title and volume 71,
issue 3 resolve consistently. The record's 2021 combination is retained;
the full validation list was not inspected. The older browser-cached LPSN
page was not used to negate the directly refreshed current status.

The scope reason's four-source wording is historical text from
`curation/seed_scope.tsv`, not the current five-source attestation count.
No history entry is rewritten to erase that distinction. All absence
statements are bounded to named complete structured reads or
ignored-inclusive searches. One new report was created; the record, prior
reports, source code, curation status and history were not edited.
Eukaryota was left untouched.
