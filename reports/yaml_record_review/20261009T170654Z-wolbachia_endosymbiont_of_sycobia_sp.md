# YAML Record Review: Wolbachia endosymbiont of Sycobia sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_sycobia_sp.yaml`
- Started UTC: 2026-10-09T17:04:52Z
- Finished UTC: 2026-10-09T17:06:54Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036845` was read: Wolbachia endosymbiont of Sycobia sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It contains no synonyms, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename search resolved this record and two numbered Sycobia concepts, but no prior own report. Target SHA-256: `2d3b9b00cc9c7caccc75057767dde69076ccad84938c5ed3f9ffe685ae46f19c`. Other records were disambiguation context only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_sycobia_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_sycobia_sp.yaml --workers 1 --out /private/tmp/taxonmech-sycobia-sp-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Own-row comparisons passed for identity, every ancestor, source attestation, PATHS/scope entries and event wording. All ten local source candidates were read in full.
- Live NCBI taxonomy and exact-taxon nucleotide/genome responses were inspected. Complete metadata, source qualifiers, annotations and references for all three nucleotide hits were read; declared/actual lengths agree. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, schema/provenance/QC/tests and site drift. `just verify-corpus` has no record selector; focused row checks are not corpus reproduction.
- Not applicable: curator-added OAK graph and iModulonDB checks; the record asserts no graph, gene, regulator, pathway, trait or transcriptomic result.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. No experimental paper is cited in the YAML.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222639` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:32234` agree with the own ID, name, species rank, parent, code and 2026-09-13 snapshot. No own synonym or retirement is supplied.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036845&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036845) support the identity. All eleven root-first lineage entries match the local backbone. EFetch supplies the ten ancestors after root, and Datasets also supplies root 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Ancestor ranks agree with the YAML.

The record denotes the bacterial concept, not the host genus or all Wolbachia associated with it. Wolbachia endosymbiont of Sycobia sp. 1 (`NCBITaxon:1248010`) and sp. 2 (`NCBITaxon:1248011`) are separate same-parent species concepts: backbone rows 287463/287464, native name rows `data/catalog/ncbi_names-0007.jsonl.gz:8331` and 8332, and scope rows 375917/375918. They are not own synonyms or children.

## Evidence

The NCBITAXON source ID, label, count, unit and snapshot note match the own inventory. One `NAME` assertion is not a count of specimens, sequences or biological abundance. `strain_count: 0` describes BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036845%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned three entries. All explicitly carry the own organism name and `taxon:1036845`:

| Accession | Bases | BIOUG voucher suffix | BOLD cross-reference |
| --- | --- | --- | --- |
| [JF902512.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902512.1) | 501 | `YLCFX398-08.w` | `ASWFW070-10.COI-5P` |
| [JF902511.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902511.1) | 642 | `YLCFX396-08.w` | `ASWFW069-10.COI-5P` |
| [JF902510.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902510.1) | 642 | `YLCFX395-08.w` | `ASWFW068-10.COI-5P` |

They annotate partial COI gene/CDS with translation table 11; all contain N ambiguity. JF902512.1 starts its CDS at codon offset 2, while the other two use 1. Source qualifiers give Diaoluoshan, Hainan, China, 19-Apr-2007, collected by Fenggui, Liwei, Huhaoyuan and Niuliming, identified by Alex Smith. These are source-specific marker/specimen annotations, not culture-deposit or assembly evidence.

All retain an unpublished Smith study reference and a 01-May-2011 direct submission. No independent BOLD or publication-level specimen mapping was established. The marker annotations do not justify taxon-wide prevalence, reproductive phenotype, supergroup assignment or full-length protein-function claims.

The local genome candidate `data/catalog/ncbi_genbank-0054.jsonl.gz:17259` is `GCA_058710985.1`, Streptococcus pneumoniae, taxon/species ID 1313. Only its isolate field is `1036845`; it is not an own taxon match and supplies no own genome link. The [own NCBI genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036845/dataset_report) returned an empty object, which is bounded lack of positive evidence, not universal genome absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded numeric ID and label/slug prefix produced ten candidates, all read completely: four native JSON rows and six backbone/scope TSV rows. The candidate set included the two numbered concepts and the unrelated isolate-number match described above.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for the three JF902510-JF902512 accessions, voucher stems and BOLD IDs found no local match in those roots. These negatives are bounded to the inspected snapshots and identifiers.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source establishes an eligible own culture-to-genome link. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and graphs are appropriately empty for the supported seeded claims.

`data/taxa/PATHS.tsv:15171` matches the filename. `curation/seed_scope.tsv:322872` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z reproduces the source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external entry; no human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The genome-catalog numeric collision is excluded by its explicit organism/taxon fields and is not a missing own link.

## Recommended Edits

None required. Preserve the distinction between the unnumbered and numbered Sycobia taxon concepts and between marker specimens, culture deposits and genome records.

Any later authorized correction belongs in maintained upstream extraction inputs, `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is needed. Future experimental enrichment needs independently inspected publication/specimen mappings. Any genome addition must use an explicit eligible culture-deposit chain, not a numeric isolate/taxon collision. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for this target. No YAML, source, scope/history entry, generated page, branch, worktree or GitHub item changed. Other taxa were disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
