# YAML Record Review: Wolbachia endosymbiont of Tachinidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_tachinidae_sp.yaml`
- Started UTC: 2026-10-09T17:27:31Z
- Finished UTC: 2026-10-09T17:29:15Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036851` was read: Wolbachia endosymbiont of Tachinidae sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It contains one exact synonym, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `f0e0159c4ce110da3217601e196856d5d90acc356144759f3a4d2254ead3d92f`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_tachinidae_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_tachinidae_sp.yaml --workers 1 --out /private/tmp/taxonmech-tachinidae-sp-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Own-row comparisons passed for identity, every ancestor, source attestation, PATHS/scope entries and event wording. The synonym was checked against its native name class, live authority and repository mapping. All four local source candidates were read completely.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. The nucleotide hit's complete metadata, source qualifiers, annotations and references were read, with length/alphabet checks. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. No experimental paper is cited by the YAML.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222645` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32243` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. The shorter form Wolbachia endosymbiont of Tachinidae is explicitly classed as `synonym` at native row 32244 and appears in the backbone's exact-synonym field.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036851&retmode=xml) also lists the shorter form under `OtherNames/Synonym`. Its `EXACT_SYNONYM` placement agrees with `src/taxonmech/ncbi_taxdump.py`, which maps native synonym/equivalent-name classes to exact synonyms and other name classes to related synonyms. It is not a broader host-group equivalence inferred from spelling.

EFetch and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036851) support the identity. All eleven root-first lineage entries match the local backbone. EFetch supplies the ten named ancestors after root; Datasets also supplies root 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Ancestor ranks agree with the YAML.

The record denotes this bacterial ID, not the Tachinidae host grouping or every associated endosymbiont. Its species rank is the bacterial concept's NCBI rank and is not inferred from the host name.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the own inventory. One `NAME` assertion does not count all aliases, specimens, sequences or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036851%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF960254.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960254.1). It explicitly carries the own organism and `taxon:1036851`, voucher `BIOUG<CAN>:ASPN525-08.w` and BOLD cross-reference `ASEND070-09.COI-5P`.

The entry annotates partial COI gene/CDS, translation table 11, `codon_start: 1` and protein AEG78092.1. Declared/actual nucleotide length is 574 bases and the alphabet is A/C/G/T. Source qualifiers give Ohu, Madang, Papua New Guinea, 20-Oct-2004, collectors Novotny et al. and identifier Alex Smith. These are source-specific marker/specimen annotations, not culture-deposit or assembly evidence.

GenBank retains an unpublished Smith study reference and a 01-May-2011 direct submission. BOLD and publication-level specimen mappings were not independently resolved. No taxon-wide prevalence, reproductive phenotype, supergroup assignment or experimentally established full-length protein function is inferred from this marker.

The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036851/dataset_report) returned an empty object. It supplies no positive assembly evidence rather than proving universal genome absence. The specimen voucher does not establish an eligible own culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete shorter synonym/label/slug prefix. All four candidates were read in full: two native name JSON rows and two backbone/scope TSV rows.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF960254, ASPN525-08 and ASEND070-09 found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The supported exact synonym is present. No inspected source establishes an eligible own culture-to-genome link. Optional additional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and graphs are appropriately empty for the seeded claims.

`data/taxa/PATHS.tsv:15177` agrees with the filename. `curation/seed_scope.tsv:322878` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The exact synonym is source-backed; unperformed BOLD/publication checks do not leave an asserted YAML claim unsupported.

## Recommended Edits

None required. Preserve the source-backed synonym without broadening the record to all endosymbionts of the host grouping. Keep specimen, culture-deposit, strain and genome identities distinct.

Any later authorized correction belongs in maintained upstream extraction inputs, the name-class mapping in `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Future name refreshes should retain native name classes and exact taxon IDs. Experimental enrichment needs independently inspected publication/specimen mappings; genome additions require explicit eligible culture-deposit chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. No host or Eukaryota record was reviewed. No paid research was performed.
