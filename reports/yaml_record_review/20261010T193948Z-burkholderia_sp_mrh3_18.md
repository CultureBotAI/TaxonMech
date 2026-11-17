# YAML Record Review: Burkholderia sp. MRh3(18)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrh3_18.yaml`
- Started UTC: 2026-10-10T19:36:51Z
- Finished UTC: 2026-10-10T19:39:48Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for Burkholderia sp. MRh3(18), `NCBITaxon:1037613`. It is a species-ranked bacterial placeholder, parent `NCBITaxon:2613784`, with `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrh3_18.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrh3_18.yaml --out /private/tmp/taxonmech-mrh318-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured checks passed for identity, complete lineage labels/ranks, synonyms, code, attestation, index, scope, and event wording. This is not full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222828` agrees on ID, label, rank, parent, genetic code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank matches its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037613&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037613), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037613) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32464` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15383` uniquely resolves the ID/slug; `curation/seed_scope.tsv:323043` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried, not reconciled with other taxonomies.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037613[Organism:exp]` returned one UID, 345019036. Complete [GenBank annotation JF779785.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779785.1) explicitly joins organism, strain MRh3(18), and taxon 1037613. This 450-base 16S rRNA marker is partial at both ends and annotated from fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a9d9cbf9971ef4691935b65fc2a2e864cd52830f147913799b38c665adf9ddbb`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Complete requested [HAL metadata and abstract](https://hal.science/hal-02916138v1), inspected earlier this turn, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRh3(18) assay results. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 14 non-target native search matches were read completely:

- `data/catalog/ncbi_genbank-0009.jsonl.gz:7616` describes Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0082, GCA_010376135.1, PRJNA560345, SAMN12576333, and JAAGIE000000000.1. Its assembly name ASM1037613v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12412` describes Salmonella enterica subsp. enterica, taxid 59201/species 28901, strain 1037613, GCA_015710775.1, PRJNA248792, SAMN16972250, and AAXMCM000000000.1. A bare numeric strain designation is not this NCBI taxonomy ID.
- `data/catalog/ncbi_genbank-0046.jsonl.gz:41527` describes Acinetobacter baumannii, taxid 470, strain AB40/isolate 10RC190004595, GCA_050715555.1, SAMN41037613, PRJNA514245, and DBIYRQ000000000.1. The match is within BioSample; PMID 30286803 is not a target citation. All three GenBank rows are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows match run-accession substrings and have scientific name Escherichia coli. Nine are r0.2 assemblies with available FASTA, E. coli Sylph assignments, and passing assembly/Sylph/HQ filters. Row 992513 is rejected with ASM_LEN, no FASTA, and no ENA analysis.
- AllTheBacteria row 2549060 is Streptococcus pneumoniae in both scientific and Sylph fields, dataset Incr_release.202408, with available FASTA and passing filters. Its match is a checksum substring in `seqkit.v0.1_DLS_k0_51037613ade0ebb423a74a9ec40d2cde`, not a taxonomy identifier or MD5 assertion.

Complete dataset, filter, SeqKit, and download fields were inspected for all 11 AllTheBacteria rows:

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992513 | SAMEA9849617 | ERR10376130 | None |
| 992514 | SAMEA9849618 | ERR10376131 | ERZ25462903 |
| 992646 | SAMEA9849849 | ERR10376132 | ERZ25576504 |
| 992647 | SAMEA9849850 | ERR10376134 | ERZ25576512 |
| 992648 | SAMEA9849851 | ERR10376138 | ERZ25463837 |
| 992649 | SAMEA9849852 | ERR10376136 | ERZ25463848 |
| 992698 | SAMEA9849901 | ERR10376133 | ERZ25464225 |
| 992699 | SAMEA9849902 | ERR10376135 | ERZ25464233 |
| 992700 | SAMEA9849903 | ERR10376139 | ERZ25464241 |
| 992701 | SAMEA9849904 | ERR10376137 | ERZ25464250 |
| 2549060 | SAMN33606643 | SRR23726170 | ERZ26477894 |

None of the 14 unrelated rows establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, and assembly identifiers remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779785, the study DOI, and S003807171100280X. Both returned 17 lines: own backbone, scope, scientific name, and 14 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. Exact organism/accession web searches yielded taxonomy-tree leads, not additional isolate-specific evidence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live evidence supports the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRh3(18)/JF779785 identity and the fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRh3(18)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input changes, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier attempts for this study found ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `8da15f627993e953affb24aa6d2a46abd16ea9f53f40d8f754453e6e44de1631`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
