# YAML Record Review

- Target: `data/taxa/eukaryota/papiliotrema_flavescens.yaml`
- Taxon: `NCBITaxon:214993` (`Papiliotrema flavescens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:214993`, label `Papiliotrema flavescens`.
- It is grounded exactly under `NCBITaxon:189450` (`Papiliotrema`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Papiliotrema`.

## Validation

- `just validate data/taxa/eukaryota/papiliotrema_flavescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/panellus_stipticus.yaml data/taxa/eukaryota/panus_rudis.yaml data/taxa/eukaryota/papiliotrema_flavescens.yaml data/taxa/eukaryota/papiliotrema_laurentii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54545` contains the seeded identifier with reason `attested rule: Papiliotrema flavescens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:42320` matches the YAML identity: parent `NCBITaxon:189450`, rank `SPECIES`, three exact synonyms, five related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:42320` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20367`, where `NCBITaxon:214993` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for strain `OH182.9_3C`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 18 type-material spellings for `NCBITaxon:214993` on lines 85767-85784, all under `Torula flavescens`.
- Exact StrainInfo side evidence has 18 direct `NCBITaxon:214993` records and 19 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:214993`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains four old IDs that now point at `NCBITaxon:214993`: `NCBITaxon:209581`, `NCBITaxon:432143`, `NCBITaxon:432158`, and `NCBITaxon:79216`; none are retained retired taxa, so the YAML correctly has no `replaces` entries.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
