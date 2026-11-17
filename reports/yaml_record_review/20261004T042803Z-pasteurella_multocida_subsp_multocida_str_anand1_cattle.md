# YAML Record Review: Pasteurella multocida subsp. multocida str. Anand1_cattle

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_cattle.yaml`
- Started UTC: 2026-10-04T04:24:57Z
- Finished UTC: 2026-10-04T04:28:03Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:1032867`, Pasteurella multocida subsp. multocida str. Anand1_cattle, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:44283`. It has eleven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. Its three source attestations are NCBITAXON, GOLD and MADIN; its seed event is dated 2026-09-13T17:54:04Z.

Future changes belong to maintained upstream source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, only if inclusion changes, `curation/seed_scope.tsv`. This review does not edit the generated YAML.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_cattle.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pasteurella_multocida_subsp_multocida_str_anand1_cattle.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched the complete backbone lineage, identity/code, own names, scope/PATHS registration, seed text and NCBI attestation. Native source and current NCBI metadata checks were evidence audits, not substitutes for corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220929`, `data/catalog/ncbi_names-0005.jsonl.gz:30241-30242`, PATHS row 13330 and scope row 36144 agree on the exact strain identity. Live NCBI Taxonomy XML and Datasets agree on its label, rank, parent, code and all eleven lineage IDs: 1, 131567, 2, 3379134, 1224, 1236, 135625, 712, 745, 747, 44283. The retained equivalent-name synonym, Pasteurella multocida subsp. multocida strain Anand1_cattle, is supported. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032867)

The current XML also contains Pasteurella multocida subsp. multocida str. Anand1cattle as a misspelling. It is not present in the pinned name projection. This bounded source-version/name-coverage difference does not invalidate the preferred label or exact identifier; a future refresh should preserve the alias's non-exact source class. The name-class handling in `src/taxonmech/ncbi_taxdump.py` was inspected rather than assuming that misspellings are intentionally omitted.

Anand1_poultry (1032866), Anand1_buffalo (1032868) and Anand1_goat (1032869) remain distinct strain taxa. In particular, Anand1_poultry has subsp. gallicida parent 123812, whereas this target has subsp. multocida parent 44283. A shared Anand1 prefix is not an identity key. This target has no GTDB mapping, synonym or xref in the pinned inventories/YAML, so the exact-species-synonym finding from the poultry record does not apply here.

## Evidence

| Assertion | Inspected support and scope |
| --- | --- |
| NCBITAXON, 1 NAME | Backbone/name catalog and live taxonomy agree; the 2026-09-13 snapshot date agrees with the source attestation. |
| GOLD, 1 ORGANISM | `data/raw/gold_organisms.tsv:428` and native `data/gold/organisms.jsonl.gz:10775` identify Go0012232, taxid 1032867, strain Anand1_cattle. The native culture-collection field is empty. |
| MADIN, 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:617` reproduces the aggregate count. Original transformed trait edges were unavailable in the configured upstream checkout; their individual meanings were not independently audited or imported as phenotype assertions. |

Native GOLD project row 10636 connects Gp0012232 to Go0012232, BioProject PRJNA66357 and BioSample SAMN02469639. Analysis row 7948 connects Ga0014357 through that project to GCA_000291645.1, WGS accession ALBY00000000 and IMG 2531839035. The analysis's direct organism field is empty, but its explicit project-to-organism chain supports this association. Organism, project and analysis identifiers are not assemblies or registered culture deposits.

Native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:3181` identifies 1032867.3, the same exact strain/taxid, GCA_000291645.1, PRJNA66357 and SAMN02469639. It has no culture_collection field; the bare strain name is not an eligible culture-identifier join.

