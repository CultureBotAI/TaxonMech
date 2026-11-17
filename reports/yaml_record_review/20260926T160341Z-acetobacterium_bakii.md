# YAML Record Review: Acetobacterium bakii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_bakii.yaml
- Started UTC: 2026-09-26T16:03:41Z
- Finished UTC: 2026-09-26T16:03:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_bakii.yaml` |
| Identifier | `NCBITaxon:52689` |
| Label | `Acetobacterium bakii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:528676`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_bakii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_bakii.yaml data/taxa/bacteria/acetobacterium_carbinolicum.yaml data/taxa/bacteria/acetobacterium_carbinolicum_subsp_kysingense.yaml data/taxa/bacteria/acetobacterium_fimetarium.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected rich species shape: 9 lineage entries, 1 LPSN nomenclature row, 1 `skos:closeMatch` GTDB mapping, 1 BacDive strain, 1 culture collection identifier, 20 genome assemblies, 15 genome records, 42 related records, 1 NCBITaxon related synonym, 2 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, `GTDB:s__Acetobacterium_bakii`, and `lpsn:772524` in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:6616`, the LPSN row at `data/raw/lpsn_names.tsv:14823`, the target GTDB mapping row at `data/raw/gtdb_mappings.tsv:294934`, the target BacDive row, processed GOLD, BactoTraits, Madin, MediaDive, StrainInfo, strain assembly/genome/related-record rows, 9 checked lineage entries with no missing rows or mismatches, and no NCBI merged rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:52689` resolves in the committed NCBI inventory to label
`Acetobacterium bakii`, rank `SPECIES`, parent `NCBITaxon:33951`, genetic code
`11`, one related synonym, and taxonomy snapshot `2026-09-13`. The record
carries those same identity fields and correctly lands in the `bacteria` path
bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through the `Acetobacterium` genus. There are no
retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN row `lpsn:772524` is the correct, legitimate, validly published
species name for `Acetobacterium bakii`, links to `NCBITaxon:52689` and
`GTDB:s__Acetobacterium_bakii`, lists ATCC 51794 and DSM 8239 as type-strain
deposits, and supplies the two DOI references and `INSDC:X96960` sequence
accession retained in YAML.

`data/raw/gtdb_species.tsv:3345` and `data/raw/gtdb_mappings.tsv:294934`
support the single GTDB species xref and `skos:closeMatch` mapping, with
`genome_count` 4 and parent `GTDB:g__Acetobacterium`.

`data/raw/bacdive_strains.tsv:5300` supports the single `BACDIVE` strain block
for BacDive 5409, designation `Z-4391, Z-S11`, and DSM 8239 culture-collection
identifier. The processed strain rows support the generated DSM 8239
assemblies, genomes, and related records from BacDive, BV-BRC, GOLD, GTDB,
NCBI Assembly, StrainInfo, and AllTheBacteria.

The auxiliary attestations are present once each for processed GOLD
(`data/raw/gold_organisms.tsv:37934`), BactoTraits
(`data/raw/bactotraits_taxa.tsv:7396`), Madin et al.
(`data/raw/madin_taxa.tsv:26072`), and MediaDive
(`data/raw/mediadive_taxa.tsv:11165`). The seed event is supported by
`curation/seed_scope.tsv:1829`.

## Completeness

No consequential required claim is absent for this generated rich species
record. The bounded scan found the same target in the normalized LPSN, GTDB,
BacDive, GOLD, BactoTraits, Madin, MediaDive, StrainInfo, and strain overlay
inputs that account for the YAML's source attestations, nomenclature, mapping,
strain, assembly, genome, and related-record sections.

The scan also found 4 native GOLD organisms, 3 native GOLD projects, 3 native
GOLD analyses, one direct StrainInfo row with ATCC 51794 and DSM 8239 deposits,
2 StrainInfo assembly rows, 3 StrainInfo related records, and 6 exact NCBI
type-material rows for this taxon. There were no NCBI merged-ID rows and no
curator-authored causal graphs or definitions to carry into the YAML.

The exact ignored-aware source scan found no prior history or ignored review
report mentioning this target before this report was written; ignored files
under `reports/` were included.

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
