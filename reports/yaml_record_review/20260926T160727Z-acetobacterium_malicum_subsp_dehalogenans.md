# YAML Record Review: Acetobacterium malicum subsp. dehalogenans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml
- Started UTC: 2026-09-26T16:07:27Z
- Finished UTC: 2026-09-26T16:07:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml` |
| Identifier | `NCBITaxon:82116` |
| Label | `Acetobacterium malicum subsp. dehalogenans` |
| Class | `TaxonRecord` |
| Rank | `SUBSPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:52692` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:593041`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_malicum.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml data/taxa/bacteria/acetobacterium_paludosum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected subspecies shape: 10 lineage entries, 0 LPSN nomenclature rows, 1 `skos:closeMatch` GTDB mapping, 1 BacDive strain classified as child `NCBITaxon:1068975`, 14 genome assemblies, 10 genome records, 32 related records, 4 synonyms, 1 xref, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, and `GTDB:s__Acetobacterium_malicum` in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:12341`, the GTDB mapping row at `data/raw/gtdb_mappings.tsv:311844`, the BacDive 5410 classification covering both `NCBITaxon:82116` and child `NCBITaxon:1068975`, the same-subspecies StrainInfo rows, 10 checked lineage entries with no missing rows or mismatches, and no same-taxon LPSN, GOLD, MediaDive, Madin, BactoTraits, or NCBI merged rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:82116` resolves in the committed NCBI inventory to label
`Acetobacterium malicum subsp. dehalogenans`, rank `SUBSPECIES`, parent
`NCBITaxon:52692`, genetic code `11`, one exact synonym, two related synonyms,
and taxonomy snapshot `2026-09-13`. The record carries those same identity
fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through parent species
`NCBITaxon:52692` / `Acetobacterium malicum`.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row, including
`Acetobacterium dehalogenans` as an exact synonym and both related NCBI
synonyms for the old dehalogenans name and the current Spring et al. 2025
subspecies name.

`data/raw/gtdb_species.tsv:3348` and `data/raw/gtdb_mappings.tsv:311844`
support the GTDB xref and `skos:closeMatch` mapping to the shared
`GTDB:s__Acetobacterium_malicum` species.

BacDive 5410 is classified as both the subspecies and its child DSM 11527
strain, and the generated strain block correctly keeps
`classified_as: NCBITaxon:1068975`. `data/straininfo/assemblies.tsv:10034`
and `data/straininfo/related_records.tsv.gz` rows 226545-226546 provide the
same-subspecies StrainInfo evidence for DSM 11527.

The seed event is supported by `curation/seed_scope.tsv:64021`, which records
`NCBITaxon:82116` as added on `2026-09-13` with reason
`attested rule: Acetobacterium malicum subsp. dehalogenans, 2 sources incl.
NCBI`.

## Completeness

No consequential required claim is absent for this generated subspecies record.
The bounded scan found no same-taxon GOLD aggregate, native GOLD, MediaDive,
Madin, BactoTraits, NCBI merged-ID, or final same-taxon raw strain rows keyed
to `NCBITaxon:82116`. The strain-specific blocks are generated through the
BacDive 5410 child strain classification rather than by rewriting the child
rows to the subspecies taxon.

LPSN contains `lpsn:65212` for `Acetobacterium malicum dehalogenans`, but that
row does not carry an NCBITaxon or GTDB ID in the normalized input; the empty
LPSN nomenclature section is therefore consistent with the current mapper.

The exact ignored-aware history/report scan found no prior history or ignored
review report mentioning this target before this report was written; ignored
files under `reports/` were included.

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

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
