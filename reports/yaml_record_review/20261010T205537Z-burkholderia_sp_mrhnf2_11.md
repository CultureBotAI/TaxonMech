# YAML Record Review: Burkholderia sp. MRhNF2(11)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_11.yaml`
- Started UTC: 2026-10-10T20:50:43Z
- Finished UTC: 2026-10-10T20:55:37Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF2(11), `NCBITaxon:1037630`. It records a species-ranked bacterial placeholder, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained source inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_11.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_11.yaml --out /private/tmp/taxonmech-mrhnf211-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage labels/ranks, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They do not establish full-corpus reproduction.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222845` agrees on ID, label, rank, parent, code, and snapshot 2026-09-13. Exact/related/broad synonym and retirement fields are empty. Each root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037630&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037630), and all 74 parsed [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037630) text lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding identifies the NCBI placeholder, not formal nomenclatural standing or a culture deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32481` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15400` uniquely resolves ID/slug; `curation/seed_scope.tsv:323060` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event. NCBI lineage is carried without reconciling other taxonomies.

## Evidence

The single attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty optional strain/nomenclature/mapping slots match those inputs. Zero inventoried strains is not biological absence of an isolate.

Exact Nucleotide query `txid1037630[Organism:exp]` returned one UID, 345019060. Complete [GenBank annotation JF779809.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779809.1) explicitly joins organism, strain MRhNF2(11), and taxon 1037630. This 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `e2bf4fcf930def9c6e4f79199e62da9b2c584fdbe978ae432462223a6858de7a`. It is not a genome assembly or deposit accession. No country, collection date, coordinates, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reclassification was performed; a partial marker does not independently prove genus placement or identity between separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). Requested [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly inspected for this target, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The study concerns 80 isolates and cohort-level comparisons of mineral-amended and control forest plots. These findings do not establish individual MRhNF2(11) assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 11 non-target native matches were read completely:

- `data/catalog/ncbi_genbank-0014.jsonl.gz:12339` describes Escherichia coli, taxid/species 562, strain 1037630, GCA_015708935.1, PRJNA315192, SAMN16961321, and AAXMBV000000000.1. It is excluded from RefSeq as part of a large multi-isolate project. A numeric strain designation equal to the target taxid is not an identity bridge.
- Ten AllTheBacteria rows match run-accession substrings. All have scientific name E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Row 992604 has current/prior Sylph Hafnia paralvei, while the other nine have E. coli. This source-level naming discrepancy does not connect the row to Burkholderia. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992463 | SAMEA9849548 | ERR10376300 | ERZ25462585 |
| 992465 | SAMEA9849550 | ERR10376304 | ERZ25462593 |
| 992466 | SAMEA9849551 | ERR10376302 | ERZ25462597 |
| 992573 | SAMEA9849685 | ERR10376308 | ERZ25463311 |
| 992575 | SAMEA9849687 | ERR10376306 | ERZ25463319 |
| 992603 | SAMEA9849715 | ERR10376301 | ERZ25576425 |
| 992604 | SAMEA9849716 | ERR10376305 | ERZ25463514 |
| 992605 | SAMEA9849718 | ERR10376303 | ERZ25463521 |
| 992746 | SAMEA9849949 | ERR10376307 | ERZ25464638 |
| 992747 | SAMEA9849950 | ERR10376309 | ERZ25464649 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, space/punctuation/hyphen variants, and a boundary after the designation number. Expanded search added JF779809, the study DOI, and S003807171100280X. Both returned 14 lines: own backbone, scope, scientific name, and 11 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. A combined exact organism/16S web query returned no results; that limited query does not establish biological absence.

Optional blanks do not establish a missing required representation. No causal graph is required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support the recorded taxonomy/name assertions. Unverified full text and isolate-specific assays limit enrichment research without contradicting recorded claims.

## Recommended Edits

None required. Preserve MRhNF2(11)/JF779809.1 identity and its non-fertilized ectomycorrhizosphere context in later enrichment; partial markers remain outside genome counts. Do not hand-edit YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before functional enrichment, inspect the primary article and isolate-level table for MRhNF2(11)-specific conditions/results. Require an explicit source chain for future deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy responses, browser text, marker annotation, native candidate rows, and the shared study's requested HAL metadata/abstract were inspected for this target. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `1d234172b53fe487ff515012a2411c09d70b2ded9119f78807f1881a6a2043ff`. Only this new report was written for the target. The review did not modify maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, or existing worktrees.
