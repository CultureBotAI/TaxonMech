# YAML Record Review: Leptospira sp. UP-MMC

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_up_mmc.yaml`
- Started UTC: 2026-10-03T23:09:08Z
- Finished UTC: 2026-10-03T23:13:27Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:103233,
Leptospira sp. UP-MMC. Rank `SPECIES`, domain `BACTERIA`, grounding
`EXACT`, mapping status `SEEDED`, one NCBI name attestation, zero
inventoried BacDive strains and one seed event are carried. There are no
genome, phenotype, nomenclature, taxonomy-mapping or graph assertions.
No generated YAML, maintained source, history or status was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_up_mmc.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_up_mmc.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Inventory comparison | Identifier, label, rank, parent, code, empty synonyms, complete lineage, path, scope and attestation agree. |
| Embedded history | Strict validation and exact seed-event/scope comparison passed. |
| Standalone history | Ignored-inclusive identifier, label and slug searches found no target history entry. |
| Graph/product checks | Not applicable: no graph or curator-added product grounding is carried. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment or per-genome
ortholog verification. Focused source comparisons do not prove corpus
reproduction. No generator or history writer ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18357`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103233&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103233)
agree on the exact name, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. Preserve the current
NCBI class Leptospiria rather than substituting older embedded source
classifications or inferring a placement in Leptospira interrogans.

The native scientific-name row is
`data/catalog/ncbi_names-0000.jsonl.gz:38375`; no synonym is supplied.
`data/taxa/PATHS.tsv:13196` and `curation/seed_scope.tsv:144017` support
the exact path and seed reason. Species rank meets scope without proving
formal nomenclatural publication or a type culture. The taxonomy browser
was unavailable; both structured authority endpoints succeeded.

## Evidence

- The NCBI attestation matches the inventory: one `NAME`, snapshot
  2026-09-13. It is not a genome or phenotype count.
- Exact Nuccore query `txid103233[Organism:noexp]` returned one sequence.
  Inspected [AB031508.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031508.1)
  is a 746-base partial flaB coding sequence annotated as flagellin, with
  exact organism, strain UP-MMC and taxon103233. It is not a 16S marker,
  genome assembly, culture-deposit registration or experimentally verified
  functional claim in this review.
- Sequence references identify a database-only 2000 entry and an August
  25, 1999 direct submission, without DOI or PMID. These references do not
  establish the identity of later NIID derivatives.
- Complete structured scans found no exact target row in BacDive, LPSN,
  GTDB, GOLD, MediaDive, Madin or BactoTraits inventories and no backbone
  child. Zero `strain_count` counts inventoried BacDive records, not every
  isolate or external sequence.
- Native genome catalogs contain similarly named UP-MMC-NIID LP and HP
  records, but their taxon is NCBITaxon:214675, Leptospira interrogans
  serovar Manilae, under species NCBITaxon:173. Inspected live NCBI
  [LP metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001047635.1/dataset_report)
  and [HP metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001047655.1/dataset_report)
  confirm their distinct current complete assemblies, paired RefSeq
  accessions, samples and projects listed below.

| Variant | GenBank / RefSeq | BioSample | Submission BioProject |
| --- | --- | --- | --- |
| UP-MMC-NIID LP | GCA_001047635.1 / GCF_001047635.1 | SAMN03780437 | PRJNA287300 |
| UP-MMC-NIID HP | GCA_001047655.1 / GCF_001047655.1 | SAMN03780438 | PRJNA287301 |

