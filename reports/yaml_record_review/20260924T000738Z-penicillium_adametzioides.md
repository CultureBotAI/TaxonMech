# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_adametzioides.yaml`
- Taxon: `NCBITaxon:70094` (`Penicillium adametzioides`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:70094`, label `Penicillium adametzioides`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_adametzioides.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/peltaster_fructicola.yaml data/taxa/eukaryota/penicilliopsis_zonata.yaml data/taxa/eukaryota/penicilliopsis_zonata_cbs_506_65.yaml data/taxa/eukaryota/penicillium_adametzioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53199` contains the seeded identifier with reason `attested rule: Penicillium adametzioides, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9769` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9769` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41616`, where `NCBITaxon:70094` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:70094`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found eight culture-from-type-material spellings centered on `ATCC 18306`, `CBS 313.59`, `IMI 068227`, and `NRRL 3405`, plus six type-material spellings centered on `FAT 1302`, `IFO 6055`, and `QM 7312`.
- Exact StrainInfo side evidence has 14 direct `NCBITaxon:70094` records and 20 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:70094`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
