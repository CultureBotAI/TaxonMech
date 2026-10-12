# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_diabolicalicense.yaml`
- Taxon: `NCBITaxon:2100459` (`Penicillium diabolicalicense`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2100459`, label `Penicillium diabolicalicense`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_diabolicalicense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_desertorum.yaml data/taxa/eukaryota/penicillium_diabolicalicense.yaml data/taxa/eukaryota/penicillium_digitatum.yaml data/taxa/eukaryota/penicillium_dipodomyicola.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62349` contains the seeded identifier with reason `attested rule: Penicillium diabolicalicense, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:518182` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:518182` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20103`, where `NCBITaxon:2100459` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2100459`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 10 rows on lines 84322-84331: 7 `culture-from-holotype` spellings centered on CBS 140967, DAOM 250542, and KAS 1726; 1 `culture-from-type-material` spelling at ICMP 21193; and 2 `holotype` spellings centered on PDD 107542.
- Exact StrainInfo side evidence has 1 direct `NCBITaxon:2100459` record and 1 deposit for ICMP 21193.
- Exact merged-ID scanning found retired `NCBITaxon:1853510` merged into current `NCBITaxon:2100459`.

## Completeness

- BacDive, retained retired old-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:2100459`.
- The merged ID is NCBI old-ID side evidence only: it did not appear as a retained retired row with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
