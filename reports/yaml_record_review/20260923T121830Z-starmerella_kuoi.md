# YAML Record Review: Starmerella kuoi
- Repository: TaxonMech
- Record: data/taxa/eukaryota/starmerella_kuoi.yaml
- Started UTC: 2026-09-23T12:18:30Z
- Finished UTC: 2026-09-23T12:18:30Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008382`, the eukaryotic yeast species record for `Starmerella kuoi`, encoded at `data/taxa/eukaryota/starmerella_kuoi.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/pseudomonas_sp_sr5.yaml data/taxa/eukaryota/starmerella_kuoi.yaml data/taxa/bacteria/marinimicrobium_sp_acht5_2.yaml data/taxa/bacteria/bacteroidetes_bacterium_acht4.yaml` scanned the batch and returned 0 errors on rerun.

`just validate data/taxa/eukaryota/starmerella_kuoi.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded to `NCBITaxon:1008382`, label `Starmerella kuoi`, as a seeded eukaryotic species under genus `Starmerella`. The `genetic_code: 1` and `taxon_domain: EUKARYOTA` agree with the NCBI lineage in the YAML.

The NCBI related synonyms `Candida sp. NRRL Y-27208`, `Starmerella kuoi (Kurtzman) C.A. Rosa & Lachance, 2018`, and `Starmerella sp. CBS 7267` are all present in the YAML.

## Evidence

Local pinned source rows support the record in `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/ncbi_type_material.tsv`. An exact `rg --no-ignore --hidden` ID search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS row for `starmerella_kuoi`, the expected NCBI taxonomy row for `NCBITaxon:1008382`, the one GOLD organism-count row, the NCBI merged-ID row from `NCBITaxon:877578` to `NCBITaxon:1008382`, and the expected `Candida kuoi` type-material designations.

A gitignore-independent exact label and synonym search for `Starmerella kuoi`, `Candida kuoi`, `Starmerella sp. CBS 7267`, `Candida sp. NRRL Y-27208`, `CBS 7267`, and `NRRL Y-27208` over `data/raw`, `data/atb`, and `data/straininfo` found no BacDive, LPSN, ATB, or StrainInfo strain row that should have instantiated a strain object.

## Completeness

The record includes the NCBI accepted name, parentage, related synonyms, genetic code, NCBITAXON source attestation, and GOLD source attestation visible in the local source rows.

The NCBI taxdump `type material` rows for `Candida kuoi` remain upstream type-material designations only in the current local projection; no local BacDive, LPSN, ATB, or StrainInfo row is available to back a distinct `strains` entry.

## Findings

No curation findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

An exact `rg --no-ignore --hidden` search over `data/taxa` resolved the reviewed file to `data/taxa/eukaryota/starmerella_kuoi.yaml`, and a gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for `starmerella_kuoi` before this report was written. Live external lookups were unavailable during this review; the pinned rows under `data/raw`, `data/atb`, and `data/straininfo` were treated as authoritative.
