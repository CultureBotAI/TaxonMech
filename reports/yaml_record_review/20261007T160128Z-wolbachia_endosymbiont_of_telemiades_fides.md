# YAML Record Review: Wolbachia endosymbiont of Telemiades fides

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_telemiades_fides.yaml`
- Started UTC: 2026-10-07T15:59:37Z
- Finished UTC: 2026-10-07T16:01:28Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035983`,
Wolbachia endosymbiont of Telemiades fides. It asserts species rank,
bacterial domain, parent 2640676, code 11, 11 root-first ancestors,
`EXACT` grounding, `SEEDED` lifecycle, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects, citations,
phenotypes, or causal graph are asserted. Seeded fields are read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_telemiades_fides.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_telemiades_fides.yaml --out /private/tmp/wol-telemiades-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed comparisons passed for the full backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks do not reproduce the corpus.
- Live NCBI EFetch XML and Datasets JSON, exact Assembly/Nuccore queries, and the sole nucleotide object's complete metadata/features/references were inspected. Sequence/translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035983&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035983)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch confirms
code 11. This denotes the bacterium, not its Telemiades host;
NCBI species rank does not establish formal nomenclatural status.

Complete pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222242`,
`data/catalog/ncbi_names-0005.jsonl.gz:31755`,
`data/taxa/PATHS.tsv:14740`, and `curation/seed_scope.tsv:322499`.
The native row is a scientific name with empty unique name. Backbone
synonym columns and live alternate-name fields are empty, consistent
with YAML omission. Snapshot date is 2026-09-13; `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia, and unclassified
Wolbachia. Parsed inventories contain no target child, type-material,
merged-ID, or dropped row. `EXACT` grounding does not promote `SEEDED` lifecycle.

## Evidence

The sole NCBITAXON attestation counts one `NAME`, not specimens,
infections, cultures, sequences, or genomes. Exact-target scans of
raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits
inventories found no applicable rows. With no backbone descendants,
zero inventoried BacDive strains agrees with the inputs without
implying biological absence of strains or infections.

Inline seed wording matches the scope row and attestation.
The `2026-09-13T17:54:04Z` timestamp equals the latest inspected raw,
ATB, and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035983[Organism:noexp]` returned
[JF902250.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902250.1), a 611-nt
partial COI object explicitly identifying the target organism and
`taxon:1035983`, with host Telemiades fides. It supplies specimen voucher
`BIOUG<CAN>:MHMXW208-09.w`, GenBank-reported BOLD cross-reference
`ASLEP070-10.COI-5P`, codon start 1, translation table 11, and protein
cross-reference `AEG78071.1`. Its locality is only Costa Rica; no
collection date, collector, coordinates, or finer locality are supplied.
Identification, both PCR primer qualifiers, and the additional reverse
primer note were read without collapsing repeated fields. Independent
BOLD/protein objects were not retrieved.

GenBank retains a Smith unpublished manuscript reference and a direct
submission dated 1 May 2011 at the University of Guelph. The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes bacterial COI recovered
during insect barcoding, `.w` sample IDs, and accession details in
Table S2. Main-text search did not match Telemiades; Table S2 was not
inspected. The paper supplies methodological context, not an inspected
exact-target allele, prevalence, or reproductive-phenotype assignment.
GenBank's unpublished label is not evidence that no related publication exists.

Exact Assembly query `txid1035983[Organism:noexp]` returned zero with
phrase-not-found/no-items diagnostics. This bounded index result does
not prove global or historical genome absence. The marker is not an
assembly or cultured strain; the voucher is not a culture deposit.
It establishes neither a missing strain-genome link nor a contradictory
inventoried BacDive count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, broader Wolbachia/Telemiades
combinations, JF902250, MHMXW208-09, and ASLEP070-10.

All 27 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- Ten ATB rows at lines 143649-143658 describe Escherichia coli samples SAMEA110359830 through SAMEA110359839. Sample digits cause the matches.
- Three ATB rows at lines 401104-401106 describe Enterococcus cecorum samples SAMEA12751083 through SAMEA12751085, assemblies ERZ25181932, ERZ25181943, and ERZ25181953. Runs ERR10359831, ERR10359832, and ERR10359839 cause the matches. Sylph's Enterococcus_E cecorum labels were retained as source classifications.
- One ATB row at line 549323 describes Klebsiella pneumoniae sample SAMEA3357202, assembly ERZ3256717, and run ERR1035983. The run ID is a numeric collision.
- Ten ATB rows at lines 1716052, 1716059-1716061, 1716063-1716064, 1716070-1716072, and 1716074 have Salmonella enterica scientific names and runs SRR10359830 through SRR10359839. Samples are SAMN13152868, SAMN13152875, SAMN13152876, SAMN13152877, SAMN13152879, SAMN13152880, SAMN13152886, SAMN13152887, SAMN13152888, and SAMN13152890. Sylph assigns SAMN13152876, SAMN13152877, and SAMN13152888 to Salmonella houtenae. These foreign-source differences are preserved, not target conflicts; the run digits cause the matches.

Expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. No additional applicable local assertion,
culture deposit, strain-genome link, or standalone target history
artifact was found within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Optional COI barcoding evidence
does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name attestation,
inventoried strain count, optional omissions, and seed provenance are
supported. The exact-taxid marker does not establish a missing genome
link or justify filling unreported collection metadata.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Before optional marker enrichment,
inspect Table S2 and accession-specific primary evidence, keeping
specimen, marker, strain, and assembly identities separate.
After separately authorized maintained-input changes, rerun the owning
generator, per-file schema/strict validation, and applicable full-corpus
acceptance gates. New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The entire YAML was reread and remained byte-identical before report
creation. All bounded local reads and public retrievals reached terminal
results. No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was changed.
Eukaryota records were not re-reviewed. Only this new timestamped
report was written for this target.
