# YAML Record Review: Thermoflexibacter ruber

- Repository: `CultureBotAI/TaxonMech`
- Record: `data/taxa/bacteria/thermoflexibacter_ruber.yaml`
- Started UTC: 2026-09-22T16:15:57Z
- Finished UTC: 2026-09-22T16:17:21Z
- Verdict: pass

## Target

- Record: `data/taxa/bacteria/thermoflexibacter_ruber.yaml`
- Identifier: `NCBITaxon:1003`
- Slug: `thermoflexibacter_ruber`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1938003` (`Thermoflexibacter`)

## Validation

- `just validate data/taxa/bacteria/thermoflexibacter_ruber.yaml`: passed.
- `just validate-strict data/taxa/bacteria/oculatella_subterranea_sp1402_zammit_2007_5.yaml data/taxa/bacteria/leptolyngbya_sp_sp1001_zammit_2007_6.yaml data/taxa/bacteria/thermoflexibacter_ruber.yaml data/taxa/eukaryota/lithodesmium_intricatum.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1003` / `Thermoflexibacter ruber`.

- `identifier`, `label`, `rank: SPECIES`, `genetic_code: 11`, `parent_taxon: NCBITaxon:1938003`, and the NCBI `Flexibacter ruber` synonym set match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- The lineage stays within Bacteria through `Pseudomonadati`, `FCB group`, `Bacteroidota/Chlorobiota group`, `Bacteroidota`, `Cytophagia`, `Cytophagales`, `Thermoflexibacteraceae`, then `Thermoflexibacter`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.
- The LPSN row `lpsn:795356` names the validly published correct name, links it to `NCBITaxon:1003` and `GTDB:s__Thermoflexibacter_ruber`, and points to `lpsn:776299` / `Flexibacter ruber` as a synonym.
- The GTDB mapping is a species-level `skos:closeMatch` for `GTDB:s__Thermoflexibacter_ruber` with `genome_count: 1`.

## Evidence

The reviewed source rows support the generated record:

- NCBI supports the exact taxon, the `Flexibacter ruber` synonyms, and the type-material designations for GEY, ATCC 23103, DSM 9560, IFO 16677, LMG 13857, and NBRC 16677.
- LPSN supports the nomenclature entry, the linked `Flexibacter ruber` synonym, type-strain accessions, publication identifiers, and `INSDC:AB078065`.
- BacDive supports one strain, `kgmicrobe.strain:bacdive_3793` / `bacdive:3793`, with designation `GEY` and culture collection IDs `ATCC-23103` and `DSM-9560`.
- GTDB, BV-BRC, GOLD, StrainInfo, and AllTheBacteria rows all match through the DSM 9560 strain or the `SAMN04488541` biosample to the same BacDive strain.
- `source_attestations` match the inspected NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, and MADIN source rows and counts.

An exact `rg --no-ignore --hidden` search over `curation/seed_scope.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the maintained source rows listed above and no same-taxon BactoTraits rows keyed to `NCBITaxon:1003` / `Thermoflexibacter ruber`.

## Completeness

The record has no `comments`, `equivalent_identifiers`, or product-level sections. None are required by the reviewed local evidence. The available LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, ATB, BV-BRC, StrainInfo, culture-collection, genome, project, and sample evidence is represented in the generated taxonomy, nomenclature, mapping, xref, source-attestation, strain, genome, and related-record slots.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- `just validate-history` was not run because this read-only review did not add a `history/` decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `thermoflexibacter_ruber` review.
