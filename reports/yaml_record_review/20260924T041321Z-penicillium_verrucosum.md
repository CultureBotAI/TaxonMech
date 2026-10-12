# Review: Penicillium verrucosum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_verrucosum.yaml`
- Target: `NCBITaxon:60171`

## Target

The record grounds `Penicillium verrucosum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7583.

## Validation

- `just validate data/taxa/eukaryota/penicillium_verrucosum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_verhagenii.yaml data/taxa/eukaryota/penicillium_verrucosum.yaml data/taxa/eukaryota/penicillium_virgatum.yaml data/taxa/eukaryota/penicillium_viridicatum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53015 with the expected reason: `attested rule: Penicillium verrucosum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium verrucosum Dierckx, 1901`; the YAML mirrors that value.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7583.
- GOLD aggregate: line 39773 records `organism_count=4` for `NCBITaxon:60171`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: two exact rows at lines 241026-241027, covering culture-from-neotype spellings for `FRR 965`.
- StrainInfo: 130 exact deposit rows and 95 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

None.
