# YAML Record Review: Cupriavidus sp. TBSe5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cupriavidus_sp_tbse5.yaml`
- Started UTC: 2026-10-04T02:56:31Z
- Finished UTC: 2026-10-04T02:57:40Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032720`, Cupriavidus sp. TBSe5. It carries SPECIES rank, BACTERIA domain, parent unclassified Cupriavidus (2640874), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It makes no phenotype, gene-function, host-interaction, graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/cupriavidus_sp_tbse5.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/cupriavidus_sp_tbse5.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared all lineage entries, inventory rows, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220904` and `data/catalog/ncbi_names-0005.jsonl.gz:30210` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032720&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032720) confirm identity, species rank, parent, code 11 and all ten root-first lineage IDs. Labels and ranks match the carried NCBI hierarchy through Betaproteobacteria, Burkholderiales, Burkholderiaceae and Cupriavidus.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the source placeholder, not a formally named species or equivalence with another Cupriavidus strain.

## Evidence

The single NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13291` and `curation/seed_scope.tsv:321275` confirm the identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443237.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443237.1) is a 1,436-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain TBSe5 and explicit taxon 1032720. Its source qualifiers specify rhizosphere, host wild rice and China: Dongxiang, Jiangxi. Do not reinterpret the strain abbreviation as a seed-tissue or endophyte claim.

References comprise an unpublished study by Fei and a direct submission on 2010-10-24; neither a PMID nor DOI is supplied. These qualifiers do not ground the host to a scientific species or establish plant-growth promotion, metal tolerance or a metabolic function. No such assertion appears in the YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. The marker is not an assembly. The Nuccore browser page was unavailable through the web tool; structured taxonomy and GenBank XML requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting the source count of zero.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded TBSe5 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All ten matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target deposit, genome association, extra source mapping or separate history record was found. TBSe5 is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; the external marker context is not a functional assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require direct strain-specific evidence for functions and explicit authority crosswalks for culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect new evidence, regenerate one canary with `just seed-canary NCBITaxon:1032720 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

SAMEA1032720 belongs to Streptococcus pneumoniae R34-3171 (1313), with GCA_001121665.1/.2, GCF_001121665.1, BV-BRC 1313.5854 and ATB run ERR067969. Its GOLD, GTDB and other source records retain that other organism identity. The numeric match is not a TBSe5 genome link, and accession versions were not collapsed.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
