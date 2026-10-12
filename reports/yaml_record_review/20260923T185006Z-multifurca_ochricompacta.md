# YAML Record Review

- Target: `data/taxa/eukaryota/multifurca_ochricompacta.yaml`
- Taxon: `NCBITaxon:376703` (`Multifurca ochricompacta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:376703`, label `Multifurca ochricompacta`.
- It is grounded exactly under `NCBITaxon:670315` (`Multifurca`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Multifurca`.

## Validation

- `just validate data/taxa/eukaryota/multifurca_ochricompacta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_zychae.yaml ... mutinus_elegans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55409` contains the seeded identifier with reason `attested rule: Multifurca ochricompacta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:79082` matches the YAML identity: parent `NCBITaxon:670315`, rank `SPECIES`, exact synonym `Russula ochricompacta`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:79082` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33766`, where `NCBITaxon:376703` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0302595` / `Multifurca ochricompacta BPL690`, linked to two native projects and no native analyses.
- `data/raw/ncbi_type_material.tsv:198534-198547` has seven `GB 146` holotype aliases and seven `GB 428` paratype aliases.

## Completeness

- The bounded scan found no exact BacDive, StrainInfo, generated raw strain, generated StrainInfo, or auxiliary source rows for `NCBITaxon:376703`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:376703`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if additional StrainInfo, BacDive, or generated strain evidence is added for this taxon.

## Additional Notes

- None.
