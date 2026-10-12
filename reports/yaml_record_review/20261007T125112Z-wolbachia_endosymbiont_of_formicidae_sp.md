# YAML Record Review: Wolbachia endosymbiont of Formicidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_formicidae_sp.yaml`
- Started UTC: 2026-10-07T12:45:44Z
- Finished UTC: 2026-10-07T12:51:12Z
- Verdict: pass

## Target

Reviewed the complete generated `TaxonRecord` for `NCBITaxon:1035898`,
Wolbachia endosymbiont of Formicidae sp.: `SPECIES`, `BACTERIA`,
`grounding_status: EXACT`, `mapping_status: SEEDED`. The record contains
11 lineage entries, two exact and six related synonyms, genetic code 11,
zero inventoried BacDive strains, one NCBITAXON name attestation, and one
inline seed event.

This bacterial taxon is not the eukaryotic host family Formicidae. Host-family
wording does not change the bacterial node's source-assigned species rank.
Future corrections belong to the maintained inputs and transforms described
below, not direct edits to this generated YAML.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_formicidae_sp.yaml`: passed; LinkML reported no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_formicidae_sp.yaml --out /private/tmp/wol-formicidae-strict.tsv`: passed; one file, zero error rows. Read the complete header-only diagnostics TSV.
- Read the entire target and compared its seeded values, all ancestor labels/ranks/links, synonym scopes, attestation, and seed-scope reason against parsed local source rows. These bounded comparisons passed; they are not a substitute for the documented corpus reproduction gate.
- Verified the target and retired alias at NCBI Taxonomy EFetch and Datasets, and read all 30 exact-taxid Nuccore metadata/feature/reference records.
- `just validate-products`: not applicable; no curated causal-graph grounding/label pairs are present. Taxonomic identifiers were checked at their source authority.
- Standalone `just validate-history`: not applicable to this target; ignored-independent history content and filename checks found no target history artifact. The inline event was covered by schema/strict validation and source comparisons.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. This is a read-only, single-record review, not a corpus-wide acceptance run.

## Identity and Grounding

