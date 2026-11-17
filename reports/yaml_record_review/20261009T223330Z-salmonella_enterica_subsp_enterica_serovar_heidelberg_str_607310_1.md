# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. 607310-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_607310_1.yaml`
- Started UTC: 2026-10-09T22:32:14Z
- Finished UTC: 2026-10-09T22:33:30Z
- Verdict: needs curation

## Target

Entire generated `TaxonRecord` read. `NCBITaxon:1037258` denotes Heidelberg strain 607310-1, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:611`, genetic code 11, grounding `EXACT`, status `SEEDED`. Twelve ancestors, two synonyms, one GTDB mapping, three attestations and the complete seed event were inspected. Zero represented BacDive strains describes source coverage. No nomenclature, nested strain entries, functional evidence, definition or graph is asserted.

HEAD freshly confirmed as `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `7ec085b3f71852f969ffa344af29fcb7bf47578de2d0d99d147825e43de96f91`. Ignored-inclusive filename resolution found one target and no prior report for this stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_607310_1.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_607310_1.yaml --out /private/tmp/taxonmech-sal-heid-607310-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: reused this turn's 17 valid records, zero invalid links after a fresh empty diff for schema, history and validator.
- Complete own-row, lineage, type/status, attestation, scope and slug comparisons passed. These are bounded source checks, not full-corpus reproduction or proof that an upstream relationship is biologically sound.
- Live NCBI EFetch, Datasets taxonomy and focused assembly identity reports succeeded. NCBI's taxonomy browser and the GTDB genome page failed. Complete native GTDB metadata was inspected; live GTDB authority verification remains unavailable.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance hash replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222709`, native names `data/catalog/ncbi_names-0005.jsonl.gz:32310` and `:32311`, slug `data/taxa/PATHS.tsv:15246` and scope `curation/seed_scope.tsv:36181` agree. The complete backbone supports the label, strain rank, parent, code, equivalent name and 2026-09-13 snapshot. The NCBI synonym expands `str.` to `strain` while preserving 607310-1.

The full twelve-ancestor chain matches the pinned inventory: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; S. enterica; S. enterica subsp. enterica; serovar Heidelberg. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037258&retmode=xml) confirms strain rank, name, synonym, parent, code and named ancestors; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037258) confirms `STRAIN` and all ancestor IDs including root. Complete backbone/status scans found no own child, type-material, merged-ID or dropped row.

The NCBI node is correctly grounded. The GTDB-derived exact species synonym and associated identity treatment extend beyond that node's strain scope, as detailed in M1.

## Evidence

`data/raw/gtdb_mappings.tsv:1475` supplies `GTDB:s__Salmonella_enterica`, closeMatch and 21,527 genomes. The independently read species inventory `data/raw/gtdb_species.tsv:163163`, freshly confirmed unchanged, supports the same species-wide count. The schema explicitly defines genome count as volume classified under the source taxon. It is not a count of 607310-1 genomes; no complete native-cluster recount was performed.

Complete native row `data/catalog/gtdb_genomes-0006.jsonl.gz:49906` places `GB_GCA_000962165.1` under the GTDB S. enterica species, while separately recording NCBI strain taxon 1037258, species taxon 28901 and strain identifier 607310-1. Its representative flag is false. This supports species membership of this genome, not exact identity between the species and strain.

Complete GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:32957` supports GCA_000962165.1, ASM96216v1, Contig, 558 contigs, 4,730,900 bases, WGS master AMMF00000000.1, sample SAMN01087983 and project PRJNA67431. Historical RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:7999` identifies GCF_000962165.1 as suppressed, non-live since 2020-06-14, with annotation-completeness/frameshift exclusions and source-specific project PRJNA224116. Neither native assembly row supplies a PMID.

Focused [live GenBank metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000962165.1/dataset_report) confirms the current assembly, strain, sample and PRJNA67431; the [RefSeq response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000962165.1/dataset_report) confirms suppression. Both live reports name PRJNA67431. Their BioSample identity view records sample label CFSAN000338 and SRA sample SRS472080; these are sample metadata, not evidence of a recognized culture-collection deposit. No sequence-equivalence analysis or name-based join was performed. A paired RefSeq accession must not be presented as current merely because the GenBank record retains it.

