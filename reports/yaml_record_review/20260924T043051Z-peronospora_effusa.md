# Review: Peronospora effusa

- Verdict: pass
- Record: `data/taxa/eukaryota/peronospora_effusa.yaml`
- Target: `NCBITaxon:542832`

## Target

The record grounds `Peronospora effusa` as an exact seeded NCBI species under `NCBITaxon:70742` (`Peronospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 125853.

## Validation

- `just validate data/taxa/eukaryota/peronospora_effusa.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peroneutypa_scoparia.yaml data/taxa/eukaryota/peronospora_belbahrii.yaml data/taxa/eukaryota/peronospora_effusa.yaml data/taxa/eukaryota/peronospora_tabacina.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55941 with the expected reason: `attested rule: Peronospora effusa, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Peronospora effusa (Grev.) Rabenh., (1854)`; the YAML mirrors that value.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 125853.
- GOLD aggregate: line 38336 records `organism_count=6` for `NCBITaxon:542832`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have six exact rows for this target.
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
