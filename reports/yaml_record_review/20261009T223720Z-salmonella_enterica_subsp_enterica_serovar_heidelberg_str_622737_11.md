# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. 622737-11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_622737_11.yaml`
- Started UTC: 2026-10-09T22:35:26Z
- Finished UTC: 2026-10-09T22:37:20Z
- Verdict: needs curation

## Target

Entire generated `TaxonRecord` read. `NCBITaxon:1037259` denotes Heidelberg strain 622737-11, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:611`, genetic code 11, grounding `EXACT`, status `SEEDED`. Twelve ancestors, two synonyms, one mapping, three attestations and the complete seed event were inspected. Zero represented BacDive strains is a source-coverage count, not a statement that the organism is unsequenced. No nomenclature, nested strains, definition, functional evidence or graph is asserted.

HEAD freshly confirmed as `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `532f58902b5e08778a3a32005ebab47dcd4828ef340c83952ce992e81deeefb0`. Ignored-inclusive filename resolution found one target and no prior report for this stem. Relevant guidance, schema and implementation were confirmed unchanged before relying on prior complete reads.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_622737_11.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_622737_11.yaml --out /private/tmp/taxonmech-sal-heid-622737-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete own-row, ancestor, type/status, attestation, scope and slug comparisons passed. These bounded checks do not certify corpus reproduction or biological mapping semantics.
- NCBI EFetch, Datasets taxonomy and focused assembly identity reads succeeded. NCBI taxonomy and GTDB genome browser opens failed; complete native GTDB metadata was inspected, not a successful live GTDB page. PubMed bibliography and abstract were read, not full text or supplements.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222710`, native names `data/catalog/ncbi_names-0005.jsonl.gz:32312` and `:32313`, slug `data/taxa/PATHS.tsv:15247` and scope `curation/seed_scope.tsv:36182` agree. The NCBI synonym expands `str.` to `strain` without dropping 622737-11. The full backbone supports strain rank, parent, code, source set and the 2026-09-13 snapshot.

All twelve ancestors match the pinned chain in ID, label and rank: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; Salmonella enterica; Salmonella enterica subsp. enterica; serovar Heidelberg. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037259&retmode=xml) confirms the strain name, equivalent name, rank, parent, code and named ancestors; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037259) confirms `STRAIN` and all ancestor IDs including root. Complete backbone/status scans found no own child, type-material, merger or dropped-ID row.

The primary identifier is well grounded. The broader GTDB species name is not supported as an exact strain synonym, as described in M1.

## Evidence

`data/raw/gtdb_mappings.tsv:1476` supplies closeMatch to `GTDB:s__Salmonella_enterica`, count 21,527. The freshly read `data/raw/gtdb_species.tsv:163163` supports that count as volume of the entire source species. The schema at `src/taxonmech/schema/taxonmech.yaml:431` defines closeMatch as denoting the same species, while `genome_count` describes assemblies under the source taxon. The 21,527 count is not independently a count defect, but must not be interpreted as 21,527 genomes of 622737-11. No full native-cluster recount was performed.

Complete native GTDB row `data/catalog/gtdb_genomes-0011.jsonl.gz:45802` places `GB_GCA_000962145.1` under S. enterica while recording NCBI strain taxon 1037259, species taxon 28901 and strain identifier 622737-11 separately. It is not the representative genome. This is genome membership in a species cluster, not evidence of strain/species equivalence.

Complete GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:32956` identifies GCA_000962145.1, ASM96214v1, Contig, 164 contigs, 4,739,181 bases, WGS master AMMG00000000.1, sample SAMN01087984 and project PRJNA67433. Historical RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:7998` identifies GCF_000962145.1 as suppressed, non-live since 2020-08-31, with annotation-completeness/frameshift exclusions and source-specific project PRJNA224116. The [live GenBank report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000962145.1/dataset_report) confirms current status, strain, sample and PRJNA67433; the [RefSeq response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000962145.1/dataset_report) confirms suppression. Both live reports name PRJNA67433. The retained paired accession does not make RefSeq current.

The live BioSample identity view names sample CFSAN000339 and SRA sample SRS472081. These are sample metadata, not recognized culture-deposit evidence. They were not promoted to collection identifiers or used to infer genome equivalence.

Complete BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3421` supplies PATRIC 1037259.3, the RefSeq accession, strain, sample and project. GOLD's complete rows `data/gold/organisms.jsonl.gz:65796`, `projects.jsonl.gz:70220` and `analyses.jsonl.gz:51231` trace `Go0116199 -> Gp0120601 -> Ga0080721`, IMG 2630968990 and GCA_000962145.1. The analysis has no direct organism field, but explicitly names the project that identifies the organism. No culture-collection accession is supplied. `data/raw/gold_organisms.tsv:515` correctly counts one organism. These source-native associations do not establish a BacDive/deposit link.

