# YAML Record Review: uncultured gamma proteobacterium TIHP302-05

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_05.yaml`
- Started UTC: 2026-10-04T02:00:17Z
- Finished UTC: 2026-10-04T02:01:01Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103265`, uncultured gamma proteobacterium TIHP302-05. This is a SPECIES-rank environmental-clone placeholder in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. There are no phenotype, gene-function, causal-graph or genome-equivalence claims.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_05.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_05.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18374` and native name row `data/catalog/ncbi_names-0000.jsonl.gz:38392` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103265&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103265) confirm the identity, species rank, parent, code 11 and all seven root-first lineage IDs. The NCBI environmental-samples division does not replace the Bacteria domain in the lineage.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT describes this NCBI identity, not a formally named cultured species. The TIHP302-05 suffix must remain distinct from previously reviewed TIHP302-03 and TIHP302-04 clone identifiers.

## Evidence

The single NCBITAXON NAME assertion and 2026-09-13 snapshot note agree with the inventory. `data/taxa/PATHS.tsv:13263` and `curation/seed_scope.tsv:144034` confirm identifier, slug and NCBI-only scope reason. The seed event at 2026-09-13T17:54:04Z preserves that reason without implying human review.

Exact-taxon Nuccore search returned one sequence, inspected as GenBank XML. [AB031593.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031593.1) is a 745-base partial 16S rRNA gene sequence with genomic DNA molecule type, taxon 103265, clone TIHP302-05 and an environmental-sample flag. Its stated isolation source is coastal marine sediment, not a culture-collection deposit.

The entry cites an unpublished microbial-community investigation by Urakawa, Yoshida, Nishimura and Ohwada and Urakawa's direct submission on 1999-08-25; it supplies no PMID or DOI. Community-level quinone profiling mentioned in the reference title does not demonstrate a clone-specific phenotype. The YAML does not make that extrapolation.

The partial marker is not a genome assembly. Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than universal absence evidence. Both structured taxonomy requests and the GenBank XML request succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the number with digit boundaries, full label, slug and clone-separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 45 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files: two hits were requests for unrelated BacDive 103265, and one was a response byte count in StrainInfo metadata.

No target-specific culture deposit, genome association, extra source mapping, source manifest entry or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only YAML; an external marker annotation is not a record gene-function claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve environmental-clone identity, generated ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not promote community measurements or similarly numbered culture accessions into this clone record.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate a single canary with `just seed-canary NCBITaxon:103265 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded identity collisions include BacDive 103265, Ornithinimicrobium humiphilum SF006419 (taxon 125288); CIP 103265, Bacillus amyloliquefaciens (1390; strain-level BacDive assignment 692420), with StrainInfo strain 1093/deposit 4419; and DSM 103265, Escherichia coli APEC 9062 (562), with StrainInfo strain 396641/deposit 903209. Their full identifiers and source taxa differ from NCBITaxon:103265.

Other numeric hits are Dactylosporangium NAICONS 103265A, Shigella isolate 103265, MGBC/MarMAG/FLAG/PNUSAS identifiers, nucleotide accession CP103265, run DRR103265, an assembly length and a SeqKit checksum. None independently establishes a target link.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
