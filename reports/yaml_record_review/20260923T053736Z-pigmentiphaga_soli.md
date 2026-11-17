# YAML Record Review: Pigmentiphaga soli

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pigmentiphaga_soli.yaml
- Started UTC: 2026-09-23T05:36:45Z
- Finished UTC: 2026-09-23T05:37:36Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007095`
- Label: `Pigmentiphaga soli`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:152267` (`Pigmentiphaga`)
- Maintained path: generated `data/taxa/bacteria/pigmentiphaga_soli.yaml`; fixes belong in `data/raw/lpsn_names.tsv`, `data/raw/bacdive_strains.tsv`, the genome input tables in `data/raw/`, or `src/taxonmech/seed.py`, depending on source.

The record is a source-rich generated species record with NCBI, LPSN, GTDB, BacDive, GOLD, BV-BRC, and NCBI Assembly support for type strain JCM 17666.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/microlunatus_sp_bs15.yaml data/taxa/bacteria/pedobacter_sp_bs03.yaml data/taxa/bacteria/pigmentiphaga_soli.yaml data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/pigmentiphaga_soli.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:210805` and the LPSN row in `data/raw/lpsn_names.tsv:31192` agree on `NCBITaxon:1007095` / `lpsn:794720` as species `Pigmentiphaga soli` in genus `Pigmentiphaga`. LPSN marks the name legitimate, validly published under the ICNP, and the correct name.

The lineage is carried from NCBI and is internally consistent from `root` through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Alcaligenaceae`, and `Pigmentiphaga`. `grounding_status: EXACT` is appropriate for the NCBI identity.

The GTDB mapping in `data/raw/gtdb_mappings.tsv:1067` is species-level and has one genome. The YAML keeps it on the species record and notes that LPSN links the GTDB species to the taxon's name, so this is not the strain-level GTDB scope bug.

## Evidence

- The `nomenclature` block matches `data/raw/lpsn_names.tsv:31192`, including `lpsn:794720`, authority `Lee et al. 2016`, type strains `JCM-17666` and `KCTC-23577`, PMID `22068507`, DOI accessions `10.1007/s12275-011-1375-8` and `10.1099/ijsem.0.001585`, and INSDC accession `JF806521`.
- The NCBI related synonyms `Pigmentiphaga soli Lee et al. 2016` and `Pigmentiphaga sp. BS12` match the related-synonym column in `data/raw/ncbitaxon_taxa.tsv:210805`.
- `data/raw/bacdive_strains.tsv:84309` supports one type strain, BacDive ID `162073`, and collection IDs `JCM-17666`, `KCTC-23577`, and `KEMB 9004-082`; the culture-collection rows for those IDs point at `NCBITaxon:1007095`.
- `data/raw/strain_assemblies.tsv:73418-73426` and `data/raw/strain_genome_records.tsv:57244-57248` support the generated BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly projections for JCM 17666.
- `data/raw/strain_related_records.tsv:226013-226032` supports the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related records for the generated strain.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pigmentiphaga_soli.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, NCBI type-material, LPSN, GTDB, BacDive, culture-collection, GOLD, strain assembly, strain genome, and strain related-record rows supporting the generated fields.
- `strain_count: 1` is complete for the inspected rows: the single BacDive strain row and its genome projections are represented under one generated strain.
- No ATB, StrainInfo, MediaDive, BactoTraits, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing source-rich record. If a future refresh changes the LPSN, GTDB, BacDive, GOLD, BV-BRC, or NCBI Assembly rows, rerun `just validate-strict data/taxa/bacteria/pigmentiphaga_soli.yaml`, `just validate data/taxa/bacteria/pigmentiphaga_soli.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

- The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
- `data/raw/ncbi_type_material.tsv` also extracts NCBI `typematerial.dmp` rows for `Pigmentiphaga soli`; the reviewed record correctly derives `nomenclature` and `is_type_strain` from LPSN and BacDive rather than from NCBI type-material rows alone.
