# YAML Record Review: Paenibacillus senegalensis JC66

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_senegalensis_jc66.yaml`
- Started UTC: 2026-10-04T19:04:52Z
- Finished UTC: 2026-10-04T19:08:43Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1033743`:
rank `STRAIN`, domain `BACTERIA`, parent species `NCBITaxon:1465766`,
`EXACT` grounding and `SEEDED` mapping status. It has ten root-first
ancestors, genetic code 11, one GTDB mapping, two exact synonyms, one
GTDB xref, zero inventoried BacDive strains and four source attestations.
The seed event is dated 2026-09-13T17:54:04Z.

The parent species YAML was read in full for scope comparison, not
reviewed as a second target. Maintained owners are source extraction,
`curation/seed_scope.tsv`, `data/taxa/PATHS.tsv` and `src/taxonmech/seed.py`.
Neither generated record was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_senegalensis_jc66.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_senegalensis_jc66.yaml`: exit 0, one file, zero errors; normal diagnostic TSV under `reports/`.
- Bounded structured checks compared identity, all ten ancestors, direct source inventories, path lock, scope and seed-event wording. They are not a focused corpus reproduction validator.
- `just verify-corpus` was skipped: it rebuilds the full corpus, with no target-record selector; `--max-diffs` only limits diagnostics.
- `just validate-products` was not applicable to this record's source identity fields: no curator-grounded graph nodes are present. NCBI identity was checked directly.
- Ignored-inclusive target searches found no separate target history artifact. Full-history validation, full `just qc`, corpus tests, all-record validation, provenance hashing and rendering checks were skipped. No history or status was changed.

## Identity and Grounding

[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033743&retmode=xml)
confirms the identifier, exact label, strain rank, species parent,
genetic code 11 and synonym `Paenibacillus sp. JC66`.
[Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033743)
corroborates the complete ancestor ID chain. These agree with the pinned
backbone at `data/raw/ncbitaxon_taxa.tsv:221308` and all ten lineage rows.
Native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:30631`
and line 30632 support the scientific name and NCBI synonym respectively.

The full relevant inventories contain no child, merged-ID, dropped-ID or
direct type-material row for this taxon. Type designations under the
parent species do not change the target's strain rank. `EXACT` NCBI
grounding is sound; the problematic equivalence is the additional GTDB
species xref and synonym, not the NCBI record identity.

## Evidence

| Emitted assertion | Inspected support and scope |
|---|---|
| NCBI name attestation, count 1 | Backbone row and live taxonomy agree; snapshot 2026-09-13. This counts a source name, not isolates. |
| GTDB mapping and attestation, count 2 | `data/raw/gtdb_mappings.tsv:1370` and `data/raw/gtdb_species.tsv:133700` reproduce the source predicate and species-cluster count. The count is not two genomes assigned specifically to JC66. |
| GOLD organism attestation, count 1 | `data/raw/gold_organisms.tsv:451` and full native `data/gold/organisms.jsonl.gz:14774` identify `Go0017282`, JC66, taxon 1033743. |
| Madin trait-assertion attestation, count 5 | `data/raw/madin_taxa.tsv:630` supplies that count and taxon. No individual phenotype is asserted in this YAML. |
| Scope and seed event | `data/taxa/PATHS.tsv:13761` fixes the slug; `curation/seed_scope.tsv:26084` supplies the four-source inclusion reason reproduced by the seed event. |

A complete scan of 901,341 GTDB genome objects found exactly two unique
members of `s__Paenibacillus_L senegalensis`:

| GTDB genome | Source object | NCBI taxon / species taxon | Assembly and sample |
|---|---|---|---|
| `RS_GCF_000285515.1` | `data/catalog/gtdb_genomes-0002.jsonl.gz:37678` | 1033743 / 1465766 | JC66, `GCA_000285515.1`, `SAMEA2271960`; representative and type material |
| `RS_GCF_902374655.1` | `data/catalog/gtdb_genomes-0007.jsonl.gz:30779` | 1465766 / 1465766 | MGYG-HGUT-01404, `GCA_902374655.1`, `SAMEA5850907`; not marked type material |

Both full native objects were read. The same species cluster also maps
to the parent species in `data/raw/gtdb_mappings.tsv:31612`. Its members
support a species-level grouping containing the JC66 genome, not an
equivalence between that entire species and the individual strain.
Matching assembly statistics do not establish strain identity or justify
merging the two BioSamples; neither do different accessions alone prove
biologically distinct strains.

[NCBI Datasets assembly](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000285515.1/dataset_report)
confirms the current JC66 GenBank assembly and current paired RefSeq
assembly, scaffold level, type-material status and `SAMEA2271960`.
An exact-taxonomy Assembly search returned one assembly record, the same
paired assembly. Native current objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:6563` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:5602` agree.

