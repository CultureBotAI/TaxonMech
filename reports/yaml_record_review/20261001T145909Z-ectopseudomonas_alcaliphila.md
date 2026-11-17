# YAML Record Review: Ectopseudomonas alcaliphila

## Target

- Record: `data/taxa/bacteria/ectopseudomonas_alcaliphila.yaml`
- Identifier: `NCBITaxon:101564`
- Slug: `ectopseudomonas_alcaliphila`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3236654` (`Ectopseudomonas`)
- Started UTC: 2026-10-01T14:59:09Z
- Finished UTC: 2026-10-01T14:59:09Z
- Verdict: pass

## Validation

- `just validate data/taxa/bacteria/ectopseudomonas_alcaliphila.yaml`: passed with no issues.
- `just validate-strict data/taxa/bacteria/ectopseudomonas_alcaliphila.yaml data/taxa/bacteria/bacterium_enrichment_culture_clone_alo1_glfrudd03gwxvg.yaml data/taxa/bacteria/bacterium_enrichment_culture_clone_alo1_glfrudd03gwy03.yaml data/taxa/bacteria/bacterium_enrichment_culture_clone_alo1_glfrudd03gwy31.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.
- `/private/tmp/taxonmech_yaml_summary.py`: confirmed 1618 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB taxonomy mapping, 5 synonyms, 1 xref, 5 BacDive strains, and 7 source attestations.
- Exact local scans found the expected `PATHS.tsv`, `seed_scope.tsv`, NCBITaxon, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, NCBI type-material, culture-collection, strain-assembly, strain-genome, strain-related, ATB, and StrainInfo rows for `NCBITaxon:101564`; child strain YAMLs point back to this species as their parent.

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101564` resolves to `Ectopseudomonas alcaliphila`, rank `SPECIES`,
parent `NCBITaxon:3236654`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy
snapshot `2026-09-13`.

The lineage is root-first, has 9 entries, and reaches the genus
`Ectopseudomonas` through `Pseudomonadati`, `Pseudomonadota`,
`Gammaproteobacteria`, `Pseudomonadales`, and `Pseudomonadaceae`.

## Evidence

Seven source attestations are backed by local source rows keyed to this taxon:

- `NCBITAXON`: 1 name assertion.
- `LPSN`: `lpsn:45266`, 1 name assertion, validly published and legitimate but marked by LPSN as a synonym, not the correct name.
- `GTDB`: `GTDB:s__Aquipseudomonas_alcaliphila`, `skos:closeMatch`, 7 genomes.
- `BACDIVE`: 5 strain assertions, with 1 strain filed under descendant NCBI taxa.
- `MEDIADIVE`: 2 medium assertions.
- `GOLD`: 12 organism assertions.
- `MADIN`: 4 trait assertions.

The species carries the expected `GTDB:s__Aquipseudomonas_alcaliphila` xref,
the matching GTDB closeMatch mapping, three NCBITaxon synonyms, one LPSN
synonym for `Pseudomonas alcaliphila`, and one GTDB synonym for
`Aquipseudomonas alcaliphila`.

## Strains

The 5 BacDive strain entries agree with the exact local BacDive and StrainInfo
footprint.

- `bacdive:13129`: type strain `AL 15-21, AL15-21`, classified as descendant `NCBITaxon:1215093`, with 10 culture-collection IDs, 19 genome assemblies, 14 genome records, and 65 related records.
- `bacdive:23212`: strain `JAB1`, with 1 culture-collection ID, 2 genome assemblies, 3 genome records, and 4 related records.
- `bacdive:131114`: strain `NE3B02`, with 1 culture-collection ID.
- `bacdive:161423`: JCM-only strain, with 1 culture-collection ID and 1 MediaDive medium.
- `bacdive:161424`: JCM-only strain, with 1 culture-collection ID and 1 MediaDive medium.

NCBI type-material rows name the expected type-strain aliases for the
`Pseudomonas alcaliphila` basionym, including `JCM 10630`, `LMG 23134`, and
`NBRC 102411`; LPSN type-strain designations normalize those into the matching
`kgmicrobe.strain:*` identifiers.

## Completeness

The record includes the expected nomenclature, taxonomy mapping, xref,
synonym, strain, genome-assembly, genome-record, and related-record sections
for a multi-source seeded species record.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

No findings.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

No follow-up needed.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
The generic bounded scan helper is limited to NCBITaxon-only records and intentionally rejected this species because its raw NCBI row has a seven-provider source set.
The LPSN entry is preserved even though LPSN marks this name as a synonym and not the correct name.
The GTDB mapping is species-level and lands on a species-level NCBI record, unlike the known strain-level mismatch pattern in `Ectopseudomonas mendocina NK-01`.
The exact `NCBITaxon:` probe included gitignored files and found child YAML references that correctly point back to this species.
