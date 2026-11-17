# YAML Record Review

- Target: `data/taxa/eukaryota/paralagenidium_karlingii.yaml`
- Taxon: `NCBITaxon:1440115` (`Paralagenidium karlingii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1440115`, label `Paralagenidium karlingii`.
- It is grounded exactly under `NCBITaxon:1440114` (`Paralagenidium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Paralagenidium`.

## Validation

- `just validate data/taxa/eukaryota/paralagenidium_karlingii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paraglomus_occultum.yaml data/taxa/eukaryota/paragyrodon_sphaerosporus.yaml data/taxa/eukaryota/paragyromitra_infula.yaml data/taxa/eukaryota/paralagenidium_karlingii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60140` contains the seeded identifier with reason `attested rule: Paralagenidium karlingii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:361323` matches the YAML identity: parent `NCBITaxon:1440114`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:361323` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:10498`, where `NCBITaxon:1440115` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for strain `1391`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found four culture-from-holotype spellings for `NCBITaxon:1440115` on lines 31146-31149, covering `C12-ES51` and `CBS 134681`.

## Completeness

- Exact StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1440115`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:1440115`: `NCBITaxon:1243778`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add local strain evidence for this species.

## Additional Notes

- None.
