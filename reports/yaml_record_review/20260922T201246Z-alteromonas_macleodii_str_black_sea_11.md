# YAML Record Review: Alteromonas macleodii str. 'Black Sea 11'
- Repository: TaxonMech
- Record: `data/taxa/bacteria/alteromonas_macleodii_str_black_sea_11.yaml`
- Started UTC: 2026-09-22T20:11:01Z
- Finished UTC: 2026-09-22T20:12:46Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1004785` / `alteromonas_macleodii_str_black_sea_11`.
- The record is a `STRAIN`-rank `BACTERIA` record for `Alteromonas macleodii str. 'Black Sea 11'`.
- Parentage is the seeded NCBI placement under `NCBITaxon:28108` (`Alteromonas macleodii`), with lineage through `Pseudomonadota`, `Gammaproteobacteria`, `Alteromonadales`, `Alteromonadaceae`, and `Alteromonas`.

## Validation
- `just validate data/taxa/bacteria/alteromonas_macleodii_str_black_sea_11.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/tetragenococcus_halophilus_ho.yaml data/taxa/archaea/desulfurococcaceae_archaeon_ebi_244.yaml data/taxa/archaea/desulfurococcaceae_archaeon_csc_16s.yaml data/taxa/bacteria/alteromonas_macleodii_str_black_sea_11.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004785`, `label: Alteromonas macleodii str. 'Black Sea 11'`, `rank: STRAIN`, `domain: BACTERIA`, `parent: NCBITaxon:28108`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon strain.
- The NCBI synonym `Alteromonas macleodii strain 'Black Sea 11'` is appropriate for this strain record.
- The GTDB-derived exact synonym `Alteromonas abrolhosensis` is not identity-equivalent to the NCBI strain `Alteromonas macleodii str. 'Black Sea 11'`.

## Evidence
- Local source rows for `NCBITaxon:1004785` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Alteromonas_abrolhosensis` to this NCBI strain with `skos:closeMatch` and `genome_count: 18`.
- `data/raw/gold_organisms.tsv` contributes one organism assertion and `data/raw/madin_taxa.tsv` contributes five trait assertions.
- A gitignore-independent `rg --no-ignore --hidden` search over the local source tables found no same-taxon ATB row.

## Completeness
- The record includes the expected NCBITAXON, GTDB, GOLD, and MADIN source attestations from `data/raw/ncbitaxon_taxa.tsv`.
- `strain_count: 0` is consistent with the absence of a same-taxon BacDive strain inventory row for `NCBITaxon:1004785`; the BACDIVE assembly rows for `kgmicrobe.strain:bacdive_23558` are not enough on their own to populate this taxon's strain list.
- No curation history decision has yet narrowed or removed the GTDB species-cluster mapping on this strain.

## Findings
- Major: a GTDB species cluster, `GTDB:s__Alteromonas_abrolhosensis`, is projected onto the NCBI strain `NCBITaxon:1004785` as a `taxonomy_mappings` entry, an `xrefs` entry, and an `EXACT_SYNONYM` of `Alteromonas abrolhosensis`. A GTDB `s__` species cluster should not be treated as identity-equivalent to the single NCBI strain `Alteromonas macleodii str. 'Black Sea 11'`.

## Recommended Edits
- Update the GTDB mapping generation in `data/raw/gtdb_mappings.tsv` and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact strain synonyms or direct strain-level xrefs.
- Re-seed this record after that guard is in place so `GTDB:s__Alteromonas_abrolhosensis`, `s__Alteromonas_abrolhosensis`, and `Alteromonas abrolhosensis` are not attached to `NCBITaxon:1004785` unless a later manual curation event intentionally records a narrower relationship.

## Follow-up Checks
- After the GTDB guard is fixed, confirm that `Alteromonas macleodii str. 'Black Sea 11'` keeps its NCBI, GOLD, and MADIN attestations while losing the species-cluster synonym and direct `GTDB:s__Alteromonas_abrolhosensis` xref.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-alteromonas_macleodii_str_black_sea_11.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; the local pinned source rows dated `2026-09-13` were treated as the source of truth.
