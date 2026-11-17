# YAML Record Review: Sphingomonas sp. F4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_f4.yaml`
- Started UTC: 2026-10-04T03:06:50Z
- Finished UTC: 2026-10-04T03:07:46Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032726`, Sphingomonas sp. F4. It carries SPECIES rank, BACTERIA domain, parent unclassified Sphingomonas (196159), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, host-interaction, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sphingomonas_sp_f4.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/sphingomonas_sp_f4.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared the full lineage, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220910` and `data/catalog/ncbi_names-0005.jsonl.gz:30216` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032726&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032726) confirm exact identity, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Alphaproteobacteria, Sphingomonadales and Sphingomonadaceae agree with the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this source placeholder, not a formally named species or another strain sharing the short label F4.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13297` and `curation/seed_scope.tsv:321281` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ647249.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ647249.1) is a 1,401-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain F4 and explicit taxon 1032726. Source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

References comprise an unpublished study by Fei and a direct submission on 2010-11-21; no PMID or DOI is supplied. The source context does not establish a scientific host-species grounding, plant-growth promotion, degradation capability or another strain-specific function. No such assertion appears in the YAML.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded result is not proof of universal genome absence, and the marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as a source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and Sphingomonas co-occurring with bounded F4 separator variants in either order across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 15 matching lines were inspected in structured context. This was a target-name and genus-qualified search, not a census of every bare F4 alias. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those bounded surfaces and queries, no independently supported target deposit, genome association, extra source mapping or separate history record was found. F4 alone is not a collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; external marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require direct strain-specific functional evidence and explicit identity crosswalks before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032726 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Sphingomonas sp. Sand_R2A_F4 is the separate taxon 1077991, present at backbone line 231122, names shard 0005 line 42459 and scope line 329887. A shared genus and F4 suffix do not establish equivalence to the target.

SAMEA1032726 belongs to Streptococcus pneumoniae 312942 (1313). The inspected sources carry GCA_001083705.1/.2/.3 and GCF_001083705.1/.2, BV-BRC 1313.6858 and ATB run ERR069818. Historical and current versions were retained without collapsing them into one accession. The numeric overlap supplies no Sphingomonas genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
