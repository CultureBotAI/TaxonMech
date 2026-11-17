# YAML Record Review: uncultured gamma proteobacterium TIHP302-03

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_03.yaml`
- Started UTC: 2026-10-04T01:39:45Z
- Finished UTC: 2026-10-04T01:41:36Z
- Verdict: pass

## Target

Read the entire 45-line generated TaxonRecord for `NCBITaxon:103263`, uncultured gamma proteobacterium TIHP302-03. It is a SPECIES-rank environmental clone in BACTERIA under environmental samples (50423), with seven lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. It makes no culture, phenotype, genome-equivalence or causal-graph claim.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_03.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp302_03.yaml` passed for one file with zero errors and refreshed the strict-validator TSV.

Read-only structured checks compared full lineage, inventory matches, source attestation, path, scope and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or independent history references require a target-specific term/reference gate.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:18372` and scientific-name row `data/catalog/ncbi_names-0000.jsonl.gz:38390` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103263&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103263) confirm identifier, label, species rank, parent, code 11 and all seven root-first lineage identifiers. NCBI's environmental-samples division does not negate the Bacteria domain established by the lineage through Pseudomonadati, Pseudomonadota and Gammaproteobacteria.

The full backbone contains no target synonyms or children. Complete structured type-material, merged-ID and dropped inventories contain no own-ID row. SPECIES is the source rank of this placeholder, not a claim of valid formal publication. EXACT does not turn an environmental clone into an isolated culture.

## Evidence

The one NAME assertion and 2026-09-13 snapshot note match the NCBI inventory. `data/taxa/PATHS.tsv:13254` and `curation/seed_scope.tsv:144032` agree on ID, slug and NCBI-only scope reason. The seed event accurately records that scope while retaining SEEDED status.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [AB031591.1](https://www.ncbi.nlm.nih.gov/nuccore/AB031591.1) is a 752-base partial 16S rRNA gene sequence of clone TIHP302-03, genomic DNA, with taxon 103263, an explicit environmental-sample flag and coastal marine sediment as the isolation source.

The entry cites an unpublished community-characterization study by Urakawa, Yoshida, Nishimura and Ohwada, without a PMID or DOI, and direct submission by Urakawa on 1999-08-25. Its study-level references to community analysis and quinone profiling do not demonstrate a phenotype of this particular clone. The record does not infer one, a culture deposit, or a whole genome from the partial marker sequence.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded query result rather than proof that no genome exists anywhere. The sequence browser view was unavailable, but structured GenBank and both taxonomy requests succeeded.

## Completeness

Complete BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventory scans found no exact target row. No descendant taxon or classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` under the source-counting contract.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the whole numeric identifier, label, slug and TIHP302-03 spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 80 matches were accounted for in structured identity context; initially truncated output was recovered by a compact structured reread. Recursive SOURCE.json traversal also included ignored files. Its two matches refer to a BacDive request for source record 103263, not NCBI taxon 103263.

No independently supported target collection deposit, assembly association, extra mapping or separate history record was found within those surfaces. Optional nomenclature, strain, phenotype and graph slots may remain empty. iModulonDB is not applicable to this taxonomy-only environmental-clone record; absence there is not negative biological evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated-file ownership, the environmental-clone identity and SEEDED status. Future authority corrections belong to maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Never join culture or genome records on the bare numeric taxon suffix.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:103263 --force`, inspect its YAML and rerun both focused validators. Run documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

The important excluded namespace collisions are BacDive 103263, Beutenbergia cavernae SF008615 (84757); CIP 103263, Propionimicrobium lymphophilum (33012, with strain-level 1123001); NBRC 103263, Ilumatobacter coccineus (467094, with older genome taxon 1313172); DSM 103263, Escherichia coli APEC 4507 (562); and StrainInfo deposit 103263, Nocardia farcinica ATCC 23826 (37329). Other matches are unrelated sequence/run identifiers, isolate names and assembly length statistics. None supports this environmental clone.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
