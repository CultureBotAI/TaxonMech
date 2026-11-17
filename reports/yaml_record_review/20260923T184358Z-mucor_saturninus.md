# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_saturninus.yaml`
- Taxon: `NCBITaxon:64648` (`Mucor saturninus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64648`, label `Mucor saturninus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_saturninus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_rouxianus.yaml ... mucor_sinensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53114` contains the seeded identifier with reason `attested rule: Mucor saturninus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8217` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor saturninus Hagem, 1910`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8217` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40367`, where `NCBITaxon:64648` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0402599` / `Mucor saturninus NRRL 2631` and `Go0631676` / `Mucor saturninus WA0000017839`, linked to two native projects and one native analysis through project ID `Gp0645224`.
- `data/raw/ncbi_type_material.tsv:244656-244657` has the `CBS 974.68` and `CBS:974.68` culture-from-neotype aliases.

## Completeness

- Exact StrainInfo has 20 direct records and 28 deposit rows for `NCBITaxon:64648`.
- The generated `data/straininfo/related_records.tsv.gz` has two `NRRL B-1268` rows linking `straininfo.strain:34667` and `straininfo.deposit:166400` to `kgmicrobe.strain:bacdive_15757`; generated StrainInfo assemblies and exclusions were empty.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64648`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:64648`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes additional local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
