# YAML Record Review: Candidatus Blochmanniella pennsylvanica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_blochmanniella_pennsylvanica.yaml
- Started UTC: 2026-10-01T11:04:58Z
- Finished UTC: 2026-10-01T11:04:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/candidatus_blochmanniella_pennsylvanica.yaml` |
| Identifier | `NCBITaxon:101534` |
| Label | `Candidatus Blochmanniella pennsylvanica` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:203804` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB/MADIN/NCBITaxon Candidatus Blochmanniella record,
with path pinned by `data/taxa/PATHS.tsv:8593`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_blochmanniella_pennsylvanica.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 97 YAML lines, 12 lineage entries, 3 source attestations across NCBITAXON, GTDB, and MADIN, 5 synonyms, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101534` in the expected seed, NCBI, MADIN, GTDB, NCBI merge, strain-child NCBI/YAML, target YAML, and `data/taxa/PATHS.tsv` rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Multi-source local scan | Confirmed direct MADIN `assertion_count` 2, GTDB `skos:closeMatch` with `genome_count` 3, and the retained merge from `NCBITaxon:203803`; the NCBI-only bounded helper rejected this intentional multi-source record with `NCBI source mismatch`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101534` resolves to `Candidatus Blochmanniella pennsylvanica`, rank `SPECIES`,
parent `NCBITaxon:203804`, genetic code `11`, source set `ncbitaxon|gtdb|madin_etal`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 12 committed NCBI rows, ending at
`NCBITaxon:203804` Candidatus Blochmanniella. All lineage identifiers resolved
without a missing row.

## Evidence

The NCBI row supports the Candidatus Blochmanniella pennsylvanica identity.
The GTDB row contributes a close species mapping over 3 genomes,
and the MADIN row contributes 2 trait assertions filed directly under this taxon.

The retained merge maps `NCBITaxon:203803` into this target,
and the exact target has no direct GOLD, BacDive, StrainInfo, or type-material row.

## Completeness

No BacDive, LPSN, direct GOLD, MediaDive, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly,
normalized genome, or exact-target related-record row is filed.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

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
`strain_count: 0` is expected because the BPEN strain child is a separate taxon record.
The rank is the NCBI retained rank for this Candidatus Blochmanniella record.
The parent is NCBI's Candidatus Blochmanniella genus.
Four NCBI synonyms and one GTDB synonym were present.
The GTDB closeMatch contributes `GTDB:s__Blochmanniella_pennsylvanica`.
MADIN contributes 2 trait assertions filed directly under this taxon.
The retained NCBI merge from `NCBITaxon:203803` preserves identity.
Twelve NCBI lineage rows are expected.
The twelve-line lineage reaches Candidatus Blochmanniella.
The 97-line YAML shape omits strain and genome sections.
The target has no direct GOLD evidence.
The record has one MADIN row.
The source set is `ncbitaxon|gtdb|madin_etal`.
The exact `NCBITaxon:` probe found one GTDB mapping.
The ignored report probe included gitignored files.
