# YAML Record Review: bromate-reducing bacterium B9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bromate_reducing_bacterium_b9.yaml`
- Started UTC: 2026-10-04T02:33:19Z
- Finished UTC: 2026-10-04T02:34:14Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032704`, bromate-reducing bacterium B9. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacteria (49928), four lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. Functional wording is a source label, not a separately curated phenotype, reductase, pathway, causal graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bromate_reducing_bacterium_b9.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bromate_reducing_bacterium_b9.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. The installed `culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets` command succeeded; its complete 28-row list did not resolve this unclassified B9 isolate.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate. Full isolate-specific experimental tables were not accessible through the inspected publisher page.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220895` and `data/catalog/ncbi_names-0005.jsonl.gz:30201` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032704&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032704) confirm identity, exact label, species rank, parent, bacterial domain, code 11 and all four root-first lineage IDs.

The short lineage retains NCBI's unresolved classification. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the authority placeholder; it does not assert formal nomenclatural validity or experimental verification of the functional label. A bare B9 designation is not an authority identifier.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13280` and `curation/seed_scope.tsv:321266` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one record, inspected as GenBank XML. [JF951740.1](https://www.ncbi.nlm.nih.gov/nuccore/JF951740.1) is a 1,502-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain B9, explicit taxon 1032704 and a biologically active carbon filter receiving dechlorinated tap water as isolation source. Direct submission was on 2011-05-12. The marker is not an assembly or functional assay.

The sequence's PMID 21943884 and DOI `10.1016/j.watres.2011.09.001` agree with [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21943884&retmode=xml) and [Crossref metadata](https://api.crossref.org/works/10.1016%2Fj.watres.2011.09.001) inspected during this turn. PubMed explicitly lists JF951740. This confirms the publication link, not a B9-specific mechanism or treatment result.

The [USDA ARS page](https://www.ars.usda.gov/research/publications/publication/?seqNo115=274528) was inspected for study context. The publisher article returned 403; isolate-specific tables remain unverified. Any future functional curation must distinguish B9's own experiments from other isolates or aggregate results. None is required to support the retained NAME-only assertion.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof of universal genome absence.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting the source-defined `strain_count: 0`, not absence of a cultured isolate in the study.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and full-label separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 10 matching lines were inspected. Recursive SOURCE.json traversal included ignored files and found no matching entry. This was not a census of unrelated bare B9 designations.

These bounded surfaces supplied no additional exact-target source mapping, culture deposit, genome association or separate history reference. Optional nomenclature, strain and graph slots may remain empty. iModulonDB was not applicable because no covered dataset resolves the target; this is not negative phenotype evidence. No broad alias-only genome absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found for the retained taxonomy-only record. Isolate-specific experimental detail remains unverified for future functional enrichment.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`.

For separately authorized functional enrichment, inspect B9-specific experimental rows and conditions and use a maintained evidence input. Do not hand-edit generated YAML, infer a reductase from the name, or treat a bare B9 alias as deposit or genome identity.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032704 --force`, inspect its YAML and rerun both focused validators. Resolve experimental-table access before adding functional claims. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved blocker affects the current NAME-only claims.

## Additional Notes

SAMEA1032704 belongs to Streptococcus pneumoniae R34-3174 (1313), including GCA_001117765.1/.2, GCF_001117765.1 and ATB run ERR067973. Its GOLD, BV-BRC, GTDB and ATB contexts consistently concern that other taxon. A BioSample number does not identify an NCBI taxon with the same digits or supply a target genome relationship.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
