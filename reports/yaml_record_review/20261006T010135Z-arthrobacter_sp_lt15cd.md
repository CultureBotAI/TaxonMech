# YAML Record Review: Arthrobacter sp. LT15CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_lt15cd.yaml`
- Started UTC: 2026-10-06T00:59:09Z
- Finished UTC: 2026-10-06T01:01:35Z
- Verdict: pass

## Target

Reviewed the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034909`, label `Arthrobacter sp. LT15CD`, rank `SPECIES`, domain `BACTERIA`. It has parent `NCBITaxon:235627`, ten root-first lineage entries, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, and `strain_count: 0`. One NCBITAXON NAME attestation and one seed event are present. Synonyms, nomenclature, taxonomy mappings, listed strains, literature evidence, discussions, and causal graphs are not populated.

The target is the specific NCBI species-rank node bearing the LT15CD designation. It is not the whole genus Arthrobacter, a formally named species inferred from sequence similarity, or a culture-collection deposit. No record or lifecycle field was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/arthrobacter_sp_lt15cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/arthrobacter_sp_lt15cd.yaml --out /private/tmp/lt15cd-validation.tsv`: exit 0; one file scanned, zero errors. The complete TSV was read and contains only the header.
- Structured source comparisons read the full backbone row, all ancestors, seven source inventories, PATHS and scope entries, and embedded source/event provenance. All comparisons passed. This is not a substitute for byte-for-byte corpus reproduction.
- Every candidate address from the ignored-inclusive source search was reconciled to a complete native JSON or header-aware TSV read, with the backbone and scope handled by the structured comparison. Live NCBI Taxonomy EFetch, Datasets, sequence-index results, and complete GenBank metadata were inspected.
- Not checked: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, full history validation, provenance hashes, render drift, README statistics, publication budget, and vendored sync. These wider gates were not run for this report-only review. No invented focused gate is claimed.
- LPSN, GTDB, causal-edge, and iModulonDB checks are not applicable to claims in this record: it has no corresponding identifier, mapping, graph, gene-function, regulator, trait, or expression-module assertion.

## Identity and Grounding

