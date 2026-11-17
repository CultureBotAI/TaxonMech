# YAML Record Review: Pasteurellaceae bacterium Delphsu3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_delphsu3.yaml`
- Started UTC: 2026-10-04T01:42:21Z
- Finished UTC: 2026-10-04T01:43:20Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032630`, Pasteurellaceae bacterium Delphsu3. It is an NCBI SPECIES-rank placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It contains no phenotype, gene-function, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_delphsu3.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_delphsu3.yaml` passed for one file with zero errors and refreshed the validator TSV.

Read-only structured checks compared all lineage entries, raw-source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. There are no curator-added graph terms or separate history references requiring a target-specific gate.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:220877` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30184` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032630&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032630) confirm identity, rank, parent, domain, code 11 and all nine root-first lineage identifiers. The ancestry through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae remains NCBI's placement.

Complete structured scans found no backbone synonyms or children and no own-ID type-material, merged-ID or dropped row. The strain-like suffix is not grounds to override NCBI's species rank. EXACT does not imply formal nomenclatural validity or an assignment to a different named species. The source identity is distinct from the separately inspected Delphsu4a and Delphsu4b records.

## Evidence

The NCBITAXON attestation correctly records one NAME from the 2026-09-13 snapshot. `data/taxa/PATHS.tsv:13255` and `curation/seed_scope.tsv:321249` agree on ID, slug and NCBI-only scope reason. The seed event accurately repeats that reason without claiming human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [HM626595.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626595.1) is a 463-base partial RpoB coding sequence, genomic DNA, strain Delphsu3 and taxon 1032630. Its source qualifiers identify Canada and a harbor-seal host.

Christensen, Bisgaard and Hansen directly submitted the entry on 2010-07-05. Its other reference is marked unpublished, with no PMID or DOI. The study title concerns Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. That bibliographic context does not make every sampled isolate a member or type strain of the proposed species. Neither the target YAML nor the inspected live taxonomy makes that unsupported transfer.

The partial marker cannot establish a whole genome, a culture-deposit identity or a phenotype. Exact Assembly search returned zero with a phrase-not-found warning; this is a bounded query result, not proof of genome absence everywhere. The browser sequence page was unavailable, but structured taxonomy and GenBank requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. The full backbone has no descendants and the inventory has no classified BacDive strain for this target, supporting `strain_count: 0` under the source-counting contract.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and Delphsu3 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 26 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target collection deposit, assembly association, additional source mapping or separate history record was found within those surfaces. Bare Delphsu3 is not a registered collection accession. Optional nomenclature, strain, phenotype and graph slots need not be invented. iModulonDB is not applicable to the taxonomy-only YAML; external marker annotation is not a gene-function claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the separate source identity, generated-file boundary and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. A species reassignment or culture-based genome link requires explicit isolate-level evidence, not a related strain label or study title.

## Follow-up Checks

For an authorized refresh, inspect changed source evidence, regenerate a single canary with `just seed-canary NCBITaxon:1032630 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric collisions include SAMEA1032630 for Streptococcus pneumoniae strain 383739; the ungapped length 1032630 of GCA_964588165.1, an unrelated Gammaproteobacteria MAG; GCA_010326305.1 for Campylobacter jejuni; Salmonella run identifiers SRR10326300 through SRR10326309; a checksum fragment; and Streptococcus pyogenes sample SAMN41032630. None establishes target strain or genome identity.

Only this new report was manually written for the target. No taxon, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
