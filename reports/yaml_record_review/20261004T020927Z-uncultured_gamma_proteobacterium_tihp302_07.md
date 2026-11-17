# YAML Record Review: uncultured gamma proteobacterium TIHP302-07

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_07.yaml`
- Started UTC: 2026-10-04T02:08:42Z
- Finished UTC: 2026-10-04T02:09:27Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103267`, uncultured gamma proteobacterium TIHP302-07. This SPECIES-rank environmental-clone placeholder belongs to BACTERIA under environmental samples (50423). It has seven lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NAME assertion and one seed event. It makes no gene-function, phenotype, causal-graph or genome-equivalence claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_07.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_07.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked the complete lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18376` and native name row `data/catalog/ncbi_names-0000.jsonl.gz:38394` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103267&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103267) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The environmental-samples division is not a different taxonomic domain; the lineage still places this entry in Bacteria.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT means grounding to this NCBI identity, not formal nomenclatural validity or availability of a culture. TIHP302-07 remains distinct from the adjacent TIHP302 clone designations.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13269` and `curation/seed_scope.tsv:144036` confirm the identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event records that reason without claiming human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [AB031595.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031595.1) is a 620-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103267, clone TIHP302-07 and an environmental-sample flag. Its isolation-source qualifier identifies coastal marine sediment, not a cultured strain.

The references comprise an unpublished microbial-community investigation by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25. They provide no PMID or DOI. The community-level quinone profiling mentioned in the study title cannot be assigned as a phenotype of this individual clone; the YAML makes no such claim.

The marker is not a genome assembly. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof of genome absence everywhere. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the number with digit boundaries, full label, slug and clone-separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 29 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

No independently supported target culture deposit, genome association, extra source mapping or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; external marker context is not a gene-function claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve environmental-clone identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not transfer community measurements or similarly numbered culture/deposit identifiers into the clone record.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103267 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103267 belongs to Sporosarcina psychrophila/Bacillus psychrophilus W16A (taxon 1476; BacDive 11984; StrainInfo strain 51842, own deposit 148926). StrainInfo deposit 103267 instead denotes ATCC 23828, Enterococcus faecium (1352), on strain record 38252. Neither full identifier is NCBITaxon:103267.

Further exclusions include Debaryomyces sequence KY103267, nucleotide accession CP103267, MGBC/MarMAG/FLAG/PNUSAS identifiers, assembly statistics and E. coli run DRR103267. The ATB row for that run carries failed Sylph-result flags and does not independently support any association with this clone.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
