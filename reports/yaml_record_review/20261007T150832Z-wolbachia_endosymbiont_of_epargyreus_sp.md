# YAML Record Review: Wolbachia endosymbiont of Epargyreus sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_epargyreus_sp.yaml`
- Started UTC: 2026-10-07T15:05:20Z
- Finished UTC: 2026-10-07T15:08:32Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for
`NCBITaxon:1035971`, Wolbachia endosymbiont of Epargyreus sp.
It asserts species rank, bacterial domain, code 11,
11 root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle,
zero inventoried BacDive strains, one NCBITAXON name
attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects,
citations, phenotypes, or causal graph are asserted.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_epargyreus_sp.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_epargyreus_sp.yaml --out /private/tmp/wol-eparg-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Bounded parsed source checks passed for identity, every ancestor label/rank/link, empty synonym columns, attestation, unique scope/path rows, and seed wording. These checks are not corpus reproduction.
- Live NCBI EFetch/Datasets taxonomy was inspected for the target and both separately named Epargyreus-associated taxa. Exact Assembly/Nuccore queries and a broader name search were inspected. All eight candidate nucleotide objects' metadata/features/references were read completely, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked against NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The target NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: historical accession reassignment, independent BOLD/protein objects, sequence alignment, or the primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035971&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035971)
confirm the active exact taxid, label, species rank,
bacterial lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms code 11.
This is the bacterial node, not the host organism.
Its NCBI species rank neither resolves the host's unspecified
species nor asserts a formally established nomenclatural name.

Complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222230`,
`data/catalog/ncbi_names-0005.jsonl.gz:31742`,
`data/taxa/PATHS.tsv:14728`, and
`curation/seed_scope.tsv:322487`.
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

Two similar names remain distinct active bacterial nodes:

- [NCBITaxon:1084943](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084943&retmode=xml): Wolbachia endosymbiont of Epargyreus 06-SRNP-101532, with synonym Wolbachia sp. Epargyreus 06-SRNP-101532.
- [NCBITaxon:1084944](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084944&retmode=xml): Wolbachia endosymbiont of Epargyreus Burns11, with synonym Wolbachia sp. Epargyreus Burns11.

Full live EFetch/Datasets responses agree with their complete
pinned backbone rows at lines 233132-233133, scope rows at
331678-331679, and native name rows at 44941-44944 in
`data/catalog/ncbi_names-0005.jsonl.gz`.
Each has one scientific-name and one synonym row.
These names are not synonyms of the target.
Shared parentage and overlapping host text do not establish
equivalence or authorize moving sequence evidence.

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
`txid1035971[Organism:noexp]` both returned zero with
phrase-not-found/no-items diagnostics. Those are bounded
indexing results, not proof of global or historical
sequence/genome absence or taxon invalidity.

Broader Nuccore query
`Wolbachia[Organism] AND Epargyreus[All Fields]`
returned eight partial COI records, all assigned to the
two separate taxids above, none to the target:

| Candidate accession | Organism taxid | Length (nt) | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- | --- |
| [JF902199.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902199.1) | 1084944 | 644 | `BIOUG<CAN>:CSRII365-04.w` | `ASLEP006-10.COI-5P` |
| [JF902200.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902200.1) | 1084944 | 626 | `BIOUG<CAN>:MHAHC753-05.w` | `ASLEP020-10.COI-5P` |
| [JF902201.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902201.1) | 1084944 | 577 | `BIOUG<CAN>:MHAHC754-05.w` | `ASLEP011-10.COI-5P` |
| [JF902202.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902202.1) | 1084944 | 613 | `BIOUG<CAN>:MHAHC765-05.w` | `ASLEP022-10.COI-5P` |
| [JF902203.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902203.1) | 1084944 | 613 | `BIOUG<CAN>:MHAHC774-05.w` | `ASLEP023-10.COI-5P` |
| [JF902204.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902204.1) | 1084944 | 657 | `BIOUG<CAN>:MHAHG137-06.w` | `ASLEP049-10.COI-5P` |
| [JN674119.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674119.1) | 1084943 | 658 | `BLPAB593-06.w` | `ASWLP002-11.COI-5P` |
| [JN674120.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674120.1) | 1084944 | 621 | `MHMXK138-07.w` | `ASWLP019-11.COI-5P` |

The six JF records retain host qualifier Epargyreus sp.
but explicitly identify their organism as the Burns11
bacterium and carry `taxon:1084944`.
The two JN records provide their more specific host labels.
A matching host qualifier does not override an organism taxid.

All eight give Costa Rican collection metadata and
translation table 11. JN674119.1 has codon start 2;
the others have codon start 1.
The JF records retain direct submission dated 1 May 2011,
and the JN records 13 September 2011, at the University
of Guelph, alongside unpublished Smith manuscript references.
Primer qualifiers and protein IDs were inspected as
GenBank data; BOLD/protein objects were not independently
retrieved. These candidate values are not target claims.

The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, gives insect-barcoding
methodological context and refers accession details to
Table S2. Main-text search did not match Epargyreus;
the supplement was not inspected. No exact-target allele,
prevalence, reproductive phenotype, or historical reassignment
is inferred. GenBank's unpublished label is retained as stored,
not interpreted as absence of a relevant publication.

Vouchers are not culture deposits and partial COI markers
are not genome assemblies. These near-name candidates
therefore neither contradict the target's inventory count
nor establish a missing strain/genome link.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Empty exact-taxid sequence queries do not justify deleting
an active taxonomy node or importing evidence from neighbors.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
It included ignored, hidden, and compressed content.
Patterns covered taxid, host-qualified label, slug,
Epargyreus generally, and all eight candidate nucleotide,
voucher, and BOLD stems.

All 21 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- Eight describe the two distinct Epargyreus-qualified bacterial nodes: backbone, scope, scientific name, and synonym for each.
- Ten ATB rows at lines 143529-143538 describe Escherichia coli samples SAMEA110359710 through SAMEA110359719. Matching sample digits are not taxonomic evidence.

Expanded marker/voucher/BOLD search returned no further rows.
Five native `SOURCE.json` files were parsed completely and
history filenames searched independently.
No additional applicable local assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within the bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module,
or transcriptomic dataset is asserted. Candidate COI
barcoding evidence is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields,
one-name attestation, inventory count, optional omissions,
and seed provenance are supported.
The broader sequence hits belong to distinct taxa and
do not establish a missing target linkage.

## Recommended Edits

None required. Preserve generated YAML and
`mapping_status: SEEDED`; no status promotion or
curation-history event is authorized by this review.

Future source corrections belong to maintained upstream
inputs and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML/pages.
Any proposed equivalence with either Epargyreus-qualified
neighbor requires explicit authority evidence.

## Follow-up Checks

No corrective follow-up is required.
Before optional enrichment, resolve exact organism taxids
and inspect accession-level primary evidence.
Historical accession/taxonomy evidence and Table S2 would
be needed before claiming a reassignment or relationship
between the three taxonomic nodes. Current checks establish
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
Eukaryota records were not re-reviewed.
Only this new timestamped report was written for this target.

