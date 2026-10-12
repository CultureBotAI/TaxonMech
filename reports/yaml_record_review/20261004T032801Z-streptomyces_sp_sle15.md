# YAML Record Review: Streptomyces sp. SLe15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_sle15.yaml`
- Started UTC: 2026-10-04T03:26:47Z
- Finished UTC: 2026-10-04T03:28:01Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032734`, Streptomyces sp. SLe15. It carries SPECIES rank, BACTERIA domain, parent unclassified Streptomyces (2593676), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, functional, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_sle15.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/streptomyces_sp_sle15.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220918` and `data/catalog/ncbi_names-0005.jsonl.gz:30224` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032734&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032734) confirm identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales and Streptomycetaceae match the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not formal species nomenclature or a culture-deposit crosswalk. Preserve the authority's mixed-case SLe15 designation.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13306` and `curation/seed_scope.tsv:321289` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443220.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443220.1) is a 1,438-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain SLe15 and explicit taxon 1032734. Source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi. References comprise Fei's unpublished actinomycete study and direct submission on 2010-10-24; no PMID or DOI is supplied.

This supports marker and collection context, not a scientific host-species grounding, endophytic localization, antimicrobial production or other function. None is asserted. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. A partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 1032734 with digit boundaries, full label, slug and bounded SLe15 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All ten matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no supported target culture deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; external marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit strain identity crosswalks before attaching deposit or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032734 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

SAMEA1032734 belongs to Streptococcus pneumoniae R34-3156 (1313), including GCA_001095745.1/.2, GCF_001095745.1, BV-BRC 1313.5537 and ATB ERR068047. GOLD labels that project Streptococcus pneumoniae sv. 11A 3156. The BioSample's numeric suffix is not this NCBI taxon identifier, and none of these records supplies target genome evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
