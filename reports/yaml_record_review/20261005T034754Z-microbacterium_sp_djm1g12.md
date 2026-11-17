# YAML Record Review: Microbacterium sp. DJM1G12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_djm1g12.yaml`
- Started UTC: 2026-10-05T03:42:49Z
- Finished UTC: 2026-10-05T03:47:54Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034220`, Microbacterium sp. DJM1G12. It is a `SPECIES`-rank bacterial isolate placeholder with parent `NCBITaxon:2609290`, `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11, and zero inventoried strains. The sole source attestation is NCBITAXON, with one `NAME` assertion from the 2026-09-13 snapshot. This is not a claim that DJM1G12 is a validly published named species.

The maintained inputs are the NCBI inventory in `data/raw/ncbitaxon_taxa.tsv` and `curation/seed_scope.tsv`; seeding behavior is owned by `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microbacterium_sp_djm1g12.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microbacterium_sp_djm1g12.yaml --out /private/tmp/microbacterium-djm1g12-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Bounded structured source comparison: passed identity, synonyms, all ten root-first ancestors, source attestation, scope, path index, and inline seed-event checks. These comparisons do not prove full-corpus reproduction.
- `just verify-corpus`: not run because it is a full-corpus check without a record selector. Its `--max-diffs` option limits diagnostics, not scope.
- `just validate-products`: not applicable; the record has no curator-added graph nodes or product-label claims.
- `just validate-history`: not run because the ignored-inclusive target search found no separate history artifact. The inline `SEEDED_FROM_SOURCES` event was inspected and agrees with the scope and source evidence. No history entry or status promotion was made.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221488` agrees with the record's identifier, exact label, species rank, parent, genetic code, snapshot date, and NCBI-only attestation. No synonyms are supplied in either representation. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30840` names this exact taxon and has an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034220&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034220) independently agree with the label, rank, and ancestry. EFetch also confirms parent 2609290 and genetic code 11. The browser page could not be opened through the web tool; the structured responses were inspected instead.

The full root-first chain is 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 201174 Actinomycetota, 1760 Actinomycetes, 85006 Micrococcales, 85023 Microbacteriaceae, 33882 Microbacterium, and 2609290 unclassified Microbacterium. Labels and ranks match the pinned backbone; the live Datasets ancestor list includes root, and EFetch supplies the remaining ancestor labels and ranks. No alternative placement is inferred.

## Evidence

The exact path-index entry at `data/taxa/PATHS.tsv:13950` and scope entry at `curation/seed_scope.tsv:321806` identify this record uniquely. The scope date and one-source reason agree with the inline seed event dated 2026-09-13T17:54:04Z. Full structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits mapped inventories found no exact target rows. The backbone has no children for this taxon. Exact scans of `ncbi_type_material.tsv`, `ncbi_merged_ids.tsv`, and `dropped.tsv` found no target entry.

The live exact-taxid Nuccore search returned one record, whose complete metadata, references, and features were inspected: [JF753473.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753473.1), a 657-base partial 16S rRNA gene sequence. Its organism is Microbacterium sp. DJM1G12, its strain qualifier is DJM1G12, and its taxon cross-reference is 1034220. Source qualifiers describe a Zea seed origin. This supports the isolate identity and a bounded isolation context, not a complete genome, culture-collection deposit, or inferred phenotype.

The sequence explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. The previously fetched [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) were reread during this review and agree on the authors, 2011 publication, and identifiers. Earlier inspection of the [publisher's relevant methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) established the culture-derived accession interval JF753401-JF753552, which contains JF753473. No fresh publisher fetch or inspection of the entire article is claimed here.

Community-level observations and results for other named isolates in that paper are not DJM1G12-specific evidence. Supplementary tables S3 and S4 were not inspected; no host genotype, medium, growth-promotion effect, metabolic phenotype, or transmission claim is inferred.

## Completeness

Ignored-inclusive, hidden-file-inclusive, compressed-file-aware searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only source-manifest `SOURCE.json` files. Boundary-aware identifier, label/slug, and designation searches returned exactly the backbone, native name, and scope contexts above. A secondary search for JF753473, its version, the whole PMID, and the DOI returned no matches in that same scope. Separate ignored-inclusive history and exact prior-report filename searches also returned no target artifact. These are bounded local-source results, not claims that no other evidence exists anywhere.

The exact-taxid Assembly query returned count zero, no IDs, and NCBI's phrase-not-found/no-items diagnostics. This is a bounded current query result, not proof of universal genome absence.

`strain_count: 0` is consistent with the BacDive-derived entry count implemented in `src/taxonmech/seed.py:483` through its count assignment at line 543. A GenBank strain qualifier does not create an inventoried BacDive strain or a CAFI-qualified culture deposit. Optional nomenclature, strain, genome, mapping, and causal-graph fields are appropriately absent for this identity seed. The missing optional marker citation is not itself a curation defect.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, status, source count/unit, and seeded provenance are supported at their represented scope. Uninspected supplementary rows limit optional enrichment but do not invalidate this record.

## Recommended Edits

None required. Do not hand-edit the generated YAML, reinterpret the marker as an assembly, manufacture a collection accession from DJM1G12, or promote `SEEDED` after this automated review.

Optional future enrichment should start from the exact supplementary row and an explicitly maintained evidence input. Any needed source representation belongs in the relevant inventory/overlay and `src/taxonmech/seed.py`, with tests before regeneration.

## Follow-up Checks

For optional enrichment, inspect the DJM1G12 row together with table headers and units; preserve the distinction between taxon, isolate, deposit, marker sequence, and genome. Repeat the focused schema and strict validators after any authorized maintained-input change. Full-corpus reproduction and broader repository gates belong to that later implementation workflow.

## Additional Notes

The original primary-search and sequence-query output handles were lost during a context transition. A process-state check showed no matching jobs remained; both read-only checks were repeated, their terminal results retained, and their evidence inspected before this verdict. Stored validator/source results and the remaining taxonomy process were also inspected to completion.

The prescribed spreadsheet dependency loader is not available in the enabled tools, and earlier supplement download attempts failed. No spreadsheet workaround, authoring, or unsupported row-level claim was made. iModulonDB is not applicable to this taxonomy-only record, which names no regulatory, gene, expression-module, or transcriptomic assertion.

Only this new report was added. No target YAML, source inventory, existing report, history, generated page, or review status was changed.

