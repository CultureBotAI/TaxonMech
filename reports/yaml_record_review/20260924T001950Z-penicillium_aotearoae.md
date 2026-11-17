# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_aotearoae.yaml`
- Taxon: `NCBITaxon:2100452` (`Penicillium aotearoae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2100452`, label `Penicillium aotearoae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_aotearoae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_annulatum.yaml data/taxa/eukaryota/penicillium_antarcticum.yaml data/taxa/eukaryota/penicillium_anthracinoglaciei.yaml data/taxa/eukaryota/penicillium_aotearoae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62348` contains the seeded identifier with reason `attested rule: Penicillium aotearoae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:518181` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:518181` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20102`, where `NCBITaxon:2100452` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2100452`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found seven culture-from-holotype spellings centered on `CBS 140999`, `DAOMC 250538`, and `KAS 3088`; one culture-from-type-material spelling for `ICMP 21194`; and two holotype spellings centered on `PDD 107543`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:2100452` record, `siID` 269891 with DOI `10.60712/SI-ID269891.1`, and one deposit.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2100452`.
- The sole merged-ID side row maps old `NCBITaxon:1853529` to current `NCBITaxon:2100452`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