The [live NCBI taxonomy record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035898&retmode=xml)
and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035898)
agree on the current identifier, exact scientific name, species rank,
bacterial placement, and lineage. Parent `NCBITaxon:2640676` is unclassified
Wolbachia. The root-first local chain agrees with the pinned backbone;
Datasets includes root, and EFetch supplies the subsequent labeled ancestors.
EFetch confirms translation code 11.

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222197` matches
the YAML, including the 2026-09-13 taxonomy snapshot and blank
`retired_into`. The target is uniquely indexed at
`data/taxa/PATHS.tsv:14696` and explicitly in scope at
`curation/seed_scope.tsv:322457`. No descendant was found in the parsed
backbone.

The two short names are NCBI `Synonym` values and correctly represented as
`EXACT_SYNONYM`. The six `Wolbachia sp. Formicidae_ASPNA...` values
are NCBI `Includes` values and correctly represented as
`RELATED_SYNONYM`: `ASPNA1149-10`, `ASPNA1152-10`,
`ASPNA1188-10`, `ASPNA1197-10`, `ASPNA1279-10`, and
`ASPNA495-09`. All nine native names, including the scientific name,
were read at `data/catalog/ncbi_names-0005.jsonl.gz:31693` through 31701.
Neither specimen labels nor similarly named Wolbachia records establish
taxonomic equivalence beyond these explicit authority assertions.

A real merge exists: `data/raw/ncbi_merged_ids.tsv:1113` maps
`NCBITaxon:1035893` to this taxon.
[EFetch for the old ID](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035893&retmode=xml)
returns 1035898 with 1035893 in `AkaTaxIds`;
[Datasets for the old ID](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035893)
also resolves to 1035898. The old identifier has no match in the compressed
retained predecessor inventory `data/ncbi/prior-taxonomy.tsv.gz` or
`PATHS.tsv`, and an ignored-inclusive scan of actual `data/taxa/`
files found no record with that identifier. The seeder derives `replaces`
from retained predecessor rows with `retired_into`, not every historical
NCBI merge. Its absence here is therefore consistent with
`src/taxonmech/extract.py`, `src/taxonmech/seed.py`, and the schema's
record-supersession semantics, not a missing retained-record link.

## Evidence

- The sole source attestation correctly records one `NAME` assertion from NCBITAXON for this exact ID and label. The eight synonyms do not multiply the inventory's name-attestation count.
- Exact-target scans of the seven raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. No target type-material or dropped-inventory row was found. The lack of children makes the zero BacDive count consistent with the bounded subtree inventory check.
- The seed event's source and scope wording agree with the inventories. Its `2026-09-13T17:54:04Z` timestamp matches the latest extraction time among the raw, ATB, and StrainInfo manifests read during the review.
- An exact `txid1035898[Organism:noexp]` Assembly query returned zero records with NCBI's organism-phrase-not-found/no-items warning. This is a bounded index result, not proof that no genome could exist under another identifier.
- The equivalent Nuccore query returned exactly 30 UIDs, all retrieved. Complete metadata, features, and references were read in two batches; nucleotide and translated sequence payloads were omitted. All carry `taxon:1035898` and code 11. Fifteen are partial COI genes and fifteen are partial WSP genes; none is a genome assembly.

| GenBank record | nt | Marker | Specimen voucher | Annotated protein |
|---|---:|---|---|---|
| [JN625800.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625800.1) | 415 | COI | `ASPNA495-09.w` | `AEO13059.1` |
| [JN625799.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625799.1) | 658 | COI | `ASPNA1279-10.w` | `AEO13058.1` |
| [JN625798.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625798.1) | 658 | COI | `ASPNA1197-10.w` | `AEO13057.1` |
| [JN625797.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625797.1) | 658 | COI | `ASPNA1188-10.w` | `AEO13056.1` |
| [JN625796.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625796.1) | 658 | COI | `ASPNA1152-10.w` | `AEO13055.1` |
| [JN625795.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625795.1) | 658 | COI | `ASPNA1149-10.w` | `AEO13054.1` |
| [JN625924.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625924.1) | 535 | WSP | `ASAMY230-07.w` | `AEO13183.1` |
| [JN625923.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625923.1) | 455 | WSP | `ASAMY229-07.w` | `AEO13182.1` |
| [JN625922.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625922.1) | 513 | WSP | `ASAMY281-07.w` | `AEO13181.1` |
| [JN625921.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625921.1) | 446 | WSP | `ASAMY245-07.w` | `AEO13180.1` |
| [JN625920.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625920.1) | 445 | WSP | `ASAMY208-07.w` | `AEO13179.1` |
| [JN625919.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625919.1) | 413 | WSP | `ASAMY285-07.w` | `AEO13178.1` |
| [JN625918.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625918.1) | 502 | WSP | `ASAMY220-07.w` | `AEO13177.1` |
| [JN625917.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625917.1) | 530 | WSP | `ASAMY346-07.w` | `AEO13176.1` |
| [JN625916.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625916.1) | 530 | WSP | `ASAMY343-07.w` | `AEO13175.1` |
| [JN625915.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625915.1) | 530 | WSP | `ASAMY339-07.w` | `AEO13174.1` |
| [JN625914.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625914.1) | 530 | WSP | `ASAMY347-07.w` | `AEO13173.1` |
| [JN625913.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625913.1) | 519 | WSP | `ASAMY342-07.w` | `AEO13172.1` |
| [JN625912.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625912.1) | 458 | WSP | `ASAMY159-07.w` | `AEO13171.1` |
| [JN625911.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625911.1) | 504 | WSP | `ASAMY181-07.w` | `AEO13170.1` |
| [JN625910.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625910.1) | 456 | WSP | `ASAMY184-07.w` | `AEO13169.1` |
| [JF902266.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902266.1) | 632 | COI | `BIOUG<CAN>:ASPNA984-10.w` | `AEG67024.1` |
| [JF902265.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902265.1) | 611 | COI | `BIOUG<CAN>:ASPNA973-10.w` | `AEG67023.1` |
| [JF902263.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902263.1) | 657 | COI | `BIOUG<CAN>:ASPNA1416-10.w` | `AEG67021.1` |
| [JF902262.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902262.1) | 657 | COI | `BIOUG<CAN>:ASPNA1402-10.w` | `AEG67020.1` |
| [JF902261.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902261.1) | 629 | COI | `BIOUG<CAN>:ASPNA055-08.w` | `AEG67019.1` |
| [JF902260.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902260.1) | 631 | COI | `BIOUG<CAN>:ASPNA027-08.w` | `AEG67018.1` |
| [JF902259.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902259.1) | 631 | COI | `BIOUG<CAN>:ASPNA026-08.w` | `AEG67017.1` |
| [JF902258.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902258.1) | 616 | COI | `BIOUG<CAN>:ASPNA016-08.w` | `AEG67016.1` |
| [JF902264.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902264.1) | 512 | COI | `BIOUG<CAN>:ASPNA164-08.w` | `AEG67022.1` |

The six `JN625795.1` through `JN625800.1` records explicitly identify
the six specimen-specific related names via their host/voucher qualifiers.
Those and the nine `JF902258.1` through `JF902266.1` COI records
have Papua New Guinea collection metadata; the fifteen
`JN625910.1` through `JN625924.1` WSP records have Madagascar
collection metadata. These are specimen-scoped source assertions, not
taxon-wide geographic, physiological, or host-range claims.

The WSP records explicitly cite DOI `10.1371/journal.pone.0036514`
and PMID `22567162`. Verified the
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/22567162/)
and inspected the [primary paper's methods](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514).
The study assays Wolbachia markers in insect extracts and explains the
`.w` specimen-label convention. The COI records retain unpublished
bibliographic entries with matching or closely matching titles; those
entries were not silently replaced with published citations. Table S2
and independent BOLD records were not checked for accession-level
reconciliation. The inspected evidence does not justify cultured-strain
entries, genome objects, taxon-wide prevalence, reproductive effects,
supergroup assignments, or causal edges.

No literature claim, PMID, DOI, genomic accession, or evidence quotation is
currently asserted by the YAML itself. These external marker observations
are bounded completeness checks, not missing mandatory source attestations.

## Completeness

Complete enough for this generated, NCBI-only identity record. Empty
nomenclature, type-strain, GTDB mapping, strain, genome, phenotype,
literature-evidence, and causal-graph slots are not defects without evidence
and a corresponding supported representation. `strain_count: 0` means
zero inventoried BacDive strains, not zero biological infections, specimens,
or sequence submissions.

Both initial and expanded local searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. Searches included hidden, ignored, and
compressed content, the current and merged numeric IDs, label/slug,
all eight synonym variants through matching name patterns, and the
30 sequence accessions, annotated protein IDs, vouchers, and BOLD IDs.

Both searches returned the same 12 candidate rows: one backbone, one
scope, one merge, and nine native-name rows. Every candidate was read
in full. The five native `SOURCE.json` metadata files were separately
parsed completely; history filenames were checked independently. No
additional applicable source assertion, culture deposit, strain-genome
link, or standalone target history was found in these bounded local
surfaces. This is not a claim of global absence from every external
database or publication.

iModulonDB was not applicable: the reviewed record has no gene, regulator,
expression module, transcriptomic dataset, or strain-specific mechanistic
claim. Optional COI/WSP sequence leads do not establish such a dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, name classes, attestation units, generated
status, zero BacDive count, and inline provenance are mutually consistent
within the inspected scope. The retired-ID merge is accounted for without
inventing a predecessor record.

## Recommended Edits

None required. Do not edit this generated YAML, promote it to
`REVIEWED`, add specimens as cultured strains, or create an audit
event solely because this read-only report exists.

If future authoritative evidence changes identity or retirement behavior,
the maintained owners are the NCBI source configuration/snapshot and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope decisions
belong in `curation/seed_scope.tsv`. Strain/genome enrichment requires
verified source records and explicit joins through the relevant maintained
source inputs, not host names or marker accessions alone.

## Follow-up Checks

No corrective action is required for this verdict.

For optional enrichment, reconcile exact accessions and specimen identities
against the primary supplement/BOLD before adding any scoped assertion.
Verify any proposed assembly at NCBI and establish an explicit strain link;
do not reinterpret short marker sequences as genomes.

After any later authorized upstream correction, run the appropriate
extraction/seeding workflow and the documented schema, strict,
corpus-reproduction, provenance, and QC gates. Run product/history
validation if that curation introduces those objects. They were not
replaced by custom focused validators here.

## Additional Notes

- Review baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was unchanged when reread before this report was written.
- This review creates only this timestamped report. No source, record, generated product, history, GitHub object, branch, or worktree was changed.
- Eukaryota remains outside this continuing review queue because it is already fully covered.
