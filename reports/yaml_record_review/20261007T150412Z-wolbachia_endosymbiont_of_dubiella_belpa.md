# YAML Record Review: Wolbachia endosymbiont of Dubiella belpa

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_dubiella_belpa.yaml`
- Started UTC: 2026-10-07T15:02:10Z
- Finished UTC: 2026-10-07T15:04:12Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for
`NCBITaxon:1035970`, Wolbachia endosymbiont of Dubiella belpa.
It carries species rank, bacterial domain, genetic code 11,
11 root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle,
zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects,
citations, phenotypes, or causal graph are asserted.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_dubiella_belpa.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_dubiella_belpa.yaml --out /private/tmp/wol-dbelpa-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Bounded parsed source comparisons passed for identity, each ancestor label/rank/link, empty synonym columns, attestation, unique scope/path rows, and seed wording. They do not substitute for corpus reproduction.
- Live NCBI EFetch/Datasets taxonomy, exact Assembly/Nuccore searches, and full metadata/features/references of the sole returned nucleotide record were inspected. Sequence/translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked against NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD/protein objects, sequence alignments, or the primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035970&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035970)
agree on the active exact taxid, label, species rank,
bacterial lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11.
This denotes the bacterial taxon associated with the named
host, not the host organism or an equivalent of another
host-qualified Wolbachia node.

Complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222229`,
`data/catalog/ncbi_names-0005.jsonl.gz:31741`,
`data/taxa/PATHS.tsv:14727`, and
`curation/seed_scope.tsv:322486`.
The native scientific-name row, empty raw synonym columns,
and absence of alternate names in the live response agree
with omission of synonyms.

Every ancestor ID, label, rank, and parent link agrees with
the pinned root-first chain. Datasets includes root;
EFetch supplies the remaining labeled chain, including
Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
The snapshot is dated 2026-09-13 and `retired_into` is empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

## Evidence

The source attestation counts one `NAME`, not a culture,
specimen, infection, sequence, or genome. Exact-target
scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin,
and BactoTraits inventories found no applicable rows.
With no backbone descendants, zero inventoried BacDive
strains agrees with the source data.

The inline seed wording matches the scope row and attestation.
Its timestamp `2026-09-13T17:54:04Z` is the latest inspected
raw, ATB, and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.
It is not manual review or biological observation time.
`EXACT` grounding is distinct from the `SEEDED` lifecycle.

Exact Nuccore query `txid1035970[Organism:noexp]`
returned [JF902195.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902195.1),
a 551-nt partial COI record explicitly assigned to
`taxon:1035970`, with host Dubiella belpa.
Its source feature gives voucher
`BIOUG<CAN>:MHAHE829-06.w`,
BOLD cross-reference `ASLEP041-10.COI-5P`,
and a collection on 27 July 2005 at Loaiciga,
Sector Pitilla, Guanacaste, Costa Rica.

The CDS is partial at both ends, with codon start 1,
translation table 11, and protein ID AEG78016.1.
Primer qualifiers, collection metadata, references, and
all non-payload fields were read.
The record retains a Smith barcoding-manuscript reference
labeled unpublished and a direct submission dated
1 May 2011 at the University of Guelph.
BOLD and protein identifiers are reported as GenBank
cross-references, not independently retrieved objects
or experimentally validated functions.

The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes bacterial COI
recovered during insect barcoding, the .w convention,
and the ASENZ collection. The main text did not match
Dubiella; accession details are deferred to Table S2,
which was not inspected. This supplies methodological
context, not an exact-target allele, prevalence, or
reproductive-phenotype assertion.
GenBank's unpublished label is preserved as stored,
not taken as proof that no relevant publication exists.

The voucher is not a culture deposit and the partial
marker is not a genome assembly. Neither contradicts
`strain_count: 0` or the one-name attestation.
Exact Assembly query `txid1035970[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics;
this bounded indexing result is not global genome absence.

## Completeness

Complete enough for the generated NCBI-only identity purpose.
Optional fields are appropriately empty without applicable
supported objects; the external marker does not require
inventing a culture or genome relationship.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Hidden, ignored, and compressed content was included.
Patterns covered taxid, host-qualified label, slug,
JF902195, MHAHE829-06, and ASLEP041-10.

All 15 candidate rows were read completely:

- Three describe the target backbone, scope, and native scientific name.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6811` describes Campylobacter jejuni PNUSAC014921, taxid 197, assembly GCA_010359705.1. Its accession digits are a collision.
- `data/catalog/ncbi_genbank-0059.jsonl.gz:7680` describes an uncultured Clostridia bacterium, taxid 244328, assembly GCA_938041105.1. The number 1035970 is its genome size, not the target taxid.
- Ten ATB rows at lines 143519-143528 describe Escherichia coli samples SAMEA110359700 through SAMEA110359709. Matching digits are not taxonomic evidence.

The expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression
module, or transcriptomic dataset is asserted.
Optional COI barcoding context is not expression evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields,
attestation unit, inventory count, optional omissions,
and seed provenance are supported.

## Recommended Edits

None required. Preserve generated YAML and
`mapping_status: SEEDED`; this review does not authorize
lifecycle promotion or a curation-history event.

Future source corrections belong to maintained upstream
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages.
Optional enrichment must preserve exact taxid, accession
version, and voucher scope without asserting genome
or culture equivalence.

## Follow-up Checks

No corrective follow-up is required.
Before optional literature enrichment, inspect Table S2
and reconcile the exact accession against current taxonomy.
Independently resolve BOLD/protein objects only when a new
claim relies on them; align sequences before allele claims.

After separately authorized maintained-input changes,
rerun the owning generator, per-file schema/strict checks,
and applicable full-corpus acceptance gates.
New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical
before report creation. All bounded local reads and public
retrievals reached terminal results.
No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was changed.
Eukaryota records were not re-reviewed.
Only this new timestamped report was written for this target.

