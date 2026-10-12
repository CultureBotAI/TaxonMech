# YAML Record Review: Leptospira sp. EP

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_ep.yaml`
- Started UTC: 2026-10-04T00:27:33Z
- Finished UTC: 2026-10-04T00:30:16Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103239,
Leptospira sp. EP. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
one NCBI name attestation, zero inventoried BacDive strains and one seed
event. No genome, phenotype, nomenclature, taxonomy mapping or graph
assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_ep.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_ep.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18363`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103239&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103239)
agree on exact label, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. The taxonomy browser
failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38381` supplies
the scientific name. `data/taxa/PATHS.tsv:13229` and
`curation/seed_scope.tsv:144023` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope, not a formal species name, type-culture designation,
serovar or equivalence to another EP-labeled isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103239[Organism:noexp]` returned one record.
  Inspected [AB031514.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031514.1)
  is a 746-base partial `flaB` coding sequence for flagellin. Its source
  qualifiers explicitly identify strain EP and taxon103239. This is not
  a 16S record or whole-genome assembly. No clinical, geographic or
  serovar assertion follows from the submitter's institutional address.
- Its references name Kawabata, Dancel, Yanagihara and Watanabe, with a
  database-only publication in 2000 and an August 25, 1999 direct
  submission. Inspected reference metadata supply no DOI or PMID;
  none was invented or borrowed from other Leptospira records.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- `CIP 103239` belongs to Serratia plymuthica, species taxon82996,
  strain taxon1218095, BacDive5151, SI-ID10390 and SI-DP154981.
  Its partial `gyrB` sequence AJ300532 explicitly names SI-DP154981
  and ATCC183/40717. SI genome GCA_900478125 instead explicitly
  names NCTC12961 / SI-DP332562, and GCA_001590925 names
  NBRC102599 / SI-DP764559. These unversioned SI accessions and the
  source's type-material rows supply no Leptospira evidence; group
  membership alone does not transfer genomes between deposits.
- `DSM 103239` belongs to Microbacterium hydrothermale, taxon857427,
  isolate 0704C9-2, BacDive132181, SI-ID387987 and SI-DP903108.
  Its BacDive record reports GCA_025960885, BV-BRC857427.7,
  IMG2721755905 and marker HM222660. SI's genome GCA_025960885
  explicitly names CGMCC1.12512 / SI-DP897652, not DSM's deposit.
  GOLD organism Go0620493 also identifies this Microbacterium.
  A related Go identifier is not itself a genome, and none of these
  records supports a join to Leptospira taxon103239.
- BacDive103239 itself describes Leucobacter sp. SF008556,
  taxon1898440. Its entry in `data/bacdive/SOURCE.json` records a
  BacDive fetch, not an NCBI taxon attestation. SI-DP103239 belongs
  to Escherichia coli ATCC23813, SI-ID38243, taxon562, alias AB3631;
  a deposit number is not NCBITaxon:103239.
- GenBank GCA_022160545.1 concerns Escherichia coli strain103239,
  taxon562, sample SAMN24019764 and project PRJNA514245.
  Neither its assembly, sample nor associated PMID30286803 transfers
  to EP through the numeric strain name.
- Three GTDB matches are assembly statistics: RS_GCF_001982405.1,
  Lactiplantibacillus plantarum RI-514, taxon1590, has contig and
  scaffold N50 value103239; RS_GCF_900596125.1, NCBI taxon28450,
  has scaffold N75 value103239; RS_GCF_949073265.1, uncultured
  Alistipes sp. MGBC105026, taxon538949, has scaffold N50 value103239.
  These metrics do not identify a taxon or culture deposit.
- The public structured iModulonDB catalog inspected during this review
  turn contains 28 keys, none for Leptospira. It was not applicable to
  this gene-context lead; lack of coverage is not negative biological
  evidence, and no unrelated expression module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The own partial gene and other
organisms' genomes do not establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and genus-qualified EP
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions,
curation and history. After identity-scoping the collisions, no own
native genome, type-material, culture-collection, merged-ID, dropped-row
or standalone history entry was found on these surfaces. Own raw and
maintained matches were backbone and scope rows. This bounded search is
not a reconciliation of every bare EP alias across organisms.

No own eligible deposit starts a StrainInfo join, and no carried BIOSAMPLE
assertion starts an ATB join. Sample/FASTA eligibility and sequence
equivalence were not audited; no global ATB absence is claimed. Empty
optional synonyms, nomenclature, mappings, definitions, evidence,
discussion and graphs remain appropriate for the NCBI-only assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by the inspected evidence.

## Recommended Edits

None required. Preserve generated YAML, exact isolate, NCBI lineage and
`SEEDED` status. Future taxonomy corrections belong upstream and in the
pinned inventory; extraction/seeding fixes belong in
`src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
`src/taxonmech/seed.py`, with tests. Optional sequence context requires
separately authorized maintained evidence, not a manual generated-YAML
edit or a join on a bare alias, culture suffix or another database's ID.

## Follow-up Checks

- At refresh, recheck the exact taxon and parent and any explicit merge
  evidence, preserving NCBITaxon:103239 versus DSM/CIP/BacDive103239.
- For authorized enrichment, retain AB031514.1 as partial `flaB`
  context outside genome counts and preserve exact strain scope.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103239, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

Native collision records were inspected at BacDive5041/27397/54491,
SI10390/26658/291779, GOLD organisms451128, GenBank0020:24079 and
GTDB0013:20290 / 0013:40228 / 0009:8890. These support exclusion
by ownership, not a review or reclassification of those taxa. The
GTDB/NCBI naming difference in GCF_900596125.1 was not reconciled;
both source classifications are outside the target identity.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
