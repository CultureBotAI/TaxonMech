# YAML Record Review: Burkholderia sp. BSNF2(2)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf2_2.yaml`
- Started UTC: 2026-10-10T07:29:06Z
- Finished UTC: 2026-10-10T07:31:11Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037601`, Burkholderia sp. BSNF2(2). This bacterial species-ranked placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML is not a manual-edit surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf2_2.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf2_2.yaml --out /private/tmp/taxonmech-bsnf22-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index, scope reason, and exact seed-event wording; this is not corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, full-corpus `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222816` agrees on ID, label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037601&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037601), and all 74 parsed [browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037601) text lines agree. EFetch omits root while Datasets includes it. Assembly count is omitted by Datasets, not stated as zero. A marker strain qualifier does not conflict with a species-ranked placeholder or establish formal nomenclature/culture deposition.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32452` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15370` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323031` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event.

## Evidence

One NCBI `NAME` is counted, not a strain, genome, publication, or assay. No own row was found by structured scans of pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains does not mean no biological isolate.

Exact Nucleotide search `txid1037601[Organism:exp]` returned UID 345019041. Complete [GenBank annotation JF779790.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779790.1) explicitly links organism, strain BSNF2(2), and taxon 1037601. This 450-base 16S rRNA fragment is incomplete at both ends and annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `c1b32a341f16675994eaf1cd859cd408747ba6fb0d5a64978b2f949a887671e7`. It is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied; the 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), freshly inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The cohort abstract does not establish individual BSNF2(2) assays. Full article text and isolate-level results were not verified; no mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All three non-target native rows were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7610`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 14T0046, GCA_010376015.1, SAMN12576340, PRJNA560345, JAAGIL000000000.1. The numeric match is assembly name ASM1037601v1.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:45976`: Acinetobacter baumannii, taxid 470, AB27/isolate 10UC190068817, GCA_050822045.1, SAMN41037601, PRJNA514245, DBJBAW000000000.1. The match is within its BioSample; PMID 30286803 is not a target citation.
- `data/catalog/allthebacteria.tsv.xz:3207240`: scientific name Shigella sonnei, Sylph species Escherichia coli, sample SAMN47208228, run SRR32562517, ENA analysis ERZ27139792, 202505 incremental release. Assembly, Sylph, and HQ filters pass and FASTA is available, but the matching string occurs only in SeqKit sum `seqkit.v0.1_DLS_k0_762f8e3cd939e68b22fd1037601619bc`. This is neither a taxon identifier nor an MD5 identity claim.

None supports a target genome, culture deposit, synonym, or extra attestation.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered ID, exact slug, organism/designation, and punctuation/space/hyphen variants, bounding the terminal designation number. The expanded pass added JF779790, soilbio.2011.07.010, and S003807171100280X. Both searches returned six lines: own backbone, scope, scientific name, and the three unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found only the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Web searches produced taxonomy-tree leads and unrelated designation-string results; no snippets were used to support claims.

Unfilled optional slots are not missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live evidence supports the recorded taxonomy/name assertions. Unavailable full text and unverified isolate assays limit possible enrichment, not those assertions.

## Recommended Edits

None required. Preserve exact BSNF2(2)/JF779790 identity and the non-fertilized context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF2(2)-specific assay conditions/results. Require an explicit source chain for future deposit/genome links. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Full taxonomy responses, browser text, marker annotation, and candidate native rows were inspected for this target. Shared HAL metadata and abstract were inspected earlier this turn. Previous access attempts for the same paper encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried per isolate. No login, paid access, or full-text reading occurred.

YAML SHA-256: `75ede8b361c44a7fffcdb0bcc6d9bef5208c26e38ddf1018ba6ad11d1f872f1c`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
