# YAML Record Review: Leptospira sp. EA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/leptospira_sp_ea.yaml`
- Started UTC: 2026-10-04T00:25:36Z
- Finished UTC: 2026-10-04T00:26:28Z
- Verdict: pass

## Target

Read all 53 lines of generated `TaxonRecord` NCBITaxon:103238,
Leptospira sp. EA. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
one NCBI name attestation, zero inventoried BacDive strains and one seed
event. No genome, phenotype, nomenclature, taxonomy mapping or graph
assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/leptospira_sp_ea.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/leptospira_sp_ea.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
checks do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18362`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103238&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103238)
agree on exact label, species rank, parent NCBITaxon:2633828 and code 11.
All ten root-first lineage entries agree through Pseudomonadati,
Spirochaetota, Leptospiria, Leptospirales, Leptospiraceae, Leptospira and
unclassified Leptospira. Datasets includes root. The taxonomy browser
failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0000.jsonl.gz:38380` supplies
the scientific name. `data/taxa/PATHS.tsv:13228` and
`curation/seed_scope.tsv:144022` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope, not a formal species name, type-culture designation,
serovar or equivalence to another EA-labeled isolate.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid103238[Organism:noexp]` returned one record.
  Inspected [AB031513.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031513.1)
  is a 746-base partial `flaB` coding sequence for flagellin. Its source
  qualifiers explicitly identify strain EA and taxon103238. This is not
  a 16S record or whole-genome assembly. No clinical, geographic or
  serovar assertion follows from the submitter's institutional address.
- Its references name Kawabata, Dancel, Yanagihara and Watanabe, with a
  database-only publication in 2000 and an August 25, 1999 direct
  submission. Inspected reference metadata supply no DOI or PMID;
  none was invented or borrowed from other Leptospira records.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all biological isolates.
- `DSM 103238` belongs to Leucobacter zeae, taxon1257004,
  BacDive132288, SI-ID382176 and SI-DP910195. Native BacDive/BV-BRC
  evidence identifies CC-MF41, GCA_016758175.1, BV-BRC1257004.3,
  IMG2995726249 and sample SAMN09988953. GOLD organism records
  Go0620489 and Go0644672 and derived Gp0680618/Ga0580930 links
  also concern that Leucobacter identity, not NCBITaxon:103238.
  The inspected SI record lists its deposits without a sequence entry;
  do not attribute other sources' genome links to SI.
- `CIP 103238` belongs to Serratia liquefaciens, species taxon614,
  strain taxon1346614, BacDive5161, SI-ID264354 and SI-DP143688.
  Its source-owned partial sequences AJ300537 and AJ306725, GOLD
  Go0172464 and type-material evidence do not concern EA. The SI genome
  GCA_000422085 explicitly names ATCC27592 / SI-DP53744; grouping
  does not transfer that genome to a different deposit or organism.
- BacDive103238 itself describes Leucobacter sp. SF008654,
  taxon1898440. Its entry in `data/bacdive/SOURCE.json` records a
  BacDive fetch, not a source attestation for Leptospira taxon103238.
- Other numeric matches are GCA_033091415.1, Pseudomonas aeruginosa
  PSA-BAB-IMI-103238, taxon287; GTDB RS_GCF_005502555.1,
  Pseudomonas sp. D(2018), NCBI taxon2502238; and
  GB_GCA_902491615.1, uncultured Collinsella sp., NCBI taxon165190.
  The last two match contig N50 value103238, not a taxon or strain ID.
  Their classifications and assembly metrics supply no target genome.
- The public structured iModulonDB catalog inspected during this review
  turn contains 28 keys, none for Leptospira. It was not applicable to
  this gene-context lead; lack of coverage is not negative biological
  evidence, and no unrelated expression module was transferred.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The own partial gene and other
organisms' genomes do not establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and genus-qualified EA
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions,
curation and history. After identity-scoping the collisions, no own
native genome, type-material, culture-collection, merged-ID, dropped-row
or standalone history entry was found on these surfaces. Own raw and
maintained matches were backbone and scope rows. This bounded search is
not a reconciliation of every bare EA alias across organisms.

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
  evidence, preserving NCBITaxon:103238 versus DSM/CIP/BacDive103238.
- For authorized enrichment, retain AB031513.1 as partial `flaB`
  context outside genome counts and preserve exact strain scope.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:103238, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

Native collision records were inspected at BacDive5051/27396/54598,
SI206298/291384, BV-BRC0000:36340, GOLD organisms110732/451124/474361,
GenBank0030:40693 and GTDB0005:23423 / 0003:26277. These support
exclusion by ownership, not a review or reclassification of those taxa.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No YAML mutation, outbound message, GitHub mutation,
history event or status promotion occurred. Older reports and completed
Eukaryota coverage were untouched.
