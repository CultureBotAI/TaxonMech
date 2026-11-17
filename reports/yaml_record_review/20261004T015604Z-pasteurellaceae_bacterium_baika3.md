# YAML Record Review: Pasteurellaceae bacterium Baika3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_baika3.yaml`
- Started UTC: 2026-10-04T01:53:01Z
- Finished UTC: 2026-10-04T01:56:04Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032646`, Pasteurellaceae bacterium Baika3. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. It makes no phenotype, gene-function, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_baika3.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_baika3.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220882` and native name row `data/catalog/ncbi_names-0005.jsonl.gz:30189` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032646&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032646) confirm the identity, species rank, parent, bacterial domain, code 11 and nine root-first lineage IDs. The ancestry through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae matches the source.

Complete structured scans found no backbone synonyms or children and no own-ID type-material, merged-ID or dropped entry. Baika3 is distinct from the previously reviewed Baika1 type-strain designation of Otariodibacter oris and from Pasteurellaceae bacterium baikas1. Similar names alone do not establish synonymy. EXACT describes NCBI grounding, not formal nomenclatural validity; the strain-style name does not override the source's species rank.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13261` and `curation/seed_scope.tsv:321254` confirm the identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event records that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HM626621.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626621.1) is a 1,437-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain Baika3 and taxon 1032646. Source qualifiers identify Denmark and a California-sea-lion host. Direct submission by Christensen, Bisgaard and Hansen was on 2010-07-05.

The other sequence reference is marked unpublished and supplies no PMID or DOI. Its title discusses Pasteurellaceae prevalence and a proposal spelled Otariobacter oris. A shared study, host or similar isolate designation does not supply an explicit isolate-level authority crosswalk. The YAML correctly retains Baika3's own taxon identity without importing Baika1's type, culture or genome evidence.

A partial 16S marker is neither a complete genome nor a demonstrated phenotype. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof of genome absence everywhere. Structured taxonomy and GenBank requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under the source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier, label, slug and Baika3 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 14 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target culture deposit, assembly association, extra source mapping or separate history record was found within those surfaces. Bare Baika3 is not a registered collection accession. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; an external marker annotation is not a gene-function claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve exact source spelling, generated-file ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require an explicit isolate-level authority crosswalk before transferring Baika1/Otariodibacter or baikas1 evidence to Baika3.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032646 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric matches include SAMEA1032646 for Streptococcus pneumoniae strain R34-3138 and its GCA/GCF_001108285 assemblies, Campylobacter jejuni assembly GCA_010326465.1, Salmonella run SRR11032646, and Streptococcus pyogenes sample SAMN41032646. Those unrelated accession strings do not establish target taxon, strain or genome identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
