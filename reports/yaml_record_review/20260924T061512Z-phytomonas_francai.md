# Review: Phytomonas francai

- Verdict: pass
- Record: `data/taxa/eukaryota/phytomonas_francai.yaml`
- Target: `NCBITaxon:1902498`

## Target

The record grounds `Phytomonas francai` as an exact seeded NCBI species under `NCBITaxon:5706` (`Phytomonas`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 491966.

## Validation

- `just validate data/taxa/eukaryota/phytomonas_francai.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/physocladia_obscura.yaml data/taxa/eukaryota/physocladia_sp.yaml data/taxa/eukaryota/phytomonas_francai.yaml data/taxa/eukaryota/phytophthora_agathidicida.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 61505 with the expected reason: `attested rule: Phytomonas francai, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 491966.
- GOLD aggregate: line 17181 records `organism_count=1` for `NCBITaxon:1902498`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this target.
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
