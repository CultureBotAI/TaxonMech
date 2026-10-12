# YAML Record Review: Hymenobacter sp. LT10CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/hymenobacter_sp_lt10cd.yaml`
- Started UTC: 2026-10-06T01:31:04Z
- Finished UTC: 2026-10-06T01:33:10Z
- Verdict: pass

## Target

Read the complete 60-line generated `TaxonRecord` for `NCBITaxon:1034917`, Hymenobacter sp. LT10CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:2615202` (unclassified Hymenobacter), with twelve root-first lineage entries, code 11, `EXACT` grounding and `SEEDED` mapping status. It has zero represented strains, one NCBITAXON NAME attestation at snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event dated `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence, discussions and causal graph are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/hymenobacter_sp_lt10cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/hymenobacter_sp_lt10cd.yaml --out /private/tmp/lt10cd-validation.tsv`: exit 0, one file, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons checked the entire target backbone and scope rows, every ancestor ID/label/rank, unique PATHS entry, source attestation and inline seed-event description. No child row was returned by the backbone scan. These bounded checks are not proof of full corpus reproduction.
- Exact-ID scans of the complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no matching row. Seven supplementary inventories returned no exact target-ID match.
- Complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore query results, and full nucleotide metadata, references and feature annotations were read. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. No full gate is claimed by this report-only review. Inspecting the inline event is not a history-schema run.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, gene, regulator, expression-module or transcriptomic assertions. No target LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The full target row at `data/raw/ncbitaxon_taxa.tsv:221745` agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034917&retmode=xml) confirms exact ID/label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034917) confirms the target and all twelve ordered ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Cytophagia, Cytophagales, Hymenobacteraceae, Hymenobacter and unclassified Hymenobacter. Every label and rank agrees. FCB group (`NCBITaxon:1783270`) and Bacteroidota/Chlorobiota group (`NCBITaxon:68336`) are both carried `CLADE` entries. GenBank abbreviates the lineage by omitting these clades and the final unclassified intermediate; dedicated taxonomy responses explicitly confirm the full chain. No reparenting or inferred alternate classification is warranted.

`data/taxa/PATHS.tsv:14215` uniquely maps the ID to `hymenobacter_sp_lt10cd`; `curation/seed_scope.tsv:322047` gives the one-source NCBI inclusion rule. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31148` identifies this same taxon. No alternate target name is supplied by the inspected taxonomy evidence. NCBI species rank for this provisional isolate-labelled entity does not establish formal nomenclatural validity or equivalence to another LT-labelled isolate.

## Evidence

The record asserts source-backed NCBI identity and carried lineage. Source ID, label, snapshot, count of one and NAME unit agree with the inventory. A name assertion is not a biological strain or genome count. No phenotype, medium, ecological mechanism, type strain or genome claim appears in the YAML.

The exact Nuccore query returned UID 333496492. Its complete [JF778661.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778661.1) describes an 880-base partial 16S rRNA gene, partial at both ends, with Hymenobacter sp. LT10CD, strain LT10CD, freshwater-lake isolation source and `taxon:1034917` qualifiers. Its only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening statement was not independently tested here. The metadata contain no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID. This partial marker and bare strain name do not establish a culture-deposit/genome chain.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778661 within JF778652-JF778667. That range and matching authors support a Lake Tawani(P), East Antarctica study association. Community observations and study conditions do not establish LT10CD-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero, with a phrase-not-found warning for `txid1034917[Organism:noexp]`. This is a bounded query result, not proof of genome absence under all other identifiers or taxa.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i`, including hidden/compressed files and excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The ID digits, full label and slug search found 17 lines. Backbone and scope were read structurally; all three other native JSON objects and twelve complete header-aware AllTheBacteria rows were inspected. Reconciliation found no unread or truncated candidate.

Three rows identify LT10CD: backbone, scope and native scientific name. Fourteen numeric collisions belong to different organisms:

- BV-BRC `1773.20359` is Mycobacterium tuberculosis ERR1034917, taxon 1773, with no GenBank accession in that object. The AllTheBacteria row for run `ERR1034917` is Mycobacterium tuberculosis sample `SAMEA3558450`, analysis `ERZ3501199`.
- GenBank `GCA_027162925.1` is Staphylococcus aureus 8-295-228, taxon 1280, sample `SAMEA1034917`, project `PRJNA514245`. Its AllTheBacteria sample match is also Staphylococcus aureus, analysis `ERZ3070314`, run `ERR086063`.
- Ten AllTheBacteria rows are Shigella sonnei samples `SAMEA110349170` through `SAMEA110349179`.

A separate ignored-inclusive search across the same ten roots for `JF778661|LT[ -]?10[ -]?CD` returned only the same three target rows. Exact-ID structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target row. Within these bounded retained sources, no eligible missing strain/deposit/genome association is supported. Zero represented strains describes inventory evidence, not the nonexistence of the named isolate.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence object was established. Optional literature enrichment is not a prerequisite for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, carried lineage, source count, provenance and seeded status are supported. Neither a partial marker nor unrelated sample/run digits establish an LT10CD genome or deposit relationship.

## Recommended Edits

None. Keep the generated YAML and `SEEDED` status unchanged.

Future taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope policy belongs in `curation/seed_scope.tsv`. Any future study-context extension needs a maintained input and target-specific support. Do not hand-edit generated YAML or count the marker as a genome.

## Follow-up Checks

No blocking follow-up remains. New deposit or genome candidates require full source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full gates after implementation. Recheck live taxonomy when refreshing the pinned dump. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; tracked guidance and relevant code had no baseline diff. One existing worktree was listed, with the other session reported closed; no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
