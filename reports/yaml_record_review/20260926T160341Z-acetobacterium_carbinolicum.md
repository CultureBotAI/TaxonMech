# YAML Record Review: Acetobacterium carbinolicum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_carbinolicum.yaml
- Started UTC: 2026-09-26T16:03:41Z
- Finished UTC: 2026-09-26T16:03:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_carbinolicum.yaml` |
| Identifier | `NCBITaxon:52690` |
| Label | `Acetobacterium carbinolicum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:528677`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_carbinolicum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_bakii.yaml data/taxa/bacteria/acetobacterium_carbinolicum.yaml data/taxa/bacteria/acetobacterium_carbinolicum_subsp_kysingense.yaml data/taxa/bacteria/acetobacterium_fimetarium.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected rich species shape: 9 lineage entries, 1 LPSN nomenclature row, 1 `skos:closeMatch` GTDB mapping, 2 BacDive strains, 4 culture collection identifiers, 10 genome assemblies, 5 genome records, 33 related records, 1 NCBITaxon related synonym, 2 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, `GTDB:s__Acetobacterium_carbinolicum`, and `lpsn:772525` in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:6617`, the LPSN row at `data/raw/lpsn_names.tsv:14824`, the target GTDB mapping row at `data/raw/gtdb_mappings.tsv:294935`, the target BacDive row, processed GOLD, BactoTraits, Madin, MediaDive, StrainInfo, strain assembly/genome/related-record rows, 9 checked lineage entries with no missing rows or mismatches, and no NCBI merged rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:52690` resolves in the committed NCBI inventory to label
`Acetobacterium carbinolicum`, rank `SPECIES`, parent `NCBITaxon:33951`,
genetic code `11`, one related synonym, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through the `Acetobacterium` genus. There are no
retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN row `lpsn:772525` is the correct, legitimate, validly published
species name for `Acetobacterium carbinolicum`, links to `NCBITaxon:52690` and
`GTDB:s__Acetobacterium_carbinolicum`, lists DSM 2925 as the type-strain
deposit, and supplies the two DOI references and `INSDC:X96956` sequence
accession retained in YAML.

`data/raw/gtdb_species.tsv:3346` and `data/raw/gtdb_mappings.tsv:294935`
support the target GTDB xref and `skos:closeMatch` mapping, with `genome_count`
6 and parent `GTDB:g__Acetobacterium`.

`data/raw/bacdive_strains.tsv:5290` supports the BacDive 5399 strain with DSM
2925 and WoProp 1 identifiers. The second generated strain, BacDive 24007 /
DSM 16427, comes from the subspecies record; its GTDB and NCBI Assembly rows
are keyed to the parent species `NCBITaxon:52690`, so the parent species
correctly retains those assemblies, genomes, and related records.

The auxiliary attestations are present once each for processed GOLD
(`data/raw/gold_organisms.tsv:37935`), BactoTraits
(`data/raw/bactotraits_taxa.tsv:7397`), Madin et al.
(`data/raw/madin_taxa.tsv:26073`), and MediaDive
(`data/raw/mediadive_taxa.tsv:11166`). The seed event is supported by
`curation/seed_scope.tsv:1830`.

## Completeness

No consequential required claim is absent for this generated rich species
record. The bounded scan found the same target in the normalized LPSN, GTDB,
BacDive, GOLD, BactoTraits, Madin, MediaDive, StrainInfo, and strain overlay
inputs that account for the YAML's source attestations, nomenclature, mapping,
strain, assembly, genome, and related-record sections.

The same `GTDB:s__Acetobacterium_carbinolicum` species also maps to
`NCBITaxon:1872094`, `NCBITaxon:1945908`, `NCBITaxon:2184575`, and
`NCBITaxon:3055467` in `data/raw/gtdb_mappings.tsv`; those rows are owned by
other Acetobacterium sp. targets and do not require additional mapping rows on
`NCBITaxon:52690`.

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
