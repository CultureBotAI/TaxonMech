# YAML Record Review: Leptospira sp. G

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_g.yaml`
- Started UTC: 2026-10-04T00:31:58Z
- Finished UTC: 2026-10-04T00:33:25Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103240,
Leptospira sp. G. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
code 11, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, mapping or causal
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_g.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_g.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18364`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103240&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103240)
agree on exact label, rank, parent NCBITaxon:2633828 and code 11.
The ten root-first lineage entries match, including Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. The taxonomy browser
failed; both structured reads succeeded. No source synonym or backbone
child was found in complete scans.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38382`,
`data/taxa/PATHS.tsv:13230` and `curation/seed_scope.tsv:144024` support
the scientific name, exact slug and seed reason. Species rank satisfies
scope; it does not establish formal nomenclature, type status, a serovar
or equivalence to other G-labeled isolates. G-h-* and G-r-* names are
different taxa, not aliases proved for this record.

## Evidence

- The attestation is one NCBI `NAME`, snapshot 2026-09-13. Its unit
  is not a genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103240[Organism:noexp]` returned one record.
  [AB031515.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031515.1) is a
  746-base partial `flaB` coding sequence for flagellin, explicitly
  strain G and taxon103240. It is neither 16S nor a whole genome.
  References name Kawabata, Dancel, Yanagihara and Watanabe, a 2000
  database-only publication and August 25, 1999 direct submission.
  Inspected metadata provide no DOI or PMID. Institutional address
  does not establish isolate geography, clinical status or serovar.
- Full raw inventory scans found no exact target row in BacDive, LPSN,
  GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all isolates.
- `CIP 103240` belongs to Budvicia aquatica, species taxon82979,
  strain taxon1111728, BacDive4310, SI-ID1364 / SI-DP5907. Native
  BacDive reports GCA_000427805, BV-BRC1111728.3 and IMG2513237113
  for DSM5075 = ATCC35567. SI explicitly assigns GCA_000427805 to
  those deposits, GCA_024343535 to JCM3902 / SI-DP5912 and
  GCA_900706715 to NCTC12282 / SI-DP342660, not CIP's deposit.
  Preserve the supplied unversioned accessions and deposit scope.
  LPSN7142/774260 and type-material matches also concern Budvicia,
  not Leptospira. Their source nomenclature is not reconciled here.
- `DSM 103240` belongs to Oenococcus alcoholitolerans, taxon931074,
  isolate UFRJ-M7.2.18, BacDive132204, SI-ID388573 / SI-DP54144.
  BacDive reports HQ009794, GCA_000769695, BV-BRC931074.3 and
  IMG2636415795. Its SI record supplies deposits but no sequence
  entry; do not attribute BacDive's genome evidence to SI. GOLD
  Go0620496 identifies the same Oenococcus and is not itself a genome.
- BacDive103240 is Leucobacter sp. SF008542, taxon1898440.
  BacDive's manifest match is a fetch ID/URL; StrainInfo's manifest
  match is a response byte count. Neither is a Leptospira attestation.
- GCA_021796875.1 is Klebsiella pneumoniae strain103240, taxon573,
  sample SAMN24297216. GCA_050885645.1 is Listeria monocytogenes
  FLAG-103240, taxon1639, sample SAMN44114579. These numeric
  matches supply no target assembly, sample or literature evidence.
- GTDB RS_GCF_008571925.1, Phocaeicola dorei BIOML-A15,
  taxon357276, matches scaffold N75 value103240. GB_GCA_002472645.1,
  Atopobium sp. UBA7261, taxon1946075; RS_GCF_900009415.1,
  Clostridioides difficile VL_0103, taxon1496; and GB_GCA_948660705.1,
  uncultured Lachnospiraceae bacterium MGBC158148, taxon297314,
  match contig N50 value103240. Statistics are not identity joins.
- Fresh `kg-microbe-sources imodulondb datasets` returned 28 keys,
  none for Leptospira. The adapter was not applicable to this gene
  context; absence is not negative biological evidence.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
proof of global genome absence. The own partial gene is optional context,
not a missing genome. No own eligible deposit or carried BIOSAMPLE starts
a StrainInfo/ATB join. ATB FASTA eligibility and sequence equivalence were
not audited; no global ATB absence is claimed.

Ignored-inclusive searches covered identifier, exact label and slug in
raw inventories, catalog shards, BacDive, BV-BRC, GOLD, SeqCode,
StrainInfo, ATB strain/genome links and exclusions, curation and history.
After resolving collisions, no own native genome, culture/type-material,
merged-ID, dropped-row or standalone history entry was found there.
The initial broad G search produced truncated output; a terminal-label
search was rerun to completion and SOURCE.json matches were inspected
with a JSON parser. This is not reconciliation of all bare G aliases.
Optional synonyms, nomenclature, mappings, evidence, definitions,
discussion and graphs are appropriately empty for current assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by inspected evidence.

## Recommended Edits

None required. Preserve generated YAML, exact identity, NCBI lineage and
`SEEDED` status. Future taxonomy fixes belong upstream and in the pinned
inventory; extraction/seeding changes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`, with tests. Optional gene context needs authorized
maintained evidence, not a hand edit or a bare-alias/genus/numeric join.

## Follow-up Checks

- Recheck exact taxon, parent and merge evidence at refresh, preserving
  NCBITaxon:103240 versus CIP/DSM/BacDive103240 and G-h-*/G-r-* taxa.
- Retain AB031515.1 as partial `flaB` context outside genome counts
  if sequence enrichment is authorized.
- After authorized changes, run extraction/seed dry runs, the exact
  taxon canary, both focused validators, `just verify-corpus` and
  `just qc` before publication.

## Additional Notes

Native collision locations: BacDive4205/27398/54514,
SI1364/291860, GOLD organisms451131, GenBank0020:6097 / 0046:49232,
GTDB0012:30880 / 0008:31207 / 0006:42868 / 0010:27134.
These establish exclusion by source ownership, not reviews of those taxa.

Local absence checks included ignored files through complete structured
scans or `rg --no-ignore --hidden -z`. Only free public reads were used.
No YAML, source, history, GitHub or status mutation occurred. Older
reports and completed Eukaryota coverage were untouched.
