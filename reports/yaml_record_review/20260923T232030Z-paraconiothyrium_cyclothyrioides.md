# YAML Record Review

- Target: `data/taxa/eukaryota/paraconiothyrium_cyclothyrioides.yaml`
- Taxon: `NCBITaxon:300256` (`Paraconiothyrium cyclothyrioides`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:300256`, label `Paraconiothyrium cyclothyrioides`.
- It is grounded exactly under `NCBITaxon:300251` (`Paraconiothyrium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Paraconiothyrium`.

## Validation

- `just validate data/taxa/eukaryota/paraconiothyrium_cyclothyrioides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parachaetomium_inaequale.yaml data/taxa/eukaryota/paracoccidioides_brasiliensis.yaml data/taxa/eukaryota/paracoccidioides_lutzii_pb01.yaml data/taxa/eukaryota/paraconiothyrium_cyclothyrioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55067` contains the seeded identifier with reason `attested rule: Paraconiothyrium cyclothyrioides, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:61153` matches the YAML identity: parent `NCBITaxon:300251`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:61153` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30091`, where `NCBITaxon:300256` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:300256`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:300256` record and one deposit.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:300256`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
