# YAML Record Review: Pyrococcus yayanosii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/pyrococcus_yayanosii.yaml
- Started UTC: 2026-09-23T12:48:06Z
- Finished UTC: 2026-09-23T12:51:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1008460` |
| Label | `Pyrococcus yayanosii` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2260` `Pyrococcus` |
| Status | `grounding_status: EXACT`; `mapping_status: SEEDED` |
| Maintained? | Generated under `data/taxa/`; no direct YAML edit is recommended |

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*pyrococcus_yayanosii.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/myroides_injenensis_m09_0166.yaml data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml data/taxa/archaea/pyrococcus_yayanosii.yaml data/taxa/bacteria/shinella_sp_agr1.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/archaea/pyrococcus_yayanosii.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: this record has no `causal_graphs`, and the product id/label gate is only for curator-added graph nodes |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:211408` supports the record identifier, label, `SPECIES` rank, `NCBITaxon:2260` parent, genetic code `11`, the authority synonym, the `ncbitaxon|bacdive|lpsn|madin_etal` source flags, and the `2026-09-13` NCBI snapshot note. `curation/seed_scope.tsv:22133` carries the matching attested-scope row for this exact species.

The lineage at `data/taxa/archaea/pyrococcus_yayanosii.yaml:6` runs from root through `NCBITaxon:2157` `Archaea` to `NCBITaxon:2260` `Pyrococcus`, so `taxon_domain: ARCHAEA` and the parent agree.

The LPSN row in `data/raw/lpsn_names.tsv:26647` supports `lpsn:789601`, the spelling `Pyrococcus yayanosii`, the `SPECIES` rank, authority `Birrien et al. 2011`, the legitimate and correct-name status, the type-strain designation `kgmicrobe.strain:JCM-16557`, the two DOIs, `PMID:21239564`, `INSDC:EU682399`, and the `GTDB:s__Pyrococcus_yayanosii` xref.

## Evidence

`data/raw/bacdive_strains.tsv:84049` supports a single BacDive strain, `kgmicrobe.strain:bacdive_161812`, for `NCBITaxon:1008460` and ties it to `lpsn:789601` and `kgmicrobe.strain:JCM-16557`; `data/raw/culture_collection_strains.tsv:102517` also associates `JCM-16557` with the same species. The `is_type_strain: true` projection is therefore consistent with the LPSN type-strain designation.

The BacDive and GOLD genome evidence on that strain traces to `data/raw/strain_assemblies.tsv:72670-72671`, `data/raw/strain_genome_records.tsv:56773-56775`, and `data/raw/strain_related_records.tsv:224248-224252`. Those rows support the unversioned BacDive `GCA_000215995`, versioned GOLD `GCA_000215995.1`, `img.taxon:650716080`, `patric:529709.11`, `bioproject:PRJNA66055`, `biosample:SAMN02603867`, and the `gold:Go0011188` / `gold:Gp0011188` / `gold:Ga0030048` chain with the matched `JCM 16557` culture identifier.

`data/raw/madin_taxa.tsv:396` supports the `MADIN` source attestation count of six trait assertions. `data/raw/gtdb_species.tsv:147816` and `data/raw/gtdb_mappings.tsv:295106` show that the GTDB species cluster has one genome and maps to the child strain `NCBITaxon:529709`; no GTDB `taxonomy_mappings` entry is expected on this parent species record.

## Completeness

The record has no curator-added `evidence`, `definition`, `discussions`, or `causal_graphs`, which is expected for a generated taxon record with no reviewed overlay.

Exact gitignore-independent searches across `data/atb/`, `data/straininfo/`, `data/raw/gold_organisms.tsv`, `data/raw/mediadive_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no same-taxon rows for `NCBITaxon:1008460` or the exact `Pyrococcus yayanosii` source identifiers, so no AllTheBacteria, StrainInfo, MediaDive, BactoTraits, merged-id, or dropped-source block is missing.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If a future upstream refresh changes `lpsn:789601`, `bacdive:161812`, the `JCM-16557` type-strain designation, or the GOLD analysis chain, rerun `just seed-canary NCBITaxon:1008460`, `just validate data/taxa/archaea/pyrococcus_yayanosii.yaml`, `just validate-strict data/taxa/archaea/pyrococcus_yayanosii.yaml`, and `just verify-corpus`.

## Additional Notes

Live NCBI, LPSN, BacDive, GOLD, and DOI pages were not used in this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
