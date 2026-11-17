# YAML Record Review

- Target: `data/taxa/eukaryota/ophiocordyceps_unilateralis.yaml`
- Taxon: `NCBITaxon:268505` (`Ophiocordyceps unilateralis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:268505`, label `Ophiocordyceps unilateralis`.
- It is grounded exactly under `NCBITaxon:474995` (`Ophiocordyceps`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiocordyceps`.

## Validation

- `just validate data/taxa/eukaryota/ophiocordyceps_unilateralis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_unilateralis.yaml data/taxa/eukaryota/ophiognomonia_clavigignenti_juglandacearum.yaml data/taxa/eukaryota/ophiosphaerella_herpotricha.yaml data/taxa/eukaryota/ophiostoma_ips.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54907` contains the seeded identifier with reason `attested rule: Ophiocordyceps unilateralis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:55518` matches the YAML identity: parent `NCBITaxon:474995`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:55518` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:24798`, where `NCBITaxon:268505` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0117584` / `Ophiocordyceps unilateralis SC16a`, linked to project `Gp0122527` and one analysis row via that project.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:268505`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
