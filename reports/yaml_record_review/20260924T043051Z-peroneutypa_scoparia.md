# Review: Peroneutypa scoparia

- Verdict: pass
- Record: `data/taxa/eukaryota/peroneutypa_scoparia.yaml`
- Target: `NCBITaxon:1736665`

## Target

The record grounds `Peroneutypa scoparia` as an exact seeded NCBI species under `NCBITaxon:889755` (`Peroneutypa`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 453703.

## Validation

- `just validate data/taxa/eukaryota/peroneutypa_scoparia.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peroneutypa_scoparia.yaml data/taxa/eukaryota/peronospora_belbahrii.yaml data/taxa/eukaryota/peronospora_effusa.yaml data/taxa/eukaryota/peronospora_tabacina.yaml`: exited successfully
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 61177 with the expected reason: `attested rule: Peroneutypa scoparia, 2 sources incl. NCBI`.
- The NCBI raw row has four exact synonyms, `Eutypa scoparia`, `Eutypella scoparia`, `Peroneutypella scoparia`, and `Sphaeria scoparia`, no broad synonyms, and four related synonyms, `Eutypa scoparia (Schwein.) L.C.Tiffany & J.C.Gilman 1965`, `Eutypella scoparia (Schwein.) Ellis & Everh. 1892`, `Peroneutypa scoparia (Schwein.) Carmarn & A.I. Romero, 2006`, and `Sphaeria scoparia Schwein., 1822`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 14978 maps old ID `NCBITaxon:140560` into `NCBITaxon:1736665`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 453703.
- GOLD aggregate: line 15056 records `organism_count=1` for `NCBITaxon:1736665`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: eight exact deposit rows and eight direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:140560` ID is consumed only through the merge map, not as a retained source row.
