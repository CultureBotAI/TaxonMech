# YAML Record Review: Burkholderia sp. MRhNF1(20)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf1_20.yaml`
- Started UTC: 2026-10-10T20:34:27Z
- Finished UTC: 2026-10-10T20:37:38Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF1(20), `NCBITaxon:1037627`. This species-ranked bacterial placeholder has parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf1_20.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf1_20.yaml --out /private/tmp/taxonmech-mrhnf120-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not prove full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222842` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Every root-first lineage label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037627&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037627), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037627) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies this NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32478` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15397` uniquely resolves ID/slug; `curation/seed_scope.tsv:323057` supplies the reason reproduced by the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037627[Organism:exp]` returned one UID, 345019061. Complete [GenBank annotation JF779810.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779810.1) explicitly joins organism, strain MRhNF1(20), and taxon 1037627. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `a5ab92eb99c8797775cc7bfe204d533c3ca6d7780ef423137301de6c4bd68c3a`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), inspected earlier this turn for the shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). Cohort-level findings do not establish individual MRhNF1(20) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 12 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0063.jsonl.gz:32567` describes uncultured Methanosarcinales archaeon, taxid 183757, isolate SRP062349_co2_27, GCA_964580555.1, PRJEB82487, SAMEA117375298, and CAZOKV000000000.1. Its total genome size 1037627 matches the target ID numerically, while ungapped size is 1036207; it has 270 contigs and 236 scaffolds.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:26423` describes uncultured archaeon, taxid 115547, isolate BILL18-1_SAMN07137075_MAG_00000056, GCA_982656595.1, PRJEB72923, SAMEA122230265, and CEXHTG000000000.1. Its ungapped size 1037627 supplies the numeric match; total size is 1038307, with 307 contigs and 293 scaffolds. The SAMN accession embedded in the isolate label is not substituted for the row's SAMEA BioSample.
- Both GenBank rows are scaffold-level archaeal metagenomic assemblies excluded from RefSeq for metagenomic origin, fragmentation, and undefined genus. Both report absent annotation provider/name and zero gene counts; this is not evidence of biological gene absence. Neither genome-length coincidence supplies a taxonomic association.
- Ten AllTheBacteria rows match run-accession substrings. Each has scientific/current/prior Sylph name E. coli, r0.2 dataset, available FASTA, and passing assembly/Sylph/HQ filters. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992456 | SAMEA9849539 | ERR10376270 | ERZ25462549 |
| 992458 | SAMEA9849542 | ERR10376272 | ERZ25462558 |
| 992552 | SAMEA9849664 | ERR10376273 | ERZ25463173 |
| 992554 | SAMEA9849666 | ERR10376271 | ERZ25463187 |
| 992565 | SAMEA9849677 | ERR10376278 | ERZ25463260 |
| 992566 | SAMEA9849678 | ERR10376274 | ERZ25463266 |
| 992567 | SAMEA9849679 | ERR10376276 | ERZ25463273 |
| 992737 | SAMEA9849940 | ERR10376275 | ERZ25464569 |
| 992739 | SAMEA9849942 | ERR10376277 | ERZ25464588 |
| 992740 | SAMEA9849943 | ERR10376279 | ERZ25464595 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779810, the study DOI, and S003807171100280X. Both returned 15 lines: own backbone, scope, scientific name, and 12 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/16S web query returned no results; that limited query does not establish biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRhNF1(20)/JF779810 identity and its non-fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRhNF1(20)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, and native candidate rows were inspected for this target. The shared study's requested HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `2a3faa0216bf00536b17a882caf86d0b9b2902fbdd4331c5184aa16cb2b4f016`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
