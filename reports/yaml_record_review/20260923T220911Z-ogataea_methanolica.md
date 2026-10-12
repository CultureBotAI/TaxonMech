# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_methanolica.yaml`
- Taxon: `NCBITaxon:1156966` (`Ogataea methanolica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1156966`, label `Ogataea methanolica`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_methanolica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_maris.yaml data/taxa/eukaryota/ogataea_mattraensis.yaml data/taxa/eukaryota/ogataea_methanolica.yaml data/taxa/eukaryota/ogataea_minuta.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58045` contains the seeded identifier with reason `attested rule: Ogataea methanolica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:253556` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:253556` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3158`, where `NCBITaxon:1156966` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0138922` / `Ogataea methanolica JCM 10240` and `Go0705640` / `Ogataea methanolica NRRL Y-7685`; one native analysis row links through project `Gp0143979`.

## Completeness

- Exact NCBI type material is limited to 27 `Pichia methanolica` culture-from-type-material rows for `ATCC 58372`, `BCRC 22099` / `CCRC 22099`, `CBS 6515`, `JCM 10240`, `NCYC 2621`, and `NRRL Y-7685`.
- Exact StrainInfo side inventory found 16 direct records and 50 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:1156966`.
- `data/raw/ncbi_merged_ids.tsv:67721` maps side-inventory old ID `NCBITaxon:33166` into `NCBITaxon:1156966`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive and checked auxiliary source rows were empty for `NCBITaxon:1156966`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
