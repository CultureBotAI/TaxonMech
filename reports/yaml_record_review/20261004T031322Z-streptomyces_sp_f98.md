# YAML Record Review: Streptomyces sp. F98

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_f98.yaml`
- Started UTC: 2026-10-04T03:12:37Z
- Finished UTC: 2026-10-04T03:13:22Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032729`, Streptomyces sp. F98. It has SPECIES rank, BACTERIA domain, parent unclassified Streptomyces (2593676), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, gene-function, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_f98.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/streptomyces_sp_f98.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220913` and `data/catalog/ncbi_names-0005.jsonl.gz:30219` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032729&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032729) confirm identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales and Streptomycetaceae match the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not a formally named species or another strain carrying F98 in its designation.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13300` and `curation/seed_scope.tsv:321284` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF793518.1](https://www.ncbi.nlm.nih.gov/nuccore/JF793518.1) is a 1,416-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain F98 and explicit taxon 1032729. Source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

The references comprise an unpublished actinomycete study by Fei and a direct submission on 2011-04-05. No PMID or DOI is supplied. The marker and collection context do not establish a scientific host-species grounding, internal plant colonization, antimicrobial production or another strain-specific function. No stronger assertion appears in the YAML.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded result is not proof of universal genome absence, and the partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded F98 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 81 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. F98 alone is not a collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; the external marker and unrelated plant-expression projects are not functional evidence for this strain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific functional evidence and explicit identity crosswalks before attaching culture or genome identifiers. Preserve supplied accession versions and do not promote a bare designation to a deposit key.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032729 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Salmonella enterica subsp. enterica F98 is taxon 59201, BacDive 5106 and StrainInfo strain 91288, with CECT 4156, CIP 110278, DSM 26529 and NCTC 12190 among its deposit designations. Myxococcus fulvus Mx f98 is taxon 33, BacDive 9793, DSM 52525 and StrainInfo strain 215795. VKM F-98 is the own deposit 461445 of Botryotrichum piluliferum StrainInfo strain 265173. None is target culture evidence.

F98-3 belongs to Malaciobacter molluscorum, also named Arcobacter molluscorum in source records: species taxon 1032072, strain taxon 870501, BacDive 166638, StrainInfo 369523, CECT 7696 and LMG 25693. BacDive and StrainInfo inventory rows supply unversioned GCA_002701265; NCBI/BV-BRC/GTDB native records supply GCA_002701265.1 or GCF_002701265.1. IMG 2871071908 and BV-BRC 870501.3 likewise refer to that other strain. The original source versions and taxonomic levels remain distinct; no accession was transferred to Streptomyces or given an invented version.

Other excluded records include Arthrobacter rhombi marker descriptions containing F98.3HR69; Selenomonas oral taxon F98 (712584); Staphylococcus sp. F98 (1581976); Burkholderia sp. 68-F98 (998145); Tenacibaculum designations containing F98 (691426 and 691427); Diplodia seriata F98.1; Merismopedia tenuissima F98-2; and a legacy Salmonella Agona page name. Listeria monocytogenes LM-F-98 has GCA_003188145.1 / GCF_003188145.1, while Escherichia coli, Campylobacter jejuni and Acinetobacter baumannii have other F98-labeled assemblies. GOLD host-associated, freshwater and seawater community samples and Brachypodium expression profiling do not identify this isolate.

SAMEA1032729 belongs to Streptococcus pneumoniae R34-3077 (1313), with GCA_001154485.1/.2, GCF_001154485.1, BV-BRC 1313.6241 and ATB run ERR065332. The numeric overlap supplies no target genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
