# YAML Record Review: Leptospira sp. AB

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_ab.yaml`
- Started UTC: 2026-10-04T00:20:21Z
- Finished UTC: 2026-10-04T00:22:10Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103236,
Leptospira sp. AB. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
one NCBI name attestation, zero inventoried BacDive strains and one seed
event. No genome, phenotype, nomenclature, taxonomy mapping or graph
assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_ab.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_ab.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18360`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103236&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103236)
agree on exact label, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. The taxonomy browser
failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38378` supplies
the scientific name. `data/taxa/PATHS.tsv:13226` and
`curation/seed_scope.tsv:144020` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope, not a formal species name, type-culture designation,
serovar or equivalence to another AB-labeled isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103236[Organism:noexp]` returned one record.
  Inspected [AB031511.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031511.1)
  is a 746-base partial `flaB` coding sequence for flagellin. Its source
  qualifiers explicitly identify strain AB and taxon103236. This is not
  a 16S record or a whole-genome assembly. No clinical, geographic or
  serovar assertion follows from the submitter's institutional address.
- Its references name Kawabata, Dancel, Yanagihara and Watanabe, with a
  database-only publication in 2000 and an August 25, 1999 direct
  submission. Inspected reference metadata supply no DOI or PMID;
  none was invented or borrowed from other Leptospira records.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- `DSM 103236` belongs to Pedobacter psychrotolerans, taxon1843235,
  BacDive133008, SI-ID402370 and SI-DP909373. Its native/derived
  evidence includes GCA/GCF_004340665.1, BV-BRC1843235.3,
  IMG2802428854 and sample SAMN10864731. GOLD's Go0456387 /
  Gp0325689 / Ga0310516 chain concerns that same Pedobacter. SI's
  own genome accession is unversioned GCA_004340665; do not silently
  add a version or transfer any of these links to taxon103236.
- The ATB hit at `data/atb/strain_links.tsv:963` and five genome-link
  rows4245-4249 also belong to BacDive133008 and DSM103236. Structured
  parsing of the embedded evidence confirms taxon1843235 and sample
  SAMN10864731 throughout. The `shares_biosample` relationships neither
  imply assembly equivalence nor supply any Leptospira association.
- `CIP 103236` belongs to Serratia proteamaculans, taxon28151,
  BacDive5157, SI-ID92711 and SI-DP143773. Its sequence AJ300531,
  GOLD Go0275810 and other own-deposit sequences are not AB evidence.
  The SI genome GCA_008830365 explicitly names another deposit in
  that Serratia grouping, CCUG14510; grouping alone cannot transfer it.
- Other numeric strain matches concern GCA_033091515.1,
  Pseudomonas aeruginosa PSA-BAB-IMI-103236, taxon287, and
  GCA_022157425.1, Klebsiella pneumoniae strain103236, taxon573.
  Six further GTDB matches contain 103236 as an assembly statistic
  rather than a taxon or culture identifier; their owners are listed
  under Additional Notes. None supplies a target genome or mapping.
- The resolved `kg-microbe-sources imodulondb datasets` runner returned
  28 keys, none for Leptospira. It was not applicable to this gene-context
  lead; lack of coverage is not negative biological evidence, and no
  unrelated expression module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The own partial gene and unrelated
organisms' genomes do not establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and genus-qualified AB
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions,
curation and history. After identity-scoping the collisions, no own
native genome, type-material, culture-collection, merged-ID, dropped-row
or standalone history entry was found on these surfaces. Own raw and
maintained matches were backbone and scope rows. This bounded search is
not a reconciliation of every bare AB alias across all organisms.

No own eligible deposit starts a StrainInfo join, and no carried BIOSAMPLE
assertion starts an ATB join. The unrelated Pedobacter ATB links were
checked for ownership, not FASTA eligibility or sequence equivalence.
No global ATB absence is claimed. Empty optional synonyms, nomenclature,
mappings, definitions, evidence, discussion and graphs remain appropriate
for the present NCBI-only assertions.

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
edit or a join on a bare alias, culture-number suffix or assembly metric.

## Follow-up Checks

- At refresh, recheck the exact taxon and parent and any explicit merge
  evidence, preserving NCBITaxon:103236 versus DSM103236 and CIP103236.
- For authorized enrichment, retain AB031511.1 as partial `flaB`
  sequence context outside genome counts and preserve exact strain scope.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103236, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

The six GTDB assembly-statistic collisions were independently inspected:
GCF_042796375.1, Streptomyces virginiae taxon1961 (scaffold N90);
GCA_027418855.1, Sulfobacillus benefaciens taxon453960 (contig/scaffold
N50); GCF_033355815.1, Salmonella enterica taxon28901 (scaffold N75);
GCF_025146485.1, Dermabacter hominis taxon36740 (contig N50); and
GCF_900596135.1 / GCF_041028035.1, NCBI taxon28450 (scaffold N75
and contig N50, respectively). Their classifications are not reconciled
locally and none is treated as a Leptospira identifier.

An initially truncated terminal excerpt was followed by complete
structured reads of the affected ATB, raw related-record and SI-link
tables. Ownership and source chains were inspected rather than inferred
from the shared numeric string. Native SI records were read at
`data/straininfo/records.jsonl.gz:70153` and `:300259`.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
