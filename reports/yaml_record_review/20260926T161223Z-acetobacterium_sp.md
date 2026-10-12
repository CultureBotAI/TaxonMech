# YAML Record Review: Acetobacterium sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_sp.yaml
- Started UTC: 2026-09-26T16:12:23Z
- Finished UTC: 2026-09-26T16:12:23Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_sp.yaml` |
| Identifier | `NCBITaxon:1872094` |
| Label | `Acetobacterium sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2638182` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:296616`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_psammolithicum.yaml data/taxa/bacteria/acetobacterium_sp.yaml data/taxa/bacteria/acetobacterium_sp_ac1.yaml data/taxa/bacteria/acetobacterium_sp_ag.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected pooled rich shape: 307 YAML lines, 10 lineage entries, 5 source attestations across NCBITAXON, GTDB, BACDIVE, MEDIADIVE, and BACTOTRAITS, 7 `skos:broadMatch` GTDB mappings, 4 BacDive strains, 5 culture collection IDs, 8 related records, 0 genome assemblies, 0 genome records, 0 synonyms, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier, exact label, exact GTDB species IDs, BacDive IDs 5403 through 5406, and the exact DSM/Gra culture IDs in the expected raw, seed, path, GTDB, BacDive, MediaDive, BactoTraits, and ignored report locations across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:489178`, 7 target GTDB mapping rows at `data/raw/gtdb_mappings.tsv:70938` through `data/raw/gtdb_mappings.tsv:70944`, 4 target BacDive rows, 5 target culture-collection rows, the target MediaDive and BactoTraits rows, 10 checked lineage entries with no missing rows or mismatches, and no target-owned rows in LPSN, direct StrainInfo target, strain assembly/genome/related-record, NCBI merged, GOLD, or Madin inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1872094` resolves in the committed NCBI inventory to label
`Acetobacterium sp.`, rank `SPECIES`, parent `NCBITaxon:2638182`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2638182` unclassified
Acetobacterium. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The pooled GTDB mapping set is supported by
`data/raw/gtdb_mappings.tsv:70938` through
`data/raw/gtdb_mappings.tsv:70944`: `GTDB:s__Acetobacterium_carbinolicum`
with `genome_count` 6, `GTDB:s__Acetobacterium_sp022013395` with
`genome_count` 2, and five additional `Acetobacterium` GTDB species with
`genome_count` 1 each, all broad-mapped to `NCBITaxon:1872094`.

The corresponding species rows are present in `data/raw/gtdb_species.tsv` at
lines 3346, 3353, 3354, 3357, 3359, 3360, and 3361 with matching source IDs,
labels, parents, and genome counts. The `GTDB` source attestation is the first
mapped species, with assertion count 6, unit `GENOME`, and notes summarizing
the 6 additional pooled broad matches.

`data/raw/bacdive_strains.tsv:5294` through
`data/raw/bacdive_strains.tsv:5297` support BacDive strains 5403, 5404, 5405,
and 5406, including the KoMAc1, LuTria 3, and LuPhet 1 designations.
`data/raw/culture_collection_strains.tsv` also has the 5 culture identifiers
linked to this target: DSM-2396 at line 72857, DSM-5193 at line 83660,
DSM-8909 at line 87152, DSM-9077 at line 87192, and Gra%20EG%2012 at line
88857.

The four DSM culture IDs also resolve in `data/straininfo/records.jsonl.gz` to
StrainInfo strains 47612, 47902, 48547, and 48577 at JSONL lines 35533, 35806,
36428, and 36456. Those rows support the 8 generated StrainInfo
deposit/strain related records attached below the BacDive strains.

The auxiliary attestations are present for BactoTraits
(`data/raw/bactotraits_taxa.tsv:4275`) and MediaDive
(`data/raw/mediadive_taxa.tsv:5649`). The seed event is supported by
`curation/seed_scope.tsv:21689`.

## Completeness

No consequential required claim is absent for this generated pooled record. The
bounded scan accounts for the normalized GTDB, BacDive, culture-collection,
MediaDive, and BactoTraits rows that drive the YAML mappings, strains, related
records, and source attestations, and found no direct target rows in
normalized GOLD, LPSN, NCBI merged, Madin, strain assembly, or strain genome
inputs.

The exact GTDB scan found expected non-target mappings that reuse two of the
pooled GTDB species. `GTDB:s__Acetobacterium_carbinolicum` also maps to
`NCBITaxon:52690`, `NCBITaxon:1945908`, `NCBITaxon:2184575`, and
`NCBITaxon:3055467`; `GTDB:s__Acetobacterium_sp022013395` also maps to
`NCBITaxon:217139`. Those rows are not target-owned by `NCBITaxon:1872094`,
so they do not imply additional mappings on this generated record.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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
