# Review: Perenniporia fraxinea

- Verdict: pass
- Record: `data/taxa/eukaryota/perenniporia_fraxinea.yaml`
- Target: `NCBITaxon:1350006`

## Target

The record grounds `Perenniporia fraxinea` as an exact seeded NCBI species under `NCBITaxon:81049` (`Perenniporia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 325225.

## Validation

- `just validate data/taxa/eukaryota/perenniporia_fraxinea.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/percolomonas_cosmopolitus.yaml data/taxa/eukaryota/perenniporia_fraxinea.yaml data/taxa/eukaryota/periconia_celtidis.yaml data/taxa/eukaryota/periconia_macrospinosa.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59617 with the expected reason: `attested rule: Perenniporia fraxinea, 2 sources incl. NCBI`.
- The NCBI raw row has five exact synonyms, `Boletus fraxineus`, `Fomes fraxineus`, `Fomitella fraxinea`, `Polyporus fraxineus`, and `Vanderbylia fraxinea`, no broad synonyms, and six related synonyms, `Boletus fraxineus Bull., 1790`, `Fomes fraxineus (Bull.) Cooke, 1885`, `Fomitella fraxinea (Bull.) Imazeki, 1989`, `Perenniporia fraxinea (Bull.) Ryvarden, 1978`, `Polyporus fraxineus (Bull.) Fr., 1821`, and `Vanderbylia fraxinea (Bull.) D.A. Reid, 1973`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 13732 maps old ID `NCBITaxon:1368284` into `NCBITaxon:1350006`, line 20537 maps old ID `NCBITaxon:157708` into `NCBITaxon:1350006`, and line 39992 maps old ID `NCBITaxon:227965` into `NCBITaxon:1350006`; exact retained-row greps of `data/raw/ncbitaxon_taxa.tsv` found no remaining rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 325225.
- GOLD aggregate: line 8516 records `organism_count=1` for `NCBITaxon:1350006`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 73 exact deposit rows and 68 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:1368284`, `NCBITaxon:157708`, and `NCBITaxon:227965` IDs are consumed only through the merge map, not as retained source rows.
