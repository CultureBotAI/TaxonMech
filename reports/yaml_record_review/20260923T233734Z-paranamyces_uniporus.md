# YAML Record Review

- Target: `data/taxa/eukaryota/paranamyces_uniporus.yaml`
- Taxon: `NCBITaxon:1675850` (`Paranamyces uniporus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1675850`, label `Paranamyces uniporus`.
- It is grounded exactly under `NCBITaxon:1675849` (`Paranamyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Paranamyces`.

## Validation

- `just validate data/taxa/eukaryota/paranamyces_uniporus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paranamyces_uniporus.yaml data/taxa/eukaryota/paraphaeosphaeria_minitans.yaml data/taxa/eukaryota/paraphaeosphaeria_sporulosa.yaml data/taxa/eukaryota/paraphoma_chrysanthemicola.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61015` contains the seeded identifier with reason `attested rule: Paranamyces uniporus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:437257` matches the YAML identity: parent `NCBITaxon:1675849`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:437257` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14437`, where `NCBITaxon:1675850` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row and one project row for strain `JEL0695`; it found no analysis rows.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two type-material spellings for `NCBITaxon:1675850` on lines 51373-51374, both centered on `PL 157`.

## Completeness

- Exact StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1675850`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:1675850`: `NCBITaxon:382592`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add local strain evidence for this species.

## Additional Notes

- None.
