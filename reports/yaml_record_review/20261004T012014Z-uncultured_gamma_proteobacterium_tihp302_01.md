# YAML Record Review: uncultured gamma proteobacterium TIHP302-01

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_01.yaml`
- Started UTC: 2026-10-04T01:19:05Z
- Finished UTC: 2026-10-04T01:20:14Z
- Verdict: pass

## Target

Read all 45 lines of this generated TaxonRecord for `NCBITaxon:103262`. It represents the SPECIES-rank environmental placeholder uncultured gamma proteobacterium TIHP302-01, not a cultured strain or a formally described species. The record carries BACTERIA, parent 50423, seven lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON attestation and one seed event.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_01.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_01.yaml` passed: one file, zero errors; the validator's diagnostic TSV was refreshed.

Structured comparisons checked all carried lineage entries, exact source rows, scope, path, attestation and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No focused reproduction substitute was claimed. There are no curator-added graph identifiers or standalone history references requiring target-specific term/reference validation.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18371` and `data/catalog/ncbi_names-0000.jsonl.gz:38389` support the ID, label and source name class. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103262&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103262) agree on the species rank, parent, code 11 and root-first lineage: 1, 131567, 2, 3379134, 1224, 1236, 50423. The environmental-samples parent has NO_RANK. NCBI's environmental division does not contradict the Bacteria domain shown in its lineage.

The complete backbone scan found no synonyms or children. Full structured scans found no own-ID type-material, merged-ID or dropped entry. EXACT denotes identity with this NCBI placeholder, not formal nomenclatural validity. Browser access failed, but the primary structured responses succeeded.

## Evidence

The single NAME assertion and 2026-09-13 snapshot note reproduce the inventory. `data/taxa/PATHS.tsv:13246` and `curation/seed_scope.tsv:144031` agree on the identifier, slug and NCBI-only scope reason. The 2026-09-13 seed event matches that reason; the record is not presented as human REVIEWED.

Exact-taxon Nuccore search returned one entry, [AB031590.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031590.1), inspected as GenBank XML. It is a 679-base partial 16S rRNA sequence with clone TIHP302-01, taxon 103262, coastal marine sediment as isolation source and an environmental-sample qualifier. References name an unpublished Urakawa, Yoshida, Nishimura and Ohwada community study and a direct submission dated 1999-08-25; no PMID or DOI is supplied. The submitter's institutional address is not an independent sampling-location claim. Community profiling does not establish a phenotype or pathway for the clone.

Exact Assembly search returned zero with a phrase-not-found warning. This bounded result is not proof of universal genome absence.

## Completeness

Structured scans found no exact taxon row in BacDive, LPSN, GTDB mappings, GOLD aggregate, MediaDive, Madin or BactoTraits. No descendants supply additional BacDive entries, so `strain_count: 0` is supported.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and clone spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 26 matched lines were inspected in their source context. Recursive SOURCE.json traversal included ignored files and found no target-specific match.

No independent target deposit, genome assertion, nomenclatural mapping or standalone history record was found on those searched surfaces. The optional culture, genome, phenotype and causal-graph slots correctly remain empty. A clone's 16S sequence is not a missing required genome link. iModulonDB is not applicable to the record's taxonomy-only claims.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the generated-file boundary and SEEDED status. Future source corrections belong in the maintained authority input and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Do not use matching numbers or clone labels as collection-deposit join keys.

## Follow-up Checks

For an authorized source refresh, inspect the changed evidence, regenerate a single canary with `just seed-canary NCBITaxon:103262 --force`, inspect its YAML and rerun both focused validators. Use the full documented reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

CIP 103262 belongs to the Cutibacterium/Propionibacterium granulosum context (33011 and strain 1160719), while DSM 103262 is Escherichia coli APEC 4500 (562). Their BacDive, LPSN, NCBI synonym and StrainInfo records do not refer to this environmental clone. GTDB `RS_GCF_001714765.1` is Serratia sp. ISTD04 (1261032); its match is a contig N50 of 103262, not the target identifier.

Only this new report was manually written. No taxon, source inventory, code, scope, history, review status, GitHub item or generated page was changed.