GenBank's PMID 25479838 resolves to [Characterization and evolution of Salmonella CRISPR-Cas systems](https://pubmed.ncbi.nlm.nih.gov/25479838/), Microbiology, February 2015, DOI `10.1099/mic.0.000005`. The abstract describes comparative analysis of more than 600 Salmonella. It does not by itself establish a specific experimental phenotype for 622737-11; no such conclusion is asserted here or in the YAML. Full text and supplements were not reviewed.

NCBITAXON 1 NAME and GOLD 1 ORGANISM agree with the inventories. GTDB 21,527 GENOME is supported as source-species volume, with relation scope qualified by M1. Complete own-ID scans found no BacDive, LPSN, MediaDive, Madin or BactoTraits row, and no descendant contributes BacDive coverage. The full seed sentence matches the source set and scope. Fresh reads of `_seed_timestamp` and all three source-manifest extraction times support `2026-09-13T17:54:04Z`, the latest extraction timestamp. `SEEDED` correctly records generation, not human approval.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched the numeric identity, strain designation and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored, hidden and compressed files. All 24 matching rows were read completely or through lossless common-field/delta representations. Five SOURCE.json files and history filenames were separately checked; no own metadata or history match was found. The newly observed live sample label was not an additional local search key; conclusions remain bounded to the stated search.

Ten unrelated ATB hits at rows 171019, 171034, 171051, 171054, 171137, 171203, 171220, 171248, 171256 and 171280 concern Campylobacter jejuni, runs ERR10372590-99. Complete sample, assembly, checksum, availability and status fields were read. All retain available FASTAs and passing source filters, but matching run digits do not establish a 622737-11 association.

No eligible whole-deposit association or missing required representation was established. The known assembly does not justify fabricating a BacDive strain entry or joining a bare name as a culture accession. Optional nomenclature, definitions, functional evidence and causal graphs may remain empty. iModulonDB is inapplicable because the YAML asserts no gene, regulator, pathway, functional trait or transcriptomic dataset; a citation found through assembly metadata does not create such a claim. Absence conclusions are bounded to inspected roots, snapshots and responses.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Broader GTDB species is promoted to exact strain identity.** YAML lines 45-60 and 70-75 treat the entire S. enterica species as closeMatch to 622737-11 and derive an exact synonym and identity xref. This target's own native GTDB row separates strain taxon 1037259 from species taxon 28901, and NCBI independently establishes the narrower strain scope. Genome membership does not make a species name interchangeable with the strain name. This is one connected scope-inflation defect, not separate findings for each derived field; the species-wide count is not independently wrong.

Maintained owners: upstream kg-microbe's GTDB mapping, imported by `src/taxonmech/extract.py:501`, and the rank-unaware promotion in `src/taxonmech/seed.py:452` and `:468`. Freshly read seeder code treats closeMatch as identity and emits an exact synonym without checking target scope. Structural validators do not catch this semantic distinction. No blocker is assigned because the main NCBI identity and lineage remain correct.

## Recommended Edits

1. Correct or qualify the relation in the maintained upstream GTDB mapping, retain its original provenance, then re-extract. Check direction from the source taxon's side explicitly; do not blindly replace closeMatch with broadMatch, which assumes the record is broader than the source.
2. Make `src/taxonmech/seed.py` scope-aware before promoting a broader source species into a strain's exact synonyms or identity xrefs. Retain the actual NCBI strain synonym and defensible species-membership evidence, keeping source-species counts clearly scoped.
3. Add a STRAIN-to-broader-GTDB-species regression and a valid same-species positive case in `tests/test_seed.py`. Regenerate through the validated writer after tests pass; do not hand-edit YAML, pages or an assumed overlay.

## Follow-up Checks

Run targeted seeder tests, schema and strict validation, `just verify-corpus` and `just qc`. Inspect the emitted record to ensure 622737-11 retains its NCBI identity without the exact species-name synonym or unqualified identity mapping. Retry live GTDB authority access when available. Future genome enrichment must preserve RefSeq suppression and establish whole-deposit identity and an explicit source chain independently of shared names, samples or taxonomy.

## Additional Notes

Only NCBITaxon:1037259 is judged using its own complete YAML and source rows. No neighboring verdict was inherited; Eukaryota was not reopened. No YAML, source, inventory, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for the target. No paid research was used.
