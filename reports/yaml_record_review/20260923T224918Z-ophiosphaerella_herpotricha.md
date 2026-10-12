# YAML Record Review

- Target: `data/taxa/eukaryota/ophiosphaerella_herpotricha.yaml`
- Taxon: `NCBITaxon:33175` (`Ophiosphaerella herpotricha`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:33175`, label `Ophiosphaerella herpotricha`.
- It is grounded exactly under `NCBITaxon:33174` (`Ophiosphaerella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Ophiosphaerella`.

## Validation

- `just validate data/taxa/eukaryota/ophiosphaerella_herpotricha.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiocordyceps_unilateralis.yaml data/taxa/eukaryota/ophiognomonia_clavigignenti_juglandacearum.yaml data/taxa/eukaryota/ophiosphaerella_herpotricha.yaml data/taxa/eukaryota/ophiostoma_ips.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52254` contains the seeded identifier with reason `attested rule: Ophiosphaerella herpotricha, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3550` matches the YAML identity: parent `NCBITaxon:33174`, rank `SPECIES`, four exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3550` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:32332`, where `NCBITaxon:33175` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:33175`.
- Exact StrainInfo side evidence has eight direct `NCBITaxon:33175` records and 13 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:33175`; the record correctly has `strain_count: 0`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:45295` to `NCBITaxon:33175`, but no retained retired source row generated a YAML `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