The inspected 2015 primary paper, DOI
[10.1128/genomeA.00882-15](https://journals.asm.org/doi/10.1128/genomea.00882-15),
PMID 26272567 and PMC4536678, supports the two NIID variant genomes.
PubMed identifiers, abstract, full text and Table 1 were inspected.
LP has chromosome/plasmid accessions CP011931-CP011933; HP has
CP011934-CP011936. The full-text XML contains neither AB031508 nor 103233;
all five UP-MMC occurrences are qualified UP-MMC-NIID. It does not provide
an explicit accession or taxon bridge to this legacy record. Shared name
prefixes do not authorize a genome transfer or inferred taxonomy merge.

The resolved `kg-microbe-sources imodulondb datasets` runner returned 28
dataset keys, none for Leptospira. iModulonDB was not applicable to this
optional flaB annotation context; its lack of coverage is not negative
biological evidence, and no other organism's module was transferred.

## Completeness

No consequential missing representation was established for the exact
record. Exact Assembly query returned zero with phrases-not-found and
no-items warnings. This unsuccessful indexed match is not global proof
of genome absence. The NIID assemblies are concrete identity follow-up
leads, not confirmed missing genomes belonging to NCBITaxon:103233.

Ignored-inclusive identifier, label, slug and UP-MMC spelling searches
covered raw inventories, all catalog shards, BacDive, BV-BRC, GOLD,
SeqCode and StrainInfo. They also covered SI strain links, related records,
assemblies and exclusions, ATB strain/genome links and exclusions, curation
and history. After scoping numeric and near-name matches by complete
identity, no target-associated type-material, culture-collection,
merged-ID, dropped-row or standalone history entry was found on these
surfaces. This is a bounded inventory result, not proof against a future
source update or an uninspected identity publication.

No inventoried BacDive strain or eligible own deposit starts a SI join;
no carried BIOSAMPLE assertion starts an ATB join. The native ATB table
was searched for target strings, but sample/FASTA eligibility and sequence
equivalence were not audited. No global ATB absence follows. Empty optional
synonyms, nomenclature, mappings, general evidence, definitions,
discussions and graphs are appropriate for the supported assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. The exact legacy/NIID identity
relationship remains unresolved, but no inspected evidence establishes a
record defect or permits reclassification. No maintained-input fix is
required on the evidence inspected.

## Recommended Edits

None required. Preserve generated YAML, source lineage and `SEEDED`
status. Do not add the NIID variant assemblies on a shared strain-name
prefix or species inference. A later authorized identity correction must
be supported upstream in NCBI and the pinned source input; extraction
changes belong in `src/taxonmech/ncbi_taxdump.py`,
`src/taxonmech/extract.py` and the seeder, not a manual YAML patch.
Optional sequence or publication enrichment requires separately maintained
evidence at the exact strain and claim scope.

## Follow-up Checks

- Resolve whether a primary identity source explicitly connects
  AB031508.1/NCBITaxon:103233 to either NIID variant, preserving derivation
  and distinct sample/assembly identities. The inspected 2015 paper does
  not settle that bridge. A 2004 publisher lead was inaccessible (403);
  its search snippet was not accepted as evidence.
- At refresh, check exact NCBI identity and explicit merge/replacement
  records; do not infer a merge from shared UP-MMC text.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103233, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

Native NIID evidence was kept separate by variant. GenBank shard0000
rows36493/36494 and RefSeq shard0000 rows30832/30833 supply LP/HP
respectively. GTDB rows shard0004:40119 and shard0010:26036 retain the
respective assemblies, not representative genomes. RefSeq/GTDB project
PRJNA224116 is not substituted for the individual submission projects.
BV-BRC shard0013 rows3971/3972 carry complete-genome records 214675.5/.6;
rows3965/3966 carry plasmid-component records 214675.18/.19. These are
not four independent isolate identities.

GOLD LP follows Go0116299, Gp0120703, Ga0111342 and IMG2654587982;
HP follows Go0116298, Gp0120702, Ga0111278 and IMG2654587974. The analysis
rows use their explicit project chains; culture fields are empty. GOLD
Go/Gp/Ga references are not themselves genome identifiers and supply no
own culture-deposit bridge to this target.

Numeric exclusions included CIP103233, a Streptococcus infantarius
deposit associated with BacDive14832, LPSN784982/784984, GOLDGo0271161
and SI-ID9430/SI-DP37430. SI-DP103233 instead denotes E. coli ATCC23810
on SI-ID38240. Other matches include GCA_033091375.1 Pseudomonas
aeruginosa strain PSA-BAB-IMI-103233, GCA_022161065.1 E. coli strain
103233 and unrelated GTDB contig-N50 values of 103233. None is an
NCBITaxon:103233 strain, genome or attestation.

All absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. Full-text Europe PMC XML and the primary publisher
page were accessible despite the PMC browser challenge. No optional
context was inserted into the YAML, and no outbound message, GitHub
mutation, history event or status promotion occurred. Older reports and
completed Eukaryota coverage were untouched.
