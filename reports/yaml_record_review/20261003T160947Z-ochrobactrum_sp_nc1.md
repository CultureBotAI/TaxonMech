# YAML Record Review: Ochrobactrum sp. NC1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/ochrobactrum_sp_nc1.yaml`
- Started UTC: 2026-10-03T16:07:06Z
- Finished UTC: 2026-10-03T16:09:47Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read before judgement. It denotes
`NCBITaxon:1303813`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:239106`, genetic code 11, grounding `EXACT`, status `SEEDED`.
Eleven lineage entries, one NCBI NAME attestation, strain count zero and
one embedded seed event are present. No synonyms, nomenclature, GTDB
mapping, equivalence xref, strain row, genome link, experimental claim or
causal graph is asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/ochrobactrum_sp_nc1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/ochrobactrum_sp_nc1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and all eleven lineage entries; the target has no children in that
  backbone. Complete exact-field inventory scans find no direct BacDive,
  LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits taxon membership.
- The complete PATHS and scope tables each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target entry.
  Standalone history validation had no target; strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308146` supports the exact ID and label,
species rank, unclassified-Ochrobactrum parent, genetic code and empty
synonym fields. Native scientific-name object
`data/catalog/ncbi_names-0007.jsonl.gz:30695` agrees.

The NCBI browser page was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303813&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 239106, code
11 and full non-root lineage without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303813)
confirms rank and all eleven ancestor IDs including root. Read-only API
calls used network escalation after established sandbox DNS failures.

The Brucella/Ochrobactrum group and unclassified Ochrobactrum ancestors
are NCBI `NO_RANK` groupings. Keep the exact supplied lineage; neither
the NC1 designation nor a neighboring named species warrants a rank,
genus or species reassignment. `EXACT` grounds this NCBI entity, not a
nomenclaturally validated binomial or resolved named-species identity.

## Evidence

The single NCBITAXON attestation identifies NCBITaxon:1303813 and
counts one NAME from the 2026-09-13 snapshot, matching the backbone
row and native name object. A name count does not establish a strain
deposit, phenotype or genome. No DOI, PMID, source accession or quoted
experimental evidence is asserted.

`curation/seed_scope.tsv:393094` admits the taxon on 2026-09-13 with
one source. The exact reason and source name appear in the
2026-09-13T17:54:04Z event, curator seed_from_sources, action
SEEDED_FROM_SOURCES. The event agrees with `SEEDED` and does not
claim human review.

## Completeness

Ignored-inclusive searches by ID, full label and slug covered
`data/raw/`, `curation/`, `history/` and all compressed JSONL files under
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/`. All matching native objects were
read in full. Four incidental numeric assembly matches were excluded:

- `data/catalog/ncbi_genbank-0066.jsonl.gz:44498`, GCA_983007015.1,
  Gammaproteobacteria bacterium taxon 1913989, SAMEA122306163.
- `data/catalog/ncbi_genbank-0066.jsonl.gz:44794`, GCA_983010485.1,
  Thermus thermophilus taxon 274, SAMEA122306373.
- `data/catalog/ncbi_genbank-0064.jsonl.gz:38225`, GCA_977196865.1,
  uncultured bacterium taxon 77133, SAMEA120687490.
- `data/catalog/ncbi_genbank-0064.jsonl.gz:41679`, GCA_977249615.1,
  uncultured bacterium taxon 77133, SAMEA120692003.

In these objects, 1303813 is a total or ungapped genome length, not the
taxon ID. None describes NC1. An additional ignored-inclusive compressed
search for whole-token NC1, retaining objects containing Ochrobactrum or
Brucella, found only the target scientific-name object. This is a bounded
name search, not proof that every record called NC1 denotes this organism.

No target BacDive strain, LPSN inventory name, GTDB mapping/genome,
NCBI assembly, BV-BRC genome, GOLD organism, SeqCode name or StrainInfo
native object was found within those sources. Full BacDive membership
and the singleton subtree support strain count zero without asserting
biological absence or nonexistence of sequences elsewhere.

Further ignored-inclusive searches of StrainInfo link/assembly/exclusion
TSVs, its compressed related-record table, `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz` found no target ID, full label or
slug. Raw assembly/genome/related tables were included in the raw-directory
search. No supported deposit/BioSample join was discovered. Do not attach
unrelated genomes on the basis of bare NC1 or a numeric match.

Optional nomenclature, synonyms, mappings and strain slots are correctly
empty at the reviewed source boundary. Do not inherit a nearby taxon's
type status, names or phenotype. No named gene, locus, regulator, pathway,
trait or transcriptomics dataset is asserted; iModulonDB is not applicable.
No causal graph is required for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required by this review. Preserve the NCBI backbone and generated
record boundary. Future supported source enrichment belongs in maintained
extraction inputs or `src/taxonmech/extract.py`, with seeder behavior in
`src/taxonmech/seed.py` and regression tests, not a manual YAML edit.
Retain `SEEDED`; this review does not promote human-review status.

## Follow-up Checks

No finding-specific check is outstanding. New source evidence would require
exact identity/deposit verification, authorized dry-run/canary steps, and
both focused validators after regeneration. Run `just verify-corpus` and
full QC for any corpus change. The focused pass does not claim that
unrun corpus-wide checks passed or that the pinned-source searches are a
complete census of external biological knowledge.

## Additional Notes

The initial unanchored lookahead name-search command was terminated after
its inefficient expression was identified. A completed equivalent two-stage
whole-token NC1 and genus-context search supplied the additional search
result; no conclusion relies on the terminated command.

The only manual write is this report; strict validation wrote its standard
diagnostic. Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden`, using `-z` for compressed sources.
No record, source, prior report, history or status was edited. No generator,
refresh, paid research, GitHub mutation or cross-repository write occurred.
No Eukaryota record was re-reviewed.
