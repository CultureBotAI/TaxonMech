# YAML Record Review: Wolbachia endosymbiont of Neosycophila sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_neosycophila_sp.yaml`
- Started UTC: 2026-10-09T16:53:50Z
- Finished UTC: 2026-10-09T16:56:27Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036843` was read. It denotes Wolbachia endosymbiont of Neosycophila sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT`, status `SEEDED`. It contains one NCBI exact synonym, zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this YAML and three separately identified omeomorpha records, but no prior own report. Its SHA-256 is `931a2eff6e72bcb5e2071f823acad536a2d3f33044c6969c7749409a75af05a9`. Other records were source disambiguation context only.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_neosycophila_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_neosycophila_sp.yaml --workers 1 --out /private/tmp/taxonmech-neosycophila-sp-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Own-row comparisons passed for identity, every ancestor, attestation fields, PATHS/scope entries and generated event wording. The exact synonym was checked against both native name class and live authority, plus the repository's name-class mapping.
- Live NCBI taxonomy and exact-taxon nucleotide/genome searches were inspected. The single nucleotide candidate's complete metadata, source qualifiers, annotations and references were read, with nucleotide length/alphabet checks. No sequence alignment or protein-function validation is claimed.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph and iModulonDB gene/component checks. The YAML contains no graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Not checked: independent BOLD resolution or external publication/supplementary specimen mapping. The YAML cites no experimental paper and no publication-level biological claim is inferred from the marker.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222637` and `data/catalog/ncbi_names-0005.jsonl.gz:32231` support the exact identifier, scientific name, species rank, parent, code and 2026-09-13 snapshot.

The shorter form, Wolbachia endosymbiont of Neosycophila, is explicitly a `synonym` at native name row 32232 and occurs in the backbone's exact-synonym field. Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036843&retmode=xml) likewise lists it under `OtherNames/Synonym`. Its `EXACT_SYNONYM` placement agrees with `src/taxonmech/ncbi_taxdump.py`, which maps NCBI synonym/equivalent-name classes to exact synonyms and retains other name classes as related. It is not a broader genus grouping inferred from spelling.

Live EFetch and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036843) agree with the identity. All eleven root-first lineage entries match the local backbone. EFetch matches the ten named ancestors after root; Datasets also supplies root ID 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676.

The record denotes the bacterial concept, not the Neosycophila host genus or every Wolbachia associated with it. Three similarly prefixed concepts are separate: Neosycophila omeomorpha endosymbiont `NCBITaxon:1036844`, omeomorpha-TIN endosymbiont `NCBITaxon:1094260`, and omeomorpha-TIN.F endosymbiont `NCBITaxon:1094261`. Their native name rows are 32233, 47535 and 47536; backbone rows 222638, 235306 and 235307. They share the same parent but are not own children or declared synonyms. No host-specific reassignment or merger follows from the own shorter synonym.

## Evidence

The NCBITAXON attestation's source ID, source label, count, unit and snapshot date match the own inventory. Its one name attestation is not a count of all catalog aliases, sequences, specimens or cultured strains. `strain_count: 0` describes classified BacDive inventory coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036843%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry, [JF902486.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902486.1). It carries the exact organism and `taxon:1036843`, voucher `BIOUG<CAN>:YLCFX520-08.w` and BOLD cross-reference `ASWFW091-10.COI-5P`.

The marker annotates partial COI gene/CDS, translation table 11 and protein AEG77946.1. Declared and actual nucleotide lengths are 639 bases; its alphabet includes N ambiguity. Source qualifiers specify Liangyuan, Yaoyuan, Hainan, China, 09-Nov-2006, collected by Huhaoyuan and Niuliming and identified by Alex Smith. These are source-specific specimen details, not culture-deposit evidence or a genome assembly.

GenBank retains an unpublished Smith study reference and a 01-May-2011 direct submission. Neither taxon-wide prevalence, supergroup membership, reproductive phenotype nor a full-length protein function is inferred from this record. BOLD and publication-level specimen mappings were not independently resolved.

The [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036843/dataset_report) returned an empty object. It supplies no positive assembly evidence, not proof of universal genome absence. The marker voucher does not establish an eligible culture-to-genome chain.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial label/ID query was broadened to include the complete shorter synonym and label/slug spelling. All thirteen final candidates were read in full: five native name JSON rows and eight backbone/scope TSV rows. They describe the own scientific name and synonym plus the three separately identified omeomorpha concepts.

All five source `SOURCE.json` files were parsed without a target match. A further ignored-inclusive compressed search for JF902486, YLCFX520-08 and ASWFW091-10 found no local match in those roots. These negative findings concern the inspected snapshots and identifiers, not all external evidence.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome link. The supported exact synonym is present; optional additional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty.

`data/taxa/PATHS.tsv:15169` agrees with the filename. `curation/seed_scope.tsv:322870` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external history entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The shorter exact synonym is source-backed, and the optional external publication/BOLD limitations do not leave an asserted YAML claim unsupported.

## Recommended Edits

None required. Preserve the exact synonym without broadening the target to all host-genus endosymbionts or merging separately identified omeomorpha concepts. Keep specimen markers distinct from culture and genome assertions.

Any later authorized correction belongs in maintained upstream extraction inputs, the name-class mapping in `src/taxonmech/ncbi_taxdump.py`, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, as appropriate, followed by regeneration. Do not hand-edit this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A future name refresh should retain the native name class and exact taxon ID rather than infer synonym scope from the label alone. Later experimental enrichment needs independent publication/specimen verification; genome links require explicit eligible culture-deposit chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item changed. The other taxa were disambiguation context only; no host or Eukaryota record was reviewed. No paid research was performed.
