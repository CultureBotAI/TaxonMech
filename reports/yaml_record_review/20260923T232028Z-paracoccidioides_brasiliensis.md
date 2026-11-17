# YAML Record Review

- Target: `data/taxa/eukaryota/paracoccidioides_brasiliensis.yaml`
- Taxon: `NCBITaxon:121759` (`Paracoccidioides brasiliensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:121759`, label `Paracoccidioides brasiliensis`.
- It is grounded exactly under `NCBITaxon:38946` (`Paracoccidioides`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Paracoccidioides`.

## Validation

- `just validate data/taxa/eukaryota/paracoccidioides_brasiliensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parachaetomium_inaequale.yaml data/taxa/eukaryota/paracoccidioides_brasiliensis.yaml data/taxa/eukaryota/paracoccidioides_lutzii_pb01.yaml data/taxa/eukaryota/paraconiothyrium_cyclothyrioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53876` contains the seeded identifier with reason `attested rule: Paracoccidioides brasiliensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:22891` matches the YAML identity: parent `NCBITaxon:38946`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:22891` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:5177`, where `NCBITaxon:121759` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows, three project rows, and two analysis rows covering strains `PbCNH`, `Pb300`, and `CNH`.
- Exact StrainInfo side evidence has 38 direct `NCBITaxon:121759` records and 40 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:121759`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains two old IDs that now point at `NCBITaxon:121759`: `NCBITaxon:70254` and `NCBITaxon:71432`; neither is retained as a retired taxon, so the YAML correctly has no `replaces` entries.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
