# YAML Record Review: Wolbachia endosymbiont of Carystus phorcus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_carystus_phorcus.yaml`
- Started UTC: 2026-10-07T14:51:55Z
- Finished UTC: 2026-10-07T14:55:46Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for
`NCBITaxon:1035968`, Wolbachia endosymbiont of Carystus phorcus.
It asserts species rank, bacterial domain, code 11,
11 root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle,
zero inventoried BacDive strains, one NCBITAXON name attestation,
and one inline seed event. No synonyms, nomenclature, mappings,
strain/genome objects, citations, phenotypes, or causal graph
are asserted. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_carystus_phorcus.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_carystus_phorcus.yaml --out /private/tmp/wol-cphor-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Bounded parsed source comparisons passed for identity, lineage labels/ranks/links, empty synonym columns, attestation, unique scope/path rows, and seed wording. These checks do not reproduce the corpus.
- Live NCBI EFetch and Datasets taxonomy, exact Assembly/Nuccore searches, and full metadata/features/references of both returned nucleotide records were inspected. Sequence/translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy terms were checked against NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- NCBI's taxonomy browser was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD/protein objects, sequence alignments, or the primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035968&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035968)
confirm the active exact taxid, label, species rank,
bacterial lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms genetic code 11.
This is the bacterium associated with the named host, not
the host taxon or an asserted synonym of another Wolbachia node.

Complete pinned source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222227`,
`data/catalog/ncbi_names-0005.jsonl.gz:31739`,
`data/taxa/PATHS.tsv:14725`, and
`curation/seed_scope.tsv:322484`.
The native name row is a scientific name; raw synonym
columns and live alternate-name fields supply no synonym.

Every ancestor ID, label, rank, and parent link matches the
pinned root-first chain. Datasets includes root; EFetch
provides the remaining labeled chain, including Pseudomonadati,
Pseudomonadota, Alphaproteobacteria, Rickettsiales,
Anaplasmataceae, Wolbachieae, and Wolbachia.
Snapshot date is 2026-09-13 and `retired_into` is empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

## Evidence

The source attestation counts one `NAME`, not two sequences,
specimens, cultures, infections, or genomes. Exact-target
scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin,
and BactoTraits inventories found no applicable rows.
With no backbone descendants, the zero BacDive inventory
count agrees with the source data.

The seed wording matches the scope row and attestations.
Its `2026-09-13T17:54:04Z` timestamp is the latest of the
three fully read raw, ATB, and StrainInfo manifests,
as specified by `src/taxonmech/seed.py::_seed_timestamp`.
It is not a claim of manual curation or biological observation.

Exact Nuccore query `txid1035968[Organism:noexp]` returned
two partial COI records. Both explicitly carry
`taxon:1035968`, host Carystus phorcus, translation table 11,
codon start 3, and collection locality Quebrada Raiz,
Sector Del Oro, Guanacaste, Costa Rica.

| Accession | Length (nt) | Specimen voucher | Collection date | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- | --- |
| [JF902190.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902190.1) | 487 | `BIOUG<CAN>:CSRII433-04.w` | 10 March 2002 | `ASLEP007-10.COI-5P` |
| [JF902191.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902191.1) | 490 | `BIOUG<CAN>:CSRII434-04.w` | 6 August 2002 | `ASLEP008-10.COI-5P` |

Both retain a Smith manuscript reference labeled unpublished
and a direct submission dated 1 May 2011 at the University
of Guelph. CDS protein IDs AEG78011.1 and AEG78012.1,
primer qualifiers, and collection metadata were read as
GenBank values, not independently verified protein functions
or BOLD objects. JF902191.1 also carries primer text in a note.

The relevant
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes bacterial COI
recovered during insect barcoding, the .w convention, and
the ASENZ collection. Its main text did not match Carystus;
accession-level details are deferred to Table S2, not inspected
here. This is methodological context, not accession-specific
proof of an allele, reproductive phenotype, or prevalence.
GenBank's unpublished label is preserved as stored, not
treated as evidence that no relevant publication exists.

Specimen vouchers are not culture deposits; these partial
markers are not genome assemblies. They do not contradict
`strain_count: 0` or the one-name attestation.
Exact Assembly query `txid1035968[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
That bounded indexing result is not global genome absence.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional fields need not be filled without applicable evidence.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed files were included.
Patterns covered taxid, host-qualified name, slug,
both nucleotide accessions, both voucher stems, and BOLD stems.

All 20 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6810` describes Campylobacter jejuni PNUSAC014825, taxid 197, assembly GCA_010359685.1. Its accession digits are a collision, not target evidence.
- `data/catalog/gtdb_genomes-0008.jsonl.gz:15329` describes GCF_042661845.1, NCBI Actinomadura yumaensis taxid 111807 and GTDB Spirillospora yumaensis, with contig N50 10359680. That numeric match is unrelated to this Wolbachia record.
- Ten ATB rows at lines 143499-143508 describe Escherichia coli samples SAMEA110359680 through SAMEA110359689.
- Five ATB rows at lines 401096-401100 describe Enterococcus cecorum samples SAMEA12751075 through SAMEA12751079; run IDs ERR10359681 through ERR10359685 are numeric collisions.

Expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. This is not a global absence claim.

iModulonDB is not applicable: the record asserts no regulator,
expression module, or transcriptomic dataset. Optional COI
barcoding context does not constitute expression evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields,
attestation unit, inventory count, optional omissions,
and seed provenance are supported.

## Recommended Edits

None required. Preserve generated YAML and
`mapping_status: SEEDED`; review does not authorize promotion
or a curation-history event.

Future source corrections belong to maintained upstream
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages.
Optional enrichment must retain exact taxid, accession
version, and specimen scope without inventing strain or
genome equivalence.

## Follow-up Checks

No corrective follow-up is required.
Before optional literature enrichment, inspect Table S2 and
reconcile its exact accessions with current sequence records.
Verify independent BOLD/protein objects only when a proposed
claim relies on those objects; align sequences before making
allele or strain-equivalence claims.

After separately authorized maintained-input changes, rerun
the owning generator, per-file schema/strict checks, and
applicable full-corpus acceptance gates. New curated history
requires `just validate-history`; new graph terms/evidence
require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical
before report creation. All bounded source reads and public
retrievals reached terminal results. No YAML, source inventory,
lifecycle, standalone history, generated page, GitHub state,
branch, or worktree was changed. Eukaryota records were not
re-reviewed. Only this new timestamped report was written.

