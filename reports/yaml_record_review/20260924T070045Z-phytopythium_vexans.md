# Review: Phytopythium vexans

- Verdict: pass
- Record: `data/taxa/eukaryota/phytopythium_vexans.yaml`
- Target: `NCBITaxon:907947`

## Target

The record grounds `Phytopythium vexans` as an exact seeded NCBI species under `NCBITaxon:795339` (`Phytopythium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 191404.

## Validation

- `just validate data/taxa/eukaryota/phytopythium_vexans.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytopythium_vexans.yaml data/taxa/eukaryota/pichia_awuae.yaml data/taxa/eukaryota/pichia_cabralensis.yaml data/taxa/eukaryota/pichia_cactophila.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 56876 with the expected reason: `attested rule: Phytopythium vexans, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, two related synonyms, and no broad synonyms; the YAML mirrors those five synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:42099` into this identifier at line 76920; an exact retained-row check found no `NCBITaxon:42099` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 191404.
- GOLD aggregate: line 44278 records `organism_count=1` for `NCBITaxon:907947`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this species target.
- StrainInfo: 28 direct exact strains and 30 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytopythium vexans` is a species-rank NCBI taxon under the `Phytopythium` genus lineage entry.
