# YAML Record Review: uncultured gamma proteobacterium TIHP302-11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_11.yaml`
- Started UTC: 2026-10-04T02:11:45Z
- Finished UTC: 2026-10-04T02:12:26Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103269`, uncultured gamma proteobacterium TIHP302-11. It is a SPECIES-rank environmental-clone placeholder in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. No phenotype, gene-function, causal-graph or genome-equivalence claim is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_11.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_11.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18378` and native name row `data/catalog/ncbi_names-0000.jsonl.gz:38396` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103269&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103269) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. NCBI's environmental-samples division does not replace the Bacteria domain in the lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT denotes identity with this NCBI placeholder, not a formally named cultured species. TIHP302-11 is distinct from neighboring TIHP302 clone designations and from other databases' numeric identifier 103269.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13271` and `curation/seed_scope.tsv:144038` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [AB031597.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031597.1) is a 692-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103269, clone TIHP302-11 and an environmental-sample flag. Its isolation-source qualifier identifies coastal marine sediment, not a culture deposit.

The references comprise an unpublished microbial-community study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25. No PMID or DOI is supplied. The study title's community-level quinone profiling does not establish a phenotype of the individual clone. The YAML makes no such extrapolation.

The partial marker is not a genome assembly. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than universal genome-absence evidence. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the number with digit boundaries, full label, slug and clone-separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 42 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; its two matches were requests for the unrelated BacDive identifier 103269.

No independently supported target culture deposit, genome association, extra source mapping, target-specific source manifest entry or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; external marker context is not a gene-function claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve environmental-clone identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require full authority identifiers and explicit source evidence; neither community results nor matching numeric strings should be transferred to this clone.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103269 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

BacDive 103269 concerns Pseudomonas putida STI11318 (taxon 303), not NCBITaxon:103269. CIP 103269 concerns Paenibacillus macquariensis, represented by BacDive 11477 with species/subspecies IDs 948756/1468 and GOLD Go0611579. StrainInfo strain 1151 has that Paenibacillus group identity, but its own CIP deposit 153611 lacks a deposit-level taxon; no group taxon was silently assigned to it. StrainInfo deposit 103269 is instead Enterococcus faecium ATCC 23829 (1352), on strain record 38253.

Further exclusions include Debaryomyces sequence KY103269, Bacteroides nucleotide CP103269, Akkermansia MGBC103269, MarMAG/PNUSAE/PNUSAS identifiers, E. coli run DRR103269, assembly statistics and a SeqKit checksum. None establishes target identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
