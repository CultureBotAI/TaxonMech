# YAML Record Review: uncultured gamma proteobacterium TIHP302-10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_10.yaml`
- Started UTC: 2026-10-04T02:10:15Z
- Finished UTC: 2026-10-04T02:10:57Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103268`, uncultured gamma proteobacterium TIHP302-10. It is a SPECIES-rank environmental-clone placeholder in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. No gene-function, phenotype, causal-graph or genome-equivalence claim is made.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_10.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_10.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18377` and native name row `data/catalog/ncbi_names-0000.jsonl.gz:38395` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103268&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103268) confirm identifier, label, species rank, parent, code 11 and all seven root-first lineage IDs. NCBI's environmental-samples division does not change the bacterial domain established by the lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not a formally named cultured species. TIHP302-10 is a distinct clone designation; evidence from other TIHP302 suffixes is not automatically interchangeable.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13270` and `curation/seed_scope.tsv:144037` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without implying human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031596.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031596.1) is a 729-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103268, clone TIHP302-10 and an environmental-sample flag. The isolation-source qualifier names coastal marine sediment, not a culture deposit.

The references comprise an unpublished microbial-community study by Urakawa, Yoshida, Nishimura and Ohwada, and Urakawa's direct submission on 1999-08-25. No PMID or DOI is supplied. Community-level quinone profiling mentioned in the study title does not establish a phenotype of this individual clone. The record makes no such claim.

The marker is not a whole-genome assembly. Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than universal genome-absence evidence. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the number with digit boundaries, full label, slug and clone-separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 27 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

No independently supported target culture deposit, genome association, extra source mapping or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML; the external marker is not a gene-function claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve environmental-clone identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not transfer community measurements or identically numbered culture accessions into this clone record.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103268 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103268 belongs to Psychrobacillus insolitus W16B (taxon 1461; BacDive 1565; StrainInfo strain 1124, own deposit 148810), not NCBITaxon:103268. Its type-strain flag cannot be transferred to this environmental clone.

Other numeric matches concern Alphaproteobacteria MGBC103268, MarMAG_103268, Listeria FLAG-103268, Salmonella PNUSAS103268, Shigella isolate 103268, Bacteroides thetaiotaomicron BFG-478 nucleotide accession CP103268, E. coli run DRR103268 and unrelated assembly statistics. None establishes target strain or genome identity.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
