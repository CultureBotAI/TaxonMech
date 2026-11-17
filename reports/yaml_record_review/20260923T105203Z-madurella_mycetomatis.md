# YAML Record Review: Madurella mycetomatis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/madurella_mycetomatis.yaml
- Started UTC: 2026-09-23T10:49:19Z
- Finished UTC: 2026-09-23T10:52:03Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/madurella_mycetomatis.yaml`.

| Field | Value |
|---|---|
| identifier | `NCBITaxon:100816` |
| label | `Madurella mycetomatis` |
| rank | `SPECIES` |
| domain | `EUKARYOTA` |
| parent | `NCBITaxon:100815` / `Madurella` |
| generated status | Seeded from pinned source inventories in `data/raw/`, `data/atb/`, and `data/straininfo/` |

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-madurella_mycetomatis.md'` | Passed: no prior report for this stem; `find` inspected ignored report files. |
| `find data/taxa/eukaryota -maxdepth 1 -type f -name 'madurella_mycetomatis.yaml'` | Passed: found exactly `data/taxa/eukaryota/madurella_mycetomatis.yaml`. |
| `find data/taxa -type f -name 'madurella_mycetomatis.yaml'` | Passed: found the same single eukaryote YAML file; this exact whole-corpus file search included ignored files. |
| `just validate-strict data/taxa/archaea/halorubrum_sp_yim_93749.yaml data/taxa/eukaryota/madurella_mycetomatis.yaml data/taxa/archaea/haloterrigena_sp_yim_93589.yaml data/taxa/archaea/natronococcus_sp_yim_93654.yaml` | Passed: 4 files scanned, 0 files with errors, 0 total error rows. |
| `just validate data/taxa/eukaryota/madurella_mycetomatis.yaml` | Passed: LinkML validation reported no issues. |

`just validate-products` was skipped because this taxon has no `causal_graphs`. `just validate-history` was skipped because this read-only review did not add a history decision. The full-corpus `just verify-corpus` gate was skipped for this individual review batch because these reports do not edit generated taxon YAML.

## Identity and Grounding

The record consistently denotes the eukaryotic fungal species `NCBITaxon:100816`, `Madurella mycetomatis`.

- `data/raw/ncbitaxon_taxa.tsv` supports the curated identifier, label, rank, parent `NCBITaxon:100815`, genetic code `1`, exact synonyms `Madurella ikedae` and `Streptothrix mycetomatis Laveran, 1902`, and related authority-string synonym `Madurella mycetomatis (Laveran) Brumpt, 1905`.
- `data/raw/gold_organisms.tsv` reports one GOLD organism for `NCBITaxon:100816`, matching the GOLD source attestation.
- The Eukaryota-to-Fungi-to-Sordariales lineage is compatible with the NCBI parent chain materialized in the record.
- The record has no nomenclature, GTDB mapping, xrefs, strains, or causal graph; exact local searches found no same-taxon rows from LPSN, GTDB, BacDive, ATB, StrainInfo, or NCBI Assembly that should have populated those sections.

## Evidence

The source projection is internally supported. Exact `rg --no-ignore --hidden` searches for `NCBITaxon:100816` and `Madurella mycetomatis` over `data/raw/`, `data/atb/`, and `data/straininfo/` found the NCBI row, one GOLD count row, and NCBI type-material rows for `Streptothrix mycetomatis`.

No external live source pages were used; the pinned NCBI and GOLD rows are the reviewed source of truth for this generated record.

## Completeness

No consequential gaps were found.

- `strain_count: 0` is consistent with the absence of exact BacDive, ATB, StrainInfo, NCBI Assembly, and GTDB genome rows for `NCBITaxon:100816`.
- `source_attestations` correctly records 1 NCBI name and 1 GOLD organism.
- `data/raw/ncbi_type_material.tsv` carries raw neotype strings for the older `Streptothrix mycetomatis` name; TaxonMech currently derives structured `nomenclature` and type-strain flags from LPSN rather than NCBI `typematerial.dmp`, so those raw NCBI rows are not by themselves an omitted generated block.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is needed. If LPSN or strain-provider rows are added for this taxon in future source snapshots, rerun source seeding and the narrow validators used above.

## Additional Notes

This review was read-only. Future generated-field changes should be made in the source seed inputs or `src/taxonmech/seed.py`, not by hand-editing this YAML.
