# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_tetrasperma.yaml`
- Taxon: `NCBITaxon:40127` (`Neurospora tetrasperma`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:40127`, label `Neurospora tetrasperma`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_tetrasperma.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_tetrasperma.yaml data/taxa/eukaryota/neurospora_tetraspora.yaml data/taxa/eukaryota/nia_vibrissa.yaml data/taxa/eukaryota/nidula_niveotomentosa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52417` contains the seeded identifier with reason `attested rule: Neurospora tetrasperma, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4559` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4559` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34462`, where `NCBITaxon:40127` has `organism_count` 4.
- Native GOLD has six exact current-taxid organism rows and two linked native project rows, `Gp0088200` and `Gp0090023`; no native analysis rows linked to those projects.

## Completeness

- Exact StrainInfo side inventory found 326 direct records and 336 deposit entries, including sampled designations `IHEM 18016`, `MUCL 14164`, `DSM 1261`, `FGSC 1270`, `DSM 1262`, `FGSC 1271`, `IFO 6982`, and `NBRC 6982`.
- `data/raw/ncbi_merged_ids.tsv:36385` maps side-inventory old ID `NCBITaxon:2056425` into `NCBITaxon:40127`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact NCBI type-material, BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:40127`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
