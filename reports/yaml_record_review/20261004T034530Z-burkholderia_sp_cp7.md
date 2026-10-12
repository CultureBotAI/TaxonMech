# YAML Record Review: Burkholderia sp. CP7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_cp7.yaml`
- Started UTC: 2026-10-04T03:43:46Z
- Finished UTC: 2026-10-04T03:45:30Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032760`, Burkholderia sp. CP7. It carries SPECIES rank, BACTERIA domain, parent unclassified Burkholderia (2613784), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, functional, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/burkholderia_sp_cp7.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/burkholderia_sp_cp7.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared every lineage entry, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220923` and `data/catalog/ncbi_names-0005.jsonl.gz:30229` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032760&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032760) confirm identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales and Burkholderiaceae match the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not formal species nomenclature or equivalence to another organism sharing CP7.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13314` and `curation/seed_scope.tsv:321294` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF280145.1](https://www.ncbi.nlm.nih.gov/nuccore/JF280145.1) is a 1,464-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain CP7 and explicit taxon 1032760. Source qualifiers identify soil and China: Shandong Province.

The sole reference is Shi and Yan's direct submission on 2011-01-30; no PMID, DOI or research-article reference is supplied. This establishes marker and collection context, not degradation capacity, antimicrobial production, pathogenicity or another strain-specific function. None is asserted by this YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. A partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric 1032760 with digit boundaries, full label, slug and bounded CP7 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 74 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no supported target culture deposit, genome association, extra source mapping or separate history record was found. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only record; no expression or functional claim is made.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit strain identity crosswalks and claim-specific evidence before adding deposit, genome or functional assertions.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032760 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Separately cataloged Acetobacteraceae bacterium CP7 (1325784), Ensifer JNVU CP7 (1719654), Bacillus Cp7 (1853289) and several Sulfurimonas Cp_7 sample names were not equated with this Burkholderia. GOLD also contains Eubacteriales Cp7, Streptococcus phage CP-7, Cyanophora Cp_7 and a hospital-wastewater CP7 sample, none with a target identity chain. GOLD organism/project/analysis identifiers are not assemblies.

Other CP7 genomes belong to Stutzerimonas zhaodongensis (1176257; GCA/GCF_047758595.1; BV-BRC 1176257.23), Corynebacterium propinquum (43769; GCA/GCF_030515715.1), Clostridium perfringens (1502; GCA/GCF_043951515.1) and Klebsiella pneumoniae (573; GCA_022054805.1; isolate 18061528). Bacillus velezensis CP7.1A, CP7.1C and CP7.2A have separate GCA/GCF_013284545.1, _013284555.1 and _013284625.1 records. A shared designation does not establish cross-genus equivalence.

SAMEA1032760 belongs to Streptococcus equi subsp. equi EQUI0156 (148942; species 1336), with GCA/GCF_001175205.1, BV-BRC 148942.19 and ATB ERR064536. Its BioSample suffix is not the reviewed taxon identifier. None of the excluded matches supplies target genome evidence.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
