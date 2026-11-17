# YAML Record Review: bromate-reducing bacterium B2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_b2.yaml`
- Started UTC: 2026-10-04T02:31:39Z
- Finished UTC: 2026-10-04T02:32:30Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032703`, bromate-reducing bacterium B2. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacteria (49928), four lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. The functional wording is a source label, not a separately curated reductase, phenotype, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_b2.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_b2.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked every lineage entry, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded; the complete 28-row list did not resolve this unclassified B2 isolate.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220894` and `data/catalog/ncbi_names-0005.jsonl.gz:30200` agree with the complete YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032703&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032703) confirm label, species rank, parent, code 11, bacterial domain and all four root-first lineage IDs.

The short lineage preserves unresolved NCBI classification. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the NCBI placeholder; it does not assert formal nomenclatural validity or experimentally establish every word of the label. A bare B2 designation is not an authority identifier.

## Evidence

The single NAME assertion and 2026-09-13 snapshot note match the source inventory. `data/taxa/PATHS.tsv:13279` and `curation/seed_scope.tsv:321265` confirm the identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without representing a human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [JF951739.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951739.1) is a 1,503-base partial 16S rRNA gene sequence. Its source feature specifies genomic DNA, strain B2, taxon 1032703, and a biologically active carbon filter receiving dechlorinated tap water. Direct submission was on 2011-05-12. It is a marker, not an assembly or functional assay.

The sequence's PMID 21943884 and DOI `10.1016/j.watres.2011.09.001` agree with inspected [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001). PubMed explicitly lists JF951739. The paper metadata and abstract were inspected during this review turn; the accession link is direct, but an abstract-level result is not a B2-specific experimental row.

The [USDA ARS page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) supplied study context, while the inspected ScienceDirect article returned 403. Full-table verification remains necessary before adding B2-specific biochemical or treatment claims. No mechanism, assay rate or respiratory inference is required for the retained NAME assertion.

Exact Assembly search returned zero with a phrase-not-found warning. That query is bounded evidence, not proof that no genome exists anywhere.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. The checked backbone has no descendants, and the BacDive inventory has no target-classified strain, supporting the source-defined `strain_count: 0`. This count does not assert an absence of cultured isolates in the cited research.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and full-label separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 11 matching lines were inspected. Recursive SOURCE.json traversal included ignored files and found no matching entry. This was not a census of all unrelated uses of the bare string B2.

Those bounded surfaces supplied no additional exact-target source mapping, culture deposit, genome association or separate history reference. Optional nomenclature, strain and graph slots may remain empty. iModulonDB was not applicable because no covered dataset resolves the target; that result is not negative phenotype evidence. No broad alias-only genome absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the current taxonomy-only record. Isolate-specific experimental detail remains unverified for any future functional enrichment.

## Recommended Edits

None required. Preserve source identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Separately authorized functional enrichment must inspect B2-specific experimental rows and conditions and use a maintained evidence input. Do not hand-edit generated YAML, infer a reductase from the source label, or treat a bare B2 alias as culture-deposit or genome identity.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate a canary with `just seed-canary NCBITaxon:1032703 --force`, inspect the output and rerun both focused validators. Resolve full-table access before functional enrichment. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the current NAME-only claims.

## Additional Notes

SAMEA1032703 identifies Streptococcus pneumoniae 430772 (1313), including GCA_001300655.1/.2, GCF_001300655.1 and ATB run ERR065956, not this NCBI taxon. Fidelibacterota bacterium XB_MAG970, assembly GCA_036228405.1, matches only because its reported genome length is 1032703. Neither numeric collision establishes identity or a genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
