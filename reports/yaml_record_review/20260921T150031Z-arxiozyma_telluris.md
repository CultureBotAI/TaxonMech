# YAML Record Review: Arxiozyma telluris

## Target

- File: `data/taxa/eukaryota/arxiozyma_telluris.yaml`
- Identifier: `NCBITaxon:36907`
- Label: `Arxiozyma telluris`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:36906` / `Arxiozyma`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Saccharomycetes` -> `Saccharomycetales` -> `Saccharomycetaceae` -> `Arxiozyma`
- Existing review report: none found for `*arxiozyma_telluris.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arxiozyma_telluris.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arxiozyma_telluris.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:36907`, labelled `Arxiozyma telluris` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:36907` is a `SPECIES` child of `NCBITaxon:36906` / `Arxiozyma`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Kazachstania telluris` and `Saccharomyces telluris`, plus related synonyms `Arxiozyma telluris (Van der Walt) Van der Walt & Yarrow, 1984`, `Kazachstania telluris (Van der Walt) Kurtzman, 2003`, and `Saccharomyces telluris Van der Walt, 1957`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arxiozyma telluris, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:36907`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:36907`, the exact label, and the slug found the expected generated taxon and path rows, raw NCBI/GOLD/scope/type-material rows, legacy page path, the `data/straininfo/strain_links.tsv` `NBRC 1331` false link, and two generated `Geodermatophilus dictyosporus` rows embedding the Arxiozyma StrainInfo IDs. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:36907`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:36907` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0705520`, `Arxiozyma telluris NRRL Y-4302`, with strain and culture collection ID `NRRL Y-4302`.
- GOLD organism `Go0705520` has one project, `Gp0831563`, with BioProject `PRJNA736342` and BioSample `SAMN20341813`; the local native GOLD snapshot has no analysis rows attached directly through `AP ORGANISM GOLD ID` or indirectly through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 34 direct strain rows for `36907` and 2 deposit-only rows. Thirty-five of those candidate IDs are already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`; the unexcluded direct row is `straininfo.strain:64505`.
- Native StrainInfo `straininfo.strain:64505` is an `Arxiozyma telluris` row with `NBRC 1331` as deposit `straininfo.deposit:334983`; its listed sequences are rRNA records, not genome records.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `36907`.
- `data/raw/ncbi_type_material.tsv` has 18 type-material rows for `NCBITaxon:36907`, covering ATCC `13603`, BCRC/CCRC `21514`, CBS `2685`, DBVPG `6288`, IFO `1331`, IGC `2663`, JCM `5298`, and NRRL `YB-4302` spellings.
- A boundary-aware lookup for those type-material tokens and the native GOLD `NRRL Y-4302` spelling found 0 BacDive rows and only `straininfo.strain:64505` in StrainInfo.
- Native BacDive `5816` is a bacterial `Geodermatophilus` record, not an `Arxiozyma` record: its `General` NCBI tax ID is `1523247`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` on `arxiozyma_telluris.yaml` is consistent with the exact source checks: BacDive has no exact NCBI match, the real `Arxiozyma telluris` StrainInfo row has no genome-bearing eligible own deposit, and the native GOLD `NRRL Y-4302` token does not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- Major: `data/raw/bacdive_strains.tsv` contains `kgmicrobe.strain:NBRC-1331` on `kgmicrobe.strain:bacdive_5816`, causing `data/straininfo/strain_links.tsv` to link real `Arxiozyma telluris` deposit `straininfo.deposit:334983` / `NBRC 1331` to bacterial BacDive record `bacdive:5816`. The false join is generated into `data/taxa/bacteria/geodermatophilus_dictyosporus.yaml` as both `straininfo.deposit:334983` and `straininfo.strain:64505` records carrying `taxon_id: NCBITaxon:36907`.

## Recommended Edits

- Do not directly edit `data/taxa/eukaryota/arxiozyma_telluris.yaml`; it is generated and validates strictly.
- Fix the BacDive culture-collection alias source that emits `kgmicrobe.strain:NBRC-1331` for `bacdive_5816` in `data/raw/bacdive_strains.tsv`. If the alias is already present in kg-microbe's BacDive transform, fix it upstream in kg-microbe; if TaxonMech introduced the truncation during extraction, fix `src/taxonmech/extract.py`.
- After the BacDive alias is corrected, rerun the source extraction, `just straininfo-index --apply`, and the seeder so `data/straininfo/strain_links.tsv` drops the `NBRC 1331` false link and the generated `Geodermatophilus dictyosporus` record drops the two `straininfo.strain:64505` / `straininfo.deposit:334983` evidence objects.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arxiozyma_telluris.yaml`, `just validate-strict data/taxa/eukaryota/arxiozyma_telluris.yaml`, and the corresponding strict validation for `data/taxa/bacteria/geodermatophilus_dictyosporus.yaml` after regenerating the affected records.
- Run a bounded no-ignore search for `straininfo.strain:64505`, `straininfo.deposit:334983`, `kgmicrobe.strain:NBRC-1331`, and `NBRC 1331` over `data/straininfo/strain_links.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, and `data/taxa/bacteria/geodermatophilus_dictyosporus.yaml`; after the fix, the false BacDive/StrainInfo link should be absent from those maintained and generated outputs.

## Additional Notes

- The native GOLD organism spells the visible accession as `NRRL Y-4302`, while NCBI type material and StrainInfo spell the NRRL type-material deposit as `NRRL YB-4302`.