The second GTDB member occurs in the historical NCBI catalogs at
`data/catalog/ncbi_genbank_historical-0001.jsonl.gz:41269` and
`data/catalog/ncbi_refseq_historical-0002.jsonl.gz:4033`: both are marked
suppressed, with non-live date 2026-04-03. This does not invalidate the
pinned GTDB cluster count, which is source membership rather than a
claim of two currently available JC66 genomes. No suppression reason
or biological duplication was inferred.

## Completeness

The full direct inventories have no target LPSN, BacDive, MediaDive or
BactoTraits row. A gitignore-independent compressed-content search
(`rg --no-ignore --hidden -z`) covered the taxon ID, species name and
JC66 designation under `data/raw`, `data/catalog`, `data/bacdive`,
`data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`,
`curation` and `history`. Numeric substrings, JC664/JC665/JC669 and an
unrelated Listeria isolate also named JC66 were excluded.

Zero listed BacDive strains is consistent with source classification,
not evidence that JC66 lacks a deposited culture. The full native
`data/bacdive/records.jsonl.gz:52824` classifies BacDive 130511 at parent
species 1465766 while its sequence assertions name strain taxon 1033743.
The live [BacDive 130511 page](https://bacdive.dsmz.de/strain/130511)
confirms this distinction, JC66, DSM 25958 and CSUR P157. The parent YAML
already retains the culture, source assembly and genome links; the seeder
rolls strains up from descendants, not down from ancestors. There is no
missing classified child strain to manufacture from a shared label.

[LPSN's species page](https://lpsn.dsmz.de/species/paenibacillus-senegalensis)
likewise identifies the parent species and its type culture. The pinned
LPSN row maps to 1465766, not 1033743, and supplies no GTDB identifier
that independently establishes strain equivalence. Its species authority
and nomenclature should not be transplanted as strain-level claims.

Optional record-level citations, definitions and causal graphs may remain
empty. No literature citation or verbatim evidence snippet is asserted
by this target. iModulonDB was not applicable: there is no gene, regulator,
pathway or transcriptomic assertion.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species mapping is promoted to strain equivalence.**
   The target is a strain, but its xref asserts equivalence to the whole
   GTDB species and its exact synonym omits the strain designation.
   This conflicts with the schema's true-equivalence requirement for
   `xrefs` and with the complete GTDB membership evidence above.
   `src/taxonmech/seed.py:451` treats every source `skos:closeMatch` as
   identity without checking rank, then lines 467-469 emit the xref and
   exact synonym. The raw mapping is faithfully copied, but its
   promotion to identity is unsupported. These are two manifestations
   of one scope error, not separate findings.

## Recommended Edits

1. In `src/taxonmech/seed.py`, make identity promotion rank-aware. Do not
   emit a GTDB species xref or exact synonym for an infraspecific taxon
   solely because the source predicate is `skos:closeMatch`. Preserve
   this strain's NCBI identity, synonym, parent and lineage.
2. Retain the source mapping and source-cluster count with an explicit
   scope note while the upstream kg-microbe mapping is investigated.
   Species membership is supported; equivalence to this strain is not.
   Any source-predicate correction belongs upstream and in maintained
   extraction (`scripts/extract_source_inventory.py` /
   `src/taxonmech/extract.py`), not a hand-edited raw row or generated YAML.
3. Add regression coverage in `tests/test_seed.py` for a strain and its
   parent species sharing this GTDB cluster, including the source count
   and rank distinction. Preserve legitimate species-level equivalences.
   After an authorized fix, regenerate through
   `scripts/seed_from_sources.py`, not by editing this report or YAML.

## Follow-up Checks

- Run `uv run pytest tests/test_seed.py` after the future seeder change and verify that the strain loses only unsupported GTDB identity claims, while its source mapping remains traceable.
- Rerun both target validators, compare the generated strain and parent species, then run full `just verify-corpus` and applicable `just qc` gates after authorized regeneration.
- Recheck GTDB membership and any upstream predicate correction at refresh time. Preserve source-cluster counts separately from current exact-taxonomy assembly counts; do not infer that MGYG-HGUT-01404 and JC66 are the same strain.

## Additional Notes

The GTDB taxon page was inaccessible through the web reader; the full
pinned native genome objects and complete membership scan supplied its
source evidence. Live NCBI taxonomy and assembly APIs, BacDive and LPSN
were accessible. Current GTDB web membership was therefore not verified.

The report does not review the parent species' entire evidence or
establish culture availability, phenotype, genome quality or a new
taxonomic interpretation. Only this review report was added apart from
the validator's normal diagnostic output. No source record, generator,
inventory, history, status or previous report was edited. No paid
research, external contact or GitHub mutation was performed.