The full GenBank catalog row at `data/catalog/ncbi_genbank-0000.jsonl.gz:6861` identifies GCA_000291645.1/ASM29164v1 as current, contig-level, 3,152 contigs and 1,438,517 bp, with the same taxid, strain, project and sample. Live NCBI Datasets independently agrees and marks paired GCF_000291645.1 suppressed. Exact-taxid Assembly ESearch returned one entry; its ESummary, UID 491288, confirms current/latest GenBank and suppressed RefSeq status. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000291645.1/)

The historical RefSeq row `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:1978` preserves GCF_000291645.1 as suppressed, with a 2015-08-27 non-live date. RefSeq uses PRJNA180801, distinct from GenBank's PRJNA66357, while sharing SAMN02469639. Native and live metadata preserve the fragmented-assembly and genome-length-too-small exclusion notes. These are limitations on the genome representation, not evidence that the YAML's taxon identity is wrong. The paired accessions must not be counted as two independent current genomes.

No DOI/PMID or sequence accession is claimed by this YAML. Bulk WGS contigs were not fetched for this taxonomy-scope review, and neither assembly quality nor a functional/clinical phenotype is asserted by the record.

## Completeness

Complete exact-ID inventory scans found no target BacDive, LPSN, GTDB, MediaDive or BactoTraits entry, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Zero strain_count agrees with the documented BacDive-subtree count; it does not assert that no genome exists. The inspected GOLD/BV-BRC sources supply genome context but no eligible registered culture-collection key, so optional strain/deposit links should not be invented.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering bounded 1032867, Anand1 and the complete target stem. All 57 matched lines and their structured contexts were inspected; SOURCE.json files were separately scanned. No target-specific BacDive/StrainInfo deposit or separate history reference was found within those bounds. The existing legacy target-page registration was observed, not reported absent.

An additional ignored-inclusive compressed search of `data/atb` and `data/catalog/allthebacteria.tsv.xz` found no SAMN02469639 or PRJNA66357 match. The numeric collision SAMEA1032867 instead belongs to Streptococcus equi EQUI0154, taxid 148942, assembly GCA/GCF_001176865.1, BV-BRC 148942.102 and ATB run ERR064534/analysis ERZ3067728. It is not this strain's BioSample. A genome-size value of 1032867 in Oscillospiraceae assembly GCA_977957255.1 is also not a taxon-ID match. Anand1_buffalo GCA_000291625.1, Anand1_goat GCA_000219335.2 and Anand1_poultry GCA_000219315.2 were kept separate.

Empty nomenclature and functional fields are appropriate for the inspected strain-scope assertions. No gene, pathway, expression-module, resistance or other mechanistic claim requires representation. iModulonDB is not applicable; its non-use is not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and source scope. The unavailable original Madin trait edges remain an explicitly bounded verification limit, not inferred support for a phenotype.

## Recommended Edits

None required for the reviewed assertions. Do not import the sibling record's GTDB synonym or infer a culture deposit from Anand1_cattle alone.

If source enrichment is authorized later, use maintained upstream transforms and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`, preserving exact source accessions, current versus suppressed statuses and the distinct GenBank/RefSeq BioProjects. During a taxonomy refresh, reconcile the live misspelling with the pinned name inventory without promoting it to an exact synonym.

## Follow-up Checks

After any authorized maintained-input change, run `just seed-canary NCBITaxon:1032867 --force`, inspect the output and repeat both focused validators. No canary ran in this review. Confirm that future genome enrichment retains the current GenBank/suppressed RefSeq distinction and does not imply a registered culture deposit.

Restore the pinned upstream Madin transformed edges before independently reproducing the individual trait assertion. Run the corpus-wide reproduction, reference/history/provenance and product gates before a broader release.

## Additional Notes

An ignored-inclusive inventory of the configured `../../kg-microbe/data` checkout found only its two NLP files, not the original transformed Madin edges. The aggregate match does not claim independent reconstruction of that upstream assertion. Source-native local records and live NCBI metadata were inspected separately and their scope/status differences retained.

No host-range, virulence or clinical inference was made from the cattle strain name or BioSample metadata. No YAML, maintained input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, and prior reports were preserved.
