# YAML Record Review: Pseudomonas sp. PG12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pg12.yaml`
- Started UTC: 2026-10-04T23:17:48Z
- Finished UTC: 2026-10-04T23:19:24Z
- Verdict: pass

## Target

Read the full generated `TaxonRecord`, `NCBITaxon:1033973`, Pseudomonas
sp. PG12: SPECIES, BACTERIA, parent `NCBITaxon:196821`, ten ancestors,
code 11, EXACT grounding, SEEDED status, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. No source, record,
code, status or history was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_pg12.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_pg12.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded backbone, complete lineage, mapped inventories, scope, filename and inline-event comparisons passed.
- Not run: full-corpus `just verify-corpus`, QC, tests or rendering. `--max-diffs` is not a focus option; bounded comparisons do not prove byte reproduction.
- Not applicable: `just validate-products`; no curator graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no target history artifact. Inline provenance was checked.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221402`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30742`,
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033973&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033973)
agree on identity, rank, domain, parent and code. All ten ancestor IDs
match: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas,
unclassified Pseudomonas. Expanded labels and ranks agree where supplied.
SPECIES and EXACT do not imply a formally resolved species name.

Complete exact-ID type-material, merged-ID and dropped-taxon scans found
no rows. The backbone has no synonyms; the native name is scientific only.
The distinct native name object for `NCBITaxon:1776275`, Pseudomonas sp.
PG12(2016), was also read. Its label is not an alias of this record.

## Evidence

The sole attestation matches the exact NCBI identifier, label, one NAME
assertion and September 13, 2026 snapshot. Complete directly mapped
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits scans found
no target rows. A complete backbone scan found no children, supporting
zero descendant-inclusive inventoried strains without denying the isolate.

Exact-taxonomy nuccore search returned one sequence. Full metadata,
references and feature qualifiers of
[JF345181.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF345181.1&rettype=gb&retmode=xml)
identify a 1498-base partial 16S marker, strain PG12, taxon 1033973,
and a February 17, 2011 University of Florida submission by Ghosh,
Rathinasabapathi and Ma. No registered deposit, BioSample or assembly
identifier is supplied. The marker is not a genome.

The linked [PubMed record 21840210](https://pubmed.ncbi.nlm.nih.gov/21840210/)
was inspected through full EFetch XML, including its abstract and identifier
list. Authors and DOI `10.1016/j.biortech.2011.07.064` match the sequence
reference. The study concerns arsenic-resistant rhizosphere bacteria and
Pteris vittata, but its abstract does not name PG12 or isolate-level results.
Full text and tables were not checked; no PMC identifier was supplied.
No quantitative phenotype or causal claim was transferred to the YAML.

Exact-taxonomy Assembly search returned zero with a phrasesnotfound
warning for `txid1033973[Organism:noexp]`. This bounded result does
not prove genome absence under other classifications.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. ID, slug and PG12 separator variants
returned 20 contexts, all inspected. Rejected near matches include
Polaribacter PG-12, Bacillus PG_12, Pseudomonas PG12(2016), Enterococcus
faecium PG12, and Bacillus velezensis PG12 assembly GCA/GCF_002835205.1.
SAMEA1033973 is Streptococcus pneumoniae; a Duodenibacillus assembly
matches only genome length 1033973. None establishes a target genome join.

A separate accession, PMID and DOI search in the same ignored-inclusive
roots returned zero matches. No eligible deposit or strain-genome
association was found within this scope. Optional nomenclature, mappings,
definition, evidence and graph slots are appropriately empty for this seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, lineage, source count,
empty strain inventory, status and inline provenance are supported.

## Recommended Edits

None. Preserve generated YAML and SEEDED status. Future supported
corrections belong in maintained inputs and, as appropriate,
`src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope changes
belong in `curation/seed_scope.tsv`. Do not join by PG12 alone.

## Follow-up Checks

Inspect the primary paper's isolate table before adding any PG12-specific
phenotype or deposit. Recheck exact taxon and marker on source refresh.
After authorized input changes, regenerate and run focused validators plus
full `just verify-corpus`. No unresolved blocker remains.

## Additional Notes

`data/taxa/PATHS.tsv:13858` pins the slug;
`curation/seed_scope.tsv:321729` supplies the September 13 scope date
and one-source reason. The event at `2026-09-13T17:54:04Z` agrees.
Ignored-inclusive filename and history-content searches found no prior
target report or history artifact. iModulonDB is not applicable: no gene,
regulator or expression module is asserted. No paid research, outside
contact, GitHub mutation, generator run or status promotion occurred.
