# YAML Record Review: Rummeliibacillus pycnus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rummeliibacillus_pycnus.yaml
- Started UTC: 2026-09-28T02:49:25Z
- Finished UTC: 2026-09-28T02:49:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/rummeliibacillus_pycnus.yaml` |
| Identifier | `NCBITaxon:101070` |
| Label | `Rummeliibacillus pycnus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:648802` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multi-source Rummeliibacillus species record,
with path pinned by `data/taxa/PATHS.tsv:3822`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/rummeliibacillus_pycnus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_nrs_156.yaml data/taxa/bacteria/burkholderia_sp_l5p12.yaml data/taxa/bacteria/bacillus_sp_nk2003.yaml data/taxa/bacteria/rummeliibacillus_pycnus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1262 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 3 GTDB broadMatch mappings, 9 synonyms, 2 xrefs, 6 BacDive strains, 10 genome assemblies, 7 genome records, 57 related rows, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:101070` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17394`, 9 checked lineage rows, 1 LPSN row, 3 GTDB broadMatch rows, 1 GOLD aggregate row, 4 native GOLD organisms, 1 GOLD project, 1 GOLD analysis, 6 BacDive rows, 3 NCBI merge rows, 10 type-material rows, and retained MediaDive, MADIN, BactoTraits, and StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101070` resolves to `Rummeliibacillus pycnus`, rank `SPECIES`,
parent `NCBITaxon:648802`, genetic code `11`, source set with eight upstreams,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:648802` genus `Rummeliibacillus`; three old NCBI ids merge here.

## Evidence

The NCBI row supports the current species name, parent, genetic code, two
exact synonyms, six related synonyms, eight upstream source flags, and the
2026-09-13 snapshot date.

LPSN `lpsn:787881` supplies the legitimate correct-name nomenclature row,
four type-strain designations, three publications, accession `INSDC:AB271739`,
the LPSN xref, and the `Bacillus pycnus` synonym.

GTDB contributes three `skos:broadMatch` mappings. GOLD contributes 4 organism
rows and DSM 15030 project/analysis rows. BacDive contributes 6 strains;
MediaDive, MADIN, BactoTraits, BV-BRC, NCBI Assembly, and StrainInfo add rows.

## Completeness

No native `data/raw/gtdb_species.tsv`, StrainInfo exclusion, definition,
or causal-graph row was filed. The normalized raw inventories account for the
generated assembly, genome, and related-record counts under this exact NCBI taxon.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
`strain_count: 6` is expected from the exact BacDive rows.
Two of the six BacDive strains are currently flagged as type strains.
The LPSN type designations are DSM-15030, JCM-11075, NBRC-101231, and NRRL-NRS-1691.
The three GTDB mappings are intentionally broad matches with one genome each.
GOLD contributes four native organisms, one project, and one analysis row.
StrainInfo contributes one DSM 15030 assembly and 23 related rows.
Old ids 101072, 101073, and 101074 all merge into this taxon.
The LPSN synonym contributes Bacillus pycnus as a related synonym.
The NCBI synonyms add 2 exact and 6 related synonyms.
The 1262-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
