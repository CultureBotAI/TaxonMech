# YAML Record Review: Sphingomonadaceae bacterium R-46192

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonadaceae_bacterium_r_46192.yaml`
- Started UTC: 2026-10-04T01:16:05Z
- Finished UTC: 2026-10-04T01:17:18Z
- Verdict: pass

## Target

Read the complete 51-line generated TaxonRecord for `NCBITaxon:1032619`, Sphingomonadaceae bacterium R-46192. This SPECIES-rank NCBI placeholder belongs to BACTERIA under unclassified Sphingomonadaceae (122612). It carries nine lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME attestation and one seed event. The target was resolved by exact identifier and path before inspecting the separate same-strain-label taxon as context.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sphingomonadaceae_bacterium_r_46192.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/sphingomonadaceae_bacterium_r_46192.yaml` passed: one file, zero errors; the validator's TSV diagnostic was refreshed.

Structured read-only checks compared all carried lineage entries, source inventories, scope, path, attestation and seed-event text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. These checks are not a substitute for corpus reproduction. No curator-added graph identifiers or external history references require a focused term/reference gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220869` and the native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:30161` agree with the record. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032619&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032619) confirm the ID, label, parent, species rank, bacterial domain, genetic code and nine root-first ancestors. These include Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Sphingomonadales and Sphingomonadaceae.

The full backbone scan found no target synonyms or children. Exact structured scans found no own-ID type-material, merged-ID or dropped row. EXACT denotes agreement with the NCBI entity, not a formal species description. The browser page was inaccessible; successful primary structured responses provided the authority evidence.

## Evidence

The single NAME and 2026-09-13 snapshot note reproduce the source inventory. `data/taxa/PATHS.tsv:13245` and `curation/seed_scope.tsv:321242` agree on the target, slug and NCBI-only reason. The 2026-09-13 seed event matches and does not imply human review.

Exact-taxon Nuccore search returned one entry, [FR863524.1](https://www.ncbi.nlm.nih.gov/nuccore/FR863524.1), inspected as GenBank XML: a 597-base partial nodC sequence annotated as N-acetylglucosaminyltransferase, with strain R-46192 and taxon 1032619. Source qualifiers record a root nodule, host spelling `Lotus pendunculatus`, Belgium:Flanders, and collection/identification by Sofie De Meyer. The record cites an unpublished De Meyer and Willems study and direct submission on 2011-05-04, without a PMID or DOI. This is sequence-annotation evidence, not direct proof of nodulation, nitrogen fixation or an entire functional pathway; the YAML asserts none of these.

A contextual live lookup confirms that [NCBI taxon 946933](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/946933) remains separately named Sandaracinobacter sp. R-46192, under Sphingosinicellaceae. Its sole exact-taxonomy sequence, [FR775143.1](https://www.ncbi.nlm.nih.gov/nuccore/FR775143.1), is a 403-base partial 16S rRNA record with strain `R-46192 = t320`, the same source host spelling, Belgian root-nodule provenance, and De Meyer/Willems references; direct submission was 2011-01-19. The shared designation and collection context suggest a relationship but do not prove taxon equivalence or authorize transferring this 16S accession into the reviewed record.

Exact Assembly searches returned zero for each of the two IDs, with phrase-not-found warnings. These bounded queries do not establish global genome absence.

## Completeness

No exact target row occurs in the fully checked BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin or BactoTraits inventories. With no descendants or classified BacDive strain, the zero strain count is supported.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered identifier, label, slug and R-46192 variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All seven hits were inspected. Additional searches for t320 and both sequence accessions yielded seven unrelated alias hits, not target deposits. Recursive SOURCE.json traversal included ignored files and found no target-specific match.

No independent target deposit, genome assertion, cross-taxonomy mapping or standalone history record was found on those searched surfaces. The alternative NCBI taxon appears in its own backbone, native-name and scope rows, not as a supported target synonym. Optional nomenclature, genome, phenotype and graph fields should not be filled by inference. iModulonDB is not applicable: the YAML has no gene, regulator, pathway or transcriptomic claim; nodC was inspected only as external identity context.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the carried YAML assertions. The relationship between the two R-46192 source taxa remains unresolved, and the pass does not authenticate two distinct biological isolates or prove equivalence between them. The record faithfully preserves its own NCBI concept without importing a conflicting classification.

## Recommended Edits

None required for this generated record. Do not merge the taxa, change the lineage, add an exact synonym or transfer sequence evidence based only on the shared strain label. Resolving the apparent upstream split belongs with the primary submitter/NCBI evidence and then the maintained NCBI input, `src/taxonmech/extract.py` and `src/taxonmech/seed.py`. No contact or external mutation was performed.

## Follow-up Checks

Before any proposed merger, inspect explicit specimen provenance, the original strain table and a primary authority decision linking the two IDs. For an authorized source refresh, inspect the updated inventory, regenerate one canary with `just seed-canary NCBITaxon:1032619 --force`, inspect its YAML and rerun both focused validators. Run the full documented reproduction, provenance, history and QC gates before publishing corpus changes.

## Additional Notes

The [Ghent University bibliography](https://biblio.ugent.be/publication/5975719) verifies a related 2015 De Meyer et al. paper, DOI `10.1016/j.soilbio.2015.01.002`, in Soil Biology & Biochemistry 83:1-11. Its accessible page supplies bibliographic metadata, not a strain-level crosswalk; full text there is institution-restricted and publisher access returned 403. Search snippets and review articles were not used to attribute that paper's experimental outcomes to this exact record. This limitation leaves the upstream relationship unresolved, without invalidating the checked NCBI claims.

`GCA_055616015.1` uses isolate number 1032619 but belongs to Streptococcus pneumoniae (1313). Alias t320 also occurs for unrelated Streptococcus macedonicus, Streptococcus pneumoniae, Paenibacillus larvae and Neurospora crassa records. These matches were excluded by their own identities; bare aliases are not culture-collection join keys.

Only this new report was manually written. No record, source inventory, code, scope, history, review status, GitHub item or generated page was changed.

