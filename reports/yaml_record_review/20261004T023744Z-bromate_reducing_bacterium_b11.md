# YAML Record Review: bromate-reducing bacterium B11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_b11.yaml`
- Started UTC: 2026-10-04T02:36:58Z
- Finished UTC: 2026-10-04T02:37:44Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032706`, bromate-reducing bacterium B11. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacteria (49928), four lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. Functional wording belongs to the source label; the YAML contains no separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_b11.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_b11.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked every lineage entry, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded; its complete 28-row list did not resolve this unclassified B11 isolate.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220897` and `data/catalog/ncbi_names-0005.jsonl.gz:30203` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032706&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032706) confirm identity, exact label, species rank, parent, code 11, bacterial domain and all four root-first lineage IDs.

The short lineage is unresolved NCBI classification, not missing YAML ancestry. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the source placeholder; it does not establish formal nomenclatural validity or an experimentally verified reductase. A bare B11 designation is not an authority identifier.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13282` and `curation/seed_scope.tsv:321268` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [JF951742.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951742.1) is a 1,358-base partial 16S rRNA gene sequence. Source qualifiers specify genomic DNA, strain B11, taxon 1032706 and a biologically active carbon filter receiving dechlorinated tap water. Direct submission was on 2011-05-12. This marker is neither a genome assembly nor a biochemical assay.

The sequence links PMID 21943884 and DOI `10.1016/j.watres.2011.09.001`, consistent with the [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) inspected during this turn. PubMed lists JF951742. The citation link is verified; it is not a substitute for a B11-specific experimental row.

The [USDA ARS page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) supplied study context. The publisher article returned 403, leaving full isolate-specific tables unverified. Future functional enrichment must inspect B11's own experimental conditions and results, not transfer other isolates' or aggregate outcomes. The retained NAME-only YAML does not require a mechanism or treatment claim.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof that no genome exists elsewhere.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. The checked backbone has no descendants and BacDive has no target-classified strain. This supports the source-defined `strain_count: 0`, not a claim that B11 was never cultured.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and full-label separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 10 matching lines were inspected. Recursive SOURCE.json traversal included ignored files and found no matching entry. This was not a census of unrelated bare B11 designations.

These bounded surfaces supplied no additional exact-target source mapping, culture deposit, genome association or separate history reference. Optional nomenclature, strain and graph slots may remain empty. iModulonDB was not applicable because no covered dataset resolves the target; absence is not negative phenotype evidence. No broad alias-only genome absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the retained taxonomy-only record. Isolate-specific experimental detail remains unverified for future functional enrichment.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Separately authorized functional enrichment must inspect B11-specific experimental rows and conditions and use a maintained evidence input. Do not hand-edit generated YAML, infer a reductase from the name, or use bare B11 aliases as culture-deposit or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate a canary with `just seed-canary NCBITaxon:1032706 --force`, inspect its YAML and rerun both focused validators. Resolve experimental-table access before adding functional claims. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the current NAME-only claims.

## Additional Notes

SAMEA1032706 belongs to Streptococcus pneumoniae 147587 (1313), including GCA_001128185.1/.2, GCF_001128185.1 and ATB run ERR069775. GOLD, BV-BRC, GTDB and ATB matches retain that unrelated source identity. A BioSample number does not identify the NCBI taxon with the same digits, nor does it establish a genome relationship to B11.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
