# YAML Record Review: Leptospira sp. MC

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_mc.yaml`
- Started UTC: 2026-10-04T00:34:19Z
- Finished UTC: 2026-10-04T00:35:33Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103241,
Leptospira sp. MC. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
code 11, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, mapping or causal
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_mc.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_mc.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18365`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103241&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103241)
agree on exact label, rank, parent NCBITaxon:2633828 and code 11.
The ten root-first lineage entries match, including Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. A web-tool browser
response marked as crawled 1.2 years ago instead displayed Spirochaetia.
A direct live read of the same
[NCBI page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103241)
showed Leptospiria, agreeing with both live endpoints and the pinned
backbone. The cached difference is not evidence for editing this record.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38383`,
`data/taxa/PATHS.tsv:13231` and `curation/seed_scope.tsv:144025` support
the scientific name, exact slug and seed reason. Complete backbone scans
found no target synonym or child. Species rank satisfies scope, not
formal nomenclature, type status, serovar or equivalence to other MC
isolates. The seed event matches its maintained scope reason exactly.

## Evidence

- The attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103241[Organism:noexp]` returned one record.
  [AB031516.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031516.1) is a
  746-base partial `flaB` coding sequence for flagellin, explicitly
  strain MC and taxon103241. It is neither 16S nor a whole genome.
  References name Kawabata, Dancel, Yanagihara and Watanabe, a 2000
  database-only publication and August 25, 1999 direct submission.
  Inspected metadata provide no DOI or PMID. Institutional address
  does not establish isolate geography, clinical status or serovar.
- Full raw inventory scans found no exact target row in BacDive, LPSN,
  GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all isolates.
- `CIP 103241` belongs to Cedecea neteri, species taxon158822,
  strain taxon1216978, BacDive4322, SI-ID1710 / SI-DP149717.
  SI's GCA_001571265 explicitly names ATCC33855 / SI-DP6939;
  GCA_900461005 names NCTC12120 / SI-DP6946. Their native BacDive
  genome descriptions and LPSN/type-material rows concern Cedecea,
  not MC. Source grouping does not assign genomes to CIP's deposit;
  preserve SI's unversioned accessions.
- `NBRC 103241` belongs to Alkalibacterium thalassium, taxon426701,
  isolate T117-1-2, BacDive2244. SI-ID407577 lists the NBRC string
  as a designation, not an own deposit: its GCA_900101165 explicitly
  names DSM19181 / SI-DP914964. BacDive reports that genome,
  BV-BRC426701.4, IMG2619619006 and markers AB681985/AB294165.
  GOLD Go0599497 and LPSN/type-material rows are also Alkalibacterium
  evidence. A Go ID is not a genome; the common number proves no join.
- `DSM 103241`, BacDive131660 and SI-ID396404 / SI-DP53257 concern
  Brevibacterium isolate NM2E3, not Leptospira. BacDive identifies
  B. metallicum, taxon1578756, with marker KM874400; SI's strain and
  DSM deposit retain genus Brevibacterium, taxon1696, while its
  HAMBI3627 deposit names B. metallicus, taxon1578756. Preserve that
  source-scope/name difference rather than silently harmonizing it.
  SI provides no sequence entry. It is not a discrepancy in MC.
- BacDive103241 itself is Leucobacter sp. SF006457, taxon1898440.
  Its manifest match is a fetch ID/URL, not an NCBI taxon attestation.
  SI-DP103241 belongs to Escherichia coli ATCC23814, SI-ID38244,
  taxon562, alias AB3632. Deposit and taxon namespaces are distinct.
- GCA_022100275.1 is Klebsiella pneumoniae strain103241, taxon573,
  sample SAMN24019657. No target assembly, sample or PMID30286803
  follows from this numeric strain name.
- GTDB GB_GCA_050015075.1, Candidatus Brocadiia bacterium
  SPRUCE14, taxon2517210; GB_GCA_902789625.1, uncultured
  Spirochaetaceae bacterium RUG13487, taxon201186; and
  GB_GCA_034100685.1, Bacilli bacterium SUG2409, taxon1903720,
  match contig N50 value103241. These are statistics, not taxon IDs,
  and even shared phylum membership does not establish isolate identity.
- The public structured iModulonDB catalog inspected during this review
  turn contains 28 keys, none for Leptospira. It was not applicable
  to this gene context; absence is not negative biological evidence.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
proof of global genome absence. The own partial gene is optional context,
not a missing genome. No own eligible deposit or carried BIOSAMPLE starts
a StrainInfo/ATB join. ATB FASTA eligibility and sequence equivalence were
not audited; no global ATB absence is claimed.

Ignored-inclusive identifier, label, slug and genus-qualified MC searches
covered raw inventories, catalog shards, BacDive, BV-BRC, GOLD, SeqCode,
StrainInfo, ATB strain/genome links and exclusions, curation and history.
SOURCE.json files were searched with a complete JSON traversal. After
resolving collisions, no own native genome, culture/type-material,
merged-ID, dropped-row or standalone history entry was found there.
This is not reconciliation of all bare MC aliases. Optional synonyms,
nomenclature, mappings, evidence, definitions, discussion and graphs are
appropriately empty for current assertions.

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

- Recheck exact taxon, parent and merge evidence at refresh; do not
  substitute a cached class name or another namespace's number.
- Retain AB031516.1 as partial `flaB` context outside genome counts
  if sequence enrichment is authorized.
- After authorized changes, run extraction/seed dry runs, the exact
  taxon canary, both focused validators, `just verify-corpus` and
  `just qc` before publication.

## Additional Notes

Native collision locations: BacDive2156/4217/27399/53970,
SI1710/26659/294293/305466, GOLD organisms430530, GenBank0020:21090,
GTDB0004:33829 / 0011:46874 / 0011:47013. These establish exclusion
by source ownership, not reviews or reclassifications of those taxa.

Local absence checks included ignored files through complete structured
scans or `rg --no-ignore --hidden -z`. Only free public reads were used.
No YAML, source, history, GitHub or status mutation occurred. Older
reports and completed Eukaryota coverage were untouched.
