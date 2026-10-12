# YAML Record Review: uncultured gamma proteobacterium TIHP302-15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_15.yaml`
- Started UTC: 2026-10-04T02:41:09Z
- Finished UTC: 2026-10-04T02:41:56Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103271`, uncultured gamma proteobacterium TIHP302-15. It is a SPECIES-rank environmental-clone placeholder in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. It contains no phenotype, gene-function, causal-graph or genome-equivalence assertion.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_15.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_15.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18380` and `data/catalog/ncbi_names-0000.jsonl.gz:38398` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103271&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103271) confirm identity, species rank, parent, code 11 and all seven root-first lineage IDs. The environmental-samples division does not replace the Bacteria domain carried in the lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not a formally named cultured species. TIHP302-15 must not be confused with neighboring TIHP302 clone designations or other authorities' numeric identifier 103271.

## Evidence

The NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13284` and `curation/seed_scope.tsv:144040` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [AB031601.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031601.1) is a 653-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103271, clone TIHP302-15 and an environmental-sample flag. Its isolation source is coastal marine sediment, not a culture deposit.

References comprise an unpublished microbial-community study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25. No PMID or DOI is supplied. Community-level quinone profiling named in the study title does not establish a phenotype of the individual clone. The YAML makes no such extrapolation.

The partial marker is not a genome assembly. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than universal genome-absence evidence. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting the source-defined `strain_count: 0`.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier number with digit boundaries, full label, slug and clone-separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 95 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files; its three matches were two references to the unrelated BacDive request ID 103271 and a StrainInfo response byte count.

No independently supported target culture deposit, genome association, extra source mapping, target-specific manifest entry or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; external marker context is not a gene-function assertion in this record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve environmental-clone identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require explicit source evidence and full authority identifiers rather than transferring community results or matching numeric strings.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103271 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

BacDive 103271 is Isoptericola sp. SF001060 (1884817), not NCBITaxon:103271. CIP 103271 is Hydrogenophaga flava, represented by BacDive 2963 with species/strain IDs 65657/1349752. Native StrainInfo strain 3010 and its own CIP deposit 151674 identify Hydrogenophaga flava (65657).

DSM 103271 is Corynebacterium fournieri (1852390), represented by BacDive 139734, StrainInfo strain 397396 and its own deposit 904019. Its associated sources carry GCA_030408775 without a version in the BacDive/StrainInfo inventories and GCA/GCF_030408775.1 in versioned genome catalogs, plus IMG 8058170124, BV-BRC 1852390.4/.5 and GOLD Go0671661/Gp0762844/Ga0617529. These are evidence about that other cultured taxon, not the environmental clone; no version was appended and no GOLD organism/project ID was counted as a genome here.

StrainInfo deposit 103271 is instead ATCC 23830 on strain 38254, with its own taxon Corynebacterium (1716). Other excluded matches include Debaryomyces maramus sequence KY103271, Bacteroides faecis BFG-513 sequence CP103271, Phocaeicola vulgatus MGBC103271, PNUSAE/PNUSAS identifiers, E. coli run DRR103271, assembly statistics and a Klebsiella SeqKit checksum. None establishes target identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
