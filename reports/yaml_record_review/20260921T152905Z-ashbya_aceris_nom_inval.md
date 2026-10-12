# YAML Record Review: [Ashbya] aceris (nom. inval.)

## Target

- File: `data/taxa/eukaryota/ashbya_aceris_nom_inval.yaml`
- Identifier: `NCBITaxon:566037`
- Label: `[Ashbya] aceris (nom. inval.)`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2640716` / `unclassified Eremothecium`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Saccharomycetes` -> `Saccharomycetales` -> `Saccharomycetaceae` -> `Eremothecium` -> `unclassified Eremothecium`
- Existing review report: none found for `*ashbya_aceris_nom_inval.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ashbya_aceris_nom_inval.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ashbya_aceris_nom_inval.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:566037`, labelled `[Ashbya] aceris (nom. inval.)` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:566037` is a `SPECIES` child of `NCBITaxon:2640716` / `unclassified Eremothecium`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Ashbya aceris F.S. Dietr., Voegeli, S. Kuo & Philippsen, 2013`, plus related synonyms `Ashbya sp. FD-2008`, `Ashbya sp. FM-2008`, `Eremothecium sp. FD-2008`, and `Saccharomycetaceae sp. 'Ashbya aceri'`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: [Ashbya] aceris (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:566037`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:566037`, the bracketed label, the plain `Ashbya aceris` synonym text, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:566037`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:566037` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0006845`, `Ashbya aceris FD-2008`, with strain `FD-2008` and no culture collection ID.
- GOLD organism `Go0006845` has one project, `Gp0006845`, with BioProject `PRJNA39551` and BioSample `SAMN03081470`.
- GOLD project `Gp0006845` is linked to genome analysis `Ga0100107` with GenBank assembly accession `GCA_000412225.2`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `566037`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `566037`.
- Exact `FD-2008` and `FM-2008` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:566037`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD `FD-2008` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ashbya_aceris_nom_inval.yaml`; it is generated and validates strictly.
- Preserve the invalid-name label, no-rank unclassified `Eremothecium` parent, NCBI synonym split, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ashbya_aceris_nom_inval.yaml` and `just validate-strict data/taxa/eukaryota/ashbya_aceris_nom_inval.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Ashbya aceris FD-2008` is project-linked through `AP PROJECT GOLD IDS = Gp0006845`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
