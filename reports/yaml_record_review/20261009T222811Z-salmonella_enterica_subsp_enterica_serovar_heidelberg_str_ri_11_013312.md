# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. RI-11-013312

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_ri_11_013312.yaml`
- Started UTC: 2026-10-09T22:25:41Z
- Finished UTC: 2026-10-09T22:28:11Z
- Verdict: needs curation

## Target

Entire 87-line generated `TaxonRecord` read. `NCBITaxon:1037256` denotes the Heidelberg strain RI-11-013312, not all Salmonella enterica. It carries rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:611`, genetic code 11, grounding `EXACT` and status `SEEDED`. Twelve ancestors, two synonyms, one GTDB mapping, three attestations and the complete seed event were inspected. Zero represented BacDive strains is a source-coverage count, not biological absence.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `1d676146a2953a800110cda73d5152a20430766ff669b2e5e969445bff857c23`. Ignored-inclusive filename resolution found exactly one target and no prior report for this stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_ri_11_013312.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_ri_11_013312.yaml --out /private/tmp/taxonmech-sal-heid-ri-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete own-row, lineage, source, status, scope and slug comparisons passed. These bounded checks do not certify corpus reproduction or biological correctness of an upstream mapping.
- Live NCBI taxonomy browser, EFetch, Datasets taxonomy and focused assembly metadata were inspected. Both GTDB tree and genome browser opens failed; complete pinned native GTDB metadata was used, with live authority access explicitly unavailable.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222707`, both native name rows in `data/catalog/ncbi_names-0005.jsonl.gz:32306`, `data/taxa/PATHS.tsv:15244` and `curation/seed_scope.tsv:36179` agree. The NCBI exact synonym expands `str.` to `strain` without changing identity. All twelve ancestor IDs, labels and ranks match the pinned backbone: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; S. enterica; S. enterica subsp. enterica; serovar Heidelberg. No own child, type-material, merged-ID or dropped row was found in complete corresponding inventory scans.

The [NCBI taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037256) confirms name, synonym, code and lineage, but renders rank as `no rank`. [EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037256&retmode=xml) explicitly returns `strain`, and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037256) returns `STRAIN` and all twelve ancestor IDs including root. Preserve this display/API difference; the YAML follows the pinned backbone and structured authority responses, so no rank rewrite is justified.

The main identifier remains well grounded. The GTDB-derived exact synonym and equivalence treatment are not supported at this strain's scope, as detailed in Finding M1.

## Evidence

`data/raw/gtdb_mappings.tsv:1473` supplies `GTDB:s__Salmonella_enterica`, `skos:closeMatch` and count 21,527. `data/raw/gtdb_species.tsv:163163` independently records that count for the whole GTDB species. `src/taxonmech/extract.py:501` counts assembly-to-species edges and carries upstream mapping predicates into the inventories; it does not establish strain/species identity. The schema at `src/taxonmech/schema/taxonmech.yaml:431` describes closeMatch as denoting the same species, while `genome_count` is explicitly the volume under the source taxon. Thus the count is supported as species-cluster volume, not 21,527 genomes of RI-11-013312. No full native-cluster recount was performed.

Complete native GTDB row `data/catalog/gtdb_genomes-0002.jsonl.gz:38958` classifies `GB_GCA_000700765.1` under S. enterica, identifies NCBI strain taxon 1037256 and species taxon 28901 separately, and gives strain identifiers `RI-11-013312`. It is not the representative genome. This directly supports classification of a strain genome in a broader species cluster, not exact synonymy between that strain and the species.

The complete native GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:25696` supports `GCA_000700765.1`, assembly SEEH3312_1.0, Contig, 57 contigs, 4,720,120 bases, WGS master AKYK00000000.1, sample SAMN01041038 and project PRJNA67427. Historical RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:6253` records `GCF_000700765.1` as suppressed, with non-live date 2021-11-13 and annotation-completeness/frameshift exclusions. The [live GenBank identity report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000700765.1/dataset_report) confirms a current assembly and suppressed paired RefSeq; the [RefSeq report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000700765.1/dataset_report) confirms suppression. Do not describe the RefSeq accession as current merely because a paired accession is retained. The live report uses PRJNA67427, whereas the pinned RefSeq catalog used its source-specific umbrella PRJNA224116.

`data/bvbrc/bvbrc-0000.jsonl.gz:3418` names the same strain, assembly, sample and project under PATRIC 1037256.3. GOLD's complete organism/project/analysis rows are `data/gold/organisms.jsonl.gz:45354`, `projects.jsonl.gz:44153` and `analyses.jsonl.gz:34398`: `Go0070962 -> Gp0070962 -> Ga0054817`, with IMG 2602041815 and GCA_000700765.1. The analysis has no direct organism field but explicitly names the project, whose organism is unambiguous. The organism has no culture-collection accession. `data/raw/gold_organisms.tsv:512` correctly counts one organism assertion.

The ATB catalog also contains a same-name entry at `data/catalog/allthebacteria.tsv.xz:3140880`: analysis ERZ27154692, sample SAMN45204657, run SRR32654019, incremental release 202505, available FASTA, all three source filters PASS, current Sylph label S. enterica, previous label NA. This is a different sample accession from SAMN01041038; the shared scientific name alone does not establish genome equivalence or an eligible whole-deposit association. No FASTA was downloaded and no sequence-equivalence claim is made.

NCBITAXON 1 NAME and GOLD 1 ORGANISM attestations match their inventories; GTDB 21,527 GENOME matches source-species volume, subject to M1's mapping scope. Complete own-ID inventory scans found no BacDive, LPSN, MediaDive, Madin or BactoTraits row. No descendant contributes BacDive coverage. The complete seed sentence matches scope and source set. Fresh reads of `src/taxonmech/seed.py:_seed_timestamp` and raw/ATB/StrainInfo manifests support `2026-09-13T17:54:04Z`, the latest extraction timestamp. `SEEDED` correctly records generation rather than human approval.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched numeric ID, strain designation and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored, hidden and compressed files were included. All 29 matching rows were read completely or through lossless common-field/delta representations. Five SOURCE.json files and history filenames were separately parsed; no matching metadata or own history entry was found.

False native hits were disambiguated: GCA_010372565.1 is Minnesota FDA474825-1-2, taxon 70803; GCA_964419835.1 is an uncultured Saccharibacteria taxon 179883 with genome size 1037256; GCA_038118005.1 is a Flavobacteriaceae taxon 1871037 with the same numeric genome size. GTDB's other matching row is the Saccharibacteria assembly, not RI-11-013312. Ten ATB rows at 171058, 171073, 171120, 171122, 171141, 171155, 171167, 171202, 171223 and 171269 concern Campylobacter jejuni, runs ERR10372560-69; full rows, statuses, samples and assembly accessions were read. Their run digits do not establish taxon identity.

No eligible BacDive/whole-deposit entry was established for the known genomes, so `strain_count: 0` and absence of nested strain links are not a missing-genome defect under the repository contract. No obligatory nomenclature, definition, evidence graph or curation history record was established. iModulonDB is inapplicable because this YAML asserts no functional gene, regulator, pathway, phenotype or transcriptomics claim. Absence conclusions are bounded to inspected roots, snapshots and responses.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Broader GTDB species is promoted to exact strain identity.** YAML lines 45-60 and 70-75 treat S. enterica as closeMatch to RI-11-013312 and add it as an exact synonym and identity xref. Pinned and live NCBI evidence distinguishes this strain from its species ancestor; native GTDB metadata places its genome within the species. Membership does not support substituting the species name for the strain. This is one linked scope-inflation defect, not separate findings for each derived field. The 21,527 source-species count is not independently erroneous, but must not be read as strain-specific volume.

Maintained owners: the upstream kg-microbe GTDB mapping, imported by `src/taxonmech/extract.py:501`, and TaxonMech's rank-unaware identity promotion in `src/taxonmech/seed.py:452` and `:468`. The latter promotes every closeMatch to an identity xref and exact synonym without testing target scope. Schema validation passes because it does not test this biological relationship. No blocker is assigned because the record's primary NCBI identity and lineage remain correct.

## Recommended Edits

1. Correct or qualify the strain-to-species relation upstream in kg-microbe, preserving the original source assertion for provenance. Do not mechanically replace closeMatch with broadMatch: predicates are expressed from the source taxon's side, and that direction must be checked explicitly. Re-extract inventories through the maintained extraction workflow after the upstream correction.
2. Add a scope-aware guard in `src/taxonmech/seed.py` so a broader source species cannot become an exact synonym or identity xref of a strain merely because its imported predicate is closeMatch. Preserve defensible species classification separately and retain the true NCBI strain synonym. Keep any source-species genome count explicitly scoped as such.
3. Add a regression case to `tests/test_seed.py` for a STRAIN target mapped to a broader GTDB species, alongside a positive same-species identity case. The inspected existing mapping test covers pooled species and a species-level identity, not this specific semantic distinction. Regenerate via the validated writer after tests pass; do not hand-edit this YAML, its generated page or an assumed overlay.

## Follow-up Checks

Run the targeted new seeder regression tests, schema and strict validation, then `just verify-corpus` and `just qc` for the regenerated change. Inspect the emitted record to ensure RI-11-013312 retains its NCBI identity while S. enterica is no longer an exact strain synonym or unqualified identity mapping. Retry live GTDB pages when available. Any later genome enrichment must preserve RefSeq suppression and require explicit deposit and source-chain evidence, not taxon or name matching.

## Additional Notes

Only NCBITaxon:1037256 is judged; no neighboring verdict was inherited. Eukaryota was not reopened. No YAML, inventory, source, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for the target. No paid research was used.
