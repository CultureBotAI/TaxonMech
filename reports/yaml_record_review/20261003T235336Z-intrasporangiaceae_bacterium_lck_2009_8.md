# YAML Record Review: Intrasporangiaceae bacterium LCK-2009.8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/intrasporangiaceae_bacterium_lck_2009_8.yaml`
- Started UTC: 2026-10-03T23:52:42Z
- Finished UTC: 2026-10-03T23:53:36Z
- Verdict: pass

## Target

Read all 51 lines of generated `TaxonRecord` NCBITaxon:1032347,
Intrasporangiaceae bacterium LCK-2009.8. It carries `SPECIES`, `BACTERIA`,
`EXACT`, `SEEDED`, one NCBI name attestation, zero inventoried BacDive
strains and one seed event. No genome, phenotype, nomenclature, taxonomy
mapping or graph assertion is present. No YAML, source, history or status
changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/intrasporangiaceae_bacterium_lck_2009_8.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/intrasporangiaceae_bacterium_lck_2009_8.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, synonyms, path, scope, attestation and seed reason agree. |
| History | Embedded event passed strict/source checks; ignored-inclusive searches found no target standalone history entry. |
| Graph/product checks | Not applicable; no graph or curator-added product grounding. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports or sequence alignment. Focused source
comparisons do not prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220850`, live NCBI
[taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032347&retmode=xml)
and [Datasets metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032347)
agree on exact label, species rank, parent NCBITaxon:234440 and code 11.
All nine root-first lineage entries agree through Bacillati, Actinomycetota,
Actinomycetes, Micrococcales, Intrasporangiaceae and unclassified
Intrasporangiaceae. Datasets includes root. No genus is supplied by the
source; preserving that unresolved placement is correct. This is a
species-ranked isolate taxon, not a record for the entire family.
Keep suffix 8 distinct from LCK-2009.18 and other similarly named isolates.

Native scientific-name row
`data/catalog/ncbi_names-0005.jsonl.gz:30132` supplies no synonym.
`data/taxa/PATHS.tsv:13215` and `curation/seed_scope.tsv:321231` support
the exact slug and seed reason. Species rank satisfies scope, not formal
nomenclatural publication or a type-culture claim. The taxonomy browser
was inaccessible; both structured authority reads succeeded.

## Evidence

- The sole attestation is one NCBI `NAME`, snapshot 2026-09-13, not a
  genome, phenotype or biological-isolate count.
- Exact Nuccore query `txid1032347[Organism:noexp]` returned one sequence.
  Inspected [JF742963.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742963.1)
  is a 1,424-base partial 16S sequence with exact organism, strain
  LCK-2009.8 and taxon1032347. Annotation records Icelandic rock collected
  in July 2009. Preserve the submitted partial status; length alone does
  not establish sequence completeness, genus placement, species
  delimitation, genome identity or a culture-collection registration.
- The marker references an unpublished Kelly/Cockell study and a March
  28, 2011 direct submission, without DOI or PMID. Its study title does
  not independently demonstrate a weathering mechanism or phenotype for
  this isolate; the YAML makes no such claim.
- Complete raw inventory scans found no exact target row in BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits and no backbone child.
  `strain_count: 0` counts inventoried BacDive records, not all isolates.
- iModulonDB was not applicable: no gene-function, regulator, pathway,
  trait or transcriptomics claim is present. Partial 16S context does not
  warrant another organism's expression-module evidence.

## Completeness

No consequential missing representation was established. Exact Assembly
query returned zero with phrases-not-found and no-items warnings, not
global proof of genome absence. The partial marker is optional context,
not a mandatory missing assembly or a reason to infer a genus.

Ignored-inclusive identifier, exact label, slug and isolate-spelling
searches covered raw inventories, all catalog shards, BacDive, BV-BRC,
GOLD, SeqCode, StrainInfo, ATB strain/genome links and exclusions, curation
and history. Matches were the exact backbone, scope and native NCBI
scientific-name rows. No target-associated assembly, type-material,
culture-collection, merged-ID, dropped-row or standalone history entry
was found within these complete inspected surfaces.

No inventoried BacDive strain or eligible own deposit starts a SI join;
no carried BIOSAMPLE assertion starts an ATB join. The native ATB catalog
was searched for target strings, but sample/FASTA eligibility and sequence
equivalence were not audited. No global ATB absence follows. Empty optional
synonyms, nomenclature, mappings, definitions, general evidence,
discussions and graphs are appropriate to the supported assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the focused review. No maintained-input fix is required.

## Recommended Edits

None required. Preserve generated YAML, unresolved genus, exact isolate,
lineage and `SEEDED` status. Future taxonomy fixes belong in the pinned
NCBI input, `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py`
and the seeder. Optional enrichment needs separately authorized maintained
evidence, not a manual YAML edit or inferred placement.

## Follow-up Checks

- At refresh, verify the exact taxon, suffix 8 and parent against explicit
  source identity or replacement evidence. Any genus placement must come
  from the authority, not local taxonomy reconciliation.
- For enrichment, establish own strain/deposit and assembly provenance;
  keep partial-marker annotations distinct from demonstrated phenotypes.
- After authorized changes, run extraction/seed dry runs, a canary for
  NCBITaxon:1032347, both focused validators, then `just verify-corpus`
  and `just qc` before publication.

## Additional Notes

All absence checks used complete structured scans or
`rg --no-ignore --hidden -z`, including ignored files. Only free public
sources were used. No optional context was inserted into the YAML, and no
outbound message, GitHub mutation, history event or status promotion
occurred. Older reports and completed Eukaryota coverage were untouched.
