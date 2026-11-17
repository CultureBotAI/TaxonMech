# YAML Record Review: Salmonella enterica subsp. enterica serovar Paratyphi B str. SARA42

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_sara42.yaml
- Started UTC: 2026-10-03T03:11:55Z
- Finished UTC: 2026-10-03T03:11:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_sara42.yaml` |
| Identifier | `NCBITaxon:1029977` |
| Label | `Salmonella enterica subsp. enterica serovar Paratyphi B str. SARA42` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:57045` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Salmonella strain record, with path pinned by
`data/taxa/PATHS.tsv:12407`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_sara42.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/sporosarcina_sp_dab_ata116.yaml data/taxa/bacteria/sporosarcina_sp_dab_ata9.yaml data/taxa/bacteria/sporosarcina_sp_dab_ata92.yaml data/taxa/bacteria/sporosarcina_sp_dab_m0r50.yaml data/taxa/bacteria/sporosarcina_sp_dab_mor51.yaml data/taxa/bacteria/pseudomonas_sp_pct01.yaml data/taxa/bacteria/pseudomonas_sp_pts02.yaml data/taxa/bacteria/dechloromonas_sp_enrichment_culture_clone_u_co_culture_2.yaml data/taxa/bacteria/stenotrophomonas_sp_enrichment_culture_clone_u_co_culture_1.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_sara42.yaml` | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 87 YAML lines, 12 lineage entries, 3 source attestations, 1 taxonomy mapping, 2 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` source scan | Found `NCBITaxon:1029977` in the expected seed, NCBI, GOLD, exact GTDB mapping, and legacy path rows; found no exact StrainInfo, ATB, BacDive, MediaDive, BactoTraits, or target-specific LPSN row. |
| Exact first-column NCBITaxon lineage scan | Found all 12 expected lineage IDs in `data/raw/ncbitaxon_taxa.tsv`; labels and ranks agree with the generated YAML. |
| Prior report probe | Found no existing `reports/yaml_record_review/*salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_sara42.md` report, with ignored files included. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1029977` resolves to label `Salmonella enterica subsp. enterica
serovar Paratyphi B str. SARA42`, rank `STRAIN`, parent `NCBITaxon:57045`,
genetic code `11`, NCBI/GTDB/GOLD source set, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and ends at `NCBITaxon:57045` Salmonella enterica
subsp. enterica serovar Paratyphi B under subspecies `NCBITaxon:59201`.

## Evidence

`data/raw/ncbitaxon_taxa.tsv:220174` supports the record identifier, label,
rank, parent, genetic code, NCBI synonym, three retained source families, and
2026-09-13 snapshot date.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1265` supports the generated
`GTDB:s__Salmonella_enterica` `skos:closeMatch` with 21527 genomes, its
matching synonym, and its xref. `data/raw/gold_organisms.tsv:369` supports the
GOLD organism assertion count of 1. The seed event is supported by
`curation/seed_scope.tsv:36110`, and the legacy generated page path is carried
by `curation/legacy_page_paths.tsv:701`.

## Completeness

No consequential required generated claim is absent for this record. The exact
source scan accounted for the expected NCBI, GTDB, GOLD, seed, legacy path,
and generated YAML inputs and found no omitted exact strain inventory row.

The `GTDB:s__Salmonella_enterica` species key maps to many Salmonella strain
taxa in the raw GTDB mapping table; the generated mapping on this record uses
the exact `NCBITaxon:1029977` closeMatch row.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

This was a read-only generated-record review; it did not append history,
promote `mapping_status`, or touch YAML.
The NCBI exact synonym for the expanded `strain SARA42` spelling is expected.
The GTDB exact synonym, taxonomy mapping, and xref are expected.
No `nomenclature` section is expected.
No strain, genome, or causal graph section is expected.
Twelve NCBI lineage rows are expected.
The ignored exact-ID and prior-report probes included gitignored files.
