# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_cinnamopurpureum.yaml`
- Taxon: `NCBITaxon:466137` (`Penicillium cinnamopurpureum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:466137`, label `Penicillium cinnamopurpureum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_cinnamopurpureum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_chrysogenum.yaml data/taxa/eukaryota/penicillium_chrzaszczii.yaml data/taxa/eukaryota/penicillium_cinereoatrum.yaml data/taxa/eukaryota/penicillium_cinnamopurpureum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55748` contains the seeded identifier with reason `attested rule: Penicillium cinnamopurpureum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:104313` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Eupenicillium cinnamopurpureum`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:104313` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36335`, where `NCBITaxon:466137` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:466137`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found the two culture-from-syntype spellings `NRRL 162` and `NRRL:162`.
- Exact StrainInfo side evidence has 36 direct `NCBITaxon:466137` records and 94 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:466137`.
- The sole merged-ID side row maps old `NCBITaxon:69795` to current `NCBITaxon:466137`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
