# Review: Phytophthora nicotianae P10297

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_nicotianae_p10297.yaml`
- Target: `NCBITaxon:1317064`

## Target

The record grounds `Phytophthora nicotianae P10297` as an exact seeded NCBI strain under `NCBITaxon:4792` (`Phytophthora nicotianae`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 313628.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_nicotianae_p10297.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_nicotianae_inra_310.yaml data/taxa/eukaryota/phytophthora_nicotianae_p10297.yaml data/taxa/eukaryota/phytophthora_nicotianae_p1569.yaml data/taxa/eukaryota/phytophthora_nicotianae_p1976.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 11 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 59445 with the expected reason: `attested rule: Phytophthora nicotianae P10297, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 313628.
- GOLD aggregate: line 7786 records `organism_count=1` for `NCBITaxon:1317064`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this strain target.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora nicotianae P10297` is a strain-rank NCBI taxon under the `Phytophthora nicotianae` species lineage entry.
