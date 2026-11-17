# Review: Pichia occidentalis

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_occidentalis.yaml`
- Target: `NCBITaxon:54552`

## Target

The record grounds `Pichia occidentalis` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6938.

## Validation

- `just validate data/taxa/eukaryota/pichia_occidentalis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_nakasei.yaml data/taxa/eukaryota/pichia_nanzhaoensis.yaml data/taxa/eukaryota/pichia_norvegensis.yaml data/taxa/eukaryota/pichia_occidentalis.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52932 with the expected reason: `attested rule: Pichia occidentalis, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, two related synonyms, and no broad synonyms; the YAML mirrors those three synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 6938.
- GOLD aggregate: line 38406 records `organism_count=3` for `NCBITaxon:54552`, matching the YAML GOLD attestation count; native GOLD has three exact organism rows, four exact project rows, and four exact analysis rows for this target.
- NCBI type material: 16 exact rows were found at lines 232250-232265.
- StrainInfo: 18 direct exact strains and 52 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia occidentalis` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
