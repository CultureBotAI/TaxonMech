# YAML Record Review: Micromonospora sp. GUI6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_gui6.yaml`
- Started UTC: 2026-10-04T00:05:57Z
- Finished UTC: 2026-10-04T00:06:51Z
- Verdict: pass

## Target

Read all 54 lines of generated `TaxonRecord` NCBITaxon:1032350,
Micromonospora sp. GUI6. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, one NCBI name attestation, zero inventoried BacDive strains and
one seed event. No genome, phenotype, nomenclature, taxonomy mapping or
graph assertion is present. No YAML, source, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/micromonospora_sp_gui6.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/micromonospora_sp_gui6.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, complete lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, sequence alignment or unpublished
manuscript text. Focused source checks do not prove corpus reproduction.
No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220853`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032350&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032350)
agree on exact label, species rank, parent NCBITaxon:2617518 and code 11.
All ten root-first lineage entries agree through Bacillati,
Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae,
Micromonospora and unclassified Micromonospora. Datasets includes root.
The taxonomy browser failed, but both structured authority reads worked.

Native name row `data/catalog/ncbi_names-0005.jsonl.gz:30135` supplies
the scientific name. `data/taxa/PATHS.tsv:13219` and
`curation/seed_scope.tsv:321234` support the exact slug and seed reason.
Complete backbone scans found no target synonym or child. Species rank
satisfies scope; it does not assert formal nomenclatural publication or
a type-strain designation.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032350[Organism:noexp]` returned one record.
  Inspected [FR856635.1](https://www.ncbi.nlm.nih.gov/nuccore/FR856635.1)
  is a 1,454-base partial 16S sequence explicitly naming strain GUI6
  and taxon1032350. Source qualifiers identify host nodules, Pisum
  sativum and Spain:Zamora. Preserve that narrow source context; it is
  neither a whole genome nor direct proof of nitrogen fixation by GUI6.
- The sequence references Carro and Trujillo's unpublished study of
  Micromonospora diversity associated with pea nodules and rhizosphere,
  plus Trujillo's May 4, 2011 INSDC submission. Inspected references
  supply no DOI or PMID. No later publication identity was assumed and
  no experimental claim was inferred from the reference title.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. `strain_count: 0`
  correctly counts inventoried BacDive records, not all isolates.
- Prefix search hits include Micromonospora sp. GUI61, taxon709877,
  and GUI63, carried as an includes-name of Micromonospora vinacea,
  taxon709878. Neither is GUI6. The latter's BacDive132608 record
  identifies DSM101695, CECT9019, GUI63, sequence FN658651 and genome
  GCA_015751785, with BV-BRC709878.3 and IMG2880495981. Those are
  other-isolate identifiers; no type-culture, nomenclature, genome or
  sequence link transfers from them to this record.
- The public structured iModulonDB catalog inspected during this review
  turn contains 28 dataset keys, none for Micromonospora. No applicable
  dataset was available for optional expression context. Absence from
  that catalog is not negative biological evidence.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The partial 16S sequence and GUI63's
genome do not establish a missing own-strain assembly.

Ignored-inclusive identifier, exact-label, slug and GUI6 spelling searches
covered raw inventories, all catalog shards, BacDive, BV-BRC, GOLD,
SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation and
history. After excluding the GUI61/GUI63 prefix collisions, no own native
genome, type-material, culture-collection, merged-ID, dropped-row or
standalone history entry was found on these surfaces. Own raw and
maintained matches were the backbone and scope rows.

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
`src/taxonmech/seed.py`, with tests. Optional host, literature or sequence
context requires separately authorized maintained evidence at exact
isolate scope, not a manual generated-YAML edit or a prefix-based join.

## Follow-up Checks

- At refresh, verify the exact taxon and parent, preserving GUI6 versus
  GUI61 and GUI63. Require explicit source identity for any reclassification.
- Before optional phenotype enrichment, inspect primary experimental
  evidence for GUI6; host nodules alone do not prove symbiotic function.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032350, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

The related-name collisions were inspected in backbone rows166361/166362,
native names0004:17823/17824 and `data/bacdive/records.jsonl.gz:54918`.
They are search leads for different records, not authority for changing
the exact GUI6 identity.

All local absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No optional context was inserted into YAML, and no
outbound message, GitHub mutation, history event or status promotion
occurred. Older reports and completed Eukaryota coverage were untouched.
