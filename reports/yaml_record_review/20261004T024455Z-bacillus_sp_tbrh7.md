# YAML Record Review: Bacillus sp. TBRh7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_tbrh7.yaml`
- Started UTC: 2026-10-04T02:44:20Z
- Finished UTC: 2026-10-04T02:44:55Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032716`, Bacillus sp. TBRh7. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacillus (185979), ten lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No curated phenotype, host interaction, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_tbrh7.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bacillus_sp_tbrh7.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220900` and `data/catalog/ncbi_names-0005.jsonl.gz:30206` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032716&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032716) confirm exact label, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs.

The lineage carries Bacillati, Bacillota and Caryophanales. Legacy wording in `unclassified Bacillus (in: firmicutes)` is NCBI's parent label, not an independently curated hierarchy conflict. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this source placeholder; it does not formally name the species or equate TBRh7 with another Bacillus isolate.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13286` and `curation/seed_scope.tsv:321271` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443232.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443232.1) is a 1,460-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain TBRh7 and explicit taxon 1032716. Source qualifiers identify rhizosphere material, host wild rice and China: Dongxiang, Jiangxi. These were checked on this accession, not inferred from another study isolate.

The references comprise an unpublished study by Fei and a direct submission on 2010-10-24. No PMID or DOI is supplied. The metadata do not establish a scientific host-species grounding, beneficial host interaction, plant-growth promotion, nitrogen fixation or other strain-specific function. The YAML makes none of those extrapolations.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query does not prove universal genome absence, and the partial marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and bounded TBRh7 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 10 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. TBRh7 is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only record; unrelated Bacillus datasets or external marker context do not establish gene-function evidence for this strain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific evidence for functions and host interactions, and a supported authority crosswalk before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032716 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

SAMEA1032716 belongs to Streptococcus pneumoniae R34-3112 (1313), including GCA_001300755.1/.2, GCF_001300755.1 and ATB run ERR068013. GOLD, BV-BRC, GTDB and ATB matches retain that other identity. A BioSample number is not the NCBI taxonomy identifier with the same digits and supplies no TBRh7 genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
