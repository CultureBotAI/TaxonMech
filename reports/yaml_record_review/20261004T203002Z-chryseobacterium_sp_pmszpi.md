# YAML Record Review: Chryseobacterium sp. PMSZPI

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_pmszpi.yaml`
- Started UTC: 2026-10-04T20:26:59Z
- Finished UTC: 2026-10-04T20:30:02Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1033900`,
Chryseobacterium sp. PMSZPI. It is SPECIES/BACTERIA under
`NCBITaxon:2593645`, with thirteen ancestors, genetic code 11, EXACT
grounding and SEEDED status. It has a two-genome GTDB closeMatch, the
corresponding GTDB synonym/xref, zero BacDive strains, NCBITAXON and
GTDB attestations, and one seed event. No record, source input, code,
status or history entry was edited.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/chryseobacterium_sp_pmszpi.yaml`; no issues found.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/chryseobacterium_sp_pmszpi.yaml`; one file, zero errors. This implements `just validate-strict` and emits `reports/instance_validation_failures.tsv`.
- Bounded source comparisons passed for identity, every ancestor, direct
  inventories, scope, slug and seed text. The full GTDB native-catalog
  scan counted and inspected both cluster members.
- Not run: full-corpus `just verify-corpus`; `--max-diffs` is only a
  diagnostic cap. These comparisons are not a byte-reproduction gate.
  Full QC, rendering and tests were not run.
- Not applicable: `just validate-products`, because no curator graph nodes
  are asserted. NCBI identifiers were checked at source.
- Not run: `just validate-history`; ignored-inclusive searches found no
  target-specific history artifact. The inline event was inspected.
- Live GTDB taxon/genome HTML could not be opened; its API documentation
  endpoint returned HTTP 403. GTDB conclusions below concern the pinned
  native catalog, not a verified newer release. NCBI live APIs succeeded.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221334`, full native name object
`data/catalog/ncbi_names-0005.jsonl.gz:30674`,
[NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033900&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033900)
agree on identity, label, species rank, bacterial domain, parent and
code 11. All thirteen lineage IDs match, including root; live expanded
labels and ranks agree where supplied. The NCBI chain includes
Pseudomonadati, the FCB and Bacteroidota/Chlorobiota clades, Bacteroidota,
Flavobacteriia, Flavobacteriales, Weeksellaceae, Chryseobacterium group,
Chryseobacterium and unclassified Chryseobacterium.

The rank is NCBI's placeholder rank, not nomenclatural validity. NCBI's
native name and backbone supply no synonyms. The YAML synonym is
explicitly GTDB-derived, not presented as an NCBI synonym. Complete
exact-ID type-material, merged-ID and dropped-taxon scans found no rows.
The live response supplies no replacement or identity correction.

## Evidence

`data/raw/gtdb_mappings.tsv:1383` and `gtdb_species.tsv:42551` provide
`GTDB:s__Chryseobacterium_sp002835665`, `skos:closeMatch` and count 2.
A complete scan of 901,341 native GTDB rows found exactly two distinct
cluster members, both with NCBI taxon and species taxon 1033900:

| Pinned member | Native row | Assembly level | BioSample |
|---|---|---|---|
| RS_GCF_002835665.1 | `data/catalog/gtdb_genomes-0009.jsonl.gz:44669` | Contig | SAMN08135438 |
| RS_GCF_047221375.1 | `data/catalog/gtdb_genomes-0010.jsonl.gz:33460` | Complete Genome | SAMN44376294 |

Both full native objects were inspected. The newer member is the pinned
GTDB representative despite the species identifier retaining the older
accession's number. This is not an identity error. Both rows have only
PMSZPI in `ncbi_strain_identifiers`, not a registered culture deposit.
The single species cluster and common NCBI identity support the retained
closeMatch, synonym/xref and two-GENOME attestation under repository
mapping rules. NCBI's Flavobacteriia and GTDB's Bacteroidia classifications
remain separate; GTDB does not overwrite the carried NCBI lineage.

The complete exact-taxonomy Assembly query returned two entries. Full
[older assembly/BioSample metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_002835665.1/dataset_report)
and [newer assembly/BioSample metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_047221375.1/dataset_report)
confirm current accessions and GenBank pairs GCA_002835665.1 and
GCA_047221375.1, respectively. Their separate projects are PRJNA421227
and PRJNA1175970. The older assembly has 79 contigs and 3,824,868 bases;
the newer has one chromosome and 4,741,859 bases. Neither complete
BioSample metadata object supplies a culture-collection accession.
These are separate assemblies and samples, not duplicate aliases.

Four complete native GenBank/RefSeq rows were checked at
`ncbi_genbank-0002.jsonl.gz:12153`, `ncbi_genbank-0043.jsonl.gz:26940`,
`ncbi_refseq-0001.jsonl.gz:33663` and `ncbi_refseq-0007.jsonl.gz:5768`
under `data/catalog/`. They agree with the assembly identities.
Full BV-BRC objects `data/bvbrc/bvbrc-0000.jsonl.gz:3250` and `:3251`
retain genome records 1033900.12 and 1033900.4, with explicit sample,
project and sequence accessions. The newer row supplies CP178384 but
does not itself supply an assembly accession. Neither row adds a
registered deposit; taxonomy/name matching alone cannot attach them
to a nonexistent BacDive strain entry.

The full GOLD chain was inspected: Go0488009 at
`data/gold/organisms.jsonl.gz:337448` connects through Gp0371797 at
`projects.jsonl.gz:259394` to Ga0339393 at `analyses.jsonl.gz:199356`.
The analysis references that project, GCA_002835665.1, PIZV00000000 and
IMG 2816332650. Its direct organism field is empty, but the project
resolves to Go0488009 without a conflicting organism. Crucially, the
organism's culture-collection field is empty. The source chain preserves
genome context but does not establish an eligible culture-deposit join.
Go/Gp/Ga IDs remain organism/project records, not genome identifiers.

The one-NAME NCBI attestation and snapshot `2026-09-13` are exact.
Complete directly mapped BacDive, LPSN, GOLD, MediaDive, Madin and
BactoTraits inventory scans returned no rows; a complete backbone scan
found no descendants. Thus zero BacDive strains is correct. Native GOLD
catalog presence is distinct from a row in the mapped GOLD inventory.

[JF768716.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JF768716.1&rettype=gb&retmode=xml)
was inspected separately: a 1,420-base partial 16S sequence explicitly
assigned to PMSZPI and taxon 1033900, citing
[PMID 23080407](https://pubmed.ncbi.nlm.nih.gov/23080407/), DOI
`10.1264/jsme2.ME12074`. Article metadata/body had already been read in
this ongoing session. A fresh
[Table 2 XML read](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4070695/fullTextXML)
checked headers, footnotes and PMSZPI/JF768716: closest match
Chryseobacterium culicis at 98.87%, not formal species identity.
The supplementary PDF was not inspected. No phenotype or mechanism is
asserted by this YAML or added from the literature.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json` manifests. The taxon/name/slug/designation/
GTDB-species search produced 17 matching lines. All matching contexts
were inspected, including the unrelated Streptococcus pneumoniae sample
SAMEA1033900. Relevant native JSON objects were read in full.

