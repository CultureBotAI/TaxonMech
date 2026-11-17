# YAML Record Review: Bacillus sp. SBRh2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_sbrh2.yaml`
- Started UTC: 2026-10-04T02:42:49Z
- Finished UTC: 2026-10-04T02:43:30Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032715`, Bacillus sp. SBRh2. It carries SPECIES rank, BACTERIA domain, parent unclassified Bacillus (185979), ten lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No curated phenotype, host interaction, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_sbrh2.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/bacillus_sp_sbrh2.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked every lineage entry, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220899` and `data/catalog/ncbi_names-0005.jsonl.gz:30205` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032715&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032715) confirm exact label, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs.

The carried lineage includes Bacillati, Bacillota and Caryophanales. The legacy wording in `unclassified Bacillus (in: firmicutes)` is NCBI's parent label, not an independent TaxonMech classification conflict. Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies the placeholder; it does not formally name the species or equate SBRh2 with a better-characterized Bacillus strain.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13285` and `curation/seed_scope.tsv:321270` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HQ443225.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ443225.1) is a 1,460-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain SBRh2 and taxon 1032715. Source qualifiers identify rhizosphere material, host wild rice and China: Dongxiang, Jiangxi. These are explicit source qualifiers; neither a scientific host-species identification nor a beneficial host interaction is inferred.

The sequence cites an unpublished study by Fei and a direct submission on 2010-10-24. No PMID or DOI is supplied. Its marker and source metadata do not demonstrate plant-growth promotion, nitrogen fixation, antagonism, a metabolic pathway or any other strain-specific function. The current YAML makes none of those extrapolations.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded query is not universal genome-absence evidence, and the partial 16S marker is not a genome assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and bounded SBRh2 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 10 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. SBRh2 is not a verified collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only record; unrelated Bacillus datasets or external marker context do not establish a gene-function claim for this strain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source-carried taxonomy, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require strain-specific evidence before adding functions or host-interaction claims, and a supported authority crosswalk before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032715 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

SAMEA1032715 belongs to Streptococcus pneumoniae R34-3176 (1313), including GCA_001152225.1/.2, GCF_001152225.1 and ATB run ERR067975. Its GOLD, BV-BRC, GTDB and ATB evidence retain that unrelated identity. A BioSample number is not the NCBI taxonomy identifier with the same digits and supplies no SBRh2 genome association.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
