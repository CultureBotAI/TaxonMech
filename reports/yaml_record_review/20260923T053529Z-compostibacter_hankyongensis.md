# YAML Record Review: Compostibacter hankyongensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/compostibacter_hankyongensis.yaml
- Started UTC: 2026-09-23T05:34:42Z
- Finished UTC: 2026-09-23T05:35:29Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007089`
- Label: `Compostibacter hankyongensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2048112` (`Compostibacter`)
- Maintained path: generated `data/taxa/bacteria/compostibacter_hankyongensis.yaml`; fixes belong in `data/raw/lpsn_names.tsv`, `data/raw/bacdive_strains.tsv`, the genome input tables in `data/raw/`, or `src/taxonmech/seed.py`, depending on source.

The record is a source-rich generated species record with NCBI, LPSN, GTDB, BacDive, GOLD, BV-BRC, NCBI Assembly, and strain-level genome support for type strain JCM 17664.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/compostibacter_hankyongensis.yaml data/taxa/bacteria/conexibacter_sp_bs10.yaml data/taxa/bacteria/dyella_sp_bs13.yaml data/taxa/bacteria/microlunatus_terrae.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/compostibacter_hankyongensis.yaml` | Passed; `linkml-validate` exited successfully. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:210799` and the LPSN row in `data/raw/lpsn_names.tsv:31043` agree on `NCBITaxon:1007089` / `lpsn:794566` as species `Compostibacter hankyongensis` in genus `Compostibacter`. LPSN marks the name legitimate, validly published under the ICNP, and the correct name.

The lineage is carried from NCBI and is internally consistent from `root` through `Bacteria`, `Pseudomonadati`, `FCB group`, `Bacteroidota/Chlorobiota group`, `Bacteroidota`, `Chitinophagia`, `Chitinophagales`, `Chitinophagaceae`, and `Compostibacter`. `grounding_status: EXACT` is appropriate for the NCBI identity.

The GTDB mapping in `data/raw/gtdb_mappings.tsv:1066` is species-level and has one genome. The YAML keeps it on the species record and notes that LPSN links the GTDB species to the taxon's name, so this is not the strain-level GTDB scope bug seen on some NCBI strain records.

## Evidence

- The `nomenclature` block matches `data/raw/lpsn_names.tsv:31043`, including `lpsn:794566`, authority `Siddiqi et al. 2016`, type strain `kgmicrobe.strain:JCM-17664`, PMID `27335062`, DOI accessions `10.1099/ijsem.0.001252` and `10.1099/ijsem.0.001620`, and INSDC accession `JF806525`.
- The NCBI related synonyms `Chitinophaga sp. BS27` and `Compostibacter hankyongensis Siddiqi et al. 2016` match the related-synonym column in `data/raw/ncbitaxon_taxa.tsv:210799`.
- `data/raw/bacdive_strains.tsv:62901` supports one type strain, BacDive ID `140616`, designation `BS27`, and collection IDs `JCM-17664` and `KACC-18745`; the culture-collection rows for both IDs point at `NCBITaxon:1007089`.
- `data/raw/strain_assemblies.tsv:46058-46066` and `data/raw/strain_genome_records.tsv:36101-36105` support the generated BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly projections for JCM 17664.
- `data/raw/strain_related_records.tsv:132907-132926` supports the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records for the generated strain.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-compostibacter_hankyongensis.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, NCBI type-material, LPSN, GTDB, BacDive, culture-collection, GOLD, strain assembly, strain genome, and strain related-record rows supporting the generated fields.
- `strain_count: 1` is complete for the inspected rows: the single BacDive strain row and its genome projections are represented under one generated strain.
- No ATB, StrainInfo, MediaDive, BactoTraits, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing source-rich record. If a future refresh changes the LPSN, GTDB, BacDive, GOLD, BV-BRC, or NCBI Assembly rows, rerun `just validate-strict data/taxa/bacteria/compostibacter_hankyongensis.yaml`, `just validate data/taxa/bacteria/compostibacter_hankyongensis.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

- The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
- `data/raw/ncbi_type_material.tsv` also extracts NCBI `typematerial.dmp` rows for `Compostibacter hankyongensis`; the reviewed record correctly derives `nomenclature` and `is_type_strain` from LPSN and BacDive rather than from NCBI type-material rows alone.
