# YAML Record Review: Wolbachia endosymbiont of Ocyba calathana

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_ocyba_calathana.yaml`
- Started UTC: 2026-10-07T15:21:02Z
- Finished UTC: 2026-10-07T15:23:29Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035974`,
Wolbachia endosymbiont of Ocyba calathana. It asserts species rank,
bacterial domain, code 11, 11 root-first ancestors, `EXACT` grounding,
`SEEDED` lifecycle, zero inventoried BacDive strains, one NCBITAXON
name attestation, and one inline seed event. It contains no synonyms,
nomenclature, mappings, strain/genome objects, citations, phenotypes,
or causal graph. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_ocyba_calathana.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_ocyba_calathana.yaml --out /private/tmp/wol-ocyba-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for the complete backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks are not corpus reproduction.
- Live NCBI EFetch XML and Datasets JSON, exact Assembly/Nuccore queries, and complete candidate nucleotide metadata/features/references were read. Sequence and translation payloads were excluded from metadata inspection.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035974&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035974)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676` (unclassified Wolbachia).
EFetch confirms genetic code 11. The record denotes the bacterium,
not its Ocyba host; NCBI species rank does not assert formal
nomenclatural establishment of the host-qualified bacterial name.

Complete pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222233`,
`data/catalog/ncbi_names-0005.jsonl.gz:31745`,
`data/taxa/PATHS.tsv:14731`, and `curation/seed_scope.tsv:322490`.
The native row is a scientific name. All pinned synonym columns are
empty, consistent with the live alternate-name fields and YAML omission.
The snapshot is 2026-09-13 and `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
Parsed inventories contain no target child, type-material, merged-ID,
or dropped row. Grounding `EXACT` and lifecycle `SEEDED` remain distinct.

## Evidence

The NCBITAXON attestation counts one `NAME`, not a sequence, specimen,
infection, culture, or genome. Exact-target scans of raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found
no applicable rows. With no backbone descendants, zero inventoried
BacDive strains agrees with the source inputs; it is not a claim
that no biological strains or infections exist.

The inline seed wording matches the scope row and attestation.
Its `2026-09-13T17:54:04Z` timestamp is the latest inspected raw,
ATB, and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035974[Organism:noexp]` returned one record:
[JF902216.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902216.1), a 657-nt
partial COI sequence explicitly assigned to `taxon:1035974`.
Its source organism and host qualifier agree with this bacterial
taxon and Ocyba calathana respectively. It reports specimen voucher
`BIOUG<CAN>:MHAHG107-06.w`, GenBank-reported BOLD cross-reference
`ASLEP048-10.COI-5P`, and collection on 17 March 2006 at Estacion
San Cristobal, Sector San Cristobal, Alajuela, Costa Rica.
The CDS has codon start 1, translation table 11, and protein
cross-reference `AEG78037.1`. Primer and other source qualifiers
were inspected; BOLD and protein objects were not independently fetched.

GenBank retains an unpublished Smith manuscript reference and a
direct submission dated 1 May 2011 at the University of Guelph.
The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes Wolbachia COI recovered
during insect barcoding, the bacterial `.w` sample suffix, and the
accession details in Table S2. Main-text search did not match Ocyba;
the supplement was not inspected. The paper provides methodological
context, not an inspected accession-level allele, prevalence, or
reproductive-phenotype assignment. GenBank's unpublished label is
retained as stored, not interpreted as absence of a relevant publication.

Exact Assembly query `txid1035974[Organism:noexp]` returned zero with
phrase-not-found/no-items diagnostics. This is a bounded index result,
not proof of global or historical genome absence.
The COI marker is not an assembly and its specimen voucher is not
a culture deposit; neither establishes a missing strain-genome link
or contradicts the inventory count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strains, genome links, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, Ocyba generally, and
marker/voucher/BOLD stems `JF902216`, `MHAHG107-06`, and `ASLEP048-10`.

All 20 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- Five describe Campylobacter strain CFSAN096335: current GenBank GCA_010359745.2, historical GCA_010359745.1 and GCF_010359745.1, GTDB GB_GCA_010359745.2, and BV-BRC 195.2743. Current rows name C. coli, taxid 195; the replaced GenBank version names C. jejuni, taxid 197. Their assembly names/accessions cause digit collisions, not Wolbachia matches. Their own source differences do not concern this target.
- One describes uncultured bacterium MarMAG_055041, GCA_977272595.1, taxid 77133; its ungapped genome size is 1035974, a numeric collision.
- Ten ATB rows at lines 143559-143568 describe Escherichia coli samples SAMEA110359740 through SAMEA110359749.
- One ATB row at line 1722859 describes Salmonella enterica sample SAMN13244620, assembly ERZ25674264; its SeqKit sum contains the matching digits. This is not taxonomic or strain-link evidence.

The expanded marker/voucher/BOLD search added no rows.
Five native `SOURCE.json` files were parsed completely and history
filenames searched independently. No additional applicable local
assertion, culture deposit, strain-genome link, or standalone history
artifact was found within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: this identity-only record asserts no
regulator, expression module, or transcriptomic dataset. The optional
COI barcoding evidence does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name
attestation, inventoried strain count, optional omissions, and seed
provenance are supported. The additional marker evidence is
compatible with, but does not require changing, the generated record.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Before optional marker enrichment,
inspect Table S2 and exact accession-level primary evidence, preserving
specimen, marker, strain, and assembly identities separately.
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
