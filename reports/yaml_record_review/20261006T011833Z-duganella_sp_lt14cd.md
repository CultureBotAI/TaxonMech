# YAML Record Review: Duganella sp. LT14CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_lt14cd.yaml`
- Started UTC: 2026-10-06T01:16:51Z
- Finished UTC: 2026-10-06T01:18:33Z
- Verdict: pass

## Target

Read all 56 lines of the generated `TaxonRecord` for `NCBITaxon:1034913`, Duganella sp. LT14CD. The record has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2636909` (unclassified Duganella), eleven root-first lineage entries, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. `strain_count` is zero. The sole source attestation is one NCBITAXON NAME at snapshot `2026-09-13`; the sole inline event is `SEEDED_FROM_SOURCES` at `2026-09-13T17:54:04Z`. Synonyms, nomenclature, mappings, strain entries, evidence objects, discussions and causal graph are unpopulated optional sections.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_lt14cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_lt14cd.yaml --out /private/tmp/lt14cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the entire header-only TSV.
- Structured source comparisons verified the target backbone row, every ancestor's ID/label/rank, unique PATHS mapping, exact scope row, source attestation and inline event description. No child row was found in the scanned backbone. This is a bounded comparison, not proof of corpus reproduction.
- Exact-ID scans of the complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary inventories returned no exact-ID target row.
- Read complete NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore query results, and complete nucleotide metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. No full gate is claimed for this report-only review; inspecting the inline event is not a history-schema run.
- `just validate-products` and iModulonDB are not applicable without curator-added graph nodes, gene/regulator/expression-module assertions or transcriptomic claims. No target LPSN or GTDB assertion required an authority-page check.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221741` agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034913&retmode=xml) confirms the ID, exact label, species rank, parent, bacterial division and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034913) confirms the same taxon and all ordered ancestor IDs including root.

Every ancestor label and rank agrees: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Burkholderiales; Oxalobacteraceae; Telluria group; Duganella; unclassified Duganella. Telluria group (`NCBITaxon:2895353`) is a no-rank carried ancestor, not an LT14CD synonym or an inferred alternate placement. GenBank abbreviates the lineage by omitting the final unclassified intermediate, which the dedicated taxonomy endpoints explicitly retain.

`data/taxa/PATHS.tsv:14211` uniquely assigns `duganella_sp_lt14cd` to the ID. `curation/seed_scope.tsv:322043` gives its one-source NCBI inclusion rule. The full native object at `data/catalog/ncbi_names-0005.jsonl.gz:31144` is the exact scientific-name entry; no alternate target name is supplied by the inspected taxonomy evidence. NCBI species rank for this isolate-labelled taxon is not proof of valid publication of a formal species name, or equivalence to nearby LT-labelled isolates.

## Evidence

The record asserts source-backed NCBI identity and lineage, not physiology or nomenclatural validity. Its source ID, label, snapshot, NAME unit and count of one agree with the inventory. Name-assertion counts are distinct from strain and genome counts. No unsupported medium, phenotype, mechanism, genome or type-strain claim is present.

The exact Nuccore query returned one UID, 333496495. Its [JF778664.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778664.1) is a 1,001-base partial 16S rRNA gene, partial at both ends, annotated with Duganella sp. LT14CD, strain LT14CD, freshwater-lake isolation source and `taxon:1034913`. The only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. A submitter Bellerophon-screening comment is not an independent check by this review. The inspected metadata contain no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID. This marker and bare strain name do not constitute a deposited-culture/genome relationship.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778664 in the submitted JF778652-JF778667 range. With the matching authors, it supports a Lake Tawani(P), East Antarctica study-context association. Community observations and study culture conditions are not LT14CD-specific phenotype or growth-optimum evidence. Supplements and figure images were not inspected.

Exact Assembly search returned zero, with a phrase-not-found warning for `txid1034913[Organism:noexp]`. This is a bounded query result, not proof that no genome exists under another identifier or taxon.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i`, including hidden and compressed files and excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searching `1034913`, the full label and slug found 18 lines. Backbone and scope were read structurally; all four other native JSON objects and twelve complete header-aware AllTheBacteria rows were inspected. Reconciliation found no unread or truncated candidate.

Three lines identify the target: backbone, scope and NCBI scientific name. Fifteen numeric collisions belong to other organisms:

- BV-BRC `1773.20364` is Mycobacterium tuberculosis ERR1034913, taxon 1773, without a GenBank accession in that object. The AllTheBacteria row for run `ERR1034913` is Mycobacterium tuberculosis sample `SAMEA3558446`, analysis `ERZ3501182`.
- GenBank `GCA_010349135.1` is Campylobacter jejuni PNUSAC014130, taxon 197, sample `SAMN13607575`, project `PRJNA239251`. The target digits occur in an assembly accession, not its taxon field.
- GenBank `GCA_027162485.1` is Staphylococcus aureus 8-316-046, taxon 1280, sample `SAMEA1034913`, project `PRJNA514245`. The AllTheBacteria row for that sample is Staphylococcus aureus, analysis `ERZ3070311`, run `ERR086085`.
- Ten AllTheBacteria rows are Shigella sonnei samples `SAMEA110349130` through `SAMEA110349139`.

A second ignored-inclusive search over the same ten roots for `JF778664|LT[ -]?14[ -]?CD` returned only the same three target lines. Exact-ID structured comparisons in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. Within these bounded sources, no eligible missing strain/deposit/genome association is supported. Zero represented strains does not deny the biological existence of the LT14CD isolate.

Ignored-inclusive ID/label/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report or history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence object was established. Optional literature-context enrichment is distinct from a defect in this taxonomy-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The asserted identity, lineage, provenance, count semantics and seeded status are supported. No unrelated numeric identifier or marker accession establishes a missing genome/deposit relationship.

## Recommended Edits

None. Do not change the generated YAML or promote `SEEDED` status.

Future primary taxonomy corrections belong at NCBI, then the pinned refresh in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`. Harmonization is owned by `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`; scope is owned by `curation/seed_scope.tsv`. Any optional study-context extension needs a maintained input and narrowly supported target relationship. Do not hand-edit generated records or count this rRNA marker as a genome.

## Follow-up Checks

No blocking follow-up remains. Future deposit or assembly evidence must be verified against complete source-native objects and an explicit identity chain before an authorized regeneration. Rerun focused schema/strict validation and the documented corpus reproduction, provenance, history and relevant full gates after any implementation. Recheck taxonomy when refreshing the pinned snapshot. Sequence reclassification and independent chimera analysis were outside this review.

## Additional Notes

The review used branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, in the existing worktree. The other session was reported closed; no new worktree was created. This target review adds only this report, with validation diagnostics under `/private/tmp`. Existing reports, records, source inventories, scope, history, lifecycle status and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
