# YAML Record Review: Pasteurellaceae bacterium Naja4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_naja4.yaml`
- Started UTC: 2026-10-04T01:33:01Z
- Finished UTC: 2026-10-04T01:33:55Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:1032625`, Pasteurellaceae bacterium Naja4. It is an NCBI SPECIES-rank placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NCBITAXON NAME assertion and a single seed event. It asserts no phenotype, mechanism, genome identity or gene function.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_naja4.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_naja4.yaml` passed for one file with zero errors and refreshed the strict-validator TSV.

Read-only structured comparisons verified the entire lineage, inventory matches, source attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No invented focused replacement was used. There are no curator-added graph terms or independent history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220873` and `data/catalog/ncbi_names-0005.jsonl.gz:30180` agree on the target identifier and scientific name. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032625&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032625) confirm rank, parent, domain, genetic code and all nine root-first lineage IDs. Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae retain NCBI's placement.

The full backbone scan found no synonyms or children. Complete structured type-material, merged-ID and dropped inventories contain no own-ID row. The strain-style label is not grounds to override NCBI's SPECIES rank. EXACT does not assert formal nomenclatural validity or membership in a named species beyond the explicit source taxon.

## Evidence

The NCBITAXON attestation is one NAME from the 2026-09-13 snapshot, not one genome or one experimentally established phenotype. `data/taxa/PATHS.tsv:13250` and `curation/seed_scope.tsv:321245` match the ID, slug and NCBI-only scope. The seed event matches the source-derived reason and does not imply human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [HM626590.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626590.1) is a 474-base partial RpoB coding sequence of Naja4, genomic DNA, with taxon 1032625. Source qualifiers give Denmark and a harbor-seal host. Christensen, Bisgaard and Hansen submitted the record on 2010-07-05.

The entry's other reference is marked unpublished and has no PMID or DOI. Its study title concerns Pasteurellaceae prevalence and a proposed name spelled Otariobacter oris. That shared bibliographic context does not make Naja4 a synonym, type strain or genome of the proposed species. The inspected taxonomy and sequence both retain the target's separate identity. A short RpoB fragment cannot establish a complete genome, a physiological trait or an experimentally demonstrated mechanism; the YAML makes none of those inferences.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof of universal absence. The sequence browser view was unavailable, but the structured GenBank and taxonomy requests succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact taxon row. The backbone has no descendants, so zero classified BacDive strains supports `strain_count: 0` without confusing the count with the named isolate.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier, label, slug and Naja4 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 32 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target culture deposit, genome association, extra source mapping or separate history record was found within those surfaces. Naja4 alone is not an eligible collection accession. Optional nomenclature, strain, phenotype and graph slots need not be populated. iModulonDB is not applicable to the taxonomy-only YAML; the externally inspected RpoB annotation is not a gene claim in this record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve SEEDED status and the generated-file boundary. Any future identity correction belongs in the maintained authority inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. An explicit isolate-level source crosswalk is needed before adding a species synonym or culture-based genome link.

## Follow-up Checks

For an authorized source refresh, inspect the changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032625 --force`, inspect its YAML and rerun the two focused validators. Run the documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Numeric collisions were excluded: SAMEA1032625 belongs to Streptococcus pneumoniae R34-3093; GCA/GCF_001032625.1 describes Klebsiella pneumoniae CHS191; GCA/GCF_011032625.1 describes Escherichia coli CAP11. Other matches occur inside unrelated assembly identifiers, sample/run accessions and a SeqKit checksum. Matching seven digits is not taxon or strain evidence.

Only this new report was manually written for the target. No taxon, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
