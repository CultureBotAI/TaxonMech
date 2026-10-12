# YAML Record Review: Streptomyces sp. PRh1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_prh1.yaml`
- Started UTC: 2026-10-04T03:16:38Z
- Finished UTC: 2026-10-04T03:17:22Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032730`, Streptomyces sp. PRh1. It has SPECIES rank, BACTERIA domain, parent unclassified Streptomyces (2593676), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, gene-function, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_prh1.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/streptomyces_sp_prh1.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220914` and `data/catalog/ncbi_names-0005.jsonl.gz:30220` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032730&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032730) confirm identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales and Streptomycetaceae match the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not a formally named species or another organism sharing PRH1. Preserve the source designation's PRh1 case.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13302` and `curation/seed_scope.tsv:321285` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443222.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443222.1) is a 1,434-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain PRh1 and explicit taxon 1032730. Source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

References comprise an unpublished actinomycete study by Fei and a direct submission on 2010-10-24; no PMID or DOI is supplied. The marker and collection context do not establish a scientific host-species grounding, endophytic localization, antimicrobial production or another strain-specific function. None is asserted by this YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. The partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded PRh1 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 16 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. PRh1 alone is not a collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; external marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific functional evidence and explicit identity crosswalks before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032730 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Arthrobacter sp. PRH1 is the separate taxon 376810. BV-BRC 71253.4 instead labels a PRH1 genome as Arthrobacter rhombi (71253). These source classifications were not reconciled through the shared bare designation, and neither establishes equivalence to Streptomyces PRh1.

SAMEA1032730 belongs to Streptococcus pneumoniae R34-3039 (1313), including GCA_001167365.1/.2, historical GCF_001167365.1, BV-BRC 1313.6380 and ATB run ERR065296. GCA_964588165.1 is an uncultured Gammaproteobacteria bacterium (86473), whose genome length alone matches 1032730. None supplies target genome evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
