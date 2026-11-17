# YAML Record Review: Pasteurellaceae bacterium Delphsu4a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurellaceae_bacterium_delphsu4a.yaml`
- Started UTC: 2026-10-04T01:30:47Z
- Finished UTC: 2026-10-04T01:32:15Z
- Verdict: pass

## Target

Read the entire 51-line generated TaxonRecord for `NCBITaxon:1032624`, Pasteurellaceae bacterium Delphsu4a. It is a SPECIES-rank NCBI placeholder in BACTERIA under unclassified Pasteurellaceae (67757), with nine lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero classified BacDive strains, one NAME assertion and one seed event. There are no phenotype, gene-function, genome-equivalence or causal-graph claims.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurellaceae_bacterium_delphsu4a.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pasteurellaceae_bacterium_delphsu4a.yaml` passed for one file with zero errors, refreshing the validator TSV.

Read-only structured comparisons checked the full lineage, source matches, scope, paths, attestation and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. The YAML has no curator-added graph identifiers or independent history references requiring a target-specific term/reference gate.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:220872` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30179` agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032624&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032624) confirm ID, label, parent, species rank, domain, genetic code and all nine root-first lineage IDs. The chain includes Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae.

The full backbone scan found no synonyms or children, and complete structured type-material, merged-ID and dropped inventories contain no own-ID row. A strain-like name does not authorize changing NCBI's rank. EXACT describes the mapping to the source taxon, not formal nomenclatural validity. The direct browser view failed, but both structured taxonomy endpoints succeeded.

## Evidence

The one NCBITAXON NAME assertion and 2026-09-13 snapshot note reproduce the source inventory. `data/taxa/PATHS.tsv:13249` and `curation/seed_scope.tsv:321244` agree on the identifier, slug and NCBI-only scope reason. The 2026-09-13 seed event faithfully repeats that scope and remains SEEDED.

Exact-taxon Nuccore search returned one sequence. Inspected GenBank XML for [HM626589.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626589.1) identifies a 471-base partial RpoB coding sequence, genomic DNA, strain Delphsu4a and taxon 1032624. Source qualifiers identify Canada and a harbor-seal host. Direct submission was by Christensen, Bisgaard and Hansen on 2010-07-05.

The entry's other reference is marked unpublished, with no PMID or DOI. Its title concerns Pasteurellaceae prevalence and a proposed name spelled Otariobacter oris. That study-level title does not assign every sampled isolate to that proposed species or establish a taxon merge. The live sequence and taxonomy still identify Delphsu4a separately, and the YAML correctly makes no inferred Otariodibacter synonym or mapping. Partial RpoB evidence is neither a whole genome nor direct evidence of a phenotype.

Exact Assembly search returned zero with a phrase-not-found warning. This is a bounded query result, not proof that no genome exists anywhere. The NAME count is not a count of sequence accessions.

## Completeness

Complete scans of the BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. With no descendant taxon or classified BacDive strain, `strain_count: 0` is supported under the repository's counting rules.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the identifier, label, slug and Delphsu4a spelling variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 15 matching lines were inspected in context. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry. An ignored-inclusive report-directory search found no previous report for this slug.

No independent target deposit, assembly association, extra mapping or separate history record was found within those searched surfaces. Bare Delphsu4a is not a registered collection accession. Optional nomenclature, strains, phenotype and graph slots need not be invented. iModulonDB is not applicable to the taxonomy-only YAML; the externally inspected RpoB annotation is context, not a gene claim in the record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve the generated-file boundary and SEEDED status. Future taxonomic corrections belong to the maintained NCBI/source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope changes belong to `curation/seed_scope.tsv`. A later species reassignment needs an explicit isolate-level authority crosswalk, not the shared study title.

## Follow-up Checks

For an authorized refresh, inspect changed authority evidence, regenerate one canary with `just seed-canary NCBITaxon:1032624 --force`, inspect the result and rerun both focused validators. Run the documented full reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Excluded numeric collisions include SAMEA1032624, which describes Streptococcus pneumoniae strain 462956; a GOLD IMG identifier containing 1032624; Campylobacter jejuni assembly GCA_010326245.1; an ATB checksum fragment; and unrelated run/sample identifiers SRR11032624 and SAMN41032624. None is taxonomic or strain evidence for this target.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or rendered page was changed.