The complete row at `data/raw/ncbitaxon_taxa.tsv:221737` agrees with the target on identifier, exact label, rank, parent, genetic code, and snapshot date. The native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31140` also identifies `NCBITaxon:1034909` as `Arthrobacter sp. LT15CD`.

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034909&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034909) independently return the same species-rank label and parent context. The full root-first chain is root 1, cellular organisms 131567, Bacteria 2, Bacillati 1783272, Actinomycetota 201174, Actinomycetes 1760, Micrococcales 85006, Micrococcaceae 1268, Arthrobacter 1663, and unclassified Arthrobacter 235627. Labels and ranks match the YAML; the root is included in the local backbone and Datasets response.

The `sp.` label does not invalidate the source's species-rank node or imply a formally described species. EXACT reflects the direct NCBI identity match, not a species-level taxonomic revision or evidence of a registered type strain. No alternative name is supplied by the inspected backbone or live taxonomy response. Exact-ID checks in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target row. The pinned backbone has no child taxon of this node. These absences are limited to the inspected sources.

## Evidence

The NCBITAXON attestation is one NAME from snapshot `2026-09-13`. `curation/seed_scope.tsv:322039` records the matching one-source attested rule; `data/taxa/PATHS.tsv:14207` uniquely maps the ID to this record stem. The embedded seed event at `2026-09-13T17:54:04Z` agrees with that rule and attestation. The count is not a number of cultured isolates, genomes, or observations.

An exact `txid1034909[Organism:noexp]` Nuccore query returned one hit, UID 333496496. The complete metadata, references, comments, and source/rRNA feature annotations of [JF778665.1](https://www.ncbi.nlm.nih.gov/nuccore/JF778665.1) were read; nucleotide bases were not reanalyzed. It is a 1,013-bp partial 16S rRNA sequence with source organism `Arthrobacter sp. LT15CD`, strain `LT15CD`, isolation source `freshwater lake`, and `taxon:1034909`. Its rRNA feature is partial at both ends. The record was created and updated on 25-May-2011 and carries a direct submission dated 23-Mar-2011 by Huang, Swain, Thacker, Ravindra, Andersen, and Bej. Its comment reports submitter-side Bellerophon chimera screening; that is not an independent check performed in this review.

The sequence metadata has no culture-collection qualifier, BioSample, BioProject, assembly link, DOI, PMID, collection date, or geographical qualifier. The listed PCR primers and bacterial taxonomy support a marker-sequence context, not a whole genome. GenBank's abbreviated taxonomy string omits the unclassified intermediate node; the explicit taxonomy API verifies that node, so this is not a conflicting lineage claim.

Primary literature was followed through the matching author set and accession range. [Huang et al. 2013, Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4), DOI `10.1186/2046-9063-9-4`, studies Lake Tawani(P)'s rock-water microbial community in East Antarctica. The inspected methods explicitly deposit JF778652-JF778667, a range containing JF778665. The matching authors and accession provide a study-level link beyond name similarity. The main text compares culture-dependent, clone-library, and pyrosequencing results; it does not establish a new formal species, registered deposit, or LT15CD-specific adaptation mechanism. No community percentage, growth optimum, nutrient-cycling role, or inferred phenotype was transferred to this taxon. Its [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC3740781/) identifies PMID 23369372 and PMCID PMC3740781. The primary article's main text was inspected through the publisher after PMC follow-up requests returned a browser challenge. Supplementary tables and figure images were not independently inspected.

## Completeness

The record is complete enough for its supported seeded scope. No matches were found in the full exact-taxon reads of the BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin, and BactoTraits inventories. Combined with the absence of descendant taxa, this supports the recorded BacDive-based `strain_count: 0`. It does not deny the existence of the submitted LT15CD isolate.

Ignored-inclusive, hidden-inclusive, compressed-content searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding `SOURCE.json` provenance descriptors. Searching the taxon number, full label, slug, and LT15CD designation returned 18 lines. Three were the target backbone, scope, and scientific-name rows; all remaining candidates were numeric substring collisions, rejected after reading their full native rows. An additional accession/spacing-variant screen for JF778665 and LT15CD returned only the same three target identity rows. Thus no additional target-linked culture, assembly, strain-overlay, or sequence assertion was established in these roots, including ignored files.

The exact-taxon Assembly index query returned zero with a phrase-not-found warning. That bounded result does not prove absence of every possible genome under other classifications. No verified culture-deposit assertion was found to enable a strain-to-genome join. A bare designation, accession fragment, or shared taxon is insufficient under the repository's identity rules.

Separate ignored-inclusive report/history searching by ID, label, and slug, plus a filesystem search for this report stem, found no previous target report before this one was created. Optional literature evidence is not required for a seeded record, and there is no unsupported causal graph to complete. No consequential missing required representation was identified.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The entire record matches its pinned and live NCBI identity, lineage, source count, and seed provenance. No unsupported nomenclature, mapping, deposit, genome, trait, habitat-generalization, or mechanistic claim is present. The marker sequence and primary study add bounded context without requiring an unsupported enrichment.

## Recommended Edits

None required. Keep the generated identity and lifecycle as they are. Do not manually add JF778665.1 as a genome assembly or convert LT15CD into a culture-collection identifier.

If later evidence supports enrichment, route primary NCBI changes through the pinned inputs and `scripts/extract_source_inventory.py`; change harmonization behavior in `src/taxonmech/seed.py` with tests, and use `curation/seed_scope.tsv` only for a genuine scope change. Any future literature annotation needs a supported maintained input consumed by the seeder. Regenerate through `scripts/seed_from_sources.py`, not direct edits to generated YAML. No such changes were made here.

## Follow-up Checks

No unresolved blocker remains. Before adding a strain or genome link, obtain an explicit registered culture-deposit assertion or other source relationship permitted by the repository's join rules and verify it at the source. Before asserting isolate-specific growth or physiology, inspect the corresponding experimental evidence; the community study and partial marker do not establish those claims by themselves.

After any authorized maintained-input change, rerun the single-record schema and strict commands, the relevant extractor/seeder tests, and the documented seed dry-run/canary workflow. Run `just verify-corpus`, `just qc`, and applicable history/provenance/render gates before accepting regenerated products. This review itself does not justify a REVIEWED lifecycle promotion.

## Additional Notes

The rejected numeric candidates were `Mycobacterium tuberculosis ERR1034909` in BV-BRC and ATB; `Caldilineaceae bacterium` isolate CHLO-7 with BioSample SAMN31034909 and assembly GCA_048499075.1; `Staphylococcus aureus` with BioSample SAMEA1034909, GenBank assembly GCA_027163165.1, and ATB analysis ERZ3070303; and Shigella sonnei ATB samples SAMEA110349090-SAMEA110349099. Their full scientific names, taxon IDs where supplied, samples, and sequence identifiers are unrelated to LT15CD. No annotation, culture, publication, or quality flag was transferred from them.

The review ran in the existing worktree on `codex/record-review-extensimonas-20261003` at `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The previously read guidance and implementation had no tracked changes at this baseline; the local checklist, relevant seeder/schema sections, curation rules, and history guidance were reread. The read-only review contract supersedes curation scaffolding instructions: no history entry, outbound contact, or GitHub mutation was made.

Only this new report was written in the repository. The validation TSV is under `/private/tmp`. Target YAML, Eukaryota, inventories, scope, prior reports, generated pages, and history were left unchanged; there was no regeneration, commit, or lifecycle promotion.
