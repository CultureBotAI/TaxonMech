# YAML Record Review: Schleiferilactobacillus perolens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/schleiferilactobacillus_perolens.yaml`
- Started UTC: 2026-09-22T19:57:28Z
- Finished UTC: 2026-09-22T20:00:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:100468` |
| Label | `Schleiferilactobacillus perolens` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2767891` |
| LPSN name | `lpsn:10712` |
| GTDB mapping | `GTDB:s__Schleiferilactobacillus_perolens` |
| Strain count | `4` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species record with one typed GTDB species mapping, four BacDive strains, one BacDive strain filed under descendant strain taxon `NCBITaxon:1423792`, and no curator-authored causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/schleiferilactobacillus_perolens.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/bifidobacterium_sp_pg2.yaml data/taxa/bacteria/bifidobacterium_sp_pg9.yaml data/taxa/bacteria/schleiferilactobacillus_perolens.yaml data/taxa/bacteria/schaalia_canis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:100468` is the pinned NCBI row for `Schleiferilactobacillus perolens`, rank `SPECIES`, parent `NCBITaxon:2767891`, and genetic code `11`. The lineage follows NCBI through `Bacillota`, `Bacilli`, `Lactobacillales`, `Lactobacillaceae`, and `Schleiferilactobacillus`. The LPSN row maps `lpsn:10712` to the same NCBI species, and the GTDB row maps `GTDB:s__Schleiferilactobacillus_perolens` to `NCBITaxon:100468` with `skos:closeMatch` and 6 genomes.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, exact synonym, and related synonyms | `data/raw/ncbitaxon_taxa.tsv` has the species row, exact synonym `Lactobacillus perolens`, and related names `"Lactobacillus perolens" Back et al. 1999`, `Lactobacillus perolens Back et al. 2000`, and `Schleiferilactobacillus perolens (Back et al. 2000) Zheng et al. 2020`. |
| LPSN nomenclature and synonym | `data/raw/lpsn_names.tsv` maps `lpsn:10712` to the species, marks it legitimate, validly published, and correct, lists type strains `DSM 12744`, `JCM 12534`, and `LMG 18936`, and links the synonym `lpsn:777373` for `Lactobacillus perolens`. |
| Strains and type strain | `data/raw/bacdive_strains.tsv` has four rows embedded here: `bacdive:6573`, `bacdive:6574`, `bacdive:165890`, and `bacdive:165891`. The `bacdive:6573` row is filed under descendant `NCBITaxon:1423792` and is correctly retained with `classified_as`. |
| Genome and related identifiers | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/atb`, and `data/straininfo` carry the NCBI, GTDB, BV-BRC, IMG, ATB, BioSample, BioProject, GOLD, and StrainInfo identifiers embedded under `bacdive:6573`. |
| Source attestations and scope | `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/madin_taxa.tsv` contain the asserted source counts, and `curation/seed_scope.tsv` lists `NCBITaxon:100468` as in scope by an `attested rule` with 7 sources including NCBI. |

## Completeness

The record includes the NCBI and LPSN synonyms, the one GTDB mapping, all four BacDive rows for this species or descendant strain, genome and ATB evidence for `bacdive:6573`, GOLD related rows for the `DSM 12744`, `JCM 12534`, `LMG 18936`, `CIP 109156`, `DSM 12745`, and `LMG 18938` deposits, and StrainInfo deposit/sequence rows for the matching culture deposits. The remaining omitted record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:100468`, `NCBITaxon:1423792`, `GTDB:s__Schleiferilactobacillus_perolens`, `lpsn:10712`, or BacDive strains `6573`, `6574`, `165890`, and `165891`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-schleiferilactobacillus_perolens.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against pinned `data/raw`, `data/atb`, and `data/straininfo` rows.

Several `bacdive:6574` related rows retain GOLD and StrainInfo source taxon `NCBITaxon:304207` and `Schleiferilactobacillus harbinensis` record names, while the BacDive row itself is filed under `NCBITaxon:100468`. Those related rows preserve a source-level conflict without changing this record's NCBI identity.
