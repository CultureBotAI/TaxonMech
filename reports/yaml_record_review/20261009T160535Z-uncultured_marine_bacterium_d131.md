# YAML Record Review: uncultured marine bacterium D131

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d131.yaml`
- Started UTC: 2026-10-09T15:58:46Z
- Finished UTC: 2026-10-09T16:05:35Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:103682` was read. It denotes uncultured marine bacterium D131, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608` (marine bacteria D ensemble), genetic code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `a2080bbae3bb0645bfd208aedd892d785f6c4967a2c01c4a8b4b1721195d60a7`. Other organism rows were inspected only to disambiguate source matches, not as additional review targets.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d131.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d131.yaml --workers 1 --out /private/tmp/taxonmech-d131-20261009-validation.tsv`: passed, one file, zero errors; the inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Structured own-row checks passed for identity, all ancestors, the source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. This YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Live NCBI EFetch and Datasets taxonomy responses, exact nucleotide search, GenBank record, PubMed metadata and relevant primary-paper text were inspected. PMC intermittently returned a browser-check page; successful direct HTML reads supplied the paper's methods, table headers and D131 row. No inaccessible response was used as evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18547` supports the identifier, exact label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0000.jsonl.gz:38563` supplies the scientific name. The own inventory has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103682&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103682) confirm the identity, species rank, parent and genetic code. All five lineage entries agree with the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; environmental samples 48479; marine bacteria D ensemble 150608. Labels and ranks match.

NCBI's species rank does not establish a formally named bacterial species or cultured type strain. The unresolved environmental lineage is faithfully retained. A partial marker or similarly named organism does not justify a replacement classification.

## Evidence

The attestation counts one NCBI name, not a culture, genome or experiment. Its source ID, label, count, unit and snapshot date agree with the own inventory. Zero inventoried strains concerns BacDive coverage, not universal biological absence.

An exact non-expanded nucleotide query for `txid103682[Organism:noexp]` returned one ID, 5882284. Complete [GenBank AF177569.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177569.1) metadata, features and references identify a 559-base partial 16S rRNA sequence with the same organism, `taxon:103682`, clone D131 and an environmental-sample flag. Its source note describes an uncultured surface-associated marine bacterium. Actual and declared lengths agree; the sequence contains A/C/G/T only. It is a marker, not a genome assembly or culture deposit.

The linked publication was verified through [PubMed 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) and the [primary paper, DOI 10.1128/AEM.66.2.467-475.2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/). Table 1 explicitly lists D131 at 1.2% in BR-24, 1.5% in PEG-S-24 and 2.0% in PU-24. These are clone-library frequencies, not cell abundance or cultured-growth measurements. Field surfaces were deployed at Clam Bank Creek, North Inlet, South Carolina. E. coli JM109 was the cloning host, not the identity of D131. These observations support environmental-clone context without transferring study-wide functional conclusions to this record.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103682/dataset_report) returned an empty object. This supplies no positive assembly evidence through that query, not proof that no genome can exist elsewhere.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label/slug-compatible spelling and bounded D131 token. All 77 candidates were read in full: 40 native JSON records and 37 TSV rows, with nested evidence parsed. All five source `SOURCE.json` files were parsed. A further ignored-inclusive compressed-source search for AF177569 found no local match in these roots. Absence claims are limited to this inspected snapshot.

The non-target candidates resolve as follows:

- Synechococcus sp. D131 is `NCBITaxon:3142292`, with its own scientific-name, backbone and scope rows. It is not a synonym or identifier for this clone.
- Staphylococcus aureus D131 is taxon 1280, GCA/GCF_036042885.1, SAMN39465500 and BV-BRC 1280.49757. Pseudomonas lundensis D131 is taxon 86185, GCA/GCF_055406825.1, SAMN55282454 and BV-BRC 86185.136. Neither supports an assembly link to taxon 103682.
- GOLD Gp0502297 and Ga0450797/IMG 3300040793 describe a brackish-water microbial-mat metagenome from Salins du Lion, Vitrolles, France, labeled D131. The source supplies no explicit link to this taxon or its South Carolina clone; a shared short name does not establish one.
- BacDive 103682 is Rhodococcus sp. ST001831, taxon 194249. The SOURCE metadata hit is a BacDive request identifier, not this NCBI taxon.
- CIP 103682 belongs to Prevotella intermedia, source species taxon 28131 and strain taxon 1122984, BacDive 12531, LPSN 779791 and StrainInfo 38613/deposit 153901. Its full marker/genome evidence belongs to that culture group. The explicit CIP-associated sequence is DQ005487, a partial rpoB gene, not D131. Nomenclatural aliases and other collection assemblies do not alter the target distinction.
- NBRC 103682 belongs to Actinoallomurus amamiensis TT00-28, taxon 478109, BacDive 17007, StrainInfo 398090, LPSN 788027 and GOLD Go0612698; AB364583 belongs there. DSM 103682 belongs to Macrococcus caseolyticus subsp. hominis, source taxon 1891096, BacDive 157751 and StrainInfo 405094. Its MH044686 and GCA_002742395 evidence is unrelated. GOLD Go0620715 uses taxon 1255615 for its Macrococcus record; that source-classification difference is preserved and does not support a D131 match.
- StrainInfo deposit 103682 is ATCC 25144, Mycobacterium nonchromogenicum, taxon 1782. Other StrainInfo hits are yeast KY103682/CBS 398, Saccharomyces cerevisiae D131#26, Candida maltosa D131-3-4#25 and Neurospora intermedia D131/FGSC 8891. These are collision checks only, not reviews of Eukaryota records.
- CP103682 belongs to Enterobacter hormaechei MB4528 Variant, with GCA_024918215.1 and GOLD Ga0608824/Gp0745320. ASM103682v1 belongs to Pseudomonas aeruginosa Pae_CF67.05r, GCA/GCF_001036825.1. MarMAG_103682, MGBC103682 and PNUSAS103682 belong to other source organisms. A Marinobacter salsuginis assembly contains d131 inside a UUID; three other GTDB matches are assembly-statistic values, not target identifiers.
- ATB `data/catalog/allthebacteria.tsv.xz:6278` is E. coli O26:H11, SAMD00076025, DRR103682 and ERZ2885972. Row 300270 is Staphylococcus aureus, SAMEA115113263 and ERR12511809, matching only an assembly checksum substring. Neither is an own sample-to-genome chain.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture, deposit, sample-to-genome or assembly chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external marker does not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15160` agrees with the filename. `curation/seed_scope.tsv:144191` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence.

## Recommended Edits

None required. Preserve the environmental-clone identity and carried source lineage. Do not turn the marker or cloning host into a cultured D131 strain or genome, or join unrelated sources on a short label or numeric suffix.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Before any later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates. Additional strain, genome or phenotype claims require explicit target-specific evidence.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Other organism rows were source context only; no Eukaryota record was reviewed. No paid research was performed.

