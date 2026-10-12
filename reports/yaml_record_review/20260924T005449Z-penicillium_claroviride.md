# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_claroviride.yaml`
- Taxon: `NCBITaxon:3078876` (`Penicillium claroviride`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3078876`, label `Penicillium claroviride`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_claroviride.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_citrinum.yaml data/taxa/eukaryota/penicillium_claroviride.yaml data/taxa/eukaryota/penicillium_clavigerum.yaml data/taxa/eukaryota/penicillium_clavistipitatum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63538` contains the seeded identifier with reason `attested rule: Penicillium claroviride, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:595231` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:595231` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31188`, where `NCBITaxon:3078876` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:3078876`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found nine culture-from-holotype spellings centered on `CBS 147458`, `CMW 56197`, and `CN014D2`, plus four holotype spellings centered on `PREM 63221`.

## Completeness

- BacDive, retained retired old-ID, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:3078876`.
- The sole merged-ID side row maps old `NCBITaxon:2796924` to current `NCBITaxon:3078876`, and the YAML correctly uses the current identifier.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
