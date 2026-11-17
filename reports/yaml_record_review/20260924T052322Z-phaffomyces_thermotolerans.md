# Review: Phaffomyces thermotolerans

- Verdict: pass
- Record: `data/taxa/eukaryota/phaffomyces_thermotolerans.yaml`
- Target: `NCBITaxon:54046`

## Target

The record grounds `Phaffomyces thermotolerans` as an exact seeded NCBI species under `NCBITaxon:83172` (`Phaffomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6828.

## Validation

- `just validate data/taxa/eukaryota/phaffomyces_thermotolerans.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaffomyces_opuntiae.yaml data/taxa/eukaryota/phaffomyces_orbus.yaml data/taxa/eukaryota/phaffomyces_thermotolerans.yaml data/taxa/eukaryota/phakopsora_pachyrhizi.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52906 with the expected reason: `attested rule: Phaffomyces thermotolerans, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 80370 maps retired `NCBITaxon:473113` to this identifier; an exact retained-row grep found no `NCBITaxon:473113` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 6828.
- GOLD aggregate: line 38287 records `organism_count=1` for `NCBITaxon:54046`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 231246-231265 record 20 exact `Pichia opuntiae var. thermotolerans` cultures from type material.
- StrainInfo: 5 direct exact strains and 21 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
