# YAML Record Review

- Target: `data/taxa/eukaryota/ophiognomonia_clavigignenti_juglandacearum.yaml`
- Taxon: `NCBITaxon:218668` (`Ophiognomonia clavigignenti-juglandacearum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:218668`, label `Ophiognomonia clavigignenti-juglandacearum`.
- It is grounded exactly under `NCBITaxon:494041` (`Ophiognomonia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiognomonia`.

## Validation

- `just validate data/taxa/eukaryota/ophiognomonia_clavigignenti_juglandacearum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_unilateralis.yaml data/taxa/eukaryota/ophiognomonia_clavigignenti_juglandacearum.yaml data/taxa/eukaryota/ophiosphaerella_herpotricha.yaml data/taxa/eukaryota/ophiostoma_ips.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54576` contains the seeded identifier with reason `attested rule: Ophiognomonia clavigignenti-juglandacearum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:43030` matches the YAML identity: parent `NCBITaxon:494041`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:43030` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20847`, where `NCBITaxon:218668` has `organism_count` 1.
- Native GOLD has two exact current-taxid organism rows, `Go0008964` and `Go0449072`, linked to two projects and two analysis rows via those projects.
- Exact StrainInfo side evidence has two direct `NCBITaxon:218668` records, `siID` 202921 and 254370, and two deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:218668`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
