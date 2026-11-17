# YAML Record Review: Cryomorpha ignava

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/cryomorpha_ignava.yaml
- Started UTC: 2026-09-30T08:28:59Z
- Finished UTC: 2026-09-30T08:28:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/cryomorpha_ignava.yaml` |
| Identifier | `NCBITaxon:101383` |
| Label | `Cryomorpha ignava` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:246876` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a source-rich generated Cryomorpha species record,
with path pinned by `data/taxa/PATHS.tsv:7006`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/cryomorpha_ignava.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 273 YAML lines, 11 lineage entries, 6 source attestations, 2 NCBI related synonyms, 1 LPSN nomenclature entry, 3 GTDB taxonomy mappings, 2 xrefs, 1 BacDive strain, 1 genome assembly, 2 genome records, 6 related records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101383` in the expected seed, NCBI, LPSN, GTDB, GOLD, MADIN, BacDive, culture-collection, type-material, StrainInfo, genome, YAML, and `data/taxa/PATHS.tsv` rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17517`, 11 checked lineage entries, 1 BacDive row, 3 culture-collection rows, 1 LPSN row, 3 GTDB rows, 1 MADIN row, 2 native GOLD organism rows, 1 native GOLD project row, 1 native GOLD analysis row, 1 GOLD aggregate row, 1 assembly row, 2 genome rows, 2 GOLD related rows, 4 StrainInfo related rows, 9 type-material rows, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101383` resolves to `Cryomorpha ignava`, rank `SPECIES`,
parent `NCBITaxon:246876`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:246876` Cryomorpha. The bounded scan found no NCBI merge row and no
retained old-id row.

## Evidence

LPSN row `lpsn:783712` supports the ICNP name, `GTDB:s__Cryomorpha_ignava`
cross-reference, LMG/CIP type-strain designations, three publications, and
`INSDC:AF170738`.

The BacDive strain `bacdive:134650` supports `kgmicrobe.strain:bacdive_134650`,
the ACAM, CIP, and LMG culture-collection identifiers, one contig assembly,
and IMG and PATRIC genome records for strain QSSC 1-22.

## Completeness

The three serialized `skos:broadMatch` GTDB mappings cover
`GTDB:s__Cryomorpha_ignava`, `GTDB:s__PHOS-HE28_sp019638085`, and
`GTDB:s__PHOS-HE28_sp040391235`.

No MediaDive, BactoTraits, StrainInfo assembly, StrainInfo exclusion, or NCBI
merge row is filed for this exact NCBI taxon.

## Findings

No findings.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

No follow-up needed.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
The NCBI related synonyms are the authority string and Cytophaga-like QSSC1-22.
NCBI provides 9 type-material strings, all covered by the BacDive/LPSN strain cluster.
StrainInfo strain 86440 contributes LMG 21436 and CIP 107453 deposit evidence.
GOLD related rows attach `gold:Go0028495` to the CIP 107453 strain.
Native GOLD additionally has organism `Go0573606` and project `Gp0548267`.
The BacDive assembly is `ncbi.assembly:GCA_010686655`.
The BacDive genome records are IMG `2994203344` and PATRIC `101383.4`.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 273-line YAML shape includes source-rich strain and genome sections.
The bounded scan found no exact MediaDive or BactoTraits row.
The source set includes BACDIVE, GOLD, GTDB, LPSN, MADIN, and NCBITAXON.
The digit-boundary `NCBITaxon:` probe avoided neighboring identifiers.
The ignored report probe included gitignored files.
