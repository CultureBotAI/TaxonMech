# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. 579082-8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_579082_8.yaml`
- Started UTC: 2026-10-09T22:43:25Z
- Finished UTC: 2026-10-09T22:46:42Z
- Verdict: needs curation

## Target

Entire generated `TaxonRecord` read. `NCBITaxon:1037261` denotes Heidelberg strain 579082-8, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:611`, genetic code 11, grounding `EXACT`, status `SEEDED`. All twelve ancestors, two synonyms, one mapping, three attestations and the seed event were inspected. Zero represented BacDive strains is a source-coverage count, not a claim that the organism lacks a genome. No nomenclature, nested strains, definition, functional evidence or graph is asserted.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `bfa3859ced8d5466317a565138990cf2b3e66009254cd613e4152ab510e7d12b`. Ignored-inclusive filename resolution found one target and no prior report for this stem. Relevant guidance, schema and implementation were confirmed unchanged before relying on prior complete reads.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_579082_8.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_579082_8.yaml --out /private/tmp/taxonmech-sal-heid-579082-20261009-validation.tsv --workers 1`: one file, zero errors; output read and header-only.
- `uv run --offline python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete own-row, ancestor, type/status, attestation, scope and slug comparisons passed. These checks do not certify full-corpus reproduction or biological mapping semantics.
- NCBI EFetch, Datasets taxonomy and focused assembly identity reads succeeded. NCBI taxonomy and GTDB genome browser opens failed. Complete native GTDB metadata was inspected; live GTDB browser access was not successful. PubMed bibliography and abstract were inspected, not full text or supplements.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222711`, native names `data/catalog/ncbi_names-0005.jsonl.gz:32314` and `:32315`, slug `data/taxa/PATHS.tsv:15249` and scope `curation/seed_scope.tsv:36183` agree. The NCBI equivalent name expands `str.` to `strain` while retaining 579082-8. The complete backbone supports strain rank, parent, genetic code, source set and the 2026-09-13 snapshot.

All twelve ancestors match the pinned chain in ID, label and rank: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; Salmonella enterica; Salmonella enterica subsp. enterica; serovar Heidelberg. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037261&retmode=xml) confirms strain identity, equivalent name, rank, parent, genetic code and named ancestors. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037261) confirms `STRAIN` and all ancestor IDs including root. Complete backbone/status scans found no own child, type-material, merger or dropped-ID row.

Primary NCBI identity is well grounded. The broader GTDB species name is not supported as an exact strain synonym; see M1.

## Evidence

`data/raw/gtdb_mappings.tsv:1477` supplies closeMatch to `GTDB:s__Salmonella_enterica`, count 21,527. The freshly read `data/raw/gtdb_species.tsv:163163` supports this as the entire source species' genome volume. The schema at `src/taxonmech/schema/taxonmech.yaml:431` defines closeMatch as denoting the same species, and `genome_count` counts assemblies under the source taxon. The number is not independently a count defect and must not be read as 21,527 genomes of 579082-8. No full native-cluster recount was performed.

Complete native GTDB row `data/catalog/gtdb_genomes-0002.jsonl.gz:21129` places `GB_GCA_000962175.1` in S. enterica while separately recording NCBI strain taxon 1037261, species taxon 28901 and strain identifier 579082-8. It is not the representative genome. Species-cluster membership does not establish strain/species equivalence.

Complete GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:32958` identifies GCA_000962175.1, ASM96217v1, Contig, 198 contigs, 4,739,267 bases, WGS master AMMH00000000.1, BioSample SAMN01087985 and project PRJNA67435. Historical RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:8000` identifies GCF_000962175.1 as suppressed, non-live since 2022-01-31, with source-specific project PRJNA224116. The GenBank exclusion field names annotation-completeness and frameshift concerns. The [live GenBank report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000962175.1/dataset_report) confirms current GenBank status, strain, sample and PRJNA67435; the [live RefSeq report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000962175.1/dataset_report) confirms suppression. Both live reports name PRJNA67435. Retaining a paired RefSeq accession is not evidence that RefSeq is current.

The live BioSample identity view names sample CFSAN000332 and SRA sample SRS472075. These are sample metadata, not recognized culture-deposit evidence. They were not promoted to collection identifiers or used to infer genome equivalence.

