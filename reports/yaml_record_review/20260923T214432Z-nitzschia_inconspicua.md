# YAML Record Review

- Target: `data/taxa/eukaryota/nitzschia_inconspicua.yaml`
- Taxon: `NCBITaxon:303405` (`Nitzschia inconspicua`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:303405`, label `Nitzschia inconspicua`.
- It is grounded exactly under `NCBITaxon:2857` (`Nitzschia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Nitzschia`.

## Validation

- `just validate data/taxa/eukaryota/nitzschia_inconspicua.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nitzschia_fonticola.yaml data/taxa/eukaryota/nitzschia_inconspicua.yaml data/taxa/eukaryota/nitzschia_palea.yaml data/taxa/eukaryota/nitzschia_pellucida.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55091` contains the seeded identifier with reason `attested rule: Nitzschia inconspicua, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:62118` matches the YAML identity: parent `NCBITaxon:2857`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:62118` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30379`, where `NCBITaxon:303405` has `organism_count` 4.
- Native GOLD has three exact current-taxid organism rows, `Go0609556`, `Go0609557`, and `Go0609558`, linked to 94 native projects; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_merged_ids.tsv:51900` maps side-inventory old ID `NCBITaxon:2787637` into `NCBITaxon:303405`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact NCBI type-material, exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:303405`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
