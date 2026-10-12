# YAML Record Review

- Target: `data/taxa/eukaryota/mycetophylax_conformis_symbiont_g26.yaml`
- Taxon: `NCBITaxon:80524` (`Mycetophylax conformis symbiont G26`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:80524`, label `Mycetophylax conformis symbiont G26`.
- It is grounded exactly under `NCBITaxon:80471` (`ant fungal symbionts (Agaricaceae)`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `ant fungal symbionts (Agaricaceae)`.

## Validation

- `just validate data/taxa/eukaryota/mycetophylax_conformis_symbiont_g26.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycetophylax_conformis_symbiont_g26.yaml data/taxa/eukaryota/mycobernardia_incrustans.yaml data/taxa/eukaryota/mycocalia_denudata.yaml data/taxa/eukaryota/mycoemilia_scoparia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53345` contains the seeded identifier with reason `attested rule: Mycetophylax conformis symbiont G26, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:12046` matches the YAML identity: parent `NCBITaxon:80471`, rank `SPECIES`, and no NCBI synonyms.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:12046` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42871`, where `NCBITaxon:80524` has `organism_count` 1.
- The bounded exact scan of the local native GOLD JSONL snapshots found no current-taxid organism, project, or analysis rows for `NCBITaxon:80524`.

## Completeness

- Exact StrainInfo has 0 direct records and 0 deposit rows for `NCBITaxon:80524`, and no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:80524`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:80524`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