Complete BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3422` supplies PATRIC 1037261.3, the RefSeq accession, strain, sample and project. GOLD's complete rows `data/gold/organisms.jsonl.gz:65792`, `projects.jsonl.gz:70216` and `analyses.jsonl.gz:51232` trace `Go0116195 -> Gp0120597 -> Ga0080722`, IMG 2639762944 and GCA_000962175.1. The analysis has no direct organism field, but explicitly identifies the project that names the organism. No culture-collection accession is supplied. `data/raw/gold_organisms.tsv:516` correctly counts one organism. These source-native chains do not establish a BacDive/deposit link.

GenBank's PMID 25479838 resolves to [Characterization and evolution of Salmonella CRISPR-Cas systems](https://pubmed.ncbi.nlm.nih.gov/25479838/), Microbiology, February 2015, DOI `10.1099/mic.0.000005`. The freshly read abstract describes comparative analysis of more than 600 Salmonella. It does not by itself establish a specific experimental phenotype for 579082-8; no such conclusion is asserted here or in the YAML. Full text and supplements were not reviewed.

NCBITAXON 1 NAME and GOLD 1 ORGANISM agree with inspected inventories. GTDB 21,527 GENOME is supported as source-species volume, subject to M1's relation-scope finding. Complete own-ID inventory scans found no BacDive, LPSN, MediaDive, Madin or BactoTraits row, and no descendant contributes BacDive coverage. The entire seed sentence matches the source set and scope. `_seed_timestamp` and the three inspected source-manifest extraction times support `2026-09-13T17:54:04Z` as the latest extraction timestamp. `SEEDED` correctly describes generation rather than human approval.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched `1037261|579082[-_]8|salmonella_enterica_subsp_enterica_serovar_heidelberg_str_579082_8` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored, hidden and compressed files. All 24 matching rows were read completely or through lossless common-field/delta representations. Five SOURCE.json files and history filenames were separately checked; no own metadata or history match was found. Newly observed live sample labels were not additional local search keys; conclusions remain bounded to the stated search.

Ten unrelated ATB hits at rows 171044, 171090, 171106, 171115, 171160, 171168, 171181, 171212, 171271 and 171304 concern Campylobacter jejuni, runs ERR10372610-19. All complete rows retain available FASTAs and passing assembly pipelines. Nine pass all source filters. Row 171304, ERR10372617, retains failing contamination/Sylph high-quality filters and unknown previous/current Sylph species; it is not in the high-quality set. Those source statuses were preserved, but matching run digits establish no association with strain 579082-8.

No eligible whole-deposit association or missing required representation was established. The known assembly does not justify inventing a BacDive strain entry or treating a bare strain name as a collection accession. Optional nomenclature, definitions, functional evidence and graphs may remain empty. iModulonDB is inapplicable because this YAML asserts no gene, regulator, pathway, functional trait or transcriptomic dataset; a publication discovered through assembly metadata does not create such an assertion. Absence conclusions are limited to the inspected roots, snapshots and responses.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Broader GTDB species is promoted to exact strain identity.** YAML lines 45-60 and 70-75 treat the entire S. enterica species as closeMatch to 579082-8 and derive an exact synonym and identity xref. This target's own native GTDB row separates strain taxon 1037261 from species taxon 28901; NCBI independently establishes the narrower strain scope. Genome membership does not make the species name interchangeable with the strain name. This is one connected scope-inflation defect rather than separate findings for each derived field; the species-wide count is not independently wrong.

Maintained owners: upstream kg-microbe's GTDB mapping, imported by `src/taxonmech/extract.py:501`, and rank-unaware promotion in `src/taxonmech/seed.py:452` and `:468`. Freshly read seeder code treats closeMatch as identity and emits an exact synonym without checking target scope. Structural validation does not detect this biological distinction. No blocker is assigned because the primary NCBI identity and lineage remain correct.

## Recommended Edits

1. Correct or qualify the maintained upstream GTDB relation, preserve provenance, then re-extract. Check relation direction from the source taxon's side explicitly; do not blindly replace closeMatch with broadMatch, which assumes the record is broader than the source.
2. Make `src/taxonmech/seed.py` scope-aware before promoting a broader source species into a strain's exact synonyms or identity xrefs. Preserve the actual NCBI strain synonym and defensible species-membership evidence, with species-wide counts clearly scoped.
3. Add a STRAIN-to-broader-GTDB-species regression and a valid same-species positive case in `tests/test_seed.py`. Regenerate through the validated writer after tests pass; do not hand-edit YAML, pages or an assumed overlay.

## Follow-up Checks

Run targeted seeder tests, schema and strict validation, `just verify-corpus` and `just qc`. Inspect the emitted record to ensure 579082-8 retains its NCBI identity without an exact species-name synonym or unqualified identity mapping. Retry live GTDB authority access when available. Future genome enrichment must preserve RefSeq suppression and establish whole-deposit identity and an explicit source chain independently of shared names, samples or taxonomy.

## Additional Notes

Only NCBITaxon:1037261 is judged using its own complete YAML and source rows. No neighboring verdict was inherited; Eukaryota was not reopened. No YAML, source, inventory, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for the target. No paid research was used.
