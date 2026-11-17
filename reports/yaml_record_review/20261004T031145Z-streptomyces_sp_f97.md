# YAML Record Review: Streptomyces sp. F97

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_f97.yaml`
- Started UTC: 2026-10-04T03:11:00Z
- Finished UTC: 2026-10-04T03:11:45Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032728`, Streptomyces sp. F97. It has SPECIES rank, BACTERIA domain, parent unclassified Streptomyces (2593676), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, gene-function, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_f97.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/streptomyces_sp_f97.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared all lineage entries, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220912` and `data/catalog/ncbi_names-0005.jsonl.gz:30218` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032728&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032728) confirm identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales and Streptomycetaceae match the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI source placeholder, not a formally named species or another strain called F97.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13299` and `curation/seed_scope.tsv:321283` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF793506.1](https://www.ncbi.nlm.nih.gov/nuccore/JF793506.1) is a 1,372-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain F97 and explicit taxon 1032728. Source qualifiers specify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

The references comprise an unpublished actinomycete study by Fei and a direct submission on 2011-04-05. No PMID or DOI is supplied. The marker and source context do not establish a scientific host-species grounding, endophytic localization, antimicrobial production or another strain-specific function. Neither the genus nor the study's subject supplies those stronger claims, and none appears in the YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. The marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded F97 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 54 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. F97 alone is not a collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; external marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific functional evidence and explicit identity crosswalks before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032728 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Myxococcus fulvus Mx f97 is taxon 33, BacDive 9792, DSM 52524 and StrainInfo strain 215794. Schizophyllum commune has an IBK F-97 designation in StrainInfo strain 234899. These names are not target culture evidence.

Other unlinked taxon labels include Streptococcus sp. oral taxon F97 (712689), Frigoribacterium sp. F97 (1581981), bacterium F97 (1749229) and Enterobacteriaceae bacterium F97 (1775229). No explicit source crosswalk makes any of these the target. Listeria monocytogenes LM-F-97 carries GCA_003188185.1 / GCF_003188185.1, while Escherichia coli F97 and F97-prefixed isolates carry other assemblies, including GCA_035826555.1 and GCA_053000385.1. Those source classifications were retained.

GOLD F97 records also describe a cattle hybrid, host-associated microbial communities, freshwater viral communities and seawater communities. They do not support a strain-specific association to this Streptomyces isolate. SAMEA1032728 belongs to Streptococcus pneumoniae 263137 (1313), with GCA_001104405.1/.2, GCF_001104405.1, BV-BRC 1313.5632 and ATB run ERR069804. The numeric overlap supplies no target genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
