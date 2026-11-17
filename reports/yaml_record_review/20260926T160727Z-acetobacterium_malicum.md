# YAML Record Review: Acetobacterium malicum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_malicum.yaml
- Started UTC: 2026-09-26T16:07:27Z
- Finished UTC: 2026-09-26T16:07:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_malicum.yaml` |
| Identifier | `NCBITaxon:52692` |
| Label | `Acetobacterium malicum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:528679`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_malicum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_malicum.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans.yaml data/taxa/bacteria/acetobacterium_malicum_subsp_dehalogenans_dsm_11527.yaml data/taxa/bacteria/acetobacterium_paludosum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected rich species shape: 9 lineage entries, 1 LPSN nomenclature row, 1 `skos:closeMatch` GTDB mapping, 2 BacDive strains, 4 culture collection identifiers, 20 genome assemblies, 13 genome records, 44 related records, 3 synonyms, 2 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, `GTDB:s__Acetobacterium_malicum`, and `lpsn:772528` in the expected raw, overlay, seed, and legacy path rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. A line-anchored rerun disambiguated fixed-string prefix hits such as `NCBITaxon:526922`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:6619`, the LPSN row at `data/raw/lpsn_names.tsv:14826`, the target GTDB mapping row at `data/raw/gtdb_mappings.tsv:294937`, the target BacDive row, processed GOLD, BactoTraits, Madin, MediaDive, StrainInfo, strain assembly/genome/related-record rows, 9 checked lineage entries with no missing rows or mismatches, and no NCBI merged rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:52692` resolves in the committed NCBI inventory to label
`Acetobacterium malicum`, rank `SPECIES`, parent `NCBITaxon:33951`, genetic
code `11`, one exact synonym, one related synonym, and taxonomy snapshot
`2026-09-13`. The record carries those same identity fields and correctly lands
in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through the `Acetobacterium` genus. There are no
retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN row `lpsn:772528` is the correct, legitimate, validly published
species name for `Acetobacterium malicum`, links to `NCBITaxon:52692` and
`GTDB:s__Acetobacterium_malicum`, lists ATCC 51201 and DSM 4132 as type-strain
deposits, and links the LPSN child `lpsn:65213` synonym retained in YAML.

`data/raw/gtdb_species.tsv:3348` and `data/raw/gtdb_mappings.tsv:294937`
support the target GTDB xref and `skos:closeMatch` mapping, with `genome_count`
4 and parent `GTDB:g__Acetobacterium`.

`data/raw/bacdive_strains.tsv:5291` supports the BacDive 5400 strain with MuME
1 / MuME1 designations and ATCC 51201 plus DSM 4132 culture-collection IDs.
The second generated strain is BacDive 5410, retained through the
`Acetobacterium malicum subsp. dehalogenans DSM 11527` child strain and its
GTDB, BV-BRC, GOLD, NCBI Assembly, and StrainInfo overlays.

The auxiliary attestations are present once each for processed GOLD
(`data/raw/gold_organisms.tsv:37937`), BactoTraits
(`data/raw/bactotraits_taxa.tsv:7399`), Madin et al.
(`data/raw/madin_taxa.tsv:26075`), and MediaDive
(`data/raw/mediadive_taxa.tsv:11168`). The seed event is supported by
`curation/seed_scope.tsv:1832`.

## Completeness

No consequential required claim is absent for this generated rich species
record. The bounded scan found the same target in the normalized LPSN, GTDB,
BacDive, GOLD, BactoTraits, Madin, MediaDive, StrainInfo, and strain overlay
inputs that account for the YAML's source attestations, nomenclature, mapping,
strain, assembly, genome, and related-record sections.

The same `GTDB:s__Acetobacterium_malicum` species maps to the species
`NCBITaxon:52692`, subspecies `NCBITaxon:82116`, and strain
`NCBITaxon:1068975`; each target owns one of those rows in
`data/raw/gtdb_mappings.tsv`, so no mapping is missing here.

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
