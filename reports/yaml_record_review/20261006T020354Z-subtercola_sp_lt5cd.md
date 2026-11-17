# YAML Record Review: Subtercola sp. LT5CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/subtercola_sp_lt5cd.yaml`
- Started UTC: 2026-10-06T02:01:46Z
- Finished UTC: 2026-10-06T02:03:54Z
- Verdict: pass

## Target

Read the entire 53-line generated `TaxonRecord` for `NCBITaxon:1034924`, Subtercola sp. LT5CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:2648727` (unclassified Subtercola), with ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. It represents zero strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strains, evidence, discussions and causal graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/subtercola_sp_lt5cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/subtercola_sp_lt5cd.yaml --out /private/tmp/lt5cd-validation.tsv`: exit 0, one file, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons checked the full backbone and scope rows, every ancestor ID/label/rank, unique PATHS entry, source attestation and inline seed-event description. The complete backbone scan found no children. These bounded comparisons are not full-corpus reproduction.
- Exact-ID scans of complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary source inventories also returned no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore responses, and full marker metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These full gates are outside this bounded report-only review. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, modules or transcriptomic assertions. No LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221752` row agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034924&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034924) confirms all ten ordered ancestor IDs, including root.

The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Subtercola and unclassified Subtercola. Ancestor labels and ranks agree with the pinned backbone and dedicated taxonomy evidence. The marker's abbreviated GenBank taxonomy ends at the genus, which does not justify removing the final unclassified intermediate.

`data/taxa/PATHS.tsv:14223` uniquely maps the ID to `subtercola_sp_lt5cd`; `curation/seed_scope.tsv:322054` supplies its one-source inclusion reason. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31155` identifies the same taxon. No alternate target name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled entry does not establish formal nomenclatural validity or identity with another Subtercola isolate.

## Evidence

Source ID, label, snapshot, count of one and NAME unit match the inventory. The YAML asserts identity, carried lineage and provenance, not a genome, culture deposit, phenotype, medium or mechanism. A name-assertion count is not a biological strain or genome count.

Exact Nuccore search returned UID 333496487. Full [JF778656.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF778656.1) identify an 878-base 16S rRNA fragment, partial at both ends, with Subtercola sp. LT5CD, strain LT5CD, freshwater-lake isolation source and `taxon:1034924`. The sole reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening statement was not independently tested. No culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID appears in this metadata. A marker and bare strain designation do not establish a deposited-culture/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778656 within JF778652-JF778667. The range and matching authors support association with the Lake Tawani(P), East Antarctica study, not isolate-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034924[Organism:noexp]`. This bounded result does not prove genome absence under all other identifiers or classifications.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including hidden/compressed files and excluding `SOURCE.json` manifests. The ID digits, complete label and slug yielded 30 lines. Backbone and scope were read structurally; all thirteen remaining native JSON objects and fifteen complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify LT5CD: backbone, scope and scientific name. The other 27 are unrelated numeric matches:

- Twelve objects describe three Escherichia coli isolates, each with BV-BRC, current GenBank, replaced GenBank and ATB entries. PNUSAE018558 has BV-BRC `562.36517`, `GCA_003760215.1`/`.2`, sample `SAMN10349245` and ATB analysis `ERZ9092516`; PNUSAE018555 has `562.36581`, `GCA_003766105.1`/`.2`, `SAMN10349248` and `ERZ9092521`; PNUSAE018560 has `562.36597`, `GCA_003767465.1`/`.2`, `SAMN10349241` and `ERZ9092517`. All three genome chains identify taxon 562 and project `PRJNA218110`, not LT5CD.
- GenBank `GCA_010349245.1` identifies Campylobacter jejuni FSIS11926496, taxon 197, sample `SAMN13446691`, project `PRJNA287430`.
- GenBank `GCA_027162565.1` identifies Staphylococcus aureus 8-315-234, taxon 1280, sample `SAMEA1034924`, project `PRJNA514245`. Its ATB sample row names Staphylococcus aureus, analysis `ERZ3070330`, run `ERR086080`.
- BV-BRC `1773.20373` identifies Mycobacterium tuberculosis ERR1034924, taxon 1773. Its ATB run row names Mycobacterium tuberculosis sample `SAMEA3558457`, analysis `ERZ3501225`.
- Ten ATB rows identify Shigella sonnei samples `SAMEA110349240` through `SAMEA110349249`, with E. coli in the sylph species field. Neither classification identifies Subtercola.

All candidate source-native objects were inspected, not merely snippets. Shared sample/run/accession digits do not establish identity, and a genuine shared BioSample would not by itself establish assembly equivalence.

A second ignored-inclusive scan of the same ten roots for `JF778656|LT[ -]?5[ -]?CD` returned only the same three target rows. Exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Within these bounded retained sources, no eligible missing strain/deposit/genome association was established. Zero represented strains describes inventory coverage, not biological absence of the named isolate.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, evidence or causal graph was established. Optional study-context enrichment is not required for a taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, provenance, source-count semantics and seeded status are supported. The marker and unrelated catalog matches do not establish an omitted LT5CD genome or culture deposit.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. Any study-context extension needs a maintained input and target-specific evidence. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. A future deposit/genome candidate requires complete source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation plus the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy on a pinned-dump refresh. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
