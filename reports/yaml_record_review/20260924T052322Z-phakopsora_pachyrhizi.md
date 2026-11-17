# Review: Phakopsora pachyrhizi

- Verdict: pass
- Record: `data/taxa/eukaryota/phakopsora_pachyrhizi.yaml`
- Target: `NCBITaxon:170000`

## Target

The record grounds `Phakopsora pachyrhizi` as an exact seeded NCBI species under `NCBITaxon:169998` (`Phakopsora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 34669.

## Validation

- `just validate data/taxa/eukaryota/phakopsora_pachyrhizi.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phaffomyces_opuntiae.yaml data/taxa/eukaryota/phaffomyces_orbus.yaml data/taxa/eukaryota/phaffomyces_thermotolerans.yaml data/taxa/eukaryota/phakopsora_pachyrhizi.yaml`: exited successfully
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54256 with the expected reason: `attested rule: Phakopsora pachyrhizi, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Physopella pachyrhizi`, related synonym `Phakopsora pachyrhizi Syd. & P. Syd., 1914`, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 34669.
- GOLD aggregate: line 14704 records `organism_count=46` for `NCBITaxon:170000`, matching the YAML GOLD attestation count; native GOLD has 46 exact organism rows, 46 exact project rows, and no exact analysis rows for this target.
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
