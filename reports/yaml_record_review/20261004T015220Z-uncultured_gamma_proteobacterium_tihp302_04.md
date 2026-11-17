# YAML Record Review: uncultured gamma proteobacterium TIHP302-04

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_04.yaml`
- Started UTC: 2026-10-04T01:51:30Z
- Finished UTC: 2026-10-04T01:52:20Z
- Verdict: pass

## Target

Read the complete generated TaxonRecord for `NCBITaxon:103264`, uncultured gamma proteobacterium TIHP302-04. It is a SPECIES-rank environmental clone in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, code 11, zero BacDive strains, one NAME assertion and one seed event. It asserts no culture, phenotype, causal graph or genome equivalence.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_04.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_04.yaml` passed for one file with zero errors and refreshed the validator TSV.

Read-only structured checks verified complete lineage, source matches, attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused equivalent was invented. There are no curator-added graph terms or independent history references requiring a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18373` and native scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38391` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103264&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103264) confirm identifier, label, species rank, parent, genetic code and all seven root-first lineage IDs. The environmental-samples division does not conflict with the Bacteria domain established by the lineage through Pseudomonadati, Pseudomonadota and Gammaproteobacteria.

The full backbone has no target synonyms or children. Complete structured type-material, merged-ID and dropped inventories contain no own-ID row. SPECIES is NCBI's rank for this placeholder, not a claim of formal nomenclatural publication. EXACT does not imply an isolated culture. The source identifier and sequence are distinct from the previously inspected TIHP302-03 record; no identity inference is made from the shared clone-series prefix.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13260` and `curation/seed_scope.tsv:144033` agree on ID, slug and NCBI-only scope reason. The seed event faithfully records that reason while retaining SEEDED status.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031592.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031592.1) is a 748-base partial 16S rRNA gene sequence, genomic DNA, with clone TIHP302-04, taxon 103264, an explicit environmental-sample flag and coastal marine sediment as isolation source.

The entry cites an unpublished community-characterization study by Urakawa, Yoshida, Nishimura and Ohwada, without a PMID or DOI, and a direct submission by Urakawa on 1999-08-25. Study-level community analysis and quinone profiling do not establish a clone-specific phenotype. The YAML appropriately avoids inferring such a trait, a culture deposit or a whole genome from this marker record.

Exact Assembly search returned zero with a phrase-not-found warning, which is a bounded query result rather than universal genome absence. Primary taxonomy and GenBank structured endpoints succeeded; conclusions are grounded in their inspected source responses.

## Completeness

Complete BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventory scans found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under source-counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the whole numeric identifier, label, slug and TIHP302-04 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 27 matching lines were inspected in structured context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry.

No independently supported target culture deposit, assembly association, additional source mapping or separate history record was found within those surfaces. Optional nomenclature, strains, phenotype and graph slots need not be filled speculatively. iModulonDB is not applicable to this taxonomy-only environmental-clone record; absence there is not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve source identity, generated-file ownership and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not join culture or genome evidence on the taxon's numeric suffix or the shared clone-series prefix.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103264 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded namespace collisions include CIP 103264, Bacillus aminovorans (29332), and DSM 103264, Escherichia coli APEC 5211 (562). StrainInfo's CIP deposit explicitly carries the former taxon even though its strain-level group says Bacillus. Other matches include CP103264, DRR103264, unrelated MGBC/MarMAG/FLAG/PNUSAS isolate labels, assembly statistics and a checksum fragment. None supports this environmental clone.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
