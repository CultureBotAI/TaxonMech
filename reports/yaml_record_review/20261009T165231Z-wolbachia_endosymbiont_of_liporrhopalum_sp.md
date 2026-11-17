# YAML Record Review: Wolbachia endosymbiont of Liporrhopalum sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_liporrhopalum_sp.yaml`
- Started UTC: 2026-10-09T16:49:39Z
- Finished UTC: 2026-10-09T16:52:31Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036842` was read. It denotes Wolbachia endosymbiont of Liporrhopalum sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT`, status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this exact YAML and no prior own report. Its SHA-256 is `e3e6be7e6ce94784d91a06a1404e952f533e031b3b205db5fc8507e9387f3dfe`. A non-target assembly row was inspected only to distinguish a numeric match.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_liporrhopalum_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_liporrhopalum_sp.yaml --workers 1 --out /private/tmp/taxonmech-liporrhopalum-sp-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed this turn, 17 valid records and zero invalid links.
- Structured own-row comparisons passed for identity, all ancestors, every attestation field, PATHS/scope entries and generated event wording.
- Live NCBI taxonomy, exact-taxon nucleotide and genome queries were inspected. The sole nucleotide candidate was fetched and its complete metadata, source qualifiers, annotations and references read; nucleotide length/alphabet checks passed. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. The documented `just verify-corpus` gate has no record selector; focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph and iModulonDB gene/component checks. No graph, gene, regulator, pathway, trait or transcriptomics assertion occurs in the YAML; external marker annotations are not added record claims.
- Not checked: independent BOLD resolution or publication/supplementary specimen mapping for the external marker. The YAML cites no experimental publication, and no study-wide biological result is assigned to this taxon.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222636` and `data/catalog/ncbi_names-0005.jsonl.gz:32230` support the exact identifier, scientific name and 2026-09-13 snapshot. Rank, parent and code agree; exact, related and broad synonym fields are empty.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036842&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036842) agree with the record. The eleven lineage entries match the local backbone. EFetch matches the ten named ancestors after root; Datasets includes root ID 1 as well: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676.

The record denotes this specific NCBI bacterial concept, not the Liporrhopalum host genus or a class of all endosymbionts of that genus. The unresolved host epithet in the source label is retained. Species rank does not establish a formally named bacterial species or cultured type strain, and does not authorize replacement by a more specific host-associated taxon.

## Evidence

The NCBITAXON attestation counts one name. Source ID, label, count, unit and snapshot date agree with the own inventory. The name assertion is not a culture, specimen or genome count. `strain_count: 0` describes classified BacDive coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036842%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry: [JF902480.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902480.1). It carries the exact organism and `taxon:1036842`, voucher `BIOUG<CAN>:YLCFY163-08.w`, and BOLD cross-reference `ASWFW169-10.COI-5P`. Its source qualifiers specify Xtbg, Yunnan, China, 30-Mar-2002, collected by Zhenwenquan and identified by Alex Smith. These are source-specific specimen details, not a culture-deposit relationship.

The marker annotates partial COI gene/CDS, translation table 11, protein AEG77940.1. Declared and actual length are 642 bases, with N ambiguity in addition to A/C/G/T. The GenBank record retains an unpublished Smith study reference and a 01-May-2011 direct submission. It does not establish a complete genome, cultured strain, full-length gene function, reproductive phenotype or taxon-wide prevalence. BOLD and publication mappings were not independently resolved.

The [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036842/dataset_report) returned an empty object. This supplies no positive assembly evidence, not proof of universal genome absence. A partial marker and specimen voucher do not establish an eligible culture-to-genome chain.

## Completeness

Gitignore-independent searches covered hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded ID 1036842 and label/slug-compatible spelling. All four candidates were read in full: two native JSON and two TSV rows. All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF902480, YLCFY163-08 and ASWFW169-10 found no local match in those roots. Negative findings concern these snapshots and search terms only.

The non-target catalog match, `data/catalog/ncbi_genbank-0066.jsonl.gz:25328`, is Candidatus Planktophila sp., taxon 2175601, metagenome-derived assembly GCA_982644385.1, isolate HRS-bin1525-RIMVE-SM17-13sep23, BioSample SAMEA122213483 and BioProject PRJEB84054. Its genome size and ungapped size are 1036842 bases. That number is a length, not an NCBI taxonomy association with this Wolbachia record. The remaining three matches are the own name, backbone and scope rows.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome relationship. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external marker does not demonstrate a missing required relationship.

`data/taxa/PATHS.tsv:15168` agrees with the filename. `curation/seed_scope.tsv:322869` records the 2026-09-13 one-source inclusion; the sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external history entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The optional external publication/BOLD limitations do not leave an asserted record claim unsupported.

## Recommended Edits

None required. Preserve the source's exact bacterial identity and unresolved host designation. Do not import an unrelated assembly because its genome length equals the taxon number, or treat the marker voucher as a culture deposit.

Any future authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A later literature-enrichment task should verify exact specimen/publication and BOLD mappings before making experimental claims. New strain/genome links require explicit eligible culture-deposit source chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item changed. The other organism was source disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
