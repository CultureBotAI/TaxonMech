# YAML Record Review: Pasteurellaceae bacterium Jack1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_jack1.yaml`
- Started UTC: 2026-10-04T01:34:38Z
- Finished UTC: 2026-10-04T01:35:27Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032626`, Pasteurellaceae bacterium Jack1. It is a SPECIES-rank NCBI placeholder in BACTERIA, parent unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and a single seed event. It contains no phenotype, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_jack1.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_jack1.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons verified lineage, raw-source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was invented. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:220874` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30181` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032626&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032626) confirm identity, rank, parent, domain, genetic code and all nine root-first lineage identifiers. The chain through Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae remains NCBI's, not an inferred placement.

Full structured scans found no backbone synonyms or children and no own-ID type-material, merged-ID or dropped entry. The strain-like label does not justify overriding NCBI's species rank. EXACT means grounded to this source taxon, not that Jack1 is a formally named species or an eligible collection accession.

## Evidence

The one NAME assertion and 2026-09-13 snapshot note match the NCBI inventory. `data/taxa/PATHS.tsv:13251` and `curation/seed_scope.tsv:321246` agree on identifier, slug and NCBI-only scope reason. The seed event reproduces that reason and is not a human-review claim.

Exact-taxon Nuccore search returned two entries, both inspected as GenBank XML. [HM626591.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626591.1) is a 459-base partial RpoB coding sequence; [HM626619.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626619.1) is a 1,473-base partial 16S ribosomal RNA gene sequence. Both have genomic DNA molecule type, strain Jack1, taxon 1032626, Canada and a grey-seal host in their source qualifiers.

Both entries identify Christensen, Bisgaard and Hansen and direct submission on 2010-07-05. Their other reference is marked unpublished and supplies neither PMID nor DOI. The study title discusses Pasteurellaceae prevalence and a proposal spelled Otariobacter oris; that title is not an isolate-level reassignment, type designation or synonym crosswalk. Both live source records retain Jack1 separately, as the YAML does.

Partial RpoB and 16S sequences do not establish a complete genome, culture-deposit identity or physiological mechanism. The single NAME assertion is independent of the two sequence accessions. Exact Assembly search returned zero with a phrase-not-found warning, which is a bounded search outcome rather than universal genome-absence evidence. The sequence browser view failed, but structured GenBank retrieval succeeded.

## Completeness

Complete BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventory scans found no exact target row. The full backbone has no descendant taxa and no classified BacDive strain was found, supporting `strain_count: 0` under the source-counting contract.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier, label, slug and Jack1 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 19 matching lines were inspected in context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independent target deposit, supported genome association, extra source mapping or separate history record was found within the searched surfaces. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only record; external RpoB sequence context does not turn the YAML into a gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated-file ownership and SEEDED status. Future authority corrections belong to maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv`. Do not create a genome join from the bare name Jack1 or from the shared publication context.

## Follow-up Checks

For an authorized source refresh, inspect changed authority evidence, regenerate one canary with `just seed-canary NCBITaxon:1032626 --force`, inspect the emitted YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

The GOLD name matches describe Pinus banksiana Jack1 and its transcriptome project, not Pasteurellaceae. Numeric collisions include SAMEA1032626 for Streptococcus pneumoniae R34-3166, GCA_010326265.1 for Campylobacter jejuni, and unrelated ATB run/sample strings. None supports bacterial strain or genome identity for this target.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
