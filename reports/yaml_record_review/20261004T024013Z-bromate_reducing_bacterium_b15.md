# YAML Record Review: bromate-reducing bacterium B15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_b15.yaml`
- Started UTC: 2026-10-04T02:39:07Z
- Finished UTC: 2026-10-04T02:40:13Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032707`, bromate-reducing bacterium B15. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacteria (49928), four lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. Functional wording belongs to the source label; the YAML contains no separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_b15.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_b15.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked every lineage entry, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded; its complete 28-row list did not resolve this unclassified B15 isolate.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220898` and `data/catalog/ncbi_names-0005.jsonl.gz:30204` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032707&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032707) confirm identity, exact label, species rank, parent, code 11, bacterial domain and all four root-first lineage IDs.

The short lineage is unresolved NCBI classification, not missing YAML ancestry. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the source placeholder; it does not establish formal nomenclatural validity or experimentally verify every word in the label. A bare B15 designation is not an authority identifier.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13283` and `curation/seed_scope.tsv:321269` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [JF951743.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951743.1) is a 1,305-base partial 16S rRNA gene sequence. Source qualifiers specify genomic DNA, strain B15, taxon 1032707 and a biologically active carbon filter receiving dechlorinated tap water. Direct submission was on 2011-05-12. This marker is neither a genome assembly nor a biochemical assay.

The sequence cites Davidson and colleagues' 2011 Water Research paper, volume 45, issue 18, pages 6051-6062. Inspected [PubMed XML for PMID 21943884](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) confirm its title, authors and DOI `10.1016/j.watres.2011.09.001`. PubMed explicitly lists JF951743 among the deposited accessions.

The abstract describes 15 isolates from three sources and differing nitrate/perchlorate behavior, with no significant improvement in tested filter performance. These aggregate findings do not identify B15's own nitrate/perchlorate phenotype, rate, reductase, respiratory mechanism or treatment result. The inspected [USDA ARS publication page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) supplies study context but not the required isolate-specific tables. ScienceDirect returned 403; structured PubMed and Crossref retrieval succeeded. No search snippet was used as experimental proof.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query result does not prove that no genome exists elsewhere. No additional biological claim is needed to support the retained NAME assertion.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. The checked backbone has no descendants and BacDive has no target-classified strain. This supports the source-defined `strain_count: 0`, not a claim that B15 was never cultured.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and full-label separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 12 matching lines were inspected. Recursive SOURCE.json traversal included ignored files and found no matching entry. This was not a census of unrelated bare B15 designations.

These bounded surfaces supplied no additional exact-target source mapping, culture deposit, genome association or separate history reference. Optional nomenclature, strain and graph slots may remain empty. iModulonDB was not applicable because no covered dataset resolves the target; absence is not negative phenotype evidence. No broad alias-only genome absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the retained taxonomy-only record. Isolate-specific experimental detail remains unverified for future functional enrichment.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Separately authorized functional enrichment must inspect B15-specific experimental rows and conditions and use a maintained evidence input. Do not hand-edit generated YAML, infer a reductase from the label, or use bare B15 aliases as culture-deposit or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate a canary with `just seed-canary NCBITaxon:1032707 --force`, inspect its YAML and rerun both focused validators. Resolve experimental-table access before adding functional claims. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the current NAME-only claims.

## Additional Notes

SAMEA1032707 belongs to Streptococcus pneumoniae 487827 (1313), including GCA_001118505.1/.2, GCF_001118505.1 and ATB run ERR065971. Candidatus Saccharimonadia bacterium L1_Bin_Bin_167_sub_1 (2890869), assembly GCA_938050265.1, matches only through a genome length of 1032707. Neither numeric collision establishes target identity or a genome relationship.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
