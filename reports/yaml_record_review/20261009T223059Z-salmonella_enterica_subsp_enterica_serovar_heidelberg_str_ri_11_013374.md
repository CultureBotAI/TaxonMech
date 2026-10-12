# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. RI-11-013374

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_ri_11_013374.yaml`
- Started UTC: 2026-10-09T22:29:25Z
- Finished UTC: 2026-10-09T22:30:59Z
- Verdict: needs curation

## Target

Entire generated `TaxonRecord` read. `NCBITaxon:1037257` denotes Heidelberg strain RI-11-013374, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:611`, genetic code 11, grounding `EXACT`, status `SEEDED`. All twelve ancestors, two synonyms, one mapping, three attestations and the seed event were inspected. No BacDive strain entries, nomenclature, definition, functional evidence or graph are asserted.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `77b39d23e98e7e8728ab55c6cf9b29a7ff1543393a94baad6a2d2ee0a540d602`. Ignored-inclusive filename resolution returned exactly one target and no prior report for this stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_ri_11_013374.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_ri_11_013374.yaml --out /private/tmp/taxonmech-sal-heid-ri3374-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: reused this turn's 17 valid records, zero invalid links after an empty fresh diff of history, schema and validator.
- Complete own-row, lineage, source, scope, status and slug comparisons passed. These bounded checks do not certify corpus reproduction or semantic mapping correctness.
- Public NCBI structured taxonomy and assembly reads succeeded. The taxonomy browser and GTDB genome page failed. Complete pinned native GTDB rows were inspected; this is not a successful live GTDB authority check. PubMed bibliography and abstract were read, not publication full text or supplements.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222708`, native names `data/catalog/ncbi_names-0005.jsonl.gz:32308` and `:32309`, slug `data/taxa/PATHS.tsv:15245` and scope `curation/seed_scope.tsv:36180` agree. The complete backbone row supports the label, strain rank, parent, code, NCBI equivalent name and 2026-09-13 snapshot.

All twelve ancestor IDs, labels and ranks match the pinned chain: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Salmonella; Salmonella enterica; Salmonella enterica subsp. enterica; serovar Heidelberg. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037257&retmode=xml) confirms the strain identity, equivalent name, parent, code and named lineage; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037257) confirms `STRAIN` and all ancestor IDs including root. Complete backbone/status scans found no own child, type-material, merged-ID or dropped row.

The NCBI synonym merely expands `str.` to `strain`. The separate GTDB synonym removes the strain and all intervening infraspecific scope; that unsupported promotion is Finding M1. The primary NCBI identifier itself remains correctly grounded.

## Evidence

`data/raw/gtdb_mappings.tsv:1474` supplies closeMatch to `GTDB:s__Salmonella_enterica` and count 21,527. The independently read species inventory `data/raw/gtdb_species.tsv:163163` supplies that same species-wide count; a fresh empty diff confirmed it unchanged. The schema defines `genome_count` as assemblies classified under the source taxon, not the number of genomes of this particular strain. No full native-cluster recount was performed.

Complete native GTDB row `data/catalog/gtdb_genomes-0000.jsonl.gz:42992` assigns `GB_GCA_000962125.1` to the S. enterica species cluster, with `ncbi_taxid=1037257`, `ncbi_species_taxid=28901`, strain identifier RI-11-013374 and representative flag false. It distinguishes the strain node from its species and therefore supports membership, not exact equivalence.

The complete GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:32955` identifies GCA_000962125.1, ASM96212v1, Contig, 744 contigs, 4,695,753 bases, WGS master AMME00000000.1, sample SAMN01087982 and project PRJNA67429. The historical RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:7997` identifies GCF_000962125.1 as suppressed, with non-live date 2020-07-29 and annotation-completeness/frameshift exclusions. Its source-specific project is PRJNA224116. The [live GenBank report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000962125.1/dataset_report) confirms the current GenBank assembly, strain, sample and PRJNA67429; the [RefSeq report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000962125.1/dataset_report) confirms suppression. Both live reports name PRJNA67429. A retained paired accession is not proof that RefSeq remains current.

`data/bvbrc/bvbrc-0000.jsonl.gz:3419` supplies PATRIC 1037257.3 and the RefSeq accession, sample, project and strain. GOLD's complete native rows `data/gold/organisms.jsonl.gz:65799`, `projects.jsonl.gz:70223` and `analyses.jsonl.gz:51229` trace `Go0116202 -> Gp0120604 -> Ga0080719`, IMG 2648501715 and GCA_000962125.1. The analysis's direct organism field is empty, but its explicit project identifies that organism. No culture-collection accession is provided. `data/raw/gold_organisms.tsv:513` correctly counts one organism assertion. These resources are source-native strain/genome leads, not evidence to invent a BacDive deposit or collection match.

The GenBank metadata's PMID 25479838 resolves to [Characterization and evolution of Salmonella CRISPR-Cas systems](https://pubmed.ncbi.nlm.nih.gov/25479838/), Microbiology, February 2015, DOI `10.1099/mic.0.000005`. Its abstract reports comparative sequence analysis across more than 600 Salmonella. The abstract alone does not establish a specific experimental function or phenotype for RI-11-013374, and this YAML asserts none. No publication conclusion was generalized to the strain, and no full-text verification was claimed.

NCBITAXON 1 NAME and GOLD 1 ORGANISM agree with complete inventory rows; GTDB 21,527 GENOME is source-species coverage, with the relationship scope qualified by M1. Complete own-ID scans found no BacDive, LPSN, MediaDive, Madin or BactoTraits row, and no descendant contributes BacDive coverage. Source set, snapshot and complete scope sentence match the seed event. This turn's inspected `_seed_timestamp` implementation and raw/ATB/StrainInfo manifests, freshly confirmed unchanged, support the latest extraction time `2026-09-13T17:54:04Z`. `SEEDED` does not claim human review.

## Completeness

Ignored-, hidden- and compression-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric identity, strain designation and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 28 matching rows were read completely or in lossless common-field/delta form. Five SOURCE.json files and history filenames were separately checked; no own metadata or history match was found.

The unrelated GenBank/GTDB pair is GCA_964646345.1, an uncultured Lachnospiraceae bacterium, taxon 297314, whose ungapped genome length is 1037257. Ten ATB rows at 171077, 171084, 171091, 171098, 171231, 171258, 171277, 171279, 171281 and 171287 concern Campylobacter jejuni runs ERR10372570-79, not this taxon. Nine pass all flags; row 171258 fails the CheckM2 contamination HQ filter while retaining an available FASTA. Row 1777098 is E. coli, run SRR11037257, analysis ERZ25715983, sample SAMN14055956, passing flags. Row 3183210 is C. jejuni, analysis ERZ27204904, sample SAMN46527448, run SRR32210226, passing flags; its checksum begins with the taxon digits. Full metadata for these false matches was inspected. None establishes an own ATB association.

Zero represented BacDive strains and absent nested genomes measure the supported deposit inventory, not absence of a sequenced organism. No eligible whole-deposit association or missing required nomenclature, definition, evidence graph or history record was established. iModulonDB is inapplicable to this YAML because it makes no gene, regulator, pathway, functional trait or transcriptomics assertion; a paper found through assembly metadata does not create one. Absence conclusions are bounded to inspected snapshots, roots and responses.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - GTDB species classification is incorrectly promoted to exact strain identity.** YAML lines 45-60 and 70-75 carry closeMatch from the entire S. enterica species to the strain and derive an exact species-name synonym and identity xref. The target's own native GTDB row distinguishes NCBI strain 1037257 from species 28901, while live NCBI and the pinned lineage independently identify the strain. Cluster membership does not make the species name an interchangeable strain name. This is one linked scope-inflation issue, not multiple findings for its derived fields. The source-species count itself is supported and is not a second count defect.

Maintained owners: upstream kg-microbe's GTDB mapping, imported through `src/taxonmech/extract.py:501`, and the identity/synonym promotion in `src/taxonmech/seed.py:452` and `:468`. Freshly inspected code treats every closeMatch as identity without checking target scope. The target's main identity remains correct, so this is major rather than a wrong-target blocker.

## Recommended Edits

1. Correct or qualify the imported relation upstream, retaining its original provenance. Do not blindly substitute broadMatch: the schema defines predicates from the source taxon's side, so source/target scope and direction must be checked. Re-extract supported changes through the maintained inventory workflow.
2. Make the seeder's identity promotion scope-aware so a broader species classification cannot supply an exact synonym or identity xref for a strain. Preserve the true NCBI synonym, explicit source classification and source-species count without implying strain equivalence.
3. Add a STRAIN-to-broader-GTDB-species regression case and a valid same-species positive case to `tests/test_seed.py`, then regenerate through the validated writer. The inspected species-level and pooling tests do not establish this case's correctness. Do not hand-edit the generated record, page or an assumed overlay.

## Follow-up Checks

Run targeted seeder regression tests, schema and strict validation, `just verify-corpus` and `just qc`. Inspect the emitted record to confirm that it still denotes RI-11-013374 and no longer presents the species name as an exact strain synonym. Retry the live GTDB authority page when available. Any later genome enrichment must preserve RefSeq suppression and prove deposit-level identity with explicit source chains rather than shared names or taxonomy.

## Additional Notes

This is an independent review of NCBITaxon:1037257 using its own complete YAML and sources, not an inherited neighboring verdict. Eukaryota was not reopened. No YAML, inventory, source, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for this target. No paid research was used.
