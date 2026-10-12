# YAML Record Review: Pasteurellaceae bacterium Svante4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_svante4.yaml`
- Started UTC: 2026-10-04T01:44:11Z
- Finished UTC: 2026-10-04T01:45:03Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1032631`, Pasteurellaceae bacterium Svante4. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, causal-graph, gene-function or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_svante4.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_svante4.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured checks compared all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. The record has no curator-added graph terms or independent history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220878` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30185` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032631&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032631) confirm identifier, label, species rank, parent, Bacteria domain, code 11 and all nine root-first lineage IDs. NCBI's ancestry through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae is preserved.

The full backbone has no target synonyms or children. Complete type-material, merged-ID and dropped inventories contain no own-ID row. The strain-like label does not change NCBI's rank, and EXACT does not imply formal nomenclatural validity. Svante4 remains a separate source identity from the previously inspected Svante2; sharing a name prefix and study does not establish equivalence.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note match the source inventory. `data/taxa/PATHS.tsv:13256` and `curation/seed_scope.tsv:321250` agree on ID, slug and NCBI-only scope reason. The seed event faithfully records that scope without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HM626596.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626596.1) is a 463-base partial RpoB coding sequence, genomic DNA, with strain Svante4 and taxon 1032631. The source gives Denmark and a harbor-seal host. Christensen, Bisgaard and Hansen directly submitted it on 2010-07-05.

The entry's other reference is marked unpublished and supplies no PMID or DOI. Its title discusses Pasteurellaceae prevalence and a proposal spelled Otariobacter oris; that title does not assign every isolate to the proposed species. The YAML correctly avoids importing a synonym, type designation, phenotype or genome identity from that shared study context. A short marker sequence is not a complete genome or direct physiological evidence.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query outcome rather than universal genome absence. The sequence browser view was unavailable, but both taxonomy endpoints and structured GenBank retrieval succeeded.

## Completeness

Complete BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventory scans found no exact target row. There are no descendant taxa or classified BacDive strains in the checked backbone/inventory, supporting `strain_count: 0` under repository counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and Svante4 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 25 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target deposit, assembly association, extra mapping or separate history record was found within those surfaces. Svante4 alone is not a registered collection accession. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only record; the external RpoB annotation is context, not a gene-function assertion in the YAML.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source identity, generated-file ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. A later species or culture crosswalk requires explicit isolate-level evidence.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032631 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric collisions include SAMEA1032631 for Streptococcus pneumoniae strain 118039, Salmonella strain FDA1032631-C001-001 and run identifiers, a Pseudomonas checksum fragment, and Streptococcus pyogenes sample SAMN41032631. These do not support Svante4 taxon, strain or genome identity.

Only this new report was manually written for the target. No taxon, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
