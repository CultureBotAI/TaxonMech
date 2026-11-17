# YAML Record Review

- Target: `data/taxa/eukaryota/paragyrodon_sphaerosporus.yaml`
- Taxon: `NCBITaxon:5372` (`Paragyrodon sphaerosporus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5372`, label `Paragyrodon sphaerosporus`.
- It is grounded exactly under `NCBITaxon:5371` (`Paragyrodon`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Paragyrodon`.

## Validation

- `just validate data/taxa/eukaryota/paragyrodon_sphaerosporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paraglomus_occultum.yaml data/taxa/eukaryota/paragyrodon_sphaerosporus.yaml data/taxa/eukaryota/paragyromitra_infula.yaml data/taxa/eukaryota/paralagenidium_karlingii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51980` contains the seeded identifier with reason `attested rule: Paragyrodon sphaerosporus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2377` matches the YAML identity: parent `NCBITaxon:5371`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2377` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38230`, where `NCBITaxon:5372` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row and two project rows for strain `FC442`; it found no analysis rows.
- Exact `data/raw/ncbi_type_material.tsv` scanning found four isotype spellings for `NCBITaxon:5372` on lines 230864-230867, all under `Boletus sphaerosporus` and centered on `MICH 10050`.

## Completeness

- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5372`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add local strain evidence for this species.

## Additional Notes

- None.
