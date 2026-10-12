# Review: Phlyctochytrium arcticum

- Verdict: pass
- Record: `data/taxa/eukaryota/phlyctochytrium_arcticum.yaml`
- Target: `NCBITaxon:1117335`

## Target

The record grounds `Phlyctochytrium arcticum` as an exact seeded NCBI species under `NCBITaxon:4819` (`Phlyctochytrium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 241072.

## Validation

- `just validate data/taxa/eukaryota/phlyctochytrium_arcticum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlegmacium_sp.yaml data/taxa/eukaryota/phleogena_faginea.yaml data/taxa/eukaryota/phlyctochytrium_arcticum.yaml data/taxa/eukaryota/phlyctochytrium_aureliae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 57710 with the expected reason: `attested rule: Phlyctochytrium arcticum, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, one related synonym, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 66888 maps retired `NCBITaxon:324678` to this identifier; an exact retained-row grep found no `NCBITaxon:324678` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 241072.
- GOLD aggregate: line 2102 records `organism_count=1` for `NCBITaxon:1117335`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: lines 7095-7100 record `ATCC 18785`, `ATCC:18785`, `CBS 666.73`, `CBS:666.73`, `IMI 143636`, and `IMI:143636` type-material designations.
- StrainInfo: 3 direct exact strains and 5 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
