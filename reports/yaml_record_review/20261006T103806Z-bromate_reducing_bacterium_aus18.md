# YAML Record Review: bromate-reducing bacterium AUS18

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_aus18.yaml`
- Started UTC: 2026-10-06T10:32:42Z
- Finished UTC: 2026-10-06T10:38:06Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1035070`, bromate-reducing bacterium AUS18. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacteria (49928), four root-first ancestors, genetic code 11, EXACT grounding, SEEDED status, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. The exact identifier and pinned path resolve the target despite the separate authority entry named bacterium AUS18. This is a taxonomic identity record, not a definition of the bromate-reducing functional guild.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_aus18.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_aus18.yaml --out /private/tmp/aus18-validation.tsv`: passed, one file and zero errors. Read the diagnostic TSV; it contains only the header.
- Structured comparisons checked the complete backbone row, all lineage entries, synonyms, seven other imported taxon tables, PATHS entry, scope row, source attestation and inline seed-event context. These comparisons passed; they do not replace corpus reproduction.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Live NCBI Taxonomy XML and Datasets checks resolved the target and the similarly named comparator separately. Exact, non-expanded Assembly and Nuccore queries and the returned nucleotide record were inspected.
- `just validate-products` was not run: there are no curator-added graph nodes. Authority checks cover the carried taxonomy identifiers; no separate focused term/reference validator was invented.
- No target-specific separate history record was found by ignored-inclusive content and filename checks. No history validator was run against a nonexistent target history file; the inline event was checked with the record.
- Full-corpus gates, including `just verify-corpus`, `just validate-all`, the full history suite, tests, provenance/site checks and `just qc`, were not run for this individual read-only review. This report is not release certification.

## Identity and Grounding

The pinned row at `data/raw/ncbitaxon_taxa.tsv:221872` and native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31308` agree with the YAML. `data/taxa/PATHS.tsv:14355` locks the identifier to the reviewed slug. The scope row at `curation/seed_scope.tsv:322163` carries the same label and one-source NCBI rationale.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035070&retmode=xml) confirms the label, species rank, parent 49928 and genetic code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035070) supplies the same root-first ancestor IDs: 1, 131567, 2 and 49928. The inventory supplies the corresponding labels and ranks. No unsupported genus or family placement is inferred, and SPECIES here is the authority rank, not a claim of valid publication of a binomial.

The authority still retains [NCBITaxon:1032697, bacterium AUS18](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032697&retmode=xml), with separate XML and Datasets responses. The two entries share a short designation and parent, but no inspected synonym, merge or explicit crosswalk establishes equivalence. This does not prove that the biological isolates differ; it prevents silently merging authority identities or moving their evidence.

## Evidence

The sole NCBITAXON attestation correctly counts one NAME from the 2026-09-13 snapshot. It is not a count of isolates, genomes or bromate experiments. The seed event at 2026-09-13T17:54:04Z agrees with the scope and source context. No retained citation, snippet, causal edge or genome-equivalence assertion is unsupported.

The exact Nuccore query returned one record, [JF951734.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951734.1). Its complete metadata, references and feature qualifiers identify a 1,382-base partial 16S rRNA sequence, strain AUS18, and source taxon 1035070. The source qualifier describes a biologically active carbon filter receiving dechlorinated tap water. This is useful independent identity context, not a genome assembly or a registered culture-collection deposit. Nucleotide bases were not used to perform a new phylogenetic placement.

