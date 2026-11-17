# YAML Record Review: uncultured marine bacterium D033

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d033.yaml`
- Started UTC: 2026-10-09T15:28:41Z
- Finished UTC: 2026-10-09T15:34:22Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:103679` was read. It denotes uncultured marine bacterium D033, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608` (marine bacteria D ensemble), genetic code 11, grounding `EXACT` and status `SEEDED`. It has zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `8c1311f2095e0ef0d05290075b01f4d10291e84826a7441469432bf9b4e6599d`. Other organisms carrying D033 or the number 103679 are source-search context, not additional review targets.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d033.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d033.yaml --workers 1 --out /private/tmp/taxonmech-d033-20261009-validation.tsv`: passed, one file, zero errors. The inspected TSV contains only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Own-row structured checks passed for every ancestor, identity field, source attestation, PATHS/scope entry and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused checks do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics claim. Discovery of an external 16S marker does not add such a claim to the record.
- Live NCBI taxonomy, nucleotide and PubMed responses were inspected. The primary paper's PMC full text was successfully read after an initial browser challenge. An alternative Europe PMC full-text endpoint returned HTTP 500; this access failure was not treated as negative biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18544` supports the exact identifier, label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0000.jsonl.gz:38560` supplies the scientific name; the own source row has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103679&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103679) confirm the identity, species rank, parent 150608 and genetic code 11. All five lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; environmental samples 48479; marine bacteria D ensemble 150608. Their labels and ranks agree.

`SPECIES` is the authority's taxonomic rank, not evidence of a formally published binomial or a type strain. The unresolved environmental lineage is faithfully represented. Partial-marker phylogenetic context does not by itself authorize replacing this generated NCBI lineage with a different classification.

## Evidence

The attestation counts one NCBI name, not one cultured organism, assembly or experiment. Its identifier, label, assertion unit, count and snapshot date match the own inventory. Zero strains is an inventory count, not a universal claim that no biological strain exists.

An exact non-expanded nucleotide query for `txid103679[Organism:noexp]` returned one ID, 5882281. Complete [GenBank AF177566.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177566.1) metadata, features and references identify a 559-base partial 16S rRNA sequence with the same organism, `taxon:103679`, clone D033 and an environmental-sample flag. Its source note describes an uncultured surface-associated marine bacterium. Declared and actual sequence lengths agree, and its alphabet contains A/C/G/T only. The source is genomic DNA, but this marker is not a genome assembly or culture deposit.

The linked publication was verified through [PubMed 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) and the [primary paper, DOI 10.1128/AEM.66.2.467-475.2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/). It uses cultivation-independent clone libraries from submerged test surfaces. Table 1 explicitly lists D033 at 1.9% in PVA-24, 3.6% in BR-72 and 2.0% in PU-24. Those are clone-library frequencies, not organism abundance or growth measurements. The methods identify E. coli JM109 as a cloning host, not D033's taxonomic identity or a D033 culture. This supports the environmental-clone context without assigning study-wide phenotypes to the target.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103679/dataset_report) returned an empty object. This supplies no positive assembly evidence through that query; it does not establish universal genome absence.

## Completeness

Gitignore-independent searches covered hidden and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label and bounded D033 token. All 102 candidate rows were fully inspected, including native JSON, compressed catalogs, complete TSV rows and nested ATB genome evidence. All five source `SOURCE.json` files were parsed. A further ignored-inclusive search for AF177566, PMID:10653705 and PMC91850 found no local matches in these roots. These findings concern the inspected snapshot only.

Namespace and name collisions do not establish an own strain/genome relationship:

- BacDive 103679 is Rhodococcus sp. ST000655, taxon 194249. Its SOURCE metadata match is a BacDive request ID, not this NCBI taxon.
- DSM 103679 belongs to Treponema rectale, taxon 744512, BacDive 140319 and LPSN 795528. Its assembly, BioSample, BV-BRC, GOLD, StrainInfo and ATB chains consistently concern that taxon, including GCA/GCF_014202035.1, GCA_014984185.1, SAMN14908544 and SAMN09770339.
- CIP 103679 belongs to Aeromonas enteropelogenes, taxon 29489, BacDive 23534. StrainInfo deposit 103679 denotes ATCC 25141, Mycobacterium xenopi, taxon 1789.
- Chlamydia sp. 14-1437_D033 is a different NCBI taxon, 1608581. CP103679 is an Enterobacter hormaechei sequence; KY103679 is a yeast sequence. Neither identifier denotes taxon 103679.
- MGBC103679, PNUSAS103679 and MarMAG_103679 are unrelated assembly-associated labels. Other matches are DRR103679 or numeric assembly/SeqKit statistics in unrelated records, not identity links.

Complete own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. The broader source inspection supplied no eligible own culture, deposit, sample-to-genome or assembly chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental assertions and causal graphs are appropriately empty; the external marker does not demonstrate a missing required relationship.

`data/taxa/PATHS.tsv:15153` agrees with the filename. `curation/seed_scope.tsv:144188` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated seeding wording. Ignored-inclusive history filename and content searches found no own external history entry. The record does not claim human review or approval.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence.

## Recommended Edits

None required. Preserve the environmental-clone identity and generated NCBI lineage. Do not convert marker evidence into a culture or genome, or join unrelated sources on a bare numeric identifier.

Any future authorized change belongs in maintained upstream extraction inputs, the seeder or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Before a later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates. Any proposed strain, genome or phenotype relationship needs independent target-specific evidence and namespace-aware identity checks.

## Additional Notes

This independent report is the only repository write for this target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Other organism rows were inspected solely to resolve source-search collisions; no Eukaryota record was reviewed. No paid research was performed.

