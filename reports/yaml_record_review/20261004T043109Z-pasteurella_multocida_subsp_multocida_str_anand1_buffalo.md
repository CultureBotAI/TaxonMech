# YAML Record Review: Pasteurella multocida subsp. multocida str. Anand1_buffalo

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_buffalo.yaml`
- Started UTC: 2026-10-04T04:29:43Z
- Finished UTC: 2026-10-04T04:31:09Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` denotes `NCBITaxon:1032868`, Pasteurella multocida subsp. multocida str. Anand1_buffalo. Its rank is `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:44283`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`. It has eleven root-first ancestors, one NCBI equivalent-name synonym, zero BacDive strains and NCBITAXON/GOLD/MADIN attestations. The seed event is dated 2026-09-13T17:54:04Z.

Generated YAML is read-only. Future changes belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_buffalo.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_buffalo.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured evidence comparisons matched backbone identity, code, complete lineage, names, scope/PATHS registration, seed text and source counts. These are not substitutes for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

The target matches `data/raw/ncbitaxon_taxa.tsv:220930`, name-catalog shard 0005 rows 30243-30244, PATHS row 13331 and scope row 36145. Live NCBI Taxonomy EFetch and Datasets confirm the label, strain rank, parent 44283, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 135625, 712, 745, 747, 44283. The retained equivalent name, Pasteurella multocida subsp. multocida strain Anand1_buffalo, is supported. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032868)

The browser page returned by the web tool was marked as crawled eight months ago and says no rank; current EFetch and Datasets both say strain, agreeing with the pinned backbone. This source-version difference is preserved rather than used to downgrade the record. Current XML also lists the misspelling Anand1buffalo, absent from the pinned name catalog; a refresh should retain its non-exact name class.

Anand1_cattle (1032867), Anand1_goat (1032869) and Anand1_poultry (1032866) are distinct taxa, not synonyms. The poultry taxon additionally has subsp. gallicida parent 123812. There is no target GTDB mapping/xref/synonym in the inspected inventories/YAML; no exact-species-synonym finding is inferred from a neighboring record.

## Evidence

| Assertion | Inspected source and scope |
| --- | --- |
| NCBITAXON, 1 NAME | Complete pinned backbone/name records and live taxonomy agree. Snapshot date 2026-09-13 is source-faithful. |
| GOLD, 1 ORGANISM | `data/raw/gold_organisms.tsv:429` and `data/gold/organisms.jsonl.gz:10140` identify Go0011542, taxid 1032868 and strain Anand1_buffalo; the culture-collection field is empty. |
| MADIN, 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:618` supports the aggregate count. Original transformed trait edges are unavailable in the configured upstream checkout, so no individual trait is independently validated or inferred. |

Native GOLD project row 9994 identifies Gp0011542, organism Go0011542, BioProject PRJNA66359 and BioSample SAMN02469637. Analysis row 9191 identifies Ga0015637, explicitly connects through that project, and supplies GCA_000291625.1, WGS accession ALBX00000000 and IMG 2534682188. Its direct organism field is empty, but the project-to-organism chain resolves consistently. GOLD organism/project/analysis IDs are not assemblies or deposits.

Native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3182` identifies genome 1032868.3, taxid 1032868, GCA_000291625.1 and the same project/sample. Its strain field is verbatim `Anand buffalo`, while its genome name contains Anand1_buffalo. Explicit taxid/accession agreement supplies context; neither spelling is a culture-collection join key, and the record supplies no culture_collection field.

The full GenBank row `data/catalog/ncbi_genbank-0000.jsonl.gz:6860` and live Datasets identify current GCA_000291625.1/ASM29162v1, contig-level with 2,188 contigs and 2,045,610 bp. Live exact-taxid Assembly ESearch returned one entry, UID 491268; its ESummary confirms latest GenBank and suppressed paired GCF_000291625.1. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000291625.1/)

The full historical RefSeq row in shard 0000 at row 1977 preserves suppressed status and the 2015-08-27 non-live date. RefSeq BioProject PRJNA180800 is distinct from GenBank PRJNA66359, while both use SAMN02469637. Native/live metadata retain the fragmented-assembly exclusion note. The paired accessions are not two independent current genomes, and the quality note does not invalidate the taxon identity. No DOI/PMID or sequence accession is asserted in the YAML, and bulk WGS contigs were not fetched for this taxonomy-scope review.

The NCBI browser's BacDive LinkOut resolves to W-9217, BacDive 11729, with DSM 16031, ATCC 43137 and NCTC 10322, classified under 747/44283. This is the subspecies type strain, not evidence that Anand1_buffalo is one of those deposits. [BacDive 11729](https://bacdive.dsmz.de/strain/11729)

## Completeness

Complete exact-ID inventory scans found no target BacDive, LPSN, GTDB, MediaDive or BactoTraits row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Zero strain_count agrees with the BacDive-subtree definition, not a claim of genome absence. Optional culture links should remain empty without an eligible registered deposit match.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 1032868, Anand1 and the target stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 56 matched lines and structured contexts were inspected; SOURCE.json files were separately scanned. No target-specific BacDive/StrainInfo deposit or separate history reference was found within these bounds. The legacy page registration at row 784 exists.

An additional ignored-inclusive compressed search in `data/atb` and `data/catalog/allthebacteria.tsv.xz` found no SAMN02469637 or PRJNA66359 match. SAMEA1032868 is a numeric collision belonging to Streptococcus equi EQUI0015, taxid 148942, GCA/GCF_001176885.1, BV-BRC 148942.104, GTDB RS_GCF_001176885.1 and ATB ERR059727/ERZ3067722. Its GOLD project and sample references do not belong to this target.

No causal graph, gene, resistance, pathway or transcriptomics claim is present. Empty functional fields are appropriate, and iModulonDB is not applicable rather than negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed assertions. Unavailable original Madin trait edges remain a bounded verification limit.

## Recommended Edits

None required. Any future enrichment must preserve source-native strain spelling, supplied accession versions, explicit GOLD chains, current versus suppressed assembly statuses and distinct BioProjects. Do not import the W-9217 deposits or sibling Anand1 GTDB mappings. During an authorized taxonomy refresh, reconcile the additional misspelling without promoting it to an exact synonym.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:1032868 --force`, inspect the result and repeat both focused validators. No canary ran here. Recheck source statuses and deposit evidence before adding genome links. Restore the pinned original Madin edges before independently reproducing their derivation, and run corpus-wide gates before broader release.

## Additional Notes

An ignored-inclusive inventory of `../../kg-microbe/data` found only `nlp/output/Output.zip` and `nlp/stopwords/stopwords.txt`, not the original transformed Madin edges. The raw aggregate comparison does not claim independent validation of those edges.

No host-range, virulence or clinical inference was made from the strain name or BioSample. No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
