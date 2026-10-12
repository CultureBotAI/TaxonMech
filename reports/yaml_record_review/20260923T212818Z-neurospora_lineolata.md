# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_lineolata.yaml`
- Taxon: `NCBITaxon:88717` (`Neurospora lineolata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:88717`, label `Neurospora lineolata`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_lineolata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_kobi.yaml data/taxa/eukaryota/neurospora_lineolata.yaml data/taxa/eukaryota/neurospora_macrospora.yaml data/taxa/eukaryota/neurospora_perkinsii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53467` contains the seeded identifier with reason `attested rule: Neurospora lineolata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14060` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14060` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43900`, where `NCBITaxon:88717` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651408` / `Neurospora lineolata FGSC 1910`, linked to projects `Gp0688312` and `Gp0699275`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:270976-270977` has duplicate culture-from-type-material spellings for `CBS 502.70` and `CBS:502.70` under `Neurospora lineolata`.
- Exact StrainInfo side inventory found 4 direct records and 5 deposit entries, including `CBS 502.70`, type-strain deposit `ATCC 18966`, `CCT 5415`, `ICMP 14014`, and `ICMP 16643`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:88717`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
