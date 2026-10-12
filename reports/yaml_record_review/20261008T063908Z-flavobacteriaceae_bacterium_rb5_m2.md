# YAML Record Review: Flavobacteriaceae bacterium RB5-M2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacteriaceae_bacterium_rb5_m2.yaml`
- Started UTC: 2026-10-08T06:35:04Z
- Finished UTC: 2026-10-08T06:39:08Z
- Verdict: pass

## Target

The entire target YAML was read before judgment. This generated `TaxonRecord` denotes `NCBITaxon:1036330`, Flavobacteriaceae bacterium RB5-M2: rank SPECIES, domain BACTERIA, parent `NCBITaxon:61432` (unclassified Flavobacteriaceae), genetic code 11, EXACT grounding and SEEDED mapping status. It has zero linked BacDive strains, one NCBITAXON NAME assertion and one seed event dated 2026-09-13. It does not assert a formal species name, known genus or phenotype.

The identifier, label and slug resolved one record. No other YAML was reviewed under this report; Eukaryota remains outside this review.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/flavobacteriaceae_bacterium_rb5_m2.yaml`: passed, no issues found.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/flavobacteriaceae_bacterium_rb5_m2.yaml --out /private/tmp/frb5-strict.tsv`: passed, one file, zero ERROR files and zero ERROR rows. The inspected TSV contains only its header.
- Read-only structured comparisons verified the full target backbone row, all ancestor identifiers/labels/ranks/order, source attestation, scope row, path index and seed-event text. These bounded checks passed; they are not corpus reproduction.
- Live NCBI Taxonomy EFetch and Datasets responses were inspected for exact identity and lineage corroboration.
- Not checked: full-corpus `verify-corpus`, provenance/history gates, global QC, vendored-source checks, full tests, and rendering/site/docs builds. No focused substitute for a documented full-corpus-only gate is claimed.
- Graph-product checks and iModulonDB are not applicable: no graph, gene, regulator, functional or transcriptomic assertion is present. This is not negative biological evidence.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222334` agrees with the ID, name, rank, parent, code and 2026-09-13 snapshot. All synonym fields are empty, consistent with the record. The complete scientific-name entry at `data/catalog/ncbi_names-0005.jsonl.gz:31878` agrees. `data/taxa/PATHS.tsv:14841` maps the ID to the exact reviewed stem; `curation/seed_scope.tsv:322581` supports the scope reason and seed-event wording.

All eleven ancestor entries match the pinned backbone: root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), FCB group (1783270), Bacteroidota/Chlorobiota group (68336), Bacteroidota (976), Flavobacteriia (117743), Flavobacteriales (200644), Flavobacteriaceae (49546), and unclassified Flavobacteriaceae (61432). Numbers here are NCBI taxon IDs. Both intervening group nodes correctly carry CLADE rank; the terminal unclassified node has NO_RANK. Missing genus-level placement is not a YAML omission when the authority does not assign one.

The inspected [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036330&retmode=xml) agrees with name, species rank, bacterial division, parent 61432, genetic code 11 and all supplied ancestor labels/ranks. It has no `OtherNames` element. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036330) supplies the same root-inclusive ancestor order; EFetch omits root from `LineageEx`. EXACT appropriately describes grounding to this taxon, not a formally established species or strain phenotype.

## Evidence

The sole NCBITAXON attestation supports exactly one NAME assertion. Its count must not be interpreted as an organism or culture count.

The exact Nuccore query `txid1036330[Organism:noexp]` returned one UID, 334701519. Inspected top-level, source-feature and reference metadata for [JN019026.1](https://www.ncbi.nlm.nih.gov/nuccore/JN019026.1) describe a 1,476-base partial 16S rRNA sequence with organism Flavobacteriaceae bacterium RB5-M2, strain RB5-M2 and `taxon:1036330`. Those fields directly corroborate the accession/strain/taxon association. Sequence bases and non-source features were not inspected, and no alignment or independent species assignment was performed.

The accession's unpublished reference by Yu, W., is titled "Biological decoloring performance of Aeromonas hydrophila strain RB5-M". Its different taxonomic name and shorter strain designation do not establish equivalence to RB5-M2 or support transferring a dye-decolorization phenotype. The relationship between that study title and the submitted sequence remains unresolved. Because the YAML makes no study, phenotype or Aeromonas identity assertion, this does not demonstrate a record defect.

The direct submission is dated 25-MAY-2011, with sequence creation and update on 07-JUN-2011. The inspected source qualifiers contain organism, genomic-DNA molecular type, strain and taxon cross-reference, but no isolation-source, geographic-location or culture-deposit qualifier. The Shanghai institutional submission address is not isolation-location evidence.

Exact-name, RB5-M2, JN019026 and unpublished-title web searches did not establish an inspected exact-target primary publication. Taxonomy listings and broad dye-study results were treated only as leads; no findings depend on search snippets. Similar RB5 strain prefixes or references to a dye named RB5 are not identity bridges.

## Completeness

No consequential required-field gap was found. Complete exact-target scans of the seven pinned inventories for BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin traits and BactoTraits found no target row requiring an additional link or attestation. The full pinned backbone had no child row for this target. Exact scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no matching row. These statements are limited to the inspected inventories.

Compressed-aware `rg --no-ignore --hidden -z` searches included ignored/hidden content in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The search covered the exact taxon ID, slug and RB5-M2 variants, then expanded to JN019026 and the unpublished reference title. Both searches found only the backbone, scope and scientific-name rows cited above; all three were read as complete parsed TSV/JSON records. Five `SOURCE.json` metadata files were separately parsed, without an identity match; history filename/content searches found no target entry within these roots.

An ignored-independent filename inventory across `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no prior report for this stem before report creation. No claim of absence outside the searched roots is made.

The exact-taxonomy NCBI Assembly query returned zero results with a phrase-not-found warning; this is not proof of global genome absence. Zero linked BacDive strains does not mean no biological strain exists. Optional literature, culture links, traits, discussion and graphs may remain empty because no supported missing assertion was demonstrated.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. The unpublished reference-title relationship is an unresolved external evidence limitation, not a demonstrated error in this taxonomy-only record.

## Recommended Edits

None. Do not assign a genus, rename the target as Aeromonas, add decolorization claims, infer an isolation country or create culture links from the inspected metadata. Preserve the SEEDED status.

A future confirmed taxonomy correction belongs first at NCBI and then in the maintained import workflow governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A seed transformation defect would belong in `src/taxonmech/seed.py` and tests; scope decisions belong in `curation/seed_scope.tsv`. Follow the documented refresh/seed workflow after an authorized upstream fix, rather than editing generated YAML directly. No such fix is established here.

## Follow-up Checks

No follow-up is required for this verdict. Future enrichment should first resolve the exact RB5-M2/JN019026.1 relationship to any claimed publication or experiment using inspected primary evidence. Shared strain prefixes and the unpublished title are insufficient.

After a separately authorized curation change, rerun both focused validators and the applicable documented corpus, provenance, history and generated-product gates. Those global gates remain unrun in this review.

## Additional Notes

This sequential individual review used the local review skill and field checklist. No record, source, curation event, review status, history entry or generated product was changed; there was no paid research, outreach, GitHub mutation, source refresh or regeneration. Existing worktrees and Eukaryota records were left untouched.

The record SHA-256 remained `6696b40a8826e1a9cc02983e0e605ae0912a419dd619a1124b1ddce49c26e1a1` through the pre-report check. This is the sole new review report for this target.
