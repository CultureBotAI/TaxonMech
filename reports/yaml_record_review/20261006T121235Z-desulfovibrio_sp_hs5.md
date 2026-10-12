# YAML Record Review: Desulfovibrio sp. HS5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/desulfovibrio_sp_hs5.yaml`
- Started UTC: 2026-10-06T12:10:36Z
- Finished UTC: 2026-10-06T12:12:35Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035115`, Desulfovibrio sp. HS5. It retains SPECIES rank, BACTERIA domain, parent unclassified Desulfovibrio (2593640), ten root-first ancestors, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one inline seed event. No habitat, phenotype, culture deposit, genome association or causal graph is asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/desulfovibrio_sp_hs5.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/desulfovibrio_sp_hs5.yaml --out /private/tmp/deshs5-validation.tsv`: passed, one file, zero errors; output TSV read and header-only.
- Structured comparisons of the complete backbone row, all ancestors, synonyms, seven other imported taxon tables, PATHS/scope, attestation and seed provenance passed.
- Exact-ID reads of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` found no target rows.
- Read live NCBI Taxonomy XML/Datasets, exact non-expanded Assembly/Nuccore results and complete marker metadata, references and feature qualifiers.
- `just validate-products` is inapplicable because no curator-added graph nodes are present. Taxonomy identifiers were checked at their authority; no undocumented focused term/reference validator was invented.
- Ignored-inclusive history content and filename searches found no separate target artifact. The inline seed event was checked; no separate history-file validator was applicable.
- Full-corpus reproduction, validation, tests, history, provenance/site checks and `just qc` were not run. Focused checks do not certify the whole corpus.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221892` and the complete scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31327` support the identifier and label. `data/taxa/PATHS.tsv:14379` resolves the slug, and `curation/seed_scope.tsv:322182` supports the seed rationale.

[NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035115&retmode=xml) confirms the name, rank, parent and genetic code. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035115) confirms the ten ancestor IDs: 1, 131567, 2, 3379134, 200940, 3031449, 213115, 194924, 872 and 2593640.

The NCBI lineage is carried, not reconciled with another authority. EXACT refers to this NCBI concept; SPECIES is its authority rank, not a claim of valid publication as a species binomial. HS5 alone does not establish organism identity.

## Evidence

One NAME assertion describes the 2026-09-13 taxonomy snapshot, not an experiment, culture or genome. The inline seed event at 2026-09-13T17:54:04Z agrees with the source and scope.

[HQ188933.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ188933.1) is a 1,465-base partial 16S rRNA sequence, not a genome. Its source feature explicitly names Desulfovibrio sp. HS5, strain HS5, taxon 1035115 and marine sediment as isolation source. Dinh, Enning, Kuever and Widdel submitted it on 2010-08-26. Its unpublished reference discusses Desulfopila corrodens and Desulfovibrio ferrophilus, but this does not rename HS5 or identify it as IS4/IS5. No DOI or PMID is attached to the sequence reference.

Enning's 2012 University of Bremen dissertation, [Bioelectrical corrosion of iron by lithotrophic sulfate-reducing bacteria](https://pure.mpg.de/rest/items/item_2484670_2/component/file_3253088/content), identifies HS5 as a hydrogen-scavenging isolate from iron-corroding enrichment (printed pages 36 and 60). Read every HS5-containing page and neighboring lactate-experiment context. Figures S1/S2 were visually checked, as was page 39. Figure S2 shows 0.98% metal loss for HS5 after 21 weeks, versus sterile controls at 0.96% and 0.77%. Page 39 separately reports HS5 with iron plus 20 mM lactate: average corrosion 0.0057 mm/year, with sulfide accumulation impeding corrosion; underlying data are not shown. These conditions must remain distinct. Neither result supports universal inability to affect corrosion or the strong direct-electron-uptake phenotype of IS4/IS5.

The dissertation association is plausible from the name and shared investigator but remains an inference: a case-insensitive scan of its searchable text found no HQ188933. An explicit isolate-to-accession bridge is needed before formal phenotype enrichment.

## Completeness

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the ID, full label, slug, Desulfovibrio-associated variants and bounded HS5 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.

All 79 initial candidate addresses were reconciled: ten complete TSV rows, twenty-four complete GOLD rows and forty-five other native JSONL rows. For the latter, inspected organism/taxon identities, source identifiers and all matching fields, with lossless factoring of that projection. The target name row was read in full; the other forty-four native candidates were not complete annotation reviews. They resolve to other organisms or numeric coincidences.

Expanded searches for HQ188933 and sequence UID 333973174 found no rows in those roots, including ignored and compressed files. All five SOURCE.json files were independently discovered and completely traversed for the initial identity pattern; none matched. Separate history content and filename searches found no target artifact.

The backbone has no synonyms or direct children; seven other imported taxon tables have no exact target row. Zero BacDive strains agrees with the pinned subtree, not a biological claim that HS5 was never isolated. The exact Assembly search returned zero items with a phrases-not-found warning, not proof of global genome absence.

Optional nomenclature, mapping, habitat, phenotype and graph slots may remain empty. iModulonDB is inapplicable to this identity-only YAML, which names no functional gene, regulator or expression module.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the retained claims. Optional enrichment is not a missing required representation.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote its status or append review history.

Later accepted enrichment belongs in maintained inventory handling and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`, with source-qualified identity tests. Keep the marker outside genome counts and require explicit source chains for culture or genome joins.

## Follow-up Checks

Before phenotype curation, verify the experimental isolate-to-accession bridge and retain each experiment's conditions, comparators and data limitations. A dissertation is not automatically a peer-reviewed article.

Run both focused validators for any accepted change, followed by corpus reproduction and full QC before release.

## Additional Notes

Short-label collisions include beta proteobacterium HS5/S24542 (240251), Rhodococcus sp. HS5 (393918), Helicobacter suis HS5 (710394; GCA_000187605.1/.2 and GCA_900196915.1), Pseudomonas monteilii HS5 (GCA_013522605.1), Escherichia coli HS5-1 (GCA_015731195.1) and Staphylococcus aureus HS5 (GCA_056621775.1). GOLD additionally contains distinct Pseudoalteromonas phage PSA-HS5/HS5 chains and a Hainan soil community.

Numeric matches include Staphylococcus haemolyticus CN1115 (SAMEA1035115; GCA/GCF_001239505.1; ATB ERZ3070575), Mycobacterium tuberculosis ERR1035115 (SAMEA3558648; ATB ERZ3502048), Bifidobacterium bifidum with SAMN41035115, Pseudomonas aeruginosa GCA_001035115.1, Campylobacter jejuni GCA_010351155.1, Klebsiella pneumoniae GCA_031035115.1/.2/.3, Enterocloster GCA_061035115.1, and Streptomyces fagopyri with genome length 10351151. GOLD's SAMN10351150-59 projects concern other communities. These matches do not establish a target strain-genome link.

The previously downloaded institutional thesis was re-read for HS5, including its title pages and all matching passages. PDFKit logged a generic CoreGraphics warning, but the relevant rendered pages and captions were legible.

Only this new report was written for this individual review. No record, source, code, page, history or older report was changed. Eukaryotic reviews were not reopened.
