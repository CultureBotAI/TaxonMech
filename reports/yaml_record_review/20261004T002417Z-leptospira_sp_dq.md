# YAML Record Review: Leptospira sp. DQ

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_dq.yaml`
- Started UTC: 2026-10-04T00:23:25Z
- Finished UTC: 2026-10-04T00:24:17Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103237,
Leptospira sp. DQ. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
one NCBI name attestation, zero inventoried BacDive strains and one seed
event. No genome, phenotype, nomenclature, taxonomy mapping or graph
assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_dq.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_dq.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18361`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103237&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103237)
agree on exact label, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. The taxonomy browser
failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38379` supplies
the scientific name. `data/taxa/PATHS.tsv:13227` and
`curation/seed_scope.tsv:144021` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope, not a formal species name, type-culture designation,
serovar or equivalence to another DQ-labeled isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103237[Organism:noexp]` returned one record.
  Inspected [AB031512.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031512.1)
  is a 746-base partial `flaB` coding sequence for flagellin. Its source
  qualifiers explicitly identify strain DQ and taxon103237. This is not
  a 16S record or whole-genome assembly. No clinical, geographic or
  serovar assertion follows from the submitter's institutional address.
- Its references name Kawabata, Dancel, Yanagihara and Watanabe, with a
  database-only publication in 2000 and an August 25, 1999 direct
  submission. Inspected reference metadata supply no DOI or PMID;
  none was invented or borrowed from other Leptospira records.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- `CIP 103237` belongs to the Serratia record represented by BacDive5158,
  SI-ID4959 and SI-DP621708. BacDive/SI carry Serratia quinivorans,
  taxon137545; GOLD Go0276061 instead carries S. proteamaculans,
  taxon28151. Preserve that source disagreement without resolving it
  locally; neither organism is Leptospira DQ. The SI genome
  GCA_900457075 explicitly names NCTC11544 / SI-DP154986, not the
  CIP deposit, and grouping cannot transfer it to another deposit or taxon.
- BacDive103237 itself is a separate database-record number: its native
  entry describes Leucobacter sp. SF006325, taxon1898440, not this
  NCBI taxon. The corresponding `data/bacdive/SOURCE.json` fetch
  entry is acquisition provenance, not a Leptospira source attestation.
- SI-DP103237 likewise is ATCC23812 in SI-ID38242, Escherichia coli
  taxon562. Its numeric deposit ID is not NCBITaxon:103237.
- Other numeric matches are GCA_033091435.1, Pseudomonas aeruginosa
  PSA-BAB-IMI-103237, taxon287; GCA_050885665.1, Listeria
  monocytogenes FLAG-103237, taxon1639; and GTDB
  RS_GCF_041399365.1, P. aeruginosa strain787256, taxon287, whose
  contig N50 is 103237. No strain-suffix or assembly-statistic match
  supplies a target genome, sample, publication or mapping.
- The public structured iModulonDB catalog inspected during this review
  turn contains 28 keys, none for Leptospira. It was not applicable to
  this gene-context lead; lack of coverage is not negative biological
  evidence, and no unrelated expression module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The own partial gene and other
organisms' genomes do not establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and genus-qualified DQ
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions,
curation and history. After identity-scoping the collisions, no own
native genome, type-material, culture-collection, merged-ID, dropped-row
or standalone history entry was found on these surfaces. Own raw and
maintained matches were backbone and scope rows. This bounded search is
not a reconciliation of every bare DQ alias across organisms.

No own eligible deposit starts a StrainInfo join, and no carried BIOSAMPLE
assertion starts an ATB join. Sample/FASTA eligibility and sequence
equivalence were not audited; no global ATB absence is claimed. Empty
optional synonyms, nomenclature, mappings, definitions, evidence,
discussion and graphs remain appropriate for the NCBI-only assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input correction is
required by the inspected evidence. The Serratia source disagreement
concerns another record and does not alter the DQ verdict.

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
  evidence, preserving the distinct NCBI, BacDive, SI-DP and CIP namespaces.
- For authorized enrichment, retain AB031512.1 as partial `flaB`
  context outside genome counts and preserve exact strain scope.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103237, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

Native identity collisions were inspected at BacDive5048/27395,
SI4959/26657, GOLD organisms214097, GenBank0030:40694,
GenBank0046:49233 and GTDB0005:12512. Their source-specific identities
were checked before any absence or completeness judgement.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