Complete `data/bvbrc/bvbrc-0000.jsonl.gz:3420` links PATRIC 1037258.3 to the strain, RefSeq accession, sample and project. GOLD organism/project/analysis records at `data/gold/organisms.jsonl.gz:65795`, `projects.jsonl.gz:70219` and `analyses.jsonl.gz:51230` trace `Go0116198 -> Gp0120600 -> Ga0080720`, IMG 2636415950 and GCA_000962165.1. The analysis lacks a direct organism field but explicitly names its project, which identifies the organism. No culture-collection accession is supplied. `data/raw/gold_organisms.tsv:514` correctly records one organism assertion. These source-native genome associations do not establish an eligible BacDive/deposit link.

NCBITAXON 1 NAME and GOLD 1 ORGANISM match complete inventory rows. GTDB 21,527 GENOME matches source-species volume, with mapping semantics qualified by M1. Complete own-ID inventories found no BacDive, LPSN, MediaDive, Madin or BactoTraits row; no descendant contributes BacDive coverage. Source set, snapshot and complete scope sentence agree. This turn's inspected `_seed_timestamp` implementation and raw/ATB/StrainInfo manifests, freshly confirmed unchanged, support `2026-09-13T17:54:04Z` as the latest extraction time. The event records generation, not human approval.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched numeric identity, strain designation and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored, hidden and compressed files. All 25 matching rows were read completely or in lossless common-field/delta representations. Five SOURCE.json files and history filenames were separately checked; no own metadata or history match was found. The newly observed live BioSample label was not used as an additional local search or join key; conclusions remain bounded to the stated search and inspected identity responses.

The unrelated native match is `data/catalog/ncbi_genbank-0009.jsonl.gz:7438`: Norwich PNUSAS000952, taxon 1194162, GCA_010372585.1, sample SAMN04125346 and project PRJNA230403. Its assembly digits are not this taxon's identity. Ten ATB hits at rows 171042, 171061, 171118, 171131, 171162, 171215, 171241, 171272, 171300 and 171301 concern Campylobacter jejuni runs ERR10372580-89. Full assembly, sample, checksum, availability and filter metadata was read. All retain available FASTAs; row 171241 fails the CheckM2 contamination HQ filter and the other nine pass. Their run digits do not establish a 607310-1 association.

No eligible whole-deposit association or missing required representation was established. Absent BacDive strain entries do not deny the known genome or justify creating a strain entry from a bare name. Optional nomenclature, definitions, functional evidence and graphs may remain empty. iModulonDB is inapplicable because the YAML asserts no functional gene, regulator, pathway, phenotype or transcriptomics claim. Absence findings are bounded to inspected roots, snapshots and responses.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Species classification is promoted to exact strain identity.** YAML lines 45-60 and 70-75 treat the broader GTDB S. enterica species as closeMatch to strain 607310-1 and derive an exact synonym and identity xref. This target's native GTDB row distinguishes its strain taxon from species taxon 28901; NCBI independently confirms the narrower strain scope. Membership in a species cluster is insufficient to make the species name an exact synonym of the strain. These derived fields are one connected scope-inflation defect. The 21,527 source-species count is not a separate counting error.

Maintained owners: upstream kg-microbe's GTDB mapping imported by `src/taxonmech/extract.py:501`, and the rank-unaware identity promotion in `src/taxonmech/seed.py:452` and `:468`. Inspected code promotes closeMatch directly to identity and an exact synonym. No blocker is assigned because the primary NCBI identity, rank and lineage remain correct. Structural validation does not detect this semantic error.

## Recommended Edits

1. Correct or qualify the species-to-strain relation in the maintained upstream mapping and re-extract supported changes, preserving original provenance. Check source/target direction explicitly; do not blindly substitute broadMatch, whose schema meaning assumes the record is broader than the source.
2. Guard identity and exact-synonym promotion in `src/taxonmech/seed.py` against a broader species mapping onto a strain. Preserve the actual NCBI strain synonym and defensible species-classification evidence, with any cluster count clearly source-scoped.
3. Add a regression case in `tests/test_seed.py` for a STRAIN-to-broader-GTDB-species mapping and a positive same-species mapping. Regenerate through the validated writer after tests pass. Do not patch generated YAML, pages or an assumed overlay.

## Follow-up Checks

Run the targeted new seeder tests, schema and strict validation, then `just verify-corpus` and `just qc`. Inspect the emitted record to ensure that 607310-1 retains its NCBI identity without an exact species-name synonym or unqualified identity mapping. Retry live GTDB authority access when available. A future genome enrichment must preserve RefSeq suppression and independently prove a whole-deposit match and explicit source chain, not infer it from taxonomy, sample labels or names.

## Additional Notes

Only NCBITaxon:1037258 is judged, using its own complete YAML and sources. No neighboring verdict was inherited; Eukaryota was not reopened. No YAML, source, inventory, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for the target. No paid research was used.
