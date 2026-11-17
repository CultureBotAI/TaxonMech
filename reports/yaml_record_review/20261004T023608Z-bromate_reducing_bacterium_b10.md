# YAML Record Review: bromate-reducing bacterium B10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_b10.yaml`
- Started UTC: 2026-10-04T02:35:08Z
- Finished UTC: 2026-10-04T02:36:08Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032705`, bromate-reducing bacterium B10. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacteria (49928), four lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. The functional source label is not represented as a separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_b10.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_b10.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded. The complete 28-row list did not resolve this unclassified B10 isolate.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220896` and `data/catalog/ncbi_names-0005.jsonl.gz:30202` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032705&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032705) confirm identity, exact label, species rank, parent, code 11, bacterial domain and all four root-first lineage IDs.

The short lineage preserves NCBI's unresolved classification, not omitted ancestry. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the authority placeholder; it does not assert formal nomenclatural validity or independently establish a biochemical mechanism. A bare B10 designation is not an authority identifier.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13281` and `curation/seed_scope.tsv:321267` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF951741.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951741.1) is a 1,416-base partial 16S rRNA gene sequence. Its source feature specifies genomic DNA, strain B10, taxon 1032705, and a biologically active carbon filter receiving dechlorinated tap water. Direct submission was on 2011-05-12. This marker is neither a genome assembly nor a functional assay.

The sequence links PMID 21943884 and DOI `10.1016/j.watres.2011.09.001`; the [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) inspected during this turn agree. PubMed lists JF951741. This establishes the citation link, not a B10-specific experimental result.

The [USDA ARS page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) supplied study context. The publisher article returned 403, leaving isolate-specific tables unverified. Any future mechanism or treatment claim must be supported by B10's own experimental rows and conditions; the retained NAME-only record does not make such a claim.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query result does not prove that no genome exists anywhere.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. The checked backbone has no descendants and the BacDive inventory has no target-classified strain. This supports the source-defined `strain_count: 0`, not a claim that B10 was never cultured.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and full-label separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 12 matching lines were inspected. Recursive SOURCE.json traversal included ignored files and found no matching entry. This was not a census of unrelated bare B10 designations.

Those bounded surfaces supplied no additional exact-target source mapping, culture deposit, genome association or separate history reference. Optional nomenclature, strain and graph slots may remain empty. iModulonDB was not applicable because no covered dataset resolves the target; absence is not negative phenotype evidence. No broad alias-only genome absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the retained taxonomy-only record. Isolate-specific experimental detail remains unverified for future functional enrichment.

## Recommended Edits

None required. Preserve source identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

Separately authorized functional enrichment must inspect B10-specific experimental rows and conditions and use a maintained evidence input. Do not hand-edit generated YAML, infer a reductase from the name, or use bare B10 aliases as culture-deposit or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate a canary with `just seed-canary NCBITaxon:1032705 --force`, inspect its YAML and rerun both focused validators. Resolve experimental-table access before functional enrichment. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects current NAME-only claims.

## Additional Notes

SAMEA1032705 belongs to Streptococcus pneumoniae R34-3109 (1313), not the target. Inspected source versions include GCA_001300675.1/.2/.3 and GCF_001300675.1/.2; BV-BRC carries the older RefSeq version while the native current catalog and GTDB carry .2. ATB run ERR068010 retains the same unrelated sample identity. These source versions were not collapsed or transferred to B10 merely because the BioSample digits match its taxon identifier.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
