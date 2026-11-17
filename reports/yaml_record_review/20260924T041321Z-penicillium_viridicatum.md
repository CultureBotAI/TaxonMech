# Review: Penicillium viridicatum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_viridicatum.yaml`
- Target: `NCBITaxon:60134`

## Target

The record grounds `Penicillium viridicatum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7576.

## Validation

- `just validate data/taxa/eukaryota/penicillium_viridicatum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_verhagenii.yaml data/taxa/eukaryota/penicillium_verrucosum.yaml data/taxa/eukaryota/penicillium_virgatum.yaml data/taxa/eukaryota/penicillium_viridicatum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53010 with the expected reason: `attested rule: Penicillium viridicatum, 2 sources incl. NCBI`.
- The NCBI raw row has the exact synonym `Penicillium aurantiogriseum var. viridicatum`, no broad synonyms, and two related synonyms, `Penicillium aurantiogriseum var. viridicatum (Westling) Frisvad & Filt. 1990` and `Penicillium viridicatum Westling, 1911`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 67949 maps old ID `NCBITaxon:332753` into `NCBITaxon:60134`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7576.
- GOLD aggregate: line 39766 records `organism_count=2` for `NCBITaxon:60134`, matching the YAML GOLD attestation count; native GOLD organism and project files each have two exact rows, and native GOLD analyses has one exact row for this target.
- NCBI type material: four exact rows at lines 240981-240984, covering culture-from-neotype spellings for `FRR 963` plus neotype spellings for `CBS 390.48`.
- StrainInfo: 233 exact deposit rows and 147 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:332753` ID is consumed only through the merge map, not as a retained source row.
