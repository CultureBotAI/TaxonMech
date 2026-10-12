# YAML Record Review: Wolbachia endosymbiont of Microgastrinae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_microgastrinae_sp.yaml`
- Started UTC: 2026-10-09T17:23:01Z
- Finished UTC: 2026-10-09T17:24:55Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036850` was read: Wolbachia endosymbiont of Microgastrinae sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It contains one exact synonym, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and no prior own report. Target SHA-256: `2960296292aac2e968cdee78fde713a5ad92d68d9c0a9c4de92e98c3ae1d3eba`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_microgastrinae_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_microgastrinae_sp.yaml --workers 1 --out /private/tmp/taxonmech-microgastrinae-sp-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, every ancestor, attestation fields, PATHS/scope entries and generated event wording. The synonym was checked against its native name class, live authority and repository mapping. All four local source candidates were read in full.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. Complete metadata, source qualifiers, annotations and references for all five nucleotide hits were read, with length/alphabet/hash checks. No alignment, phylogeny or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the YAML asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. No experimental paper is cited by the YAML.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222644` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32241` agree with the exact ID, label, species rank, parent, code and 2026-09-13 snapshot. The shorter form Wolbachia endosymbiont of Microgastrinae is explicitly classed as `synonym` at native row 32242 and appears in the backbone's exact-synonym field.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036850&retmode=xml) also lists the shorter form under `OtherNames/Synonym`. Its `EXACT_SYNONYM` placement agrees with `src/taxonmech/ncbi_taxdump.py`, which maps native synonym/equivalent-name classes to exact synonyms and other name classes to related synonyms. It is not an inferred equivalence to all endosymbionts of the named host grouping.

EFetch and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036850) support the identity. All eleven root-first lineage entries match the local backbone. EFetch supplies the ten named ancestors after root; Datasets also supplies root 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Ancestor ranks agree with the YAML.

This record denotes the bacterial ID, not the host grouping or every Wolbachia associated with it. Its species rank is the bacterial concept's NCBI rank, not an inference from the host name.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the own inventory. One `NAME` assertion does not count all aliases, specimens, sequences or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036850%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned five entries. All explicitly carry the own organism and `taxon:1036850`:

| Accession | BIOUG voucher suffix | BOLD cross-reference | Collection date | Nucleotide alphabet |
| --- | --- | --- | --- | --- |
| [JF960253.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960253.1) | `ASPNE038-10.w` | `ASEND157-10.COI-5P` | 27-Jul-2007 | A/C/G/N/T |
| [JF960252.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960252.1) | `ASPNE034-10.w` | `ASEND156-10.COI-5P` | 06-Aug-2007 | A/C/G/T |
| [JF960251.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960251.1) | `ASPNE031-10.w` | `ASEND155-10.COI-5P` | 06-Aug-2007 | A/C/G/N/T |
| [JF960250.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960250.1) | `ASPNE030-10.w` | `ASEND154-10.COI-5P` | 06-Aug-2007 | A/C/G/N/T |
| [JF960249.1](https://www.ncbi.nlm.nih.gov/nuccore/JF960249.1) | `ASPNE028-10.w` | `ASEND153-10.COI-5P` | 27-Jul-2007 | A/C/G/T |

Every entry annotates partial COI gene/CDS with `codon_start: 1`, translation table 11 and a BARCODE keyword. Declared/actual lengths are all 657 bases. Source qualifiers give Wanang, Madang, Papua New Guinea, local collectors and identifier Alex Smith. These are source-specific marker/specimen details, not culture-deposit or assembly evidence.

JF960252.1 and JF960249.1 have the same inspected nucleotide hash, `67d2f39634952c0a306c5fdee808b32fac1b9509677154750ea2f8f79520dde8`, but different vouchers and collection dates. Matching a partial marker does not establish identical specimens, cultures, strains or whole genomes; no deduplication or identity transfer follows.

All five retain an unpublished Smith study reference and a 01-May-2011 direct submission. BOLD and publication-level specimen mappings were not independently resolved. No taxon-wide prevalence, reproductive phenotype, supergroup assignment or experimentally established full-length protein function is inferred from these markers.

The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036850/dataset_report) returned an empty object. It supplies no positive assembly evidence rather than proving universal genome absence. None of the specimen vouchers establishes an eligible own culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID and complete shorter synonym/label/slug prefix. All four candidates were read completely: two native name JSON rows and two backbone/scope TSV rows.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF960249-JF960253 and all five listed voucher/BOLD stems found no local match in those roots. These negatives concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The supported exact synonym is present. Optional additional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and graphs are appropriately empty for the seeded claims.

`data/taxa/PATHS.tsv:15176` agrees with the filename. `curation/seed_scope.tsv:322877` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The exact synonym is source-backed; the five marker records do not establish five cultured strains or a genome linkage requirement.

## Recommended Edits

None required. Preserve the synonym's source-backed scope and retain separate voucher identities even when partial marker sequences match. Keep specimen, strain, culture-deposit and genome identities distinct.

Any later authorized correction belongs in maintained upstream extraction inputs, the name-class mapping in `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Future name refreshes should retain native name classes and exact taxon IDs. Experimental enrichment requires independently inspected publication/specimen mappings; genome additions require explicit eligible culture-deposit chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. No host or Eukaryota record was reviewed. No paid research was performed.
