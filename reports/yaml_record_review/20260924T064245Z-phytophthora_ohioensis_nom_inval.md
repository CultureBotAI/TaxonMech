# Review: Phytophthora ohioensis (nom. inval.)

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_ohioensis_nom_inval.yaml`
- Target: `NCBITaxon:508680`

## Target

The record grounds `Phytophthora ohioensis (nom. inval.)` as an exact seeded NCBI species under `NCBITaxon:211524` (`unclassified Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 115586.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_ohioensis_nom_inval.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_ohioensis_nom_inval.yaml data/taxa/eukaryota/phytophthora_palmivora.yaml data/taxa/eukaryota/phytophthora_pisi.yaml data/taxa/eukaryota/phytophthora_plurivora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 11 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 55861 with the expected reason: `attested rule: Phytophthora ohioensis (nom. inval.), 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 115586.
- GOLD aggregate: line 37471 records `organism_count=1` for `NCBITaxon:508680`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this species target.
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

`Phytophthora ohioensis (nom. inval.)` is a species-rank NCBI taxon under the `unclassified Phytophthora` lineage entry.
