# YAML Record Review: Brevibacterium hankyongi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/brevibacterium_hankyongi.yaml
- Started UTC: 2026-09-23T05:32:40Z
- Finished UTC: 2026-09-23T05:33:26Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007087`
- Label: `Brevibacterium hankyongi`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1696` (`Brevibacterium`)
- Maintained path: generated `data/taxa/bacteria/brevibacterium_hankyongi.yaml`; fixes belong in `data/raw/lpsn_names.tsv`, `data/raw/bacdive_strains.tsv`, `data/straininfo/strain_links.tsv`, `data/raw/`, or `src/taxonmech/seed.py`, depending on source.

The record is a source-rich generated species record with NCBI, LPSN, BacDive, culture-collection, and StrainInfo support.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml data/taxa/bacteria/micrococcus_sp_kc5.yaml data/taxa/bacteria/brevibacterium_hankyongi.yaml data/taxa/bacteria/chitinophaga_sp_bs20.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/brevibacterium_hankyongi.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:210797` and the LPSN row in `data/raw/lpsn_names.tsv:33064` agree on `NCBITaxon:1007087` / `lpsn:797919` as species `Brevibacterium hankyongi` in genus `Brevibacterium`. LPSN marks the name legitimate, validly published under the ICNP, and the correct name.

The lineage is internally consistent from `root` through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Brevibacteriaceae`, and `Brevibacterium`. `grounding_status: EXACT` is appropriate for the NCBI identity, and the LPSN xref is supported.

## Evidence

- The `nomenclature` block matches `data/raw/lpsn_names.tsv:33064`, including `name_id: lpsn:797919`, authority `Choi et al. 2018`, type strain `kgmicrobe.strain:LMG-29562`, PMID `30063198`, DOI accessions `10.1099/ijsem.0.002886` and `10.1099/ijsem.0.003030`, and INSDC accession `JF806518`.
- The NCBI related synonyms `Brevibacterium hankyongi Choi et al. 2018` and `Brevibacterium sp. BS05` match the related-synonym column in `data/raw/ncbitaxon_taxa.tsv:210797`.
- The BacDive row `data/raw/bacdive_strains.tsv:82122` supports one type strain, designation `BS05`, and collection IDs `JCM-30949`, `KACC-18875`, and `LMG-29562`.
- The culture-collection rows in `data/raw/culture_collection_strains.tsv` attach those three collection IDs to `NCBITaxon:1007087`.
- `data/straininfo/strain_links.tsv:58855` links BacDive strain `kgmicrobe.strain:bacdive_159885` to StrainInfo strain `273103`, deposit `26857`, LMG 29562, and DOI `10.60712/SI-ID273103.1`; the generated strain's two related records correctly represent the deposit and strain views of that link.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-brevibacterium_hankyongi.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, NCBI type-material, LPSN, BacDive, culture-collection, and StrainInfo rows supporting the generated fields.
- `strain_count: 1` is complete for the inspected rows: one BacDive strain row was found, and its three culture-collection IDs plus the StrainInfo link are represented under the single generated strain.
- No GTDB, GOLD, ATB, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing source-rich record. If a future refresh changes the LPSN, BacDive, or StrainInfo rows, rerun `just validate-strict data/taxa/bacteria/brevibacterium_hankyongi.yaml`, `just validate data/taxa/bacteria/brevibacterium_hankyongi.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

- The live LPSN, BacDive, StrainInfo, and NCBI lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
- `data/raw/ncbi_type_material.tsv` also extracts NCBI `typematerial.dmp` rows for `Brevibacterium hankyongi`; the reviewed record correctly derives `nomenclature` and `is_type_strain` from LPSN, BacDive, and StrainInfo rather than from NCBI type-material rows alone.
