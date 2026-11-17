# YAML Record Review: Aquisalimonas halophila

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aquisalimonas_halophila.yaml`
- Started UTC: 2026-10-03T18:04:52Z
- Finished UTC: 2026-10-03T18:12:19Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303863`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:406099`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
The record contains nine lineage entries, one LPSN nomenclature entry,
two related synonyms, one BacDive strain, eight strain-related records,
six source attestations and one embedded seed event. No genome assembly,
genome record, experimental phenotype assertion or causal graph is asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aquisalimonas_halophila.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aquisalimonas_halophila.yaml`:
  PASS; one file, zero errors; standard diagnostic written to
  `reports/instance_validation_failures.tsv`. Both validators were rerun
  immediately before writing this report and passed again.
- Structured comparisons reproduced identity, all nine lineage objects,
  source memberships, PATHS and scope rows, and all eight related-record
  objects, including parsed StrainInfo evidence. No children occur in
  the inspected backbone. Culture identifiers passed the repository's
  normalization and CURIE-key helpers.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, rendered products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308191` supports the carried identity,
rank, parent, code, synonyms and 2026-09-13 snapshot. Full native
scientific-name, authority and includes-name objects at
`data/catalog/ncbi_names-0007.jsonl.gz:30742` and the following two
lines agree. The nine ancestors are root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Chromatiales,
Ectothiorhodospiraceae and Aquisalimonas. Preserve the source lineage.

Inspected [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303863&retmode=xml)
confirms the ID, label, species rank, parent, code, non-root lineage,
authority and includes-name. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303863)
confirms all nine ancestor identifiers. The two alternate names remain
related synonyms; type-material entries are not synonymous species names.
Exact grounding and bacterial domain are supported.

[LPSN record 791954](https://lpsn.dsmz.de/species/aquisalimonas-halophila)
supports the species name, Zhang et al. 2014 authority, valid publication,
correct-name status, three type-strain designations, marker accession and
two bibliographic references. The raw LPSN row at
`data/raw/lpsn_names.tsv:28741` reproduces the YAML's status flags,
publications and sequence accession, but lists only DSM 25902 as a
nomenclature type designation. The minor completeness difference is
retained below; the supported DSM identifier is not erroneous.

## Evidence

[BacDive strain 130289](https://bacdive.dsmz.de/strain/130289), its full
native object and `data/raw/bacdive_strains.tsv:52604` agree on the
target taxon, type-strain status and CCTCC AB 2012043, DSM 25902 and
YIM 95345 culture identifiers. The [DSMZ catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25902)
independently identifies the same type strain and these aliases.
Repository normalization preserves the complete case-sensitive accession
and the encoded space in `kgmicrobe.strain:CCTCC-AB%202012043`.
These are deposits/designations for one BacDive strain, not three strains.

[PubMed 24699066](https://pubmed.ncbi.nlm.nih.gov/24699066/) was
verified through the public PubMed EFetch XML after the browser page
presented a challenge. Its metadata confirms DOI
`10.1099/ijs.0.059428-0`, and the inspected abstract explicitly equates
YIM 95345, DSM 25902 and CCTCC AB 2012043 as the type strain.
The [publisher's notification-list page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.068833-0)
confirms the second DOI, Oren and Garrity authorship and the 2014
volume-64-part-7 notification context cited by LPSN. The individual
species row in the notification's full text was not retrieved; this is
a bounded verification limit, not evidence of a wrong citation.

[NCBI nucleotide KC577145](https://www.ncbi.nlm.nih.gov/nuccore/KC577145)
was inspected through nuccore EFetch XML: KC577145.1 is a 1,538-base
partial 16S rRNA sequence annotated to this taxon, strain YIM 95345,
and type material. Preserve the source's unversioned `INSDC:KC577145`;
this marker is not a whole-genome assembly. Sequence integrity was not
audited. No experimental traits from the paper were imported into the
record by this review.

Six GOLD relationships reproduce
`data/raw/strain_related_records.tsv:42453` and the following five
rows and the three full native GOLD organism objects. Go0615078
identifies YIM 95345, Go0615079 DSM 25902 and Go0615080 CCTCC
AB 2012043; each has taxon 1303863 and an exact culture match.
Each organism is represented once for its culture-collection field and
once for its strain field. Those are distinct field-level provenance
claims, not six independent organisms or redundant identical assertions.
No genome relationship follows merely from a GOLD organism identifier.

Two StrainInfo relationships reproduce the strain-link row and both
compressed related-record rows, including every evidence field.
The full native source and [live StrainInfo strain 394319](https://api.straininfo.dsmz.de/v2/data/strain/max/394319)
confirm DSM 25902 deposit SI-DP 896978, taxon 1303863, BacDive
130289, available deposit status, published-online strain status and
DOI `10.60712/SI-ID394319.3`. The [DataCite registration](https://api.datacite.org/dois/10.60712/SI-ID394319.3)
confirms the dataset DOI, publisher and strain-page target. Preserve
the distinction between `straininfo.deposit:896978` and
`straininfo.strain:394319`; neither is an assembly accession.

All source-coverage counts match the corresponding inventories:
NCBI 1 NAME, LPSN 1 NAME with `skos:closeMatch`, BacDive 1 STRAIN,
MediaDive 1 MEDIUM, GOLD 3 ORGANISM and BactoTraits 1
TRAIT_ASSERTION. The MediaDive inventory identifies medium 1452;
BacDive and DSMZ independently associate that medium with DSM 25902.
The MediaDive page's strain section was not successfully retrieved.
The source-count attestation is not an encoded growth experiment or a
specific physiological assertion. BacDive inventory `medium_count=0`
does not negate the separately sourced MediaDive attestation.

`data/taxa/PATHS.tsv:106296` pins the slug, and
`curation/seed_scope.tsv:12073` supports the six-source admission
reason. The embedded 2026-09-13T17:54:04Z seed event, source list,
curator and action agree. `SEEDED` remains appropriate; this report
does not promote the record's curation status.

## Completeness

Complete structured scans and ignored-inclusive ID, label, slug and
culture-designation searches covered raw inventories, curation, history,
native catalogs, BacDive, BV-BRC, GOLD, SeqCode and StrainInfo objects.
All ten matching native objects from the initial taxon search were read
in full. Exact-field inventory comparisons found no direct GTDB or
Madin membership. NCBI type-material rows explicitly support all three
existing type aliases; they are already present in the strain object.

The full [SeqCode API record 2987](https://api.seqco.de/v1/names/2987.json)
and its local native object independently corroborate the ICNP species
and three type designations. No separate SeqCode nomenclature entry is
required merely because a retained catalog object exists.

Complete exact-strain scans found no rows in the raw strain assembly
or genome-record inventories, StrainInfo assemblies, or AllTheBacteria
strain/genome links. Ignored-inclusive searches additionally covered
the full AllTheBacteria catalog and overlays, StrainInfo link, assembly,
exclusion and related-record tables. Exact GOLD organism identifiers
were searched across the local organism, project and analysis sources;
no additional target project/analysis chain was established. Neither the
inspected native nor live StrainInfo object supplies sequence objects.
The empty genome slots are justified within these boundaries, not proof
that no genome exists elsewhere.

StrainInfo also contains LMG 28486 / SI-DP 901948 for this strain.
This is a potential upstream inventory enrichment, not a broken current
link: the importer links deposits already represented in the BacDive
culture inventory, which contains the other three designations. Do not
attach a new deposit solely by group membership or expand a genome
match through it. Any future addition should verify that deposit's own
primary culture record and the maintained BacDive inventory first.

Numeric near-matches were rejected using complete objects and typed
identifiers. NCBI assembly GCA_022563135.1 belongs to Chloroflexota
bacterium taxon 2026724; its matching number was a genome-size value.
The StrainInfo occurrence of SI-DP 130289 belongs to Campylobacter
jejuni subsp. jejuni, SI-ID 45143 / CCUG 10968, not BacDive 130289.
No genome or culture link was inferred from these numeric collisions.

No gene, regulator, pathway, explicit trait or transcriptomic claim is
present; iModulonDB is not applicable. A source count with unit
TRAIT_ASSERTION does not supply such a biological claim. No causal
graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Nomenclature type-designation coverage is narrower than
  the inspected authorities. Only `kgmicrobe.strain:DSM-25902` appears
  in `nomenclature.type_strain_designations`; LPSN, the original paper,
  DSMZ, SeqCode and NCBI type material also support
  `kgmicrobe.strain:CCTCC-AB%202012043` and
  `kgmicrobe.strain:YIM-95345`. Both aliases already occur in the
  same type-strain object, so identity and strain coverage remain sound.
  Maintained owners: the kg-microbe LPSN transform configured through
  `conf/sources.yaml`, `src/taxonmech/extract.py:420` and
  `src/taxonmech/seed.py`; `data/raw/lpsn_names.tsv` is an intermediate
  projection, not the authoritative manual-edit location.

## Recommended Edits

For M1, trace LPSN 791954 through the maintained upstream transform
and its source snapshot. `extract_lpsn` collects strain objects from
`biolink:close_match` edges in the transformed LPSN edge table; the
inspected downstream inventory contains only the DSM edge's identifier.
Determine whether the two other aliases were absent from that snapshot
or lost during transformation. No particular extraction defect is
established without that comparison. Correct the owning transform with
a regression test if evidence was lost, or incorporate the aliases in
an authorized source refresh if they were not in the pinned input.
Then use the documented extraction and seeding workflow to regenerate.

Do not patch generated YAML, broaden type material beyond supported
deposits, merge the two GOLD source-field assertions, convert marker
or dataset identifiers into genomes, or alter `SEEDED` status during
this read-only review. LMG inventory enrichment is optional follow-up,
not a prerequisite for this verdict.

## Follow-up Checks

After an authorized correction, compare source edges, the raw LPSN row
and generated nomenclature; prove all three supported designations
resolve to the existing type strain without changing strain_count.
Test accession case and percent-encoded spaces. Rerun both focused
validators above after the documented dry-run/canary regeneration.
Corpus-wide claims additionally require `just verify-corpus` and full
QC, neither run here. The notification's species row and the MediaDive
page's strain section remain limited direct-web verification gaps.

## Additional Notes

Absence checks included ignored files through complete structured reads,
`find` and `rg --no-ignore --hidden -z`. An initially overbroad source-ID
search included a large manifest and truncated output; a corrective
complete search restricted to TSV, compressed TSV and compressed JSONL
completed and was inspected. No absence finding relies on truncated
output. Original source archives were not reproduced.

All known evidence-search and validator processes completed. Public
NCBI, StrainInfo and DataCite metadata reads used network escalation
after established sandbox DNS failures. Unavailable browser DOI,
PubMed and SeqCode views were supplemented with inspected primary
API or publisher metadata; uninspected full text is explicitly bounded.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
