# YAML Record Review: Burkholderia sp. BSNF3(9)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_bsnf3_9.yaml`
- Started UTC: 2026-10-10T08:14:40Z
- Finished UTC: 2026-10-10T08:19:33Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037608`, Burkholderia sp. BSNF3(9). This bacterial species-ranked placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes; generated YAML is not an edit surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_bsnf3_9.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_bsnf3_9.yaml --out /private/tmp/taxonmech-bsnf39-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identity, full lineage labels/ranks, synonyms, code, attestation, index uniqueness, scope reason, and seed-event wording. This is not a corpus reproduction check.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. These full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222823` agrees on ID, label, rank, parent, code, and the 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Each root-first lineage label/rank matches its individual backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037608&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037608), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037608) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding preserves this NCBI identity; it does not establish formal nomenclatural standing.

The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32459` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15377` uniquely resolves the ID/slug. `curation/seed_scope.tsv:323038` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The attestation counts one NCBI `NAME`, not one genome, strain, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide search `txid1037608[Organism:exp]` returned one UID, 345019053. Complete [GenBank annotation JF779802.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779802.1) explicitly joins organism, strain BSNF3(9), and taxon 1037608. This is a 450-base 16S rRNA fragment, incomplete at both ends, annotated from non-fertilized bulk soil in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `38e6e81a5e665ff55e37f031c838a93f3b14000ff5fc15452ee6417d043bb114`. It is not a genome assembly or deposit identifier. The annotation supplies no country, collection date, coordinates, or deposit qualifier. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz, Turpault, Van Scholl, Palin, and Frey-Klett's mineral-amendment study, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Freshly read complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1) confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The abstract describes a cohort of 80 isolates from beech ectomycorrhizosphere and bulk soil under control and calcium-amended conditions. It does not establish individual BSNF3(9) assays. No mineral-weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7613` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0166, GCA_010376085.1, SAMN12576336, PRJNA560345, and JAAGIH000000000.1. The numeric match is assembly name ASM1037608v1.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41463` describes Acinetobacter baumannii, taxid 470, strain AB35/isolate 21BC200034662, GCA_050714275.1, SAMN41037608, PRJNA514245, and DBIYQE000000000.1. The match is a BioSample substring; PMID 30286803 is not a target citation.
- Ten AllTheBacteria rows have Escherichia coli in the scientific-name and Sylph fields, available FASTA, and passing assembly/Sylph/HQ filters. Complete SeqKit, dataset, filter, and download fields were read. Each numeric match is within a run accession.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992495 | SAMEA9849593 | ERR10376080 | ERZ25462781 |
| 992496 | SAMEA9849595 | ERR10376081 | ERZ25462787 |
| 992497 | SAMEA9849596 | ERR10376082 | ERZ25462798 |
| 992498 | SAMEA9849599 | ERR10376083 | ERZ25462808 |
| 992630 | SAMEA9849808 | ERR10376084 | ERZ25463711 |
| 992631 | SAMEA9849810 | ERR10376086 | ERZ25463730 |
| 992632 | SAMEA9849814 | ERR10376088 | ERZ25576459 |
| 992682 | SAMEA9849885 | ERR10376085 | ERZ25464087 |
| 992684 | SAMEA9849887 | ERR10376087 | ERZ25464102 |
| 992685 | SAMEA9849888 | ERR10376089 | ERZ25464116 |

None of these rows establishes an additional target attestation, synonym, deposit, or genome. Sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns included numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. The expanded search added JF779802, the study DOI, and S003807171100280X. Both returned 15 lines: own backbone, scope, scientific name, and the 12 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/accession web searches yielded taxonomy-tree leads, not evidence for additional isolate-level claims.

Optional blanks do not establish a missing required representation, and no causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the taxonomy/name-only assertions. Unverified full text and isolate-specific assay results limit enrichment research without contradicting the record.

## Recommended Edits

None required. Preserve exact BSNF3(9)/JF779802 identity and the explicitly non-fertilized context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, obtain the primary article and isolate-level table and inspect BSNF3(9)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, candidate native rows, and the shared study's requested HAL metadata/abstract were inspected. Earlier attempts for the same study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried for this isolate. No login, payment, or full-text reading occurred.

YAML SHA-256: `4d250ea93221b4bd83869c8c1073b6ba81ca4789d65cc72e921dfde9c1ec0b2a`. The only repository write for this target is this new report. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were not modified by the review.
