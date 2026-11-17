# YAML Record Review: Wolbachia endosymbiont of Agathidinae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_agathidinae_sp.yaml`
- Started UTC: 2026-10-09T17:10:45Z
- Finished UTC: 2026-10-09T17:13:03Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036847` was read: Wolbachia endosymbiont of Agathidinae sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It has one exact synonym, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `e0ff9151707b828cc52fcf930267872146a0f9e3e43b5db95b4115e38e5d55e7`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_agathidinae_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_agathidinae_sp.yaml --workers 1 --out /private/tmp/taxonmech-agathidinae-sp-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, every ancestor, attestation, PATHS/scope entries and generated event wording. The exact synonym was checked against the native name class, live authority and repository mapping. All seven local source candidates were read completely.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. The nucleotide hit's complete metadata, source qualifiers, annotations and references were read, with length/alphabet checks. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. No experimental paper is cited by the YAML.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222641` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32236` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. The shorter form Wolbachia endosymbiont of Agathidinae is explicitly classed as `synonym` at native row 32237 and appears in the backbone's exact-synonym field.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036847&retmode=xml) also lists the shorter form under `OtherNames/Synonym`. `src/taxonmech/ncbi_taxdump.py` maps native synonym/equivalent-name classes to `EXACT_SYNONYM`, preserving other name classes as related. The YAML's source-backed exact synonym is therefore not a broader host-group equivalence inferred from spelling.

EFetch and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036847) support the own identity. All eleven root-first lineage entries match the local backbone. EFetch supplies the ten named ancestors after root; Datasets also supplies root 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Ancestor ranks agree with the YAML.

The record denotes this bacterial ID, not the host grouping named in the label or every Wolbachia associated with that grouping. Its bacterial species rank is carried from NCBI, not derived from the host's name.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the inventory. One `NAME` assertion does not count all aliases, specimens, sequences or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036847%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF960241.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960241.1). It explicitly carries the own organism name and `taxon:1036847`, voucher `BIOUG<CAN>:ASPNE019-10.w` and BOLD cross-reference `ASEND152-10.COI-5P`.

The entry annotates partial COI gene/CDS, translation table 11, `codon_start: 1` and protein AEG78079.1. Declared/actual length is 595 bases, with N and R ambiguity. Source qualifiers specify Wanang, Madang, Papua New Guinea, 30-Jul-2007, collected by local collectors and identified by Alex Smith. These are source-specific marker/specimen annotations, not culture-deposit or genome-assembly evidence.

GenBank retains an unpublished Smith study reference and a 01-May-2011 direct submission. BOLD and publication-level specimen mappings were not independently resolved. The marker does not justify taxon-wide prevalence, reproductive phenotype, supergroup assignment or experimentally established full-length protein function.

Three local native genome candidates are unrelated numeric matches:

- `data/catalog/ncbi_genbank-0051.jsonl.gz:19537`: `GCA_055615555.1`, Streptococcus pneumoniae, taxon/species ID 1313; its isolate field alone is `1036847`.
- `data/catalog/ncbi_genbank-0061.jsonl.gz:13714`: `GCA_949287385.1`, uncultured bacterium, taxon/species ID 77133; genome and ungapped sizes are `1036847`.
- `data/catalog/gtdb_genomes-0001.jsonl.gz:10295`: the same `GB_GCA_949287385.1`, NCBI taxon 77133, GTDB Coprosoma sp944363935; total and ungapped lengths supply the numeric match, not taxon identity.

None supplies an own strain or genome link. The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036847/dataset_report) returned an empty object, which supplies no positive assembly evidence rather than proving universal genome absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded numeric ID and label/slug query was broadened to include the complete shorter synonym. All seven final candidates were read in full: five native JSON rows and two backbone/scope TSV rows.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF960241, ASPNE019-10 and ASEND152-10 found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source establishes an eligible own culture-to-genome link. The supported exact synonym is present; optional additional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and graphs are appropriately empty for the seeded claims.

`data/taxa/PATHS.tsv:15173` agrees with the filename. `curation/seed_scope.tsv:322874` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The shorter exact synonym is source-backed. All three genome candidates are excluded by explicit identity fields rather than joined through numeric coincidences.

## Recommended Edits

None required. Preserve the source-backed synonym without broadening the record to all endosymbionts of the host grouping. Keep specimen markers, culture deposits and genome identifiers distinct.

Any later authorized correction belongs in maintained upstream extraction inputs, the name-class mapping in `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. A later name refresh should retain native name classes and exact taxon IDs. Experimental enrichment needs independently inspected publication/specimen mappings; genome links require explicit eligible culture-deposit chains, not matching isolate numbers or assembly lengths. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for this target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Unrelated genome rows were disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
