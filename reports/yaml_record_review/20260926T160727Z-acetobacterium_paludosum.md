# YAML Record Review: Acetobacterium paludosum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_paludosum.yaml
- Started UTC: 2026-09-26T16:07:27Z
- Finished UTC: 2026-09-26T16:07:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_paludosum.yaml` |
| Identifier | `NCBITaxon:52693` |
| Label | `Acetobacterium paludosum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:528683`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_paludosum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_malicum.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml data/taxa/bacteria/acetobacterium_paludosum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected rich species shape: 9 lineage entries, 1 LPSN nomenclature row, 1 `skos:closeMatch` GTDB mapping, 1 BacDive strain, 1 culture collection identifier, 16 genome assemblies, 11 genome records, 30 related records, 1 NCBITaxon related synonym, 2 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, `GTDB:s__Acetobacterium_paludosum`, and `lpsn:772529` in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. A line-anchored rerun disambiguated fixed-string prefix hits such as `NCBITaxon:526923`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:6620`, the LPSN row at `data/raw/lpsn_names.tsv:14827`, the target GTDB mapping row at `data/raw/gtdb_mappings.tsv:294938`, the target BacDive row, processed GOLD, BactoTraits, Madin, MediaDive, StrainInfo, strain assembly/genome/related-record rows, 9 checked lineage entries with no missing rows or mismatches, and no NCBI merged rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:52693` resolves in the committed NCBI inventory to label
`Acetobacterium paludosum`, rank `SPECIES`, parent `NCBITaxon:33951`, genetic
code `11`, one related synonym, and taxonomy snapshot `2026-09-13`. The record
carries those same identity fields and correctly lands in the `bacteria` path
bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through the `Acetobacterium` genus. There are no
retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN row `lpsn:772529` is the correct, legitimate, validly published
species name for `Acetobacterium paludosum`, links to `NCBITaxon:52693` and
`GTDB:s__Acetobacterium_paludosum`, lists ATCC 51793 and DSM 8237 as
type-strain deposits, and supplies the two DOI references and `INSDC:X96958`
sequence accession retained in YAML.

`data/raw/gtdb_species.tsv:3349` and `data/raw/gtdb_mappings.tsv:294938`
support the single GTDB species xref and `skos:closeMatch` mapping, with
`genome_count` 2 and parent `GTDB:g__Acetobacterium`.

`data/raw/bacdive_strains.tsv:5298` supports the single `BACDIVE` strain block
for BacDive 5407, designation `Z-4092, Z-B12`, and the DSM 8237
culture-collection identifier. The processed strain rows support the generated
DSM 8237 assemblies, genomes, and related records from BacDive, BV-BRC, GOLD,
GTDB, NCBI Assembly, StrainInfo, and AllTheBacteria.

The auxiliary attestations are present once each for processed GOLD
(`data/raw/gold_organisms.tsv:37940`), BactoTraits
(`data/raw/bactotraits_taxa.tsv:7400`), Madin et al.
(`data/raw/madin_taxa.tsv:26076`), and MediaDive
(`data/raw/mediadive_taxa.tsv:11169`). The seed event is supported by
`curation/seed_scope.tsv:1833`.

## Completeness

No consequential required claim is absent for this generated rich species
record. The bounded scan found the same target in the normalized LPSN, GTDB,
BacDive, GOLD, BactoTraits, Madin, MediaDive, StrainInfo, and strain overlay
inputs that account for the YAML's source attestations, nomenclature, mapping,
strain, assembly, genome, and related-record sections.

The scan also found 4 native GOLD organisms, 2 native GOLD projects, 2 native
GOLD analyses, one direct StrainInfo row with ATCC 51793 and DSM 8237 deposits,
2 StrainInfo assembly rows, 3 StrainInfo related records, and 6 exact NCBI
type-material rows for this taxon. There were no NCBI merged-ID rows and no
curator-authored causal graphs or definitions to carry into the YAML.

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
