# Review: Phytophthora palmivora

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_palmivora.yaml`
- Target: `NCBITaxon:4796`

## Target

The record grounds `Phytophthora palmivora` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2064.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_palmivora.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_ohioensis_nom_inval.yaml data/taxa/eukaryota/phytophthora_palmivora.yaml data/taxa/eukaryota/phytophthora_pisi.yaml data/taxa/eukaryota/phytophthora_plurivora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 51848 with the expected reason: `attested rule: Phytophthora palmivora, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, one related synonym, and no broad synonyms; the YAML mirrors those four synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:611791` into this identifier at line 88779; an exact retained-row check found no `NCBITaxon:611791` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 2064.
- GOLD aggregate: line 36714 records `organism_count=3` for `NCBITaxon:4796`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have two exact rows for this target.
- NCBI type material: 23 exact rows were found at lines 220579-220601.
- StrainInfo: 152 direct exact strains and 164 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora palmivora` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
