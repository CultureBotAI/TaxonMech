# YAML Record Review: Janthinobacterium sp. LT1CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/janthinobacterium_sp_lt1cd.yaml`
- Started UTC: 2026-10-06T01:40:53Z
- Finished UTC: 2026-10-06T01:43:37Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034919`, Janthinobacterium sp. LT1CD. It is a `SPECIES` in `BACTERIA`, parent `NCBITaxon:2610881` (unclassified Janthinobacterium), with ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. It carries zero represented strains, one NCBITAXON NAME assertion from snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence, discussions and causal graphs are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/janthinobacterium_sp_lt1cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/janthinobacterium_sp_lt1cd.yaml --out /private/tmp/lt1cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the full header-only diagnostic TSV.
- Structured comparisons checked the complete backbone and scope rows, all ancestor IDs/labels/ranks, unique PATHS mapping, source attestation and inline seed-event description. The backbone scan found no children. These bounded checks do not prove full-corpus reproduction.
- Complete exact-ID scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no matching row. Seven supplementary source inventories also had no exact target-ID match.
- Read complete live NCBI Taxonomy EFetch/Datasets responses, exact non-expanding Assembly/Nuccore search responses, and full marker metadata, references and feature annotations. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. These remain outside this bounded report-only review; inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable without curator-added graph grounding, genes, regulators, modules or transcriptomic assertions. No LPSN/GTDB assertion in this record required an authority-page check.

## Identity and Grounding

The complete `data/raw/ncbitaxon_taxa.tsv:221747` row matches the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034919&retmode=xml) confirms the ID, label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034919) confirms the target and all ten ordered ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Janthinobacterium and unclassified Janthinobacterium. All ancestor labels and ranks agree with the pinned backbone and dedicated taxonomy evidence. The marker's abbreviated GenBank taxonomy ends at the genus, which does not justify removing the final unclassified intermediate.

`data/taxa/PATHS.tsv:14217` uniquely maps this ID to `janthinobacterium_sp_lt1cd`; `curation/seed_scope.tsv:322049` supplies the one-source inclusion rule. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31150` names the same taxon. No additional target name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled entity does not establish a formally valid species name or equivalence with another Janthinobacterium isolate.

## Evidence

The YAML asserts NCBI identity, carried lineage and source provenance, not a phenotype, genome, culture deposit or mechanism. The source ID, label, snapshot, count of one and NAME unit match the retained inventory. A name assertion is not a biological strain or genome count.

Exact Nuccore search returned UID 333496483. The complete [JF778652.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF778652.1) describe an 865-base 16S rRNA fragment, partial at both ends, with strain LT1CD, freshwater-lake isolation source, and `taxon:1034919`. The only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening comment was not independently tested. No culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID appears in this metadata. The marker supports the named isolate, not a culture-deposit/genome linkage.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) explicitly includes JF778652 in its JF778652-JF778667 submission range. The range and matching authors support a Lake Tawani(P), East Antarctica study association. Community results and culture-method conditions do not establish LT1CD-specific physiology, growth optima or deposit identity. Supplements and figure images were not inspected.

Exact Assembly search returned zero with a phrase-not-found warning for `txid1034919[Organism:noexp]`. This bounded search does not prove that no genome exists under another identifier or classification.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including hidden/compressed files but excluding `SOURCE.json` manifests. The ID digits, complete label and slug returned 30 lines. Backbone and scope rows were read structurally; every remaining thirteen native JSON objects and fifteen complete header-aware AllTheBacteria rows was read. Reconciliation found no unread or truncated candidate.

Three rows identify LT1CD: backbone, scope and native scientific name. The other 27 are numeric collisions:

- Twelve objects describe three Escherichia coli isolates, each with BV-BRC, current GenBank, replaced GenBank and AllTheBacteria records. PNUSAE019348 has BV-BRC `562.36450`, `GCA_003754685.1`/`.2`, sample `SAMN10349196` and ATB analysis `ERZ9092479`; PNUSAE019349 has `562.36572`, `GCA_003765605.1`/`.2`, `SAMN10349193` and `ERZ9092476`; PNUSAE019347 has `562.36575`, `GCA_003765725.1`/`.2`, `SAMN10349199` and `ERZ9092481`. Their GenBank taxon is 562 and project is `PRJNA218110`, not LT1CD.
- GenBank `GCA_010349195.1` is Campylobacter jejuni PNUSAC014082, taxon 197, sample `SAMN13527250`, project `PRJNA292664`.
- GenBank `GCA_027162645.1` is Staphylococcus aureus 8-312-218, taxon 1280, sample `SAMEA1034919`, project `PRJNA514245`. Its ATB sample row is also Staphylococcus aureus, analysis `ERZ3070312`, run `ERR086077`.
- BV-BRC `1773.20361` names Mycobacterium tuberculosis ERR1034919, taxon 1773. The ATB row for that run names sample `SAMEA3558452`, analysis `ERZ3501208`, and Mycobacterium tuberculosis.
- Ten ATB rows name Shigella sonnei samples `SAMEA110349190` through `SAMEA110349199`; their sylph species field says Escherichia coli. Neither classification is Janthinobacterium.

All these native objects were inspected, not merely their search snippets. Shared digits within sample/run/accession strings do not establish taxon identity, and sharing a sample would not itself establish genome equivalence.

A second ignored-inclusive search of the same ten roots for `JF778652|LT[ -]?1[ -]?CD` returned only the same three target rows. Exact-ID scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target row. No eligible missing deposit/strain/genome association was established within these retained sources. Zero represented strains describes the inventory, not the biological nonexistence of LT1CD.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No consequential missing required synonym, mapping, nomenclature, evidence or graph representation was established. Optional study-context enrichment is not required for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, carried lineage, provenance, source-count semantics and seeded status are supported. None of the marker or numeric-collision evidence supplies a missing LT1CD genome/deposit link.

## Recommended Edits

None. Preserve the generated YAML and `SEEDED` status.

Future taxonomy corrections belong upstream at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization fixes belong in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope changes belong in `curation/seed_scope.tsv`. A study-context extension needs a maintained input and explicit target-specific evidence. Do not patch generated YAML or count a marker as a genome.

## Follow-up Checks

No blocking follow-up remains. New strain/deposit/genome candidates require complete source-native inspection and an explicit identity/linkage chain before authorized regeneration. Rerun focused schema/strict validation plus the documented reproduction, provenance, history and relevant full gates after any implementation. Recheck live taxonomy when refreshing the pinned dump. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, existing worktree. The other session was reported closed; no additional worktree was created. This review adds only this report; diagnostics are under `/private/tmp`. Records, source inventories, scope, history, lifecycle statuses, prior reports and generated pages were preserved. No commit, GitHub mutation, external contact or paid research occurred. Eukaryota was left untouched.
