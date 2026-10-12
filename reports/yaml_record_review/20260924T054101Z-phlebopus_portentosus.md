# Review: Phlebopus portentosus

- Verdict: pass
- Record: `data/taxa/eukaryota/phlebopus_portentosus.yaml`
- Target: `NCBITaxon:80661`

## Target

The record grounds `Phlebopus portentosus` as an exact seeded NCBI species under `NCBITaxon:150793` (`Phlebopus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 12072.

## Validation

- `just validate data/taxa/eukaryota/phlebopus_portentosus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlebiella_tulasnelloidea.yaml data/taxa/eukaryota/phlebiella_vaga.yaml data/taxa/eukaryota/phlebiopsis_gigantea.yaml data/taxa/eukaryota/phlebopus_portentosus.yaml`: exited successfully
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53357 with the expected reason: `attested rule: Phlebopus portentosus, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Phaeogyroporus portentosus`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 18258 and 86058 map retired `NCBITaxon:150794` and `NCBITaxon:555538` to this identifier; exact retained-row greps found neither old ID in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 12072.
- GOLD aggregate: line 42883 records `organism_count=1` for `NCBITaxon:80661`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 265275-265276 record `K(M) 120755` and `K(M):120755` holotype designations.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

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
