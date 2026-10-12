# Review: Phyllosticta ampelicida

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllosticta_ampelicida.yaml`
- Target: `NCBITaxon:115983`

## Target

The record grounds `Phyllosticta ampelicida` as an exact seeded NCBI species under `NCBITaxon:121621` (`Phyllosticta`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 21186.

## Validation

- `just validate data/taxa/eukaryota/phyllosticta_ampelicida.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phylloporia_minima.yaml data/taxa/eukaryota/phylloporus_rhodoxanthus.yaml data/taxa/eukaryota/phylloporus_sp.yaml data/taxa/eukaryota/phyllosticta_ampelicida.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53821 with the expected reason: `attested rule: Phyllosticta ampelicida, 2 sources incl. NCBI`.
- The NCBI raw row has five exact synonyms, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 22961 maps retired `NCBITaxon:1648145` to this identifier; an exact retained-row grep found no `NCBITaxon:1648145` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 21186.
- GOLD aggregate: line 3428 records `organism_count=3` for `NCBITaxon:115983`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: lines 10410-10411 record `ATCC 200578` and `ATCC:200578` culture-from-epitype designations.
- StrainInfo: 11 direct exact strains and 20 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
