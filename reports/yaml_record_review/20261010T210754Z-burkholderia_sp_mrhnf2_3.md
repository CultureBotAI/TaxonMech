# YAML Record Review: Burkholderia sp. MRhNF2(3)

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_mrhnf2_3.yaml`
- Started UTC: 2026-10-10T21:05:32Z
- Finished UTC: 2026-10-10T21:07:54Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, Burkholderia sp. MRhNF2(3), `NCBITaxon:1037633`. It has species rank, bacterial domain, parent `NCBITaxon:2613784`, `EXACT` grounding, `SEEDED` status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/burkholderia_sp_mrhnf2_3.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/burkholderia_sp_mrhnf2_3.yaml --out /private/tmp/taxonmech-mrhnf23-20261010-validation.tsv --workers 1`: one file, zero errors; inspected TSV is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons passed for identity, complete lineage, synonyms, code, attestation, unique index entry, scope reason, and seed-event wording. They are not full-corpus reproduction checks.
- `just validate-products`: not applicable without curator-added graph nodes. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: full `just qc`, `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus checks were not run for this individual review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222848` agrees on identity, rank, parent, code, and snapshot 2026-09-13; synonym and retirement fields are empty. Every root-first ancestor label/rank agrees with its own backbone row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Betaproteobacteria 28216; Burkholderiales 80840; Burkholderiaceae 119060; Burkholderia 32008; unclassified Burkholderia 2613784.

Complete live [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037633&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037633), and all 74 parsed [Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037633) lines agree. EFetch omits root while Datasets includes it. Datasets omits assembly count rather than reporting zero. Exact grounding denotes the NCBI placeholder, not nomenclatural standing or a deposit.

The complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:32484` agrees. Exact scans found no own child, type-material, merged-ID, or dropped-ID row. `data/taxa/PATHS.tsv:15403` uniquely resolves ID/slug; `curation/seed_scope.tsv:323063` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

## Evidence

The attestation counts one NCBI `NAME`, not a strain, genome, study, or assay. Structured scans found no own rows in pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Optional blanks and zero inventoried strains match those inputs; they do not imply biological absence of an isolate.

Exact Nucleotide query `txid1037633[Organism:exp]` returned one UID, 345019059. Complete [GenBank annotation JF779808.1](https://www.ncbi.nlm.nih.gov/nuccore/JF779808.1) explicitly joins organism, strain MRhNF2(3), and taxon 1037633. The 450-base 16S rRNA marker is partial at both ends and annotated from non-fertilized ectomycorrhizosphere in a beech forest. Declared/actual length and A/C/G/T checks passed; lowercase sequence SHA-256 is `8333259d129a539ca7d9beb07b93342e466ba1c50cf0d68d07ddbb6f7eca2fad`. It is not a genome or deposit accession. No country, coordinates, collection-date, or deposit qualifier is supplied. The 5 April 2011 submission and INRA Champenoux address are not collection metadata. No alignment or phylogenetic reassessment was performed; the marker alone does not independently validate genus placement or merge separately named isolates.

The marker cites Uroz and colleagues, Soil Biology and Biochemistry 43(11):2275-2282 (2011). [HAL metadata and complete abstract](https://hal.science/hal-02916138v1), freshly read earlier this turn for MRhNF2(12)'s shared study, confirm DOI [10.1016/j.soilbio.2011.07.010](https://doi.org/10.1016/j.soilbio.2011.07.010). The 80-isolate cohort compares mineral-amended and control forest plots; cohort-level results do not establish MRhNF2(3)-specific assays. No weathering, iron-release, chitin-degradation, or plant-growth phenotype was inferred.

All 13 non-target native matches were read completely:

- `data/catalog/gtdb_genomes-0001.jsonl.gz:5952`: Bacillus subtilis B-23067, taxid/species 1423, RS_GCF_035810255.1/GCA_035810255.1, PRJNA224116, SAMN33940541, JARSKB000000000.1. GTDB and NCBI classifications agree on B. subtilis. The row carries `gtdb_representative=f` and `gtdb_type_species_of_genus=f`; these source fields were not converted into an independent nomenclatural judgement about B. subtilis. Contig/scaffold N50 1037633 supplies the match, not a taxon identifier.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7626`: Francisella tularensis subsp. holarctica, taxid 119857/species 263, strain 13T0019, GCA_010376335.1, PRJNA560345, SAMN12576323, JAAGHU000000000.1. Assembly name ASM1037633v1 supplies the match.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:12294`: Shigella flexneri, taxid/species 623, strain 1037633, GCA_015707595.1, PRJNA315192, SAMN16961272, AAXMBG000000000.1. Its numeric strain designation is not an identity bridge. Both GenBank assemblies above are excluded from RefSeq as part of a large multi-isolate project.
- Ten AllTheBacteria rows have scientific name/current and prior Sylph E. coli, dataset r0.2, available FASTA, passing assembly/Sylph/HQ filters, and true prior HQ membership. Their run-accession substrings supply the matches. Complete SeqKit, filter, and download fields were inspected.

| Physical row in `data/catalog/allthebacteria.tsv.xz` | Sample | Run | ENA analysis |
| --- | --- | --- | --- |
| 992470 | SAMEA9849556 | ERR10376330 | ERZ25462621 |
| 992472 | SAMEA9849558 | ERR10376334 | ERZ25462634 |
| 992473 | SAMEA9849559 | ERR10376332 | ERZ25462637 |
| 992474 | SAMEA9849560 | ERR10376336 | ERZ25462647 |
| 992581 | SAMEA9849693 | ERR10376338 | ERZ25463359 |
| 992610 | SAMEA9849742 | ERR10376333 | ERZ25463557 |
| 992611 | SAMEA9849745 | ERR10376331 | ERZ25576431 |
| 992612 | SAMEA9849746 | ERR10376337 | ERZ25463568 |
| 992613 | SAMEA9849747 | ERR10376335 | ERZ25463581 |
| 992753 | SAMEA9849956 | ERR10376339 | ERZ25464692 |

None establishes a target attestation, synonym, deposit, or genome. Strain, sample, project, run, marker, and assembly identities remain distinct.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns covered numeric ID, exact slug, organism/designation, punctuation/spacing/hyphen variants, and a boundary after the designation number. Expanded search added JF779808, the DOI, and S003807171100280X. Both returned the same 16 lines: own backbone, scope, scientific name, and 13 unrelated rows above. Ignored and compressed files were included. No additional target-linked assertion/history artifact was established on these bounded surfaces.

All five `SOURCE.json` files were independently enumerated and fully parsed without a match. Ignored-independent filename checks found the exact YAML and no pre-existing target report/history filename. Eukaryota contents were not opened. An exact organism/16S web search returned NCBI taxonomy tree leads; the dedicated primary taxon page was independently inspected, and snippets were not treated as new evidence.

No missing required representation was established. A causal graph is not required. iModulonDB is not applicable because the record asserts no gene function, regulator, expression module, or transcriptomics/stress-response dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Pinned and live sources support recorded taxonomy/name claims. Unchecked full text and isolate-specific assays constrain enrichment research without contradicting those claims.

## Recommended Edits

None required. Preserve MRhNF2(3)/JF779808.1 identity and non-fertilized ectomycorrhizosphere context in later enrichment. Partial markers remain outside genome counts. Do not hand-edit generated YAML, append history, or promote status. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Inspect the primary article and isolate-level table before adding MRhNF2(3)-specific functions. Require an explicit source chain for deposit/genome associations. After authorized maintained-input edits, rerun focused schema/strict/history checks, extraction dry run, seed canary, corpus reproduction, and full quality gates. Status promotion requires separate human sign-off.

## Additional Notes

Taxonomy responses, browser text, marker annotation, and native rows were inspected for this target. Shared HAL metadata/abstract were read earlier this turn. Earlier reviews encountered ScienceDirect 403 and an ISTEX institutional-login HTML redirect instead of PDF; those failed routes were not retried. No login, payment, or full-text reading occurred.

YAML SHA-256: `7b58361bdeb74069270029e18f8f0467a5a12839dc2a1f9b3e5fbba8492d4628`. Only this new report was written for the target; maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and worktrees were unchanged.
