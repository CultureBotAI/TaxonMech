# YAML Record Review: Burkholderia sp. BSNF3(12)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf3_12.yaml`
- Started UTC: 2026-10-10T07:41:26Z
- Finished UTC: 2026-10-10T07:45:06Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037604`, Burkholderia sp. BSNF3(12). This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf3_12.yaml`: passed.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf3_12.yaml --out /private/tmp/taxonmech-bsnf312-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured identity, complete lineage labels/ranks, synonyms, code, attestation, unique index, scope reason, and seed-event comparisons passed. These are not full corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222819` agrees on ID, label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037604&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037604), and all 74 parsed [browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037604) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count, not a statement of zero assemblies. The marker's strain qualifier is compatible with the species-ranked placeholder, not proof of formal nomenclature or a culture deposit.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32455` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15373` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323034` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping sections match those inputs. Zero inventoried strains does not imply no biological isolate.

Exact Nucleotide search `txid1037604[Organism:exp]` returned one UID, 345019052. Complete [GenBank annotation JF779801.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779801.1) explicitly joins organism, strain BSNF3(12), and taxon 1037604. It contains a 450-base 16S rRNA fragment incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `e3a10f9a2a94c48e6be7a3e4df972c45bd1a6c88728eb6734df8aec2178f6040`. It is not a genome assembly. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's 2011 mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282. A fresh complete read of requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) confirms DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort abstract does not establish BSNF3(12)-specific assays. Full article text and isolate-level results were not verified; no weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 11 non-target native rows were read completely. `data/catalog/ncbi_genbank-0046.jsonl.gz:41511` is Acinetobacter baumannii, taxid 470, AB17/isolate 10RC190003778, GCA_050715235.1, SAMN41037604, PRJNA514245, DBIYRE000000000.1. The number matches within its BioSample; PMID 30286803 is not a target citation.

The other ten rows are AllTheBacteria r0.2 entries matching run-accession substrings. All have available FASTA and passing assembly/Sylph/HQ filters; full filter, SeqKit, and download fields were inspected. These do not override their unrelated organism/sample identities.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Scientific name | Sample | Run | ENA analysis |
| --- | --- | --- | --- | --- |
| 415745 | Enterobacter hormaechei | SAMEA13299062 | ERR10376040 | ERZ25187132 |
| 415746 | Enterobacter hormaechei | SAMEA13299063 | ERR10376042 | ERZ25187138 |
| 415747 | Enterobacter hormaechei | SAMEA13299064 | ERR10376041 | ERZ25187147 |
| 415748 | Enterobacter hormaechei | SAMEA13299065 | ERR10376043 | ERZ25187158 |
| 415749 | Enterobacter hormaechei | SAMEA13299066 | ERR10376044 | ERZ25187169 |
| 415750 | Enterobacter hormaechei | SAMEA13299067 | ERR10376045 | ERZ25187178 |
| 415752 | Enterobacter hormaechei | SAMEA13299069 | ERR10376046 | ERZ25187199 |
| 415753 | Stutzerimonas stutzeri | SAMEA13299070 | ERR10376047 | ERZ25187208 |
| 415754 | Enterobacter cloacae | SAMEA13299071 | ERR10376048 | ERZ25187220 |
| 415756 | Enterobacter bugandensis | SAMEA13299073 | ERR10376049 | ERZ25187239 |

Sylph calls the E. hormaechei entries Enterobacter hormaechei_A; other species labels agree with those rows' scientific names. None of the 11 non-target rows establishes another target attestation, synonym, deposit, or genome.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, and space/punctuation/hyphen variants, bounding the final designation number. Expanded search added JF779801, soilbio.2011.07.010, and S003807171100280X. Both searches returned 14 lines: own backbone, scope, scientific name, and the 11 unrelated rows above. Ignored and compressed files were included; no further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism web search yielded taxonomy-tree leads; no snippet supported a scientific claim.

Optional blanks do not establish missing required representation, and no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected pinned and live sources support the taxonomy/name-only assertions. Unavailable full text and unverified isolate assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve exact BSNF3(12)/JF779801 identity and the non-fertilized context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF3(12)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, native candidates, and fresh HAL metadata/abstract were inspected for this review. Earlier attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried here. No login, payment, or full-text reading occurred.

YAML SHA-256: `134eac2e75cd2caeda600a21460f918a6a6d6c87c9e92e753966fc243d8112d1`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
