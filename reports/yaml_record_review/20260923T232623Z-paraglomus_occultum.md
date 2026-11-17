# YAML Record Review

- Target: `data/taxa/eukaryota/paraglomus_occultum.yaml`
- Taxon: `NCBITaxon:144539` (`Paraglomus occultum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:144539`, label `Paraglomus occultum`.
- It is grounded exactly under `NCBITaxon:144537` (`Paraglomus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Paraglomus`.

## Validation

- `just validate data/taxa/eukaryota/paraglomus_occultum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paraglomus_occultum.yaml data/taxa/eukaryota/paragyrodon_sphaerosporus.yaml data/taxa/eukaryota/paragyromitra_infula.yaml data/taxa/eukaryota/paralagenidium_karlingii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54025` contains the seeded identifier with reason `attested rule: Paraglomus occultum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:29168` matches the YAML identity: parent `NCBITaxon:144537`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:29168` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:10599`, where `NCBITaxon:144539` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for strain `IA702`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found one reference-material row for `NCBITaxon:144539` at line 31584, designation `INVAM IA702`.

## Completeness

- Exact StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:144539`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:144539`: `NCBITaxon:55591`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add local strain evidence for this species.

## Additional Notes

- None.
