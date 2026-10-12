# YAML Record Review: Cupriavidus sp. TBRh4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cupriavidus_sp_tbrh4.yaml`
- Started UTC: 2026-10-04T02:49:24Z
- Finished UTC: 2026-10-04T02:50:14Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032719`, Cupriavidus sp. TBRh4. It carries SPECIES rank, BACTERIA domain, parent unclassified Cupriavidus (2640874), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No curated phenotype, host interaction, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/cupriavidus_sp_tbrh4.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/cupriavidus_sp_tbrh4.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked every lineage entry, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220903` and `data/catalog/ncbi_names-0005.jsonl.gz:30209` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032719&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032719) confirm exact label, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs.

The Pseudomonadati, Pseudomonadota, Betaproteobacteria and Burkholderiaceae placement is carried from NCBI, not inferred from a phenotype. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the source placeholder; it neither formally names the species nor equates TBRh4 with another Cupriavidus isolate.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13289` and `curation/seed_scope.tsv:321274` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443228.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443228.1) is a 1,442-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain TBRh4 and explicit taxon 1032719. Source qualifiers identify rhizosphere material, host wild rice and China: Dongxiang, Jiangxi.

The references comprise an unpublished study by Fei and a direct submission on 2010-10-24. No PMID or DOI is supplied. The marker and source qualifiers do not establish a scientific host-species grounding, metal tolerance, a metabolic pathway, plant-growth promotion or any other strain-specific function. None is asserted by this YAML.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query does not prove universal genome absence, and the partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and bounded TBRh4 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 12 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. TBRh4 is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; external marker context is not a gene-function assertion for this strain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific functional evidence and an explicit authority crosswalk before attaching culture or genome identifiers. Do not infer a function from the genus name.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032719 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

SAMEA1032719 belongs to Streptococcus pneumoniae R34-3058 (1313), including GCA_001089825.1/.2, GCF_001089825.1 and ATB run ERR065314. Its GOLD, BV-BRC, GTDB and ATB evidence retain that other identity. Assembly GCA_949462565.1 belongs to an uncultured Bacilli bacterium (224209); its genome length alone matches 1032719. Neither numeric collision supplies a TBRh4 genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
