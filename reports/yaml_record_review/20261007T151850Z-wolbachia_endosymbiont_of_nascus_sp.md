# YAML Record Review: Wolbachia endosymbiont of Nascus sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_nascus_sp.yaml`
- Started UTC: 2026-10-07T15:13:48Z
- Finished UTC: 2026-10-07T15:18:50Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for
`NCBITaxon:1035973`, Wolbachia endosymbiont of Nascus sp.
It asserts species rank, bacterial domain, code 11,
11 root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle,
zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects,
citations, phenotypes, or causal graph are asserted.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_nascus_sp.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_nascus_sp.yaml --out /private/tmp/wol-nascus-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Bounded parsed source checks passed for identity, every ancestor label/rank/link, empty synonym columns, attestation, unique scope/path rows, and seed wording. These checks are not corpus reproduction.
- Live NCBI EFetch/Datasets taxonomy was inspected for the target and the separately named Nascus Burns01 bacterium. Exact Assembly/Nuccore queries and a broader name search were inspected. The candidate nucleotide object's metadata/features/references were read completely, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked against NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The target NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: historical accession reassignment, independent BOLD/protein objects, sequence alignment, or the primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035973&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035973)
confirm the active exact taxid, label, species rank,
bacterial lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11.
This is the bacterial node, not the host organism.
Its NCBI species rank neither resolves the host's unspecified
species nor asserts a formally established nomenclatural name.

Complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222232`,
`data/catalog/ncbi_names-0005.jsonl.gz:31744`,
`data/taxa/PATHS.tsv:14730`, and
`curation/seed_scope.tsv:322489`.
The native row is a scientific name. Empty pinned synonym
columns and live alternate-name fields agree with omission
of synonyms.

Every ancestor ID, label, rank, and parent link agrees with
the pinned root-first chain. Datasets includes root;
EFetch supplies the remaining labeled chain through
Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
Snapshot date is 2026-09-13 and `retired_into` is empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

[NCBITaxon:1094259](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1094259&retmode=xml),
Wolbachia endosymbiont of Nascus Burns01, is a distinct
active species-ranked bacterial node under the same parent.
Its full EFetch and Datasets responses agree with complete
pinned backbone row 235305, scope row 333618, and native
scientific-name row 47534 in the same files above.
No synonym identifies it as the target.
Shared parentage and overlapping host text do not establish
equivalence or authorize transferring sequence evidence.

## Evidence

The attestation counts one `NAME`, not a sequence, infection,
specimen, culture, or genome. Exact-target scans of raw
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits
inventories found no applicable rows. With no backbone
descendants, zero inventoried BacDive strains agrees
with the source inputs.

Inline seed wording matches the scope row and attestation.
The timestamp `2026-09-13T17:54:04Z` equals the latest
inspected raw, ATB, and StrainInfo extraction timestamp,
following `src/taxonmech/seed.py::_seed_timestamp`.
`EXACT` grounding is not a promotion of the `SEEDED` lifecycle.

Exact Assembly and Nuccore queries
`txid1035973[Organism:noexp]` both returned zero with
phrase-not-found/no-items diagnostics. Those are bounded
indexing results, not proof of global or historical
sequence/genome absence or taxon invalidity.

Broader Nuccore query
`Wolbachia[Organism] AND Nascus[All Fields]`
returned one candidate,
[JF902214.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902214.1),
a 639-nt partial COI sequence assigned explicitly to
`taxon:1094259`, the Nascus Burns01 bacterium, not this target.
The source feature retains host qualifier Nascus sp.;
that qualifier does not override the organism taxid.

The candidate gives specimen voucher
`BIOUG<CAN>:CSRII459-04.w`, GenBank-reported BOLD cross-reference
`ASLEP009-10.COI-5P`, and a 28 December 1996 collection at
Quebrada Las Yeguitas, Sector Orosi, Guanacaste, Costa Rica.
Its CDS uses translation table 11 and codon start 1,
with protein cross-reference `AEG78035.1`.
Primer and other source qualifiers were inspected as
GenBank data; BOLD/protein objects were not independently
retrieved. These candidate values are not target claims.

The sequence retains an unpublished Smith manuscript
reference and a direct submission dated 1 May 2011 at
the University of Guelph. The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, gives insect-barcoding
methodological context and refers accession details to
Table S2. Main-text search did not match Nascus;
the supplement was not inspected. No exact-target allele,
prevalence, reproductive phenotype, or historical reassignment
is inferred. GenBank's unpublished label is retained as stored,
not interpreted as absence of a relevant publication.

A specimen voucher is not a culture deposit and a partial
COI marker is not a genome assembly. This near-name candidate
therefore neither contradicts the target's inventory count
nor establishes a missing strain/genome link.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Empty exact-taxid sequence queries do not justify deleting
an active taxonomy node or importing evidence from a neighbor.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
It included ignored, hidden, and compressed content.
Patterns covered taxid, host-qualified label, slug,
Nascus generally, and candidate nucleotide, voucher,
and BOLD stems `JF902214`, `CSRII459-04`, and `ASLEP009-10`.

All 20 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- Three describe the distinct Nascus Burns01 bacterium: backbone, scope, and native scientific name.
- Three backbone rows, at lines 14351, 126469, and 522512, describe Monascus ruber, Blastobotrys apis, and Blastobotrys vanleenenianus. Related Monascus/Trichomonascus names produce substring matches, not Wolbachia identities.
- One complete StrainInfo object at `data/straininfo/records.jsonl.gz:194265` describes SI-ID 252276, Monascus ruber, taxid 89489. Its ATCC 16433 and NRRL 1753 deposits and ATCC-linked partial LSU sequence AF364978 belong to that fungus; the stored sequence description contains Monascus sp. No target linkage is established.
- Ten ATB rows at lines 143549-143558 describe Escherichia coli samples SAMEA110359730 through SAMEA110359739. Matching sample digits are not taxonomic evidence.

Expanded marker/voucher/BOLD search returned no further rows.
Five native `SOURCE.json` files were parsed completely and
history filenames searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within the bounded roots. No global absence is claimed.
Fungal source candidates were inspected only to disambiguate
false matches; no Eukaryota YAML record was re-reviewed.

iModulonDB is not applicable: no regulator, expression module,
or transcriptomic dataset is asserted. Candidate COI
barcoding evidence is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields,
one-name attestation, inventory count, optional omissions,
and seed provenance are supported.
The broader sequence hit belongs to a distinct taxon and
does not establish a missing target linkage.

## Recommended Edits

None required. Preserve generated YAML and
`mapping_status: SEEDED`; no status promotion or
curation-history event is authorized by this review.

Future source corrections belong to maintained upstream
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages.
Any proposed equivalence with the Nascus Burns01 node
requires explicit authority evidence.

## Follow-up Checks

No corrective follow-up is required.
Before optional enrichment, resolve exact organism taxids
and inspect accession-level primary evidence.
Historical accession/taxonomy evidence and Table S2 would
be needed before claiming a reassignment or relationship
between the two taxonomic nodes. Current checks establish
present separate identities, not their historical derivation.

After separately authorized maintained-input changes,
rerun the owning generator, per-file schema/strict validation,
and applicable full-corpus acceptance gates.
New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical
before report creation. All bounded local reads and public
retrievals reached terminal results.
No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was changed.
Only this new timestamped report was written for this target.
