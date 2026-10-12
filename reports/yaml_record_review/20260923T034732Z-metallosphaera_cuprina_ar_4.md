# YAML Record Review: Metallosphaera cuprina Ar-4

- Repository: TaxonMech
- Record: data/taxa/archaea/metallosphaera_cuprina_ar_4.yaml
- Started UTC: 2026-09-23T03:47:32Z
- Finished UTC: 2026-09-23T03:47:32Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006006`
- Label: `Metallosphaera cuprina Ar-4`
- Rank: `STRAIN`
- Domain: `ARCHAEA`
- Parent: `NCBITaxon:1006005` (`Metallosphaera cuprina`)
- Path registry row: `data/taxa/PATHS.tsv:2007`

## Validation

- `just validate-strict data/taxa/bacteria/buttiauxella_agrestis_atcc_33320.yaml data/taxa/archaea/metallosphaera_cuprina.yaml data/taxa/archaea/metallosphaera_cuprina_ar_4.yaml data/taxa/bacteria/priestia_megaterium_wsh_002.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/archaea/metallosphaera_cuprina_ar_4.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-metallosphaera_cuprina_ar_4.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, archaeal genetic code, and NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210669`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1006006` under parent species `Metallosphaera cuprina`.
- `data/raw/gtdb_mappings.tsv:1054` maps the 30-genome GTDB species cluster `GTDB:s__Metallosphaera_cuprina` to the child strain as `skos:closeMatch`.

## Evidence

- `data/raw/madin_taxa.tsv:355` supplies the four Madin trait assertions summarized by the child strain record.
- `data/raw/strain_assemblies.tsv:72188` and `data/raw/strain_assemblies.tsv:72189`, `data/raw/strain_genome_records.tsv:56403` through `data/raw/strain_genome_records.tsv:56405`, and `data/raw/strain_related_records.tsv:222982` through `data/raw/strain_related_records.tsv:222985` show local BacDive and GOLD rows for this Ar-4 strain.
- An exact `rg --no-ignore --hidden` lookup for `bacdive:161630`, `GCA_000204925`, `Ga0029342`, `650716051`, `patric:1006006.8`, and `NCBITaxon:1006006` found the same-strain child assembly, genome, and related-record rows only in `data/raw/`.

## Completeness

- The NCBI, GTDB, and Madin attestations are present.
- The raw BacDive and GOLD Ar-4 genome payload is represented on the parent species `Metallosphaera cuprina`, but this child strain YAML has `strain_count: 0` and no local assembly, genome, or related-record sections of its own.

## Findings

- Major: the GTDB species cluster `GTDB:s__Metallosphaera_cuprina` is projected as a `skos:closeMatch`, xref, and exact synonym `Metallosphaera cuprina` onto the narrower NCBI strain `NCBITaxon:1006006`.
- Minor: local BacDive/GOLD rows for `kgmicrobe.strain:bacdive_161630` and `gold:Ga0029342` are keyed to `NCBITaxon:1006006` in raw strain sidecars but are absent from this child strain record.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.
- Revisit BacDive/GOLD child-strain projection so the raw `NCBITaxon:1006006` Ar-4 assembly, genome, and related-record rows are either retained on the Ar-4 child or explicitly cross-linked from the parent species record.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Metallosphaera cuprina` is no longer an exact synonym of `Metallosphaera cuprina Ar-4`.
- Verify that the Ar-4 BacDive/GOLD payload from `data/raw/strain_assemblies.tsv` and `data/raw/strain_related_records.tsv` remains reachable from the child strain.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
