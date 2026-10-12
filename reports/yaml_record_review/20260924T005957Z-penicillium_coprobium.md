# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_coprobium.yaml`
- Taxon: `NCBITaxon:293379` (`Penicillium coprobium`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:293379`, label `Penicillium coprobium`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_coprobium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_confertum.yaml data/taxa/eukaryota/penicillium_consobrinum.yaml data/taxa/eukaryota/penicillium_coprobium.yaml data/taxa/eukaryota/penicillium_coprophilum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55035` contains the seeded identifier with reason `attested rule: Penicillium coprobium, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:59900` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:59900` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:28928`, where `NCBITaxon:293379` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:293379`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found the two `type material` spellings `CBS 561.90` and `CBS:561.90`.
- Exact StrainInfo side evidence has eight direct `NCBITaxon:293379` records and 10 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:293379`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
