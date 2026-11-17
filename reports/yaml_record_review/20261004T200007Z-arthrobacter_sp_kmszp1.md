# YAML Record Review: Arthrobacter sp. KMSZP1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_kmszp1.yaml`
- Started UTC: 2026-10-04T19:58:23Z
- Finished UTC: 2026-10-04T20:00:07Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033890`,
Arthrobacter sp. KMSZP1: SPECIES, BACTERIA, parent `NCBITaxon:235627`,
`grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11.
It contains ten root-first ancestors, zero inventoried BacDive strains,
one NCBITAXON name attestation and one seed event. It asserts no external
name equivalence, deposit, genome or mechanism.

This is one target review. Other isolates in the inspected literature
were evidence context, not additional reviewed records. No record,
source input, code, status or curation-history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_kmszp1.yaml`.
  Output: `No issues found`.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_kmszp1.yaml`.
  One file scanned, zero files with errors and zero error rows. This is
  the implementation of `just validate-strict`; its standard diagnostic
  is `reports/instance_validation_failures.tsv`.
- Passed bounded source comparisons of identity, the complete ancestor
  chain, direct inventories, filename lock, scope and seed wording. A
  complete backbone scan found no child taxa.
- Not run: `just verify-corpus`. Its inspected implementation compares
  the entire corpus; `--max-diffs` only caps diagnostic output. Bounded
  source comparisons do not establish byte-level reproduction.
- Not applicable: `just validate-products`, because there are no
  curator-added causal-graph nodes. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.
  Full-corpus QC, provenance, rendering and test-suite gates were not run.

## Identity and Grounding

The complete backbone row `data/raw/ncbitaxon_taxa.tsv:221324`, native
name object `data/catalog/ncbi_names-0005.jsonl.gz:30664` and inspected
[NCBI taxonomy response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033890&retmode=xml)
agree on the identifier, scientific name, species rank, parent, bacterial
domain and genetic code. The
[Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033890)
confirms all ten lineage IDs, including root 1. The live expanded lineage
agrees with the backbone's labels and ranks where supplied.

The direct parent is unclassified Arthrobacter under genus Arthrobacter;
the family, order, class, phylum and kingdom are Micrococcaceae,
Micrococcales, Actinomycetes, Actinomycetota and Bacillati. These are
carried NCBI placements, not an inferred reconciliation of literature
identifications. SPECIES is NCBI's rank for this placeholder concept,
not a claim that KMSZP1 is a validly published species name.

The native name object contains only the scientific name. The backbone
synonym fields are empty, and complete exact-ID scans of type-material,
merged-ID and dropped-taxon tables returned no matching rows. The live
response does not supply a replacement or synonym.

## Evidence

The source attestation reproduces one NAME assertion, the exact NCBI
identifier and label, and the pinned taxonomy snapshot `2026-09-13`.
Complete directly mapped BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
BactoTraits inventory scans found no target rows. No descendant pool
exists from which to gather additional BacDive strains.

An exact-taxonomy nuccore search returned one entry. Its metadata,
references and feature qualifiers were read through the
[NCBI sequence response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768706.1&rettype=gb&retmode=xml):
`JF768706.1` is a 1,408-base partial 16S rRNA sequence, explicitly
classified as taxon 1033890 and strain KMSZP1. The source describes a
uranium-rich site at Domiasiat, India. It supplies no registered culture
deposit or genome accession.

The sequence links [PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/),
DOI `10.1264/jsme2.ME12074`, Microbes and Environments 28(1):33-41
(2013; online October 2012). PubMed metadata and abstract, the article
body and the exact Table 2 row with its headers and footnotes were
inspected via the [Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML).
Table 2 explicitly connects KMSZP1 to JF768706 and lists Arthrobacter
ureafaciens as its closest 16S match at 99.36% similarity. This is
sequence-based literature identification, not an authoritative NCBI
merge or a deposit identity. The comparison culture MTCC 3454 is
separate and must not be assigned to KMSZP1. Study-wide uranium-binding
results or other isolates' gene results cannot be transferred wholesale
to this record. Supplementary PDF content was not inspected.

These sources support the isolate/taxon context while leaving NCBI's
placeholder classification intact. The record contains no physiological
claim requiring import of the paper's assays, and optional record-level
literature evidence is not required for a seeded name-only record.

The exact-taxonomy Assembly search returned zero entries with a
`phrasesnotfound` warning for `txid1033890[Organism:noexp]`. It is not
proof that no genome exists anywhere or under another classification.
The Taxonomy Browser HTML was inaccessible, and PMC's HTML page showed
a browser check; the direct public APIs and Europe PMC XML succeeded.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The taxon, name, slug and
KMSZP1 spelling variants produced five matching lines, all inspected.
The complete matching native NCBI name object was also read.

Three relevant matches were the backbone, scope and scientific-name
object. The other two were unrelated Streptococcus pneumoniae records:
a GenBank isolate named `1033890`, and AllTheBacteria sample
`SAMEA1033890`. These numeric collisions do not establish taxon or
strain identity. A separate ignored-inclusive search for JF768706 and
23080407 across the same roots completed with zero matches.

No eligible deposit or strain-genome assertion for KMSZP1 was found in
that searched scope. The zero strain count means zero inventoried
BacDive strains, not absence of a biological isolate. A partial 16S
sequence and its paper do not create a missing genome assembly link.
Empty optional nomenclature, mappings, definitions, evidence and
mechanism fields are appropriate for the current source-supported record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected evidence scope. Identity, lineage,
attestation, strain count, lifecycle status and inline provenance are
supported. The paper's closest-match identification is preserved as
source context rather than used to overwrite NCBI's classification.

## Recommended Edits

None. Preserve the generated YAML. Any future source-backed identity or
strain-link correction belongs in the maintained inventory pipeline and,
when necessary, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`.
Scope changes belong in `curation/seed_scope.tsv`. A literature
similarity result alone is insufficient to change the NCBI identity.

## Follow-up Checks

On future source refreshes, recheck the exact taxon and KMSZP1/JF768706
pair for explicit deposit or genome evidence. Keep comparison strain
MTCC 3454 and similarly named study isolates separate. Any later
phenotype curation should use this isolate's own assay row and conditions
in the sibling repository that models the phenotype. Rerun focused
validators after an authorized change and the full `just verify-corpus`
gate after regeneration. No unresolved blocker prevents this verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13780` locks the current slug.
`curation/seed_scope.tsv:321654` supplies the September 13, 2026 addition
and one-source reason. The inline seed event at `2026-09-13T17:54:04Z`
exactly reproduces the NCBITAXON source list and scope reason. This
read-only review does not promote SEEDED to REVIEWED or append an event.

Ignored-inclusive report/history/curation filename searches found no
earlier target report or target-specific history artifact before this
report was created. iModulonDB is not applicable to the record's
taxonomic assertions; the paper was used for identity context, not a
new gene or expression-module claim. No paid research, outside contact,
GitHub mutation or generator run occurred.
