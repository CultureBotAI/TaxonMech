# YAML Record Review: Pseudomonas sp. RL1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_rl1.yaml`
- Started UTC: 2026-10-04T02:01:48Z
- Finished UTC: 2026-10-04T02:02:33Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032652`, Pseudomonas sp. RL1. This is a SPECIES-rank placeholder in BACTERIA under unclassified Pseudomonas (196821), with ten lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. It makes no gene-function, phenotype, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_rl1.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pseudomonas_sp_rl1.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the full lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220884` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30191` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032652&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032652) confirm identity, species rank, parent, bacterial domain, code 11 and all ten root-first lineage IDs. The Pseudomonadales/Pseudomonadaceae/Pseudomonas chain is carried from NCBI.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT describes the specific NCBI placeholder, not formal nomenclatural validity. NCBI's species rank is preserved despite the strain-style label; RL1 alone cannot identify an isolate across organisms or sources.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13264` and `curation/seed_scope.tsv:321256` confirm the identifier, slug and NCBI-only scope reason. The seed event at 2026-09-13T17:54:04Z records that reason without claiming human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [HQ625017.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ625017.1) is a 1,502-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain RL1, taxon 1032652 and a soil isolation source. The only reference is Rao's direct submission on 2010-11-09; no PMID or DOI is supplied. The institution's Chinese mailing address is not a collection-location qualifier and was not used to infer one.

This marker provides isolate identity context, not a genome assembly, physiological result or type designation. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof of genome absence everywhere. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and bounded RL1/RL 1/RL-1 tokens across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 90 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

No independently supported target culture deposit, assembly association, extra source mapping or separate history record was found within those surfaces. RL1 is a bare designation, not a registered collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; the external marker annotation is not a record gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the source identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require an explicit isolate/deposit crosswalk before transferring evidence from another RL1 record.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032652 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Name collisions include Sharpea azabuensis RL 1 (BacDive 5379, StrainInfo 39174), Rhodococcus qingshengii RL1 (BacDive 169602, StrainInfo 402752), Xanthomonas vasicola RL1 and Arthrobacter YC-RL1. Bacillus, Paenibacillus, Enterobacter, Listeria, fungal, cyanobacterial and community-sample matches also have distinct full identities. None is evidence for this Pseudomonas merely because its designation contains RL1.

Numeric exclusions include SAMEA1032652 for Streptococcus pneumoniae R34-3167, SAMN41032652 for Streptococcus pyogenes, Salmonella run SRR11032652, Campylobacter assembly GCA_010326525.1, a contig N50 and a SeqKit checksum. These matches do not identify target genomes.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
