# YAML Record Review: uncultured marine bacterium D042

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d042.yaml`
- Started UTC: 2026-10-09T15:43:18Z
- Finished UTC: 2026-10-09T15:46:10Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:103680` was read. It denotes uncultured marine bacterium D042, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608` (marine bacteria D ensemble), genetic code 11, grounding `EXACT` and status `SEEDED`. It has zero inventoried strains, one NCBITAXON name attestation and one seeding event.

An ignored-inclusive filename inventory resolved only this YAML and no prior own report. SHA-256: `bac828d0270b5ab45b3b8f197bb9835851b280b91a9fd6e2e5a2d7ae5e45068a`. Other organism rows were inspected solely to resolve source-search candidates, not as additional review targets.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d042.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d042.yaml --workers 1 --out /private/tmp/taxonmech-d042-20261009-validation.tsv`: passed, one file, zero errors; the inspected TSV has only its header.
- `uv run --offline python scripts/validate_history.py history`: passed earlier in this review turn, 17 valid records and zero invalid links; history was not changed.
- Structured own-row checks passed for every ancestor, identity field, source attestation, PATHS/scope entry and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion; an external marker discovery does not add such a claim to the YAML.
- Live NCBI taxonomy, sequence and PubMed responses and the primary paper's relevant full-text sections were inspected. The Taxonomy browser page was inaccessible through the web tool; EFetch and Datasets supplied the authority evidence instead.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18545` supports the identifier, exact label, rank, parent, genetic code, NCBI-only attestation and 2026-09-13 snapshot. `data/catalog/ncbi_names-0000.jsonl.gz:38561` supplies the scientific name. The own inventory has no exact, related or broad synonyms requiring representation.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103680&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103680) confirm the identity, species rank, parent and genetic code. All five lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; environmental samples 48479; marine bacteria D ensemble 150608. Labels and ranks agree.

The authority's species rank does not imply a formally named bacterial species or a cultured type strain. `EXACT` correctly denotes the match to this NCBI concept; it does not resolve the biological origin of an environmental marker. The record carries the source lineage without inferring a more specific classification.

## Evidence

The sole attestation counts one NCBI name, not a culture, genome or experiment. The source ID, label, count, unit and snapshot date agree with the own inventory. `strain_count: 0` is consistent with no own or descendant BacDive entry, not a statement about universal biological absence.

An exact non-expanded nucleotide query for `txid103680[Organism:noexp]` returned one ID, 5882282. Complete [GenBank AF177567.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177567.1) metadata, references and features identify a 564-base partial 16S rRNA sequence with the same organism, `taxon:103680`, clone D042 and an environmental-sample flag. Its source note describes an uncultured surface-associated marine bacterium. Actual and declared lengths agree; the sequence contains A/C/G/T only. The marker is not a culture deposit or genome assembly.

The linked publication was verified through [PubMed 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/) and the [primary paper, DOI 10.1128/AEM.66.2.467-475.2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/). Table 1 lists D042 at 1.8% in PVA-72, 1.5% in PEG-S-24, 1.5% in PEG-L-72 and 9.3% in PU-72. These describe environmental clone-library frequencies, not cell abundance or cultured growth.

Importantly, the sequence-analysis results place D042 near cyanobacteria and chloroplasts. It is not one of the Roseobacter-group clones, so the paper's Roseobacter-specific conclusions cannot be transferred to D042. This leaves biological-origin uncertainty but does not establish a particular plastid host or justify replacing the carried NCBI lineage. The YAML makes no more specific phylogenetic or functional assertion.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/103680/dataset_report) returned an empty object. It supplies no positive assembly evidence through that query, not proof that no genome can exist elsewhere.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric ID, current label/slug-compatible spelling and bounded D042 token. All 60 candidate rows were fully read, including 27 native JSON records and 33 TSV rows, with nested source evidence parsed. All five source `SOURCE.json` files were parsed. A further ignored-inclusive search for AF177567, PMID:10653705 and PMC91850 found no local match in these roots. These are bounded snapshot findings.

The non-target candidates resolve as follows:

- BacDive 103680 is Rhodococcus sp. ST000658, taxon 194249. The corresponding SOURCE metadata match is a BacDive request identifier, not this NCBI taxon.
- CIP 103680 is Aeromonas enteropelogenes, taxon 29489, BacDive 251 and StrainInfo 7710/deposit 148471.
- NBRC 103680 is Actinoallomurus fulvus TT99-66, taxon 478108, BacDive 17009, LPSN 788030 and GOLD Go0612704. Its AB364582 marker and type-material rows concern that organism.
- DSM 103680 is Macrococcus/Macrococcoides bohemicus/bohemicum, taxon 1903056, BacDive 157749 and StrainInfo 139386/deposit 54264. Its LPSN names, type-material rows, GCA_003259675 assembly, BV-BRC 1903056.3, IMG 2895698585, SAMN05781217 and GOLD Go0620711 do not identify D042.
- StrainInfo deposit 103680 is ATCC 25142, Mycobacterium nonchromogenicum, taxon 1782. KY103680 belongs to a yeast source record, not D042.
- CP103680 belongs to Enterobacter hormaechei MB4528 Variant, taxon 158836, in BV-BRC and GOLD records. MGBC103680 is Duncaniella muris; PNUSAS103680 is Salmonella enterica. ASM103680v1 identifies a Pseudomonas aeruginosa assembly, and a PELAGICS bin numbered 103680 belongs to Rickettsiales bacterium UBA1997.
- A D042 segment in a Listeria isolate UUID and GTDB N50 statistics of 103680 are unrelated matches. The two ATB candidates match an E. coli sequencing run, DRR103680, and a Klebsiella SeqKit checksum, respectively; neither provides target-specific sample or genome evidence.

Complete own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture, deposit, sample-to-genome or assembly chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. The external partial marker does not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15156` agrees with the filename. `curation/seed_scope.tsv:144189` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human review status is implied.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The unresolved environmental-sequence placement is a limitation of the current source concept, not an unsupported more-specific assertion in this YAML.

## Recommended Edits

None required. Preserve the environmental-clone identity and source lineage. Do not assign Roseobacter-specific traits, infer a plastid host, promote a partial marker to a genome or link unrelated accessions through a shared numeric suffix.

Any later authorized correction belongs in the relevant upstream authority or maintained extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to the generated YAML.

## Follow-up Checks

No defect-specific repair is required. A future attempt to resolve the marker's biological origin would need source-authority clarification and target-specific phylogenetic evidence; no such resolution is claimed here. Before any authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Other organism rows were source context only; no Eukaryota record was reviewed. No paid research was performed.

