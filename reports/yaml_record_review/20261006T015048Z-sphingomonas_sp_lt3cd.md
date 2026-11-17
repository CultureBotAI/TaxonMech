# YAML Record Review: Sphingomonas sp. LT3CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_lt3cd.yaml`
- Started UTC: 2026-10-06T01:48:44Z
- Finished UTC: 2026-10-06T01:50:48Z
- Verdict: pass

## Target

Read the full 54-line generated `TaxonRecord` for `NCBITaxon:1034921`, Sphingomonas sp. LT3CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:196159` (unclassified Sphingomonas), with ten root-first ancestors, code 11, `EXACT` grounding and `SEEDED` mapping status. It represents zero strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z`. Synonyms, nomenclature, taxonomy mappings, strain entries, evidence, discussions and causal graphs are unpopulated optional slots.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/sphingomonas_sp_lt3cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/sphingomonas_sp_lt3cd.yaml --out /private/tmp/lt3cd-validation.tsv`: exit 0, one file, zero ERROR rows. Read the entire header-only diagnostic TSV.
- Structured comparisons checked the full backbone and scope rows, all ancestor IDs/labels/ranks, the unique PATHS mapping, attestation and inline seed-event description. No children were found in the complete backbone scan. These bounded checks are not full-corpus reproduction.
- Exact-ID scans of complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary source inventories also returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore search responses, and full nucleotide metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These are outside this bounded report-only review. Inline-event inspection is not a history-schema validation run.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, expression modules or transcriptomic assertions. No LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The full `data/raw/ncbitaxon_taxa.tsv:221749` row agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034921&retmode=xml) confirms the exact ID and label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034921) confirms all ten ancestor IDs, including root.

The root-first chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Sphingomonadales, Sphingomonadaceae, Sphingomonas and unclassified Sphingomonas. Ancestor labels and ranks agree with the backbone and dedicated taxonomy evidence. The marker's shorter GenBank taxonomy ends at the genus, not evidence for removing the final unclassified intermediate.

`data/taxa/PATHS.tsv:14220` uniquely maps the target to `sphingomonas_sp_lt3cd`; `curation/seed_scope.tsv:322051` supplies its one-source inclusion reason. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31152` identifies the same taxon. No alternative name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled entry does not prove formal nomenclatural validity or identity with another Sphingomonas isolate.

## Evidence

The source ID, label, snapshot, count of one and NAME unit match the retained inventory. The record asserts NCBI identity and carried lineage, not a culture deposit, genome, medium, phenotype or mechanism. Its name-assertion count is not a biological strain or genome count.

Exact Nuccore search returned UID 333496485. Full [JF778654.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF778654.1) identify a 971-base 16S rRNA fragment, partial at both ends, with Sphingomonas sp. LT3CD, strain LT3CD, freshwater-lake isolation source and `taxon:1034921`. The sole reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening comment was not independently tested. No culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID appears in this metadata. A partial marker and bare strain designation do not establish a deposited-culture/genome linkage.

[Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4), whose main text was inspected, includes JF778654 in JF778652-JF778667. That range and matching authors associate the marker with the Lake Tawani(P), East Antarctica study, not isolate-specific physiology or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034921[Organism:noexp]`. This bounded result does not prove genome absence under all other identifiers or classifications.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including hidden/compressed files and excluding `SOURCE.json` manifests. The ID digits, complete label and slug yielded 32 lines. Backbone and scope were read structurally; all nine remaining native JSON objects and twenty-one complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify LT3CD: backbone, scope and scientific name. The other 29 are numeric collisions with unrelated records:

- Four objects concern Escherichia coli PNUSAE017466: BV-BRC `562.36549`, current `GCA_003763965.2`, replaced `GCA_003763965.1`, and ATB analysis `ERZ9092490`. The genome metadata name taxon 562, sample `SAMN10349213` and project `PRJNA218110`. The ATB row retains scientific name E. coli but has `SYLPH_RESULTS_FAIL` and unknown current sylph species. Non-HQ status alone is not an exclusion rule; the missing LT3CD identity chain is decisive here.
- Two further E. coli GenBank/ATB pairs concern OH-18-20817-1 (`GCA_013046645.1`, `SAMN10349216`, `ERZ9092491`) and OH-18-20225-1-E (`GCA_013046695.1`, `SAMN10349211`, `ERZ9092489`). Both GenBank entries identify taxon 562 and project `PRJNA338676`.
- Salmonella enterica OH-18-20225-2-S has GenBank `GCA_005457925.1`, taxon 28901, sample `SAMN10349219`, project `PRJNA338674`, and ATB analysis `ERZ9092493`.
- Staphylococcus aureus 8-343-195 has GenBank `GCA_027161845.1`, taxon 1280, sample `SAMEA1034921`, project `PRJNA514245`. Its ATB sample row is Staphylococcus aureus, analysis `ERZ3070332`, run `ERR086107`.
- BV-BRC `1773.20362` identifies Mycobacterium tuberculosis ERR1034921, taxon 1773. The ATB row for that run names Mycobacterium tuberculosis sample `SAMEA3558454`, analysis `ERZ3501217`.
- Ten ATB rows name Shigella sonnei samples `SAMEA110349210` through `SAMEA110349219`, with E. coli in the sylph species field. Neither classification identifies Sphingomonas.
- Five more ATB rows match runs `SRR10349210` through `SRR10349214`: Salmonella enterica samples `SAMN13117272` and `SAMN13117278`, and Campylobacter jejuni samples `SAMN13117282`, `SAMN13117284` and `SAMN13117286`. The three Campylobacter rows have `SYLPH_RESULTS_FAIL`/unknown current sylph species, but none supplies an LT3CD identity link regardless of HQ status.

Every candidate source-native row was inspected. Digits shared across a sample, run and taxon ID are not identity evidence. Shared samples would not themselves establish assembly equivalence, and source quality flags cannot create a missing biological relationship.

A separate ignored-inclusive scan of the same ten roots for `JF778654|LT[ -]?3[ -]?CD` returned only the same three target rows. Exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. No eligible missing strain/deposit/genome association was established within these bounded retained sources. Zero represented strains describes inventory support, not biological absence of LT3CD.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, evidence or causal graph was established. Optional study-context enrichment is not required for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, provenance, source-count semantics and seeded status are supported. Neither the marker nor the unrelated catalog matches establishes an omitted LT3CD genome or culture deposit.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. Any study-context extension needs a maintained input and target-specific evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. A new deposit/genome candidate requires full source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation plus the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy on a pinned-dump refresh. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
