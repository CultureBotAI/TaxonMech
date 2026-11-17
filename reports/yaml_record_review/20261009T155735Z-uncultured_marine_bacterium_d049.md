# YAML Record Review: uncultured marine bacterium D049

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d049.yaml`
- Started UTC: 2026-10-09T15:54:58Z
- Finished UTC: 2026-10-09T15:57:35Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:103681` was read. It denotes uncultured marine bacterium D049, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608` (marine bacteria D ensemble), genetic code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `a324d1187c0fab0a71b44b6f36a776d250bf153338ebb84a1f1aaf91e9162b49`. Other organism rows were inspected solely to resolve search matches, not as additional review targets.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d049.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d049.yaml --workers 1 --out /private/tmp/taxonmech-d049-20261009-validation.tsv`: passed, one file, zero errors; the inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Structured own-row checks passed for identity, every ancestor, the source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. This YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Live NCBI taxonomy, sequence and PubMed responses and the primary paper's relevant full-text sections were inspected. The Taxonomy browser page was inaccessible through the web tool; EFetch and Datasets supplied the authority evidence instead.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18546` supports the identifier, exact label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0000.jsonl.gz:38562` supplies the scientific name. The own inventory has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103681&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103681) confirm the identity, species rank, parent and genetic code. All five lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; environmental samples 48479; marine bacteria D ensemble 150608. Labels and ranks agree.

NCBI's species rank is not evidence of a formally named bacterial species or cultured type strain. The unresolved environmental lineage is faithfully retained; partial-marker context is not used to infer a replacement classification.

## Evidence

The attestation counts one NCBI name, not a culture, genome or experiment. Its source ID, label, count, unit and snapshot date agree with the own inventory. Zero inventoried strains concerns BacDive coverage, not universal biological absence.

An exact non-expanded nucleotide query for `txid103681[Organism:noexp]` returned one ID, 5882283. Complete [GenBank AF177568.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177568.1) metadata, features and references identify a 559-base partial 16S rRNA sequence with the same organism, `taxon:103681`, clone D049 and an environmental-sample flag. Its source note describes an uncultured surface-associated marine bacterium. Actual and declared lengths agree; the sequence contains A/C/G/T only. It is a marker, not a genome assembly or culture deposit.

The linked publication was verified through [PubMed 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) and the [primary paper, DOI 10.1128/AEM.66.2.467-475.2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/). Table 1 explicitly lists D049 at 1.8% in PVA-72, 1.9% in PEG-M-24 and 3.7% in PU-72. These are environmental clone-library frequencies, not cell abundance or cultured-growth measurements. The methods use E. coli JM109 as a cloning host; that does not identify D049 as E. coli or establish a D049 culture. The evidence supports the clone context without transferring study-wide functional conclusions to this record.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103681/dataset_report) returned an empty object. This supplies no positive assembly evidence through that query, not proof that no genome can exist elsewhere.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label/slug-compatible spelling and bounded D049 token. All 61 candidates were read in full: 33 native JSON records and 28 TSV rows, with nested source evidence parsed. All five source `SOURCE.json` files were parsed. A further ignored-inclusive search for AF177568, PMID:10653705 and PMC91850 found no local match in these roots. These findings concern the inspected snapshot only.

The non-target candidates resolve as follows:

- BacDive 103681 is Rhodococcus sp. ST000661, taxon 194249. The corresponding SOURCE metadata hit is a BacDive request identifier, not this NCBI taxon.
- CIP 103681 belongs to Campylobacter upsaliensis, source species taxon 28080 and strain taxon 1121269, BacDive 2126, LPSN 774391 and StrainInfo 1572/deposit 149654. Its extensive marker and genome evidence concerns that organism, not D049. GOLD Go0234530 agrees.
- DSM 103681 belongs to Macrococcus epidermidis, taxon 1902580, BacDive 157750, LPSN 797867 and StrainInfo 139385/deposit 55322. GCA_003259695, GCA_042659445, BV-BRC 1902580.3, IMG 2882429405, SAMN05771339 and GOLD Go0620713 concern that organism.
- NBRC 103681 identifies Actinoallomurus iriomotensis, taxon 478107. NCBI/GTDB GCA/GCF_030269445.1, BV-BRC 478107.4, BioSample SAMD00540741 and the GOLD Go0672391 -> Gp0763575 -> Ga0617211 chain with IMG 8058251114 concern that culture, not D049.
- StrainInfo deposit 103681 is ATCC 25143, Mycobacterium nonchromogenicum, taxon 1782. KY103681 belongs to a yeast source record.
- CP103681 belongs to Enterobacter hormaechei MB4528 Variant. MGBC103681 is an uncultured Lachnospiraceae bacterium; PNUSAS103681 is Salmonella enterica. ASM103681v1 identifies a Pseudomonas aeruginosa assembly. Other GTDB matches are N50/N75 statistics, not identifiers.
- The ATB row at `data/catalog/allthebacteria.tsv.xz:6277` is E. coli O26:H11, BioSample SAMD00076024 and run DRR103681. Its eligible assembly status does not make its unrelated run-number match a D049 link.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture, deposit, sample-to-genome or assembly chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external marker does not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15159` agrees with the filename. `curation/seed_scope.tsv:144190` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence.

## Recommended Edits

None required. Preserve the environmental-clone identity and carried source lineage. Do not turn the marker or its cloning host into a cultured D049 strain or genome, or join unrelated sources on a shared numeric suffix.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. Before any later authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates. Additional strain, genome or phenotype claims require their own explicit target-specific evidence.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Other organism rows were source context only; no Eukaryota record was reviewed. No paid research was performed.

