# YAML Record Review: Sphingomonas sp. LT8CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_lt8cd.yaml`
- Started UTC: 2026-10-06T01:56:30Z
- Finished UTC: 2026-10-06T01:58:50Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034923`, Sphingomonas sp. LT8CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:196159` (unclassified Sphingomonas), with ten root-first lineage entries, code 11, `EXACT` grounding and `SEEDED` mapping status. It represents zero strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence, discussions and causal graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/sphingomonas_sp_lt8cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/sphingomonas_sp_lt8cd.yaml --out /private/tmp/lt8cd-validation.tsv`: exit 0, one file, zero ERROR rows. Read the complete header-only diagnostic TSV.
- Structured comparisons checked the full backbone and scope rows, every ancestor ID/label/rank, unique PATHS mapping, source attestation and inline seed-event description. The complete backbone scan found no children. These bounded comparisons do not prove full-corpus reproduction.
- Exact-ID scans of complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no match. Seven supplementary source inventories also returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore responses, and full marker metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These full gates are outside this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, modules or transcriptomic assertions. No LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221751` row agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034923&retmode=xml) confirms the exact ID and label, species rank, parent, bacterial division and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034923) confirms all ten ordered ancestor IDs, including root.

The root-first chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Sphingomonadales, Sphingomonadaceae, Sphingomonas and unclassified Sphingomonas. All ancestor labels and ranks agree with the pinned backbone and dedicated taxonomy evidence. The GenBank marker lineage ends at the genus; that abbreviated string does not justify changing the full parent chain.

`data/taxa/PATHS.tsv:14222` uniquely maps this ID to `sphingomonas_sp_lt8cd`; `curation/seed_scope.tsv:322053` supplies the one-source inclusion reason. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31154` identifies the same target. No alternate target name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled taxon does not establish formal nomenclatural validity or identity with another Sphingomonas isolate.

## Evidence

The source ID, label, snapshot, count of one and NAME unit agree with the inventory. The YAML asserts identity, carried lineage and provenance, not a genome, culture deposit, phenotype, medium or mechanism. A name-assertion count is not a biological strain or genome count.

Exact Nuccore search returned UID 333496490. Full [JF778659.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF778659.1) identify an 868-base 16S rRNA fragment, partial at both ends, with Sphingomonas sp. LT8CD, strain LT8CD, freshwater-lake isolation source and `taxon:1034923`. Its only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening statement was not independently tested. No culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID appears in this metadata. A bare strain name and marker do not establish a culture-deposit/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778659 within JF778652-JF778667. The range and matching authors support association with the Lake Tawani(P), East Antarctica study, not isolate-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034923[Organism:noexp]`. This bounded result does not prove genome absence under every other identifier or classification.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including hidden/compressed files and excluding `SOURCE.json` manifests. The ID digits, complete label and slug yielded 47 lines. Backbone and scope rows were read structurally; all twenty-five remaining native JSON objects and twenty full header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify LT8CD: backbone, scope and scientific name. The other 44 are numeric collisions with different taxa. Twenty-four objects concern six Escherichia coli isolates: six BV-BRC entries, six current GenBank entries, five replaced GenBank entries, six ATB rows and one GOLD project. The six isolate chains are:

| E. coli isolate | BV-BRC | GenBank versions inspected | BioSample | ATB analysis |
| --- | --- | --- | --- | --- |
| PNUSAE019654 | `562.36448` | `GCA_003754785.1`, `GCA_003754785.2` | `SAMN10349234` | `ERZ25499594` |
| PNUSAE018562 | `562.36449` | `GCA_003754845.1`, `GCA_003754845.2` | `SAMN10349238` | `ERZ9092513` |
| PNUSAE018564 | `562.36451` | `GCA_003754885.1` | `SAMN10349235` | `ERZ9092508` |
| PNUSAE017847 | `562.36477` | `GCA_003756605.1`, `GCA_003756605.2` | `SAMN10349232` | `ERZ9092510` |
| PNUSAE018561 | `562.36545` | `GCA_003763185.1`, `GCA_003763185.2` | `SAMN10349237` | `ERZ9092511` |
| PNUSAE018563 | `562.36558` | `GCA_003764545.1`, `GCA_003764545.2` | `SAMN10349236` | `ERZ9092509` |

The six genome chains identify taxon 562 and project `PRJNA218110`. GOLD project `Gp0386999` identifies organism `Go0502722`, E. coli PNUSAE017847, sample `SAMN10349232`, and the same project. GOLD organism/project IDs are not genomes. None of these E. coli source chains can transfer to LT8CD.

The other twenty unrelated matches are:

- Six objects describe two Salmonella enterica isolates, each with BV-BRC, GenBank and ATB entries. PNUSAS059169 has `28901.5183`, `GCA_003754745.1`, `SAMN10349233` and `ERZ9092506`; PNUSAS058013 has `28901.5529`, `GCA_003766065.1`, `SAMN10349231` and `ERZ9092505`. Both GenBank entries identify taxon 28901 and project `PRJNA230403`.
- GenBank `GCA_027160335.1` identifies Staphylococcus aureus 9-018-035, taxon 1280, sample `SAMEA1034923`, project `PRJNA514245`. The corresponding ATB sample row names Staphylococcus aureus, analysis `ERZ3070325`, run `ERR086130`.
- BV-BRC `1773.20371` identifies Mycobacterium tuberculosis ERR1034923, taxon 1773. Its ATB run row names Mycobacterium tuberculosis sample `SAMEA3558456`, analysis `ERZ3501224`.
- Ten ATB entries name Shigella sonnei samples `SAMEA110349230` through `SAMEA110349239`, with E. coli in the sylph species field. Neither classification identifies Sphingomonas.

Every candidate was read as a complete source-native object, not a search snippet. Shared sample/run/accession digits do not establish identity. Even a genuine shared BioSample would not prove assembly equivalence; project and organism IDs remain separate from genome IDs.

A second ignored-inclusive scan of the same ten roots for `JF778659|LT[ -]?8[ -]?CD` returned only the same three target rows. Exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. No eligible missing strain/deposit/genome association was established within these bounded retained sources. Zero represented strains describes inventory coverage, not the biological absence of LT8CD.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence representation was established. Optional study-context enrichment is not required for a taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, provenance, source-count semantics and seeded status are supported. The marker and unrelated source chains do not establish an omitted LT8CD genome or culture deposit.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. Any study-context extension needs a maintained input and target-specific evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. A future deposit/genome candidate needs complete source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy on a pinned-dump refresh. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
