# YAML Record Review: Bacillus sp. EGY-SCuR2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_egy_scur2.yaml`
- Started UTC: 2026-10-03T18:27:15Z
- Finished UTC: 2026-10-03T18:28:22Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303880`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:185979`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded
seed event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_egy_scur2.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bacillus_sp_egy_scur2.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured comparison reproduced identity, rank, parent, code,
  empty synonym fields and all ten lineage objects. No children occur.
  Complete exact-field scans found no membership in seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308198` supports the exact label,
species rank, parent, code, empty synonyms and 2026-09-13 snapshot.
The full scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30751` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Bacillus
and unclassified Bacillus (in: firmicutes). Preserve this chain and
the parent's qualified source label and `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303880&retmode=xml)
confirms ID, name, species rank, parent 185979, code 11 and all
non-root lineage entries. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303880)
confirms label, rank and all ten ancestor identifiers, including root.
Exact grounding and bacterial domain are supported. Preserve the
mixed-case EGY-SCuR2 source label. It does not establish a registered
deposit, a type strain or grounds for changing NCBI's species rank.

## Evidence

The NCBITAXON / NCBITaxon:1303880 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not biological
strains, phenotypes or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by this YAML.

`data/taxa/PATHS.tsv:106303` pins the slug.
`curation/seed_scope.tsv:393144` admits this species on 2026-09-13
with the exact one-source reason in the embedded seed event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML folding does not
change the reason. `SEEDED` remains appropriate; this review does
not confer human-review status.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and
EGY-SCuR2 searches covered raw inventories, curation and history,
returning only the target backbone and scope rows. Complete structured
exact-field scans found no direct BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits membership. No descendants in the
inspected backbone can contribute BacDive strains, supporting the zero
count within these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. Two objects matched and were
read in full: the target scientific-name object and an unrelated
assembly object. No eligible culture-deposit or explicit strain-genome
chain was established for this Bacillus.

`data/catalog/ncbi_genbank-0064.jsonl.gz:49696` identifies
GCA_977506855.1, uncultured archaeon taxon 115547, isolate
MarMAG_093387, BioProject PRJEB104710 and BioSample SAMEA120721781.
Its value 1303880 is `genome_size_ungapped`, not a taxon reference.
The assembly supplies no Bacillus relationship. No archaeal YAML was
re-reviewed while excluding this typed-identity mismatch.

Additional complete ignored-inclusive searches covered `data/atb/`,
the entire `data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV
and compressed TSV link, assembly, exclusion and related-record tables,
without a match. Empty optional fields are supported at this boundary,
not proof that cultures or sequences cannot exist elsewhere. Original
primary archives were not independently reproduced.

No gene, regulator, pathway, trait or transcriptomic assertion is
present; iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Retain the supported identity, source label and lineage, zero
strain count and `SEEDED` status. Do not infer a deposit from EGY-SCuR2
or join the unrelated archaeal assembly by its numeric genome length.
Future evidence belongs in maintained source pipelines and inventories,
followed by authorized seeding, not manual edits to generated YAML.

## Follow-up Checks

No corrective check is required. After an authorized source refresh,
compare this taxon's exact rows and any explicit deposit/genome chain,
then rerun both focused validators. Corpus-wide claims additionally
require `just verify-corpus` and full QC; neither was run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. Case-insensitive
searching was a discovery aid, not an instruction to normalize labels
or deposit accessions. All searches and validators completed. Public
NCBI metadata reads used network escalation after established sandbox
DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