The sequence explicitly cites [Davidson et al. 2011, PMID:21943884](https://pubmed.ncbi.nlm.nih.gov/21943884/), [DOI:10.1016/j.watres.2011.09.001](https://doi.org/10.1016/j.watres.2011.09.001). The inspected PubMed record confirms the bibliographic link and describes a study of 15 bromate-reducing isolates. The [USDA ARS publication page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) provides the authors' summary and technical abstract. These group-level summaries do not identify which five isolates lacked nitrate/perchlorate reduction, or establish an AUS18-specific enzymatic mechanism. No such result is transferred into this record.

The publisher page returned HTTP 403 when opened. Search-index excerpts were treated only as leads; the full article, Table 2 and supplements were not inspected. AUS18-specific kinetics, phylogenetic nearest neighbors, nitrate effects and proposed mechanisms therefore remain outside this review's evidence claims. This access limit does not undermine the checked identity-only YAML.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and AUS18/AUS 18/AUS-18 forms across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 71 matching source rows were read completely through structured TSV/JSON parsing, including losslessly factored common fields. The read-address set reconciles to all 71 discovered addresses. The broad expression also captures longer names and numeric substrings, which were excluded by source identity rather than treated as links.

A further ignored-inclusive search for JF951734, PMID 21943884 and the exact DOI returned no rows in those source/curation/history roots. The five SOURCE.json files, excluded from row discovery, were independently discovered without honoring ignore rules and traversed in full as JSON; no matching metadata values or keys were found. These are bounded local-snapshot observations, not claims of global biological absence.

There are no direct rows for this taxon in the seven other imported taxon tables and no children in the pinned backbone. Zero imported BacDive strains is therefore consistent with the record; it does not deny the existence of laboratory strain AUS18. No supported target culture deposit, strain-genome association or additional source mapping was found in the inspected catalogs. Bare AUS18 is not sufficient to create a culture-deposit join. The exact Assembly query returned zero items, with a phrases-not-found warning; this is only an exact-ID query result, not proof that no genome exists anywhere.

Optional nomenclature, synonyms, mappings, strains, evidence and causal-graph fields need not be manufactured. The newly verified marker and article are supplementary review context, not missing required genome links. iModulonDB is not applicable to this identity-only YAML: the functional wording is the NCBI name, with no asserted gene, regulator or expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained record. Biological equivalence with taxon 1032697 is unresolved and not asserted. The unavailable isolate-level article table limits potential enrichment, not the present identity verdict.

## Recommended Edits

None required. Preserve the separate authority IDs, carried lineage, generated ownership and SEEDED status.

Any future identity reconciliation requires an explicit authority correction or evidence-backed crosswalk. Relevant maintained owners are `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, with scope in `curation/seed_scope.tsv`; generated YAML is not the correction surface. A future marker association would need a supported source model and identity join, and must remain outside genome counts. Phenotype, isolation-source and medium curation belongs to the relevant sibling repositories.

## Follow-up Checks

For any later upstream correction, re-read the exact NCBI identity and source rows, preserve the 1032697/1035070 distinction unless explicitly resolved, rerun both focused validators, and then run corpus reproduction and the full QC gates before release. Future strain links additionally require explicit eligible deposit and genome/sample provenance, not substring matching.

Before adding strain-specific functional claims, inspect the original article's isolate-level tables and conditions. Do not infer AUS18 membership in the abstract's five-isolate subgroup, or a reductase mechanism, from the abstract.

## Additional Notes

Excluded source matches include:

- Pseudomonas aeruginosa AUS182, AUS183, AUS185 and AUS186: longer designations, taxon 287, with their own assembly and sample records.
- Staphylococcus haemolyticus 51-37: BioSample SAMEA1035070, paired GCA/GCF_001228405.1, BV-BRC 1283.111 and ATB ERZ3070512 are unrelated numeric matches.
- Phocaeicola vulgatus RTP21002st1_H3_RTP21002_201210: SAMN41035070 and paired GCA/GCF_040928445.1 do not denote this taxon.
- GOLD AUS-18, AUS-18_1 through AUS-18_4 and AUS-18a variants: wastewater-community projects/analyses, not explicit isolate links.
- GOLD SAMN10350700 through SAMN10350709: coculture or environmental/root metatranscriptome samples, not target taxon IDs.
- ATB ERR1035070: a Mycobacterium tuberculosis run, not an NCBI taxon.
- StrainInfo's Micromonas pusilla RCC 647 and Bathycoccus prasinos RCC 682: the substring in the designation Klaus 18 is not AUS18.

The existing report `reports/yaml_record_review/20261004T021751Z-bacterium_aus18.md` reviews the distinct 1032697 target. It was a disambiguation lead, not evidence replacing primary checks and not a prior review of the current target.

Only this new report is written. No generated record, existing report, source inventory, history entry, mapping status, GitHub object or eukaryotic review is changed.