An initially broad accession search returned 79 lines, including other
assemblies with the same numeric suffix and other WGS prefixes. A
refined search using the complete assembly numbers, samples, projects,
GOLD/IMG IDs, marker and bounded PIZV prefix returned 13 matching lines,
all in the already inspected GTDB, NCBI, BV-BRC and GOLD sources. It
found no additional eligible deposit or strain crosswalk, nor an ATB
entry for either actual sample in these roots. JF768716 had no local hit.

The exact-taxonomy nuccore query reported 164 records; only the first
20 IDs were returned, and all 164 sequence records were not inspected.
This review makes no exhaustive nucleotide or gene-content claim.
Both Assembly entries, both complete embedded BioSamples and the
target marker were inspected directly.

No supported BacDive/deposit anchor was found. The absence of strain
links is therefore consistent with the current model; it is not a claim
of genome absence. Empty nomenclature, definition, record-level evidence
and causal graphs are appropriate for this source-attested seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, carried lineage,
two-genome GTDB mapping/attestation, source-derived synonym/xref, zero
BacDive count, status and seed provenance are supported. Live GTDB
availability remains a verification limit, not evidence of an error.

## Recommended Edits

None. Do not attach genomes using bare PMSZPI or a shared taxon ID, and
do not patch generated YAML. A future explicit deposit or BacDive
classification should enter the maintained inventory pipeline; joining
changes belong in `src/taxonmech/extract.py` or `src/taxonmech/seed.py`
with tests, and scope changes in `curation/seed_scope.tsv`.

## Follow-up Checks

Recheck the GTDB species and both members at its authority when access
is available. On source refresh, verify complete deposit identifiers
before adding strain links, and preserve the two assemblies' separate
sample/project chains. After authorized changes, rerun focused
validators and the full `just verify-corpus` gate after regeneration.
No unresolved blocker prevents the pinned-record verdict.

## Additional Notes

`data/taxa/PATHS.tsv:13790` locks the slug;
`curation/seed_scope.tsv:66002` records the September 13, 2026 addition
and two-source reason. The event at `2026-09-13T17:54:04Z` reproduces
the GTDB, NCBITAXON source list and scope reason. NAME and GENOME units
were not summed.

Both live BioSamples report collection date 2012-08-23, whereas the
marker's direct submission is dated 2011-04-01. These are retained as
source metadata, not silently reconciled into a single physical-sample
history. The YAML makes no collection-date or cross-sample equivalence
claim, so this does not require a record correction.

Ignored-inclusive report/history/curation filename searches found no
prior target report or target-specific history artifact before creation.
iModulonDB is not applicable to the asserted taxonomic claims. No paid
research, outside contact, GitHub mutation, generator run, status
promotion or history event occurred.
