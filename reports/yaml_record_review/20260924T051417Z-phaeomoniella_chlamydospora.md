# Review: Phaeomoniella chlamydospora

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeomoniella_chlamydospora.yaml`
- Target: `NCBITaxon:158046`

## Target

The record grounds `Phaeomoniella chlamydospora` as an exact seeded NCBI species under `NCBITaxon:158045` (`Phaeomoniella`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 32756.

## Validation

- `just validate data/taxa/eukaryota/phaeomoniella_chlamydospora.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeomonas_parva.yaml data/taxa/eukaryota/phaeomoniella_chlamydospora.yaml data/taxa/eukaryota/phaeosolenia_platensis.yaml data/taxa/eukaryota/phaeosphaeria_elongata.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54143 with the expected reason: `attested rule: Phaeomoniella chlamydospora, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Phaeoacremonium chlamydosporum`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 90572 maps retired `NCBITaxon:65419` to this identifier; an exact retained-row grep found no `NCBITaxon:65419` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 32756.
- GOLD aggregate: line 12745 records `organism_count=1` for `NCBITaxon:158046`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 44075-44076 record `CBS 229.95` and `CBS:229.95` as cultures from the holotype.
- StrainInfo: 13 direct exact strains and 14 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
