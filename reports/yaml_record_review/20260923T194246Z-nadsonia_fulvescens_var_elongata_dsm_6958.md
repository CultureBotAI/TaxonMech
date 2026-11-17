# YAML Record Review

- Target: `data/taxa/eukaryota/nadsonia_fulvescens_var_elongata_dsm_6958.yaml`
- Taxon: `NCBITaxon:857566` (`Nadsonia fulvescens var. elongata DSM 6958`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:857566`, label `Nadsonia fulvescens var. elongata DSM 6958`.
- It is grounded exactly under `NCBITaxon:58631` (`Nadsonia fulvescens var. elongata`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Nadsonia fulvescens var. elongata`.

## Validation

- `just validate data/taxa/eukaryota/nadsonia_fulvescens_var_elongata_dsm_6958.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/nadsonia_fulvescens_var_elongata_dsm_6958.yaml data/taxa/eukaryota/nadsonia_starkeyi_henricii.yaml data/taxa/eukaryota/naegleria_fowleri.yaml data/taxa/eukaryota/naegleria_gruberi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56731` contains the seeded identifier with reason `attested rule: Nadsonia fulvescens var. elongata DSM 6958, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:180313` matches the YAML identity: parent `NCBITaxon:58631`, rank `STRAIN`, and no synonyms.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:180313` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43280`, where `NCBITaxon:857566` has `organism_count` 1.
- The local native GOLD exact-current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:857566`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:857566`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:857566`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:857566`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local native GOLD or strain rows for this strain taxon.

## Additional Notes

- The generated GOLD assertion count follows transformed `data/raw/gold_organisms.tsv`; the local native `data/gold/*.jsonl.gz` exact scan did not carry a current-taxid organism row for this strain.
